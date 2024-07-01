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

def list_lights():
    url = f'http://{hue_hub_ip}/api/{api_key}/lights'
    response = requests.get(url)
    lights = response.json()
    print("Available Lights:")
    for light_id, light_info in lights.items():
        print(f"Light ID: {light_id}, Name: {light_info['name']}")
    return lights

def control_light(light_id, state):
    url = f'http://{hue_hub_ip}/api/{api_key}/lights/{light_id}/state'
    data = {
        "on": state
    }
    json_data = json.dumps(data)
    response = requests.put(url, data=json_data)
    print(response.json())

def change_light_color(light_id, hex_value):
    url = f'http://{hue_hub_ip}/api/{api_key}/lights/{light_id}/state'
    # Convert hex color to XY color space (used by Philips Hue)
    # For simplicity, let's assume the user input is a valid hex color
    hex_color = hex_value.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    # Convert RGB to XY color space (Philips Hue specific conversion)
    xy_color = convert_rgb_to_xy(r, g, b)
    data = {
        "xy": xy_color
    }
    json_data = json.dumps(data)
    response = requests.put(url, data=json_data)
    print(response.json())

def convert_rgb_to_xy(r, g, b):
    # Normalize the RGB values to the range 0-1
    r = r / 255.0
    g = g / 255.0
    b = b / 255.0

    # Apply gamma correction
    r = r / 12.92 if r <= 0.04045 else ((r + 0.055) / 1.055) ** 2.4
    g = g / 12.92 if g <= 0.04045 else ((g + 0.055) / 1.055) ** 2.4
    b = b / 12.92 if b <= 0.04045 else ((b + 0.055) / 1.055) ** 2.4

    # Convert RGB to XYZ using the Wide RGB D65 conversion formula
    X = r * 0.664511 + g * 0.154324 + b * 0.162028
    Y = r * 0.283881 + g * 0.668433 + b * 0.047685
    Z = r * 0.000088 + g * 0.072310 + b * 0.986039

    # Convert XYZ to xy
    xy = [X / (X + Y + Z), Y / (X + Y + Z)]
    return xy

def print_instructions():
    print("""
Instructions:
1. List all lights
2. Choose active light
3. Turn on active light
4. Change light color (prompt hex value)
5. Turn off active light
6. Exit the app
""")

def main():
    active_light_id = None

    while True:
        print_instructions()
        choice = input("Enter your choice: ")

        if choice == '1':
            lights = list_lights()
        elif choice == '2':
            if lights:
                active_light_id = input("Enter the ID of the light to activate: ")
                if active_light_id not in lights:
                    print("Invalid light ID. Please choose a valid light ID.")
                    active_light_id = None
                else:
                    print(f"Active light set to ID: {active_light_id}, Name: {lights[active_light_id]['name']}")
            else:
                print("No lights available. Please list lights first (option 1).")
        elif choice == '3':
            if active_light_id:
                control_light(active_light_id, True)
            else:
                print("No active light set. Please choose an active light first (option 2).")
        elif choice == '4':
            if active_light_id:
                hex_value = input("Enter the hex color value (e.g., #ff0000 for red): ")
                change_light_color(active_light_id, hex_value)
            else:
                print("No active light set. Please choose an active light first (option 2).")
        elif choice == '5':
            if active_light_id:
                control_light(active_light_id, False)
            else:
                print("No active light set. Please choose an active light first (option 2).")
        elif choice == '6':
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
