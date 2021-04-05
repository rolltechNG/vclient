import zeep


def call_soap():
    wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
    client = zeep.Client(wsdl=wsdl)
    return client.service.Method1('Zeep', 'is cool')
