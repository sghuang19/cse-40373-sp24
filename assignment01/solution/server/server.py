import time
import zmq
import requests
import json

context = zmq.Context()
socket = context.socket(zmq.REP)

url = "http://ns-mn1.cse.nd.edu/sysprogfa23/assignment08/data/2019-01-21/0.json"
path = "../data/data.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Data fetched from URL")
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
else:
    print(f"Failed to fetch data: status code {response.status_code}")
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            print("Using cached data instead")
    except FileNotFoundError:
        print("No cached data found")
        exit()

serverPort = 40226
try: 
    print('Starting up server on port ' + str(serverPort))
    socket.bind("tcp://*:" + str(serverPort))
except:
    print('Failed to bind on port ' + str(serverPort))
    exit()

keys = ["factory_id", "name", "battery_level", "battery_updated_date", "hardware"]
while True:
    #  Wait for next request from client
    beacon = socket.recv().decode("ascii").strip()
    print(f"Received beacon: {repr(beacon)}")

    message = None
    for item in data:
        if item["name"] == beacon:
            message = ', '.join(item[key] for key in keys)
            break
    if not message:
        message = "Error: beacon name doesn't exist"

    #  Send reply back to client
    socket.send_string(message)
    print(f"Message sent: {message}")
