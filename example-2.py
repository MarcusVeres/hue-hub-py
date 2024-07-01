import requests
import json

# Philips Hue Hub IP address and API key
hue_hub_ip = '10.0.0.34'
api_key = 'u4H4IwzEyCYwDqJYgpPqNaR0PDZcJE13wm18hGGX'  # Replace with the actual API key

# Light ID and URL
light_id = 1
url = f'http://{hue_hub_ip}/api/{api_key}/lights/{light_id}/state'

# Data to send in the request
data = {
    "on": True
}

# Convert the data to JSON format
json_data = json.dumps(data)

# Send the PUT request to turn on the light
response = requests.put(url, data=json_data)

# Print the response
print(response.json())
