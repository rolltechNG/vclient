This is a NIMC Verification client which is built on python-django and enable users make verification request.
This also have an admin modules to enable administration of account

To make a request, you ll be issued a client token

First its made up of a Rest Endpoint. This Rest Endpoint interfaces with NIMC soap api to make a number of request. Some of the supported request are

1. http://127.0.0.1:8000/api/nin/[token]/[nin] : this is a GET request that retrieves match details upon provision of a valid NIN.
Details retrieved include names, signature, photo etc. This will only return a single record if NIN is valid
2. http://127.0.0.1:8000/api/demo/[token]/[firstname]/[lastname]/[dob in format DD-MM-YYYY] : this is a GET request that retrieves match details upon 
provision of a valid Demographic (firstname, lastname, dob). Details retrieved include names, signature, photo etc. This can return 1 or more records
3. http://127.0.0.1:8000/api/phone/[token]/[phone] : this is a GET request that retrieves match details upon 
provision of a valid phone number. Details retrieved include names, signature, photo etc. This can return 1 or more records

Possible Response
1. Invalid token : if token provided is invalid
2. No Record Found
3. Not unit to service this request


