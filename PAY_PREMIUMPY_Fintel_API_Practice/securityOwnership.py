# Data provided by Fintel.io"
# Security Ownership
# Retrieves a list of institutions and funds reporting positions in a security.


import requests

url = "https://api.fintel.io/web/v/0.0/so/us/tsla"

response = requests.request("GET", url)

print(response.text)