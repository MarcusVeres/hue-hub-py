import requests

ip = 10.0.0.34
port = 80

url = "http://" + ip + ":" + port + "/api/your-api-key/lights/1/state"
data = {
    "on": True
}

response = requests.post(url, json=data)
print(response.json())

