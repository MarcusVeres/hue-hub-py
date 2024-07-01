import requests
import json

# Philips Hue Hub IP address and API key
hue_hub_ip = '10.0.0.34'
api_key = 'u4H4IwzEyCYwDqJYgpPqNaR0PDZcJE13wm18hGGX'  # Replace with the actual API key

# URL to get the list of lights
url = f'http://{hue_hub_ip}/api/{api_key}/lights'

# Send the GET request to list all lights
response = requests.get(url)

# Parse the response
lights = response.json()

# Print the list of lights and their IDs
for light_id, light_info in lights.items():
    print(f"Light ID: {light_id}, Name: {light_info['name']}")
