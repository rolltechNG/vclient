from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import call_soap, auth_api, generic_search
from django.views.decorators.csrf import csrf_exempt

# from soapc import call_soap

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'nin': '/<str:token>/<str:nin>',
        'doc': '/<str:token>/<str:doc>',
        'phone': '/<str:token>/<str:phone>',
        'demo': '/<str:token>/<str:firstname>/<str:lastname>/<str:dob>/<str:gender>',
        'fingerSearch': '/<str:token>/<str:data>/<str:pos>',
        'fingerVerification': '/<str:token>/<str:nin>/<str:finger>/<str:pos>',
        'photoverification': '<str:token>/<str:nin>/<str:photo>/<str:pos>'

    }

    return Response(api_urls)


@api_view(['GET'])
def nin_verification_vw(request, token, nin):

    return JsonResponse(generic_search(token, "nin", nin))


@api_view(['GET'])
def phone_verification_vw(request, token, phone):
    return JsonResponse(generic_search(token, "phone", phone))


@api_view(['GET'])
def doc_verification_vw(request, token, doc):
    return JsonResponse(generic_search(token, "doc", doc))


@api_view(['GET'])
def demo_verification_vw(request, token, firstname, lastname, dob):
    return JsonResponse(generic_search(token, "demo", {'firstname': firstname, 'lastname': lastname, 'dateOfBirth': dob, 'gender': 'm'}))


@api_view(['GET'])
def finger_search_vw_deprecated(request, token, data, pos):
    return JsonResponse(generic_search(token, "finger", {'data': data, 'pos': pos}))


@api_view(['POST'])
def finger_verification_vw(request, token, nin):
    finger = None
    pos = None
    print("herlooooo")
    try:
        print(request.data)
        finger = request.data['finger']
        pos = request.data['pos']
       # request.data.pos
    except Exception:
        return JsonResponse({"err": "one or more required attributes not provided (finger<string>,pos<string>)"})
    else:
        print("Exists")
    return JsonResponse(generic_search(token, "fingerV", {'nin': nin, 'data': finger, 'pos': pos}))


def photo_verification_vw(request, token, nin):
    photo = None
    try:
        photo = request.data['photo']

    except Exception:
        return JsonResponse({"err": "one or more required attributes not provided (photo<string>)"})
    else:
        print("Exists")
    return JsonResponse(generic_search(token, "photoV", {'nin': nin, 'photo': photo}))


@api_view(['POST'])
def finger_search_vw(request, token):

    print("token")
    print(token)
    finger = None
    pos = None
    try:
        finger = request.data['finger']
        pos = request.data['pos']
       # request.data.pos
    except Exception:
        return JsonResponse({"err": "one or more required attributes not provided (finger<string>,pos<string>)"})
    else:
        print("Exists")

    return JsonResponse(generic_search(token, "finger", {'data': finger, 'pos': pos}))
