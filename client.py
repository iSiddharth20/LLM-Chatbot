import requests
import os
from dotenv import load_dotenv

load_dotenv()
server_ip_address = os.getenv('SERVER_IP_ADDRESS')
server_port_number = os.getenv('SERVER_PORT_NUMBER')
server_ip_and_port = f"{server_ip_address}:{server_port_number}"

# Send Query to Server
query = r"Hello! You up for a quick chat?"
requests.get(f"http://{server_ip_and_port}/query/", params={'query': query})

# Obtain Response from Server
post_response = requests.post(f"http://{server_ip_and_port}/response/")

# Display Obtained Response
response_data = post_response.json()
print(response_data["text"])

