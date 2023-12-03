from parkingSpot import *
import requests
from utils import *

HASH_TOKEN = 'ZHUzemJnNzFzaHxWN0o0YUZja21QOXZrZUFOTjY4QTY2dnlPWE92TUFyYThZMm5COTYz'
APP_ID = 'Pdu3zbg71sh'
TOKEN_URL = 'https://api.iq.inrix.com/auth/v1/appToken'
RADIUS = 2000
POINT = '37.74638779388551%7C-122.42209196090698'

def get_token():
    #Pass in the app_id and hash_token as query parameters
    params = {
        'appId': APP_ID,
        'hashToken': HASH_TOKEN
    }
    # Make the request to the INRIX token endpoint
    try:
        response = requests.get("https://api.iq.inrix.com/auth/v1/appToken?appId=du3zbg71sh&hashToken=ZHUzemJnNzFzaHxWN0o0YUZja21QOXZrZUFOTjY4QTY2dnlPWE92TUFyYThZMm5COTYz")
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        # Extract the token from the response
        # For more info on how to parse the response, see the json_parser_example.py file
        token = data['result']['token']
        return token
    except requests.exceptions.RequestException as e:
        return f'Request failed with error: {e}', None
    except (KeyError, ValueError) as e:
        return f'Error parsing JSON: {e}', None

url = "https://api.iq.inrix.com/lots/v3?point=" + POINT + "&radius=" + str(RADIUS)

bear_token = get_token()
bear_auth = "Bearer " + bear_token
headers = {
  'Authorization': bear_auth
}

response = requests.request("GET", url, headers=headers)
# print(response.text)

resp = response.json()

write_to_file(getCoordinates(resp), 'coordinates')
print(sort_by_lowest(getDistances(resp, [0,0])))