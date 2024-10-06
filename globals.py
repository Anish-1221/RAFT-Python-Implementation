import json
import os

SERVERS_FILE = 'servers.json'

# Load the servers from the JSON file
if os.path.exists(SERVERS_FILE):
    with open(SERVERS_FILE, 'r') as file:
        servers = json.load(file)
else:
    servers = {}

# Function to save the current state of the servers dictionary
def save_servers():
    with open(SERVERS_FILE, 'w') as file:
        json.dump(servers, file)

print("Servers dictionary after modification:", servers)