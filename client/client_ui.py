import requests
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
server_ip_address = os.getenv('SERVER_IP_ADDRESS')
server_port_number = os.getenv('SERVER_PORT_NUMBER')
server_ip_and_port = f"{server_ip_address}:{server_port_number}"

st.set_page_config(page_title="OllamaBot")
st.title('Welcome to Ollama-Bot')

with st.form('form_chat_history'):
  query = st.text_area('Enter Query:', 'Hello! You up for a quick chat?')
  submitted = st.form_submit_button('Send Query')
if submitted:
    # Send Query to Server
    get_response = requests.get(f"http://{server_ip_and_port}/query/", params={'query': query})
    # Obtain Response from Server
    post_response = post_response = requests.post(f"http://{server_ip_and_port}/response/")
    # Display Obtained Response
    response_data = post_response.json()
    st.info(response_data["text"])

