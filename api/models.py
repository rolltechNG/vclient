from django.db import models
from verification.models import Credential, AccessToken, VerificationLogs, Unit
import hashlib
import base64
from django.contrib.auth.models import User
import xmltodict
import json
import xml.etree.ElementTree as et
import jsonpickle
from django.core import serializers
import traceback


# Create your models here.


import zeep

import codecs


class Demo:

    def getDemo(self, data):
        return {"id": data.centralID, "nin": data.nin, "surname": data.surname,
                "telephone": data.telephoneno, "tracking_id": data.trackingId,
                "firstname": data.firstname, "title": data.title, "middlename": data.middlename,
                "residence_address": {"address_line1": data.residence_AdressLine1, "address_line2": data.residence_AdressLine2,
                                      "town": data.residence_Town, "lga": data.residence_lga, "post_code": data.residence_postalcode, "state": data.residence_state},
                "birthdate": data.birthdate, "birthcountry": data.birthcountry, "birthstate": data.birthstate,
                "signature": data.signature, "photo": data.photo
                }

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def int2bytes(i):
    hex_value = '{0:x}'.format(i)
    # make length of hex_value a multiple of two
    hex_value = '0' * (len(hex_value) % 2) + hex_value
    return codecs.decode(hex_value, 'hex_codec')


def getPasswordHash(pwd):
    hex = hashlib.sha256(
        pwd.encode('utf-8')).hexdigest()
    return hex


def encryptPassword(password):
    e = 113621440243785421499955306133900099987164309503876199371900611085975699194905621710442876441889195302451922443555354266645737454327409509639333989384262385729949578624044207610948821627355876693570108394899808569346703874513552461157771585312437842555207875241788331401870311503661882350734256428011446552231
    m = 99656440840574176563305385521896948249485597887868788305755844436736813735716889384156081404108856785411701458057572807701609821377138238971482595936817351313377639458003034637351529602924774615106031875065736828376549082962569871367654360928995574432638495308492887000005021125506027838956077501182295786099
    ph = getPasswordHash(password)
    pm = int.from_bytes(ph.encode(), byteorder='big')
    d = pow(pm, e, m)
    sample_string_bytes = str(d).encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    return base64_bytes.decode("utf-8")


def call_soap():
    wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
    client = zeep.Client(wsdl=wsdl)
    print("how are you")
    print(print(encryptPassword("abc12345")))
    return client.service.Method1('Zeep', 'is cool')


def call_soap2():
    wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
    client = zeep.Client(wsdl=wsdl)
    print("how are you")
    return "Thanks you"


def auth_api():

    qr = Credential.objects.all().first()

    try:
        if qr is None:
            return "No Auth Parameter provided"
        username = getattr(qr, 'username', False)
        password = encryptPassword(getattr(qr, 'password', False))
        print("password = "+str(password))
        url = getattr(qr, 'url', False)
        orgid = getattr(qr, 'orgid', False)

        if username is None or password is None or url is None or orgid is None:
            return ("err", "No Auth Parameter provided")

        try:
            client = zeep.Client(wsdl=url)
        except:
            return ("err", "unable to reach the verification service")

        ix = client.service.createTokenString(username, password, orgid)

        return ("success", ix, url)
    except Exception as e:
        traceback.print_exc()

        return ("err", "Network Exception Thrown ")


# nin_verification("mbaocha", "123")

def log(email, request_type, input, output, fuilfiled, message):

    user = User.objects.get(email=email)
    b = VerificationLogs(user=user, request_type=request_type, input=input,
                         output=output, fuilfiled=fuilfiled, message=message)

    if message == 'success':
        u = Unit.objects.filter(
            user=user, access_type=request_type, direction='debit')

        if u.count() > 0:
            uone = u[0]
            uone.units = uone.units+1
            uone.save()
        else:
            Unit.objects.create(user=user, direction='debit',
                                units=1, access_type=request_type)

    b.save()
    print("done saving logs")


def is_unit_available(email, type):
    unit = Unit.objects.filter(
        user=User.objects.get(email=email), access_type=type)
    credit = 0
    debit = 0
    for u in unit:
        if u.direction == 'credit':
            credit = credit+u.units
        else:
            debit = debit+u.units
    print(str(credit) + "    " + str(debit))
    if (credit-debit) > 0:
        return True
    return False


def generic_search(mytoken, type, parameter):
    authTk = AccessToken.objects.filter(
        token=mytoken, active=True)
    res_msg = ""
    output = ""
    fuilfield = False
    message = 'success'
    if not authTk:
        return ({"data": None, "message": "Authentication failed! Either invalid or inactive token or cant reach the service. contact admin"})
    if type not in authTk[0].access_type:
        return ({"data": None, "message": "Authorization failed! you have no right to call that service. contact admin"})
    try:
        print("nnnnnnn")
        print(type not in authTk[0].access_type)
        # print(check_unit())

        auth = auth_api()
        if auth[0] != 'success':
            # print(auth)
            return {"data": None, 'message': auth[1]}

        # unit check

        if is_unit_available(authTk[0], type) == False:
            return {"data": None, 'message': "unitError", 'detail': "No unit available to service this request type"}

        i = 0
        client = zeep.Client(wsdl=auth[2])
        ix = None
        print(".............")
        print(auth[1])
        print(parameter)
        if type == 'nin':
            ix = client.service.searchByNIN(auth[1], parameter)
        elif type == "phone":
            ix = client.service.searchByDemoPhone(auth[1], parameter)
        elif type == "doc":
            ix = client.service.searchByDocumentNumber(auth[1], parameter)
        elif type == "demo":
            # {dateOfBirth:"",firstname:"",lastname:"",gender:""}
            ix = client.service.searchByDemo(auth[1], parameter)
        elif type == "finger":
            # {dateOfBirth:"",firstname:"",lastname:"",gender:""}

            ix = client.service.searchByFinger(
                auth[1], parameter['data'], parameter['pos'])
        elif type == "fingerV":
            ix = client.service.verifyFingerWithData(
                auth[1], parameter['nin'], parameter['data'], parameter['pos'])
        elif type == "photoV":
            ix = client.service.verifyPhotoWithData(auth[1], parameter)
        # print(ix.data)
        demo = Demo()
        list = []
        c = 0
        for d in ix.data:
            if c == 0:
                output = d.centralID
            else:
                output = output+","+d.centralID

            list.append(demo.getDemo(d))

        if(len(list) < 1):
            return {'data': None, 'message': 'success', 'detail': 'No matching record found'}

        frozen = jsonpickle.encode(list[0])
        # print(list)

        fuilfield = True

        return {'data': list, 'message': 'success'}
        # serialized_obj
    except Exception as e:
        print("err "+str(e))
        traceback.print_exc()

        message = str(e)
        fuilfield = False
        # return str(e)
        output = "None"
        return {"data": None, "message": str(e)}
    finally:
        if type == 'finger' or type == 'fingerV' or type == 'photoV':
            parameter = "biometrics"
        log(authTk[0].user.email, type, parameter,
            output, fuilfield, message)

    return {"data": None, "message": "verification error"}
