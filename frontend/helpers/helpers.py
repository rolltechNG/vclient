import json


def process_resp(r):
    try:
        resp = r.text
        resp_json = json.loads(resp)
        resp_list = resp_json['data']
        for key in resp_list:
            img_decode = key['photo']
            signature_decode = key['signature']
            key['photo'] = f"data:image/png;base64,{img_decode}"
            key['signature'] = f"data:image/png;base64,{signature_decode}"
            response = key

            return response

    except TypeError:
        return "", 404
