import requests

# Send Query to Server
query = r"Hello! You up for a quick chat?"
requests.get(f"http://127.0.0.1:8000/query/", params={'query': query})

# Obtain Response from Server
post_response = requests.post("http://127.0.0.1:8000/response/")

# Display Obtained Response
response_data = post_response.json()
print(response_data["text"])

