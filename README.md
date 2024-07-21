# Ollama-FastAPI-LlamaIndex
### Comes with Streamlit UI
---

### What does `Client` do: 
>* STEP 1 : Request Query from User
>* STEP 2 : Send Query to Server
>* STEP 3 : Receive Response from Server
>* STEP 4 : Display Response to User

### What does `Server` do: 
>* STEP 1 : Receive Query from Client
>* STEP 2 : Send Query to Ollama
>* STEP 3 : Receive Response from Ollama
>* STEP 4 : Send Response to Client

---

### `Common Setup` for Client and Server: 
>* STEP 1 : Clone this Repo
>* STEP 2 : [Optional but Recommended] Create a Conda Environment with `python=3.11`

### Setup for `Server`: 
>* STEP 1 : Download and Install Ollama, link provided below
>* STEP 2 : Download desired model from Ollama
<br>&nbsp;&nbsp;NOTE: To download Meta-Llama-3-8B, Run command: `ollama run llama3`
>* STEP 3 : Install Dependencies: `pip install -r requirements_server.txt`
>* STEP 4 : Run command : `uvicorn app:app`
<br>&nbsp;&nbsp;NOTE: Do not close the Terminal/CMD, or else Server will Stop

### Setup for `Client` without Stramlit UI: 
>* STEP 1 : Install Dependencies: `pip install -r requirements_client.txt`
>* STEP 2 : Change Server IP and Port Number in `.env` file.
<br>&nbsp;&nbsp;NOTE: If you are not using separate device as Server, do not change contents of `.env` file
>* STEP 3 : Run command : `python client.py`

### Setup for `Client` with Stramlit UI: 
>* STEP 1 : Install Dependencies: `pip install -r requirements_client_ui.txt`
>* STEP 2 : Change Server IP and Port Number in `.env` file.
<br>&nbsp;&nbsp;NOTE: If you are not using separate device as Server, do not change contents of `.env` file
>* STEP 3 : Run command : `streamlit run client_with_gui.py`

---

### Tested On: 
>* Client &nbsp;: MacBook Pro 14"
>* Server : RTX 3060 12G || Ubuntu Server 24.04 LTS
>* LLM &nbsp;&nbsp;&nbsp;&nbsp;: Meta-Llama-3-8B

---

### Additional Resources: 
* Download and Install [Ollama](https://ollama.com/download)