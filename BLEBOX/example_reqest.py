import requests
url = 'https://...'
payload = {'key1': 'value1', 'key2': 'value2'}

# GET
r = requests.get(url)

# GET with params in URL
r = requests.get(url, params=payload)

# POST with form-encoded data
r = requests.post(url, data=payload)

# POST with JSON
import json
r = requests.post(url, data=json.dumps(payload))

# Response, status etc
print(r.text)
print(r.status_code)