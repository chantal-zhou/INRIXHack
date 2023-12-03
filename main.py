import requests

HASH_TOKEN = 'PASTE YOUR HASH TOKEN HERE'
APP_ID = 'PASTE YOUR APP ID HERE'
TOKEN_URL = 'https://api.iq.inrix.com/auth/v1/appToken'

def get_token():
    #Pass in the app_id and hash_token as query parameters
    params = {
        'appId': APP_ID,
        'hashToken': HASH_TOKEN
    }
    # Make the request to the INRIX token endpoint
    try:
        response = requests.get(TOKEN_URL, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses

        data = response.json()
        # Extract the token from the response
        # For more info on how to parse the response, see the json_parser_example.py file
        token = data['result']['token']
        return token, response.status_code

    except requests.exceptions.RequestException as e:
        return f'Request failed with error: {e}', None
    except (KeyError, ValueError) as e:
        return f'Error parsing JSON: {e}', None

url = "https://api.iq.inrix.com/lots/v3?point=37.74638779388551%7C-122.42209196090698&radius=150"
# url = "https://api.iq.inrix.com/lots/v3"
# payload = {'point': '37.74638779388551%7C-122.42209196090698', "radius" : "150"}

headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6ImR1M3piZzcxc2giLCJ0b2tlbiI6eyJpdiI6ImFiZjE0MTdjM2NmZTMyY2YwNTQwZjcxZTlmYTg3MDc0IiwiY29udGVudCI6Ijg5MmM5ZTEzNGJiZWEyY2EzZThhZWNmNTYxYzBhNmE4ZGViZDNhNjhjMTg3NjdmODIzOWU5YWFhMTczNWMyNjFiNmYwYjRjYmE2ZDk1NzU3ZmFlYWUyMjYwMTQ1ZjIwMjMxNjg0NDMyYTE0YWQ3MmM2NmM5M2M3NDI2ZWRlZjdhMjRkOGU2OTVmNjJmMjk2NDhlMDBkM2M2Y2YyMmI5NTRjNzYyNDdmN2EwNjM4MjAyMjJhNDVjYTZkNTgzYTExM2Q1MjQxNTg0MGU2MTkyYWY4NTBiMzliMDMzNmNiN2ZkOThiZjI0ODZhYzdkMDljMzExNjAxMmI3ZjIwYWY4MjA4MTEyNWUzZGI2MDBjZDNjYjgyZDViNjlkOGFhYTIyOTEzZTA5ZTYyMWJjOTZhM2EwY2U4MDBiNWJlOTJiNzBkYTI2NjFhMjM5ZDgxYWM5N2QwMmI4MDcyNDVjNzUwNTAwY2RkNTVlZThmZjZhOGMxZWRlZGZlNGNhOWRkNmIwZGVlYzg3NTQ2NzJlMTkxMzUwYTAxZTg1NDJjOWVhOTgzZDUzNWNjYjAwNjcwNDAzMmUzMjgwMjQxNTg3Nzg4NzAwNGUyZWI0NjhkNDg3Y2FiZTQ4YmJlNjlkNTE0ZmRlZDc4NGU1NTFkZmMzNGQ5MTg4MjI2ZTJmNzVlZDcwNzNmNjNjZjg1NDI1YmY5MGM2N2EzODBjMDBkMDU5ZWRlYmFlYmE4MTk4NTE0YWZkZjJkODliNjBiYTFhNWQyYjY1MzBjNWViY2NlMjE1MmVmMjRkODRiYjgwZDcyM2YzOTE4M2E2NzU5YzUxNWE2OTQ4NmViN2M0OWQ2Y2NjNjI5NWQxZjhlMWMxMGFlNWMzNTQ1ZDljNjFkIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiJhYmYxNDE3YzNjZmUzMmNmMDU0MGY3MWU5ZmE4NzA3NCIsImNvbnRlbnQiOiJhODNkODMyYTExYmQ4N2UyMTNiNmY3OGQwY2YzZDZlMWRiZWMxNzRjZTZhMTU3YjUyMTkyYjFlNjA5MWZmMDBhYjZjMGNlODVkMmU1Njk2NGUyYzVmMzE4In0sImp0aSI6IjFhMzYyOTk1LTQzMmQtNGQ2Ni1iNzBlLTcyM2I1MjE5MTFlZSIsImlhdCI6MTcwMTU3MTAzMCwiZXhwIjoxNzAxNTc0NjMwfQ.2eXaMWIGsfcBuio4oVFJcnXZEqGx_v2LDDovlcLLqwM'
}

response = requests.request("GET", url, headers=headers)
# print(response.text)

resp = response.json()
# print(resp["result"][0])
print(resp["count"])
