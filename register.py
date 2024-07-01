import requests
import json

# Philips Hue Hub IP address
hue_hub_ip = '10.0.0.34'

# The URL to send the request to
url = f'http://{hue_hub_ip}/api'

# The data to send in the request
data = {
    "devicetype": "hue_controller#laptop"  # Change "hue_controller#laptop" to your preferred app and device name
}

# Convert the data to JSON format
json_data = json.dumps(data)

# Print instructions to press the link button
print("Press the link button on your Philips Hue Hub, then press any key to continue.")

# Wait for user input
input("")

# Send the POST request
response = requests.post(url, data=json_data)

# Parse the response
response_data = response.json()

# Check if the response contains the username (API key)
if 'success' in response_data[0]:
    api_key = response_data[0]['success']['username']
    print(f"API key generated successfully: {api_key}")
else:
    print("Failed to generate API key. Please make sure you pressed the link button and try again.")
