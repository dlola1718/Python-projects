# Data provided by Fintel.io"
# Institutional Holdings
# Shows the most recent holdings disclosed by an institution or fund in 13F or N-PORT filings



#paused paused paused paused






import requests

institution_name = "scion-asset-management-llc"

url = "https://api.fintel.io/web/v/0.0/i/" + institution_name



# headers = {"Accept": "application/json"}

# response = requests.request("GET", url, headers=headers)

# print(response)

# print(response.json())


# Making a get request
response = requests.get(url)
  
# print response
print(response)
  
# print json content
print(response.json())