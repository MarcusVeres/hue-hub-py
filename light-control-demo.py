import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv('HUE_API_KEY')

# Philips Hue Hub IP address
hue_hub_ip = '10.0.0.34'

# URL to get the list of lights
url = f'http://{hue_hub_ip}/api/{api_key}/lights'

# Send the GET request to list all lights
response = requests.get(url)

# Parse the response
lights = response.json()

# Print the list of lights and their IDs
for light_id, light_info in lights.items():
    print(f"Light ID: {light_id}, Name: {light_info['name']}")

# Function to turn a light on or off
def control_light(light_id, state):
    url = f'http://{hue_hub_ip}/api/{api_key}/lights/{light_id}/state'
    data = {
        "on": state
    }
    json_data = json.dumps(data)
    response = requests.put(url, data=json_data)
    print(response.json())

# Replace with the actual light ID you want to control
light_id = '15'

# Turn the light on
control_light(light_id, True)

# Wait for a few seconds
import time
time.sleep(5)

# Turn the light off
control_light(light_id, False)
