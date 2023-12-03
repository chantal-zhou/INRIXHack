import requests

HASH_TOKEN = 'ZHUzemJnNzFzaHxWN0o0YUZja21QOXZrZUFOTjY4QTY2dnlPWE92TUFyYThZMm5COTYz'
APP_ID = 'Pdu3zbg71sh'
TOKEN_URL = 'https://api.iq.inrix.com/auth/v1/appToken'

def get_token():
    #Pass in the app_id and hash_token as query parameters
    params = {
        'appId': APP_ID,
        'hashToken': HASH_TOKEN
    }
    # Make the request to the INRIX token endpoint
    try:
        print("Getting Token")
        response = requests.get("https://api.iq.inrix.com/auth/v1/appToken?appId=du3zbg71sh&hashToken=ZHUzemJnNzFzaHxWN0o0YUZja21QOXZrZUFOTjY4QTY2dnlPWE92TUFyYThZMm5COTYz")
        response.raise_for_status()  # Raise HTTPError for bad responses
        print("Got Token")
        data = response.json()
        # Extract the token from the response
        # For more info on how to parse the response, see the json_parser_example.py file
        token = data['result']['token']
        print("hi")
        return token
    

    except requests.exceptions.RequestException as e:
        return f'Request failed with error: {e}', None
    except (KeyError, ValueError) as e:
        return f'Error parsing JSON: {e}', None

url = "https://api.iq.inrix.com/lots/v3?point=37.74638779388551%7C-122.42209196090698&radius=150"
# url = "https://api.iq.inrix.com/lots/v3"
# payload = {'point': '37.74638779388551%7C-122.42209196090698', "radius" : "150"}

bear_token = get_token()
bear_auth = "Bearer " + bear_token
headers = {
  'Authorization': bear_auth
}

response = requests.request("GET", url, headers=headers)
# print(response.text)

resp = response.json()
# print(resp["result"][0])
print(resp["count"])
