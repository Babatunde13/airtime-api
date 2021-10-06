import requests

def send_request(url, data, method, headers):
    try:
        response = requests.request(method, url, headers=headers, data=data)
        return {
            'data': response.json(),
            'status': response.status_code,
            'error': None
        }
    except Exception as e:
        print(e)
        return {
            'data': None,
            'error': e,
            'status': None
        }