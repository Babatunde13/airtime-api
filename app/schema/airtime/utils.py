import json
from flask import current_app as app
from ..utils import send_request

def get_token():
    url = "https://auth.reloadly.com/oauth/token"

    payload = json.dumps({
        "client_id": app.config['RELOADLY_CLIENT_ID'],
        "client_secret": app.config['RELOADLY_CLIENT_SECRET'],
        "grant_type": "client_credentials",
        "audience": "https://topups.reloadly.com"
        })
    headers = {
        'Content-Type': 'application/json'
    }
    response = send_request(url, payload, "POST", headers)
    if response['data']:
        return response['data']
    else:
        return None
        

def topup(amt, phone_number, my_number):
    url = f"{app.config['RELOADLY_API_URL']}/topups"
    payload = json.dumps({
        "operatorId": "685",
        "amount": amt,
        "useLocalAmount": False,
        "customIdentifier": "This is example identifier 092",
        "recipientPhone": {
            "countryCode": "NG",
            "number": phone_number
        },
        "senderPhone": {
            "countryCode": "NG",
            "number": my_number
        }
    })
    access_token = get_token()['access_token'] if get_token() else None
    if not access_token:
        print("No access token")
        exit()
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/com.reloadly.topups-v1+json',
        'Content-Type': 'application/json'
    }

    return send_request(url, payload, "POST", headers)
