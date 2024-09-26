# Ollama-FastAPI-LlamaIndex

#### Client-Server Architecture LLM Chatbot with optional Streamlit UI

---

<div align="center">

### Project Demo on YouTube

[![Project Demo on YouTube](https://img.youtube.com/vi/HSHE49v4_qg/0.jpg)](https://www.youtube.com/watch?v=HSHE49v4_qg)

</div>

---

### Understand Role of:

- [Server](#role-server) Component
- [Client](#role-client) Component

### How to Setup:

- [Server](#setup-server) Component
- Cient Component [without Streamlit UI](#setup-client-no-ui)
- Cient Component [with Streamlit UI](#setup-client-with-ui)

### How to Run:

- [Server](#run-server) Component
- Cient Component [without Streamlit UI](#run-client-no-ui)
- Cient Component [with Streamlit UI](#run-client-with-ui)

### Prerequisites for Client and Server:

- STEP 1 : Clone this Repo
- STEP 2 : [Optional but Recommended] Download and Install [Miniconda](https://docs.anaconda.com/miniconda/#latest-miniconda-installer-links), to create and manage conda environments

---

<a name="role-client"></a>

#### What does `Client` do:

- STEP 1 : Request Query from User
- STEP 2 : Send Query to Server
- STEP 3 : Receive Response from Server
- STEP 4 : Display Response to User

<a name="role-server"></a>

#### What does `Server` do:

- STEP 1 : Receive Query from Client
- STEP 2 : Send Query to Ollama
- STEP 3 : Receive Response from Ollama
- STEP 4 : Send Response to Client

---

<a name="setup-server"></a>

#### Setup for `Server`:

- STEP 1 : Download and Install [Ollama](https://ollama.com/download)
- STEP 2 : Download desired model from Ollama
  <br>&nbsp;&nbsp;NOTE : To download Meta-Llama-3.1-8B, Run command: `ollama pull llama3.1`
- STEP 3 : [Optional but Recommended] Create a Conda Environment, Run command : `conda create -n "env_server" python=3.11 -y`
  <br>&nbsp;&nbsp;NOTE: This is a one-time setup
- STEP 4 : [Optional but Recommended] Activate the created Conda Environment with `conda activate env_server`
  <br>&nbsp;&nbsp;NOTE: Activate conda environment with each new instance of Terminal
- STEP 5 : Install Dependencies: `pip install -r requirements.txt`

<a name="setup-client-no-ui"></a>

#### Setup for `Client` without Stramlit UI:

- STEP 1 : [Optional but Recommended] Create a Conda Environment, Run command : `conda create -n "env_client" python=3.11 -y`
  <br>&nbsp;&nbsp;NOTE: This is a one-time setup
- STEP 2 : [Optional but Recommended] Activate the created Conda Environment with `conda activate env_client`
  <br>&nbsp;&nbsp;NOTE: Activate conda environment with each new instance of Terminal
- STEP 3 : Install Dependencies: `pip install -r requirements.txt`
- STEP 4 : Change Server IP and Port Number in `.env` file.
  <br>&nbsp;&nbsp;NOTE: If you are not using separate device as Server, do not change contents of `.env` file

<a name="setup-client-with-ui"></a>

#### Setup for `Client` with Stramlit UI:

- STEP 1 : [Optional but Recommended] Create a Conda Environment, Run command : `conda create -n "env_client" python=3.11 -y`
- STEP 2 : [Optional but Recommended] Activate the created Conda Environmen, Run command : `conda activate env_client`
- STEP 3 : Install Dependencies: `pip install -r requirements_ui.txt`
- STEP 4 : Change Server IP and Port Number in `.env` file.
  <br>&nbsp;&nbsp;NOTE: If you are not using separate device as Server, do not change contents of `.env` file

---

<a name="run-server"></a>

#### Run `Server` component:

- STEP 1 : [Optional but Recommended] Activate the created Conda Environment, Run command : `conda activate env_server`
  <br>&nbsp;&nbsp;NOTE: Activate conda environment with each new instance of Terminal
- STEP 2 : Run command : `uvicorn app:app --host 0.0.0.0 --port 8000`
  <br>&nbsp;&nbsp;NOTE: You can change the Port Number, make sure to update it in .env file on client
- IMP : Do not close the Terminal, else Server will Stop

<a name="run-client-no-ui"></a>

#### Run `Client` component without Stramlit UI:

- STEP 1 : [Optional but Recommended] Activate the created Conda Environment, Run command : `conda activate env_client`
  <br>&nbsp;&nbsp;NOTE: Activate conda environment with each new instance of Terminal
- STEP 2 : Verify Server IP and Port Number in `.env` file.
  <br>&nbsp;&nbsp;NOTE: If you are not using separate device as Server, do not change contents of `.env` file
- STEP 3 : Run command : `python client.py`

<a name="run-client-with-ui"></a>

#### Run `Client` component with Stramlit UI:

- STEP 1 : [Optional but Recommended] Activate the created Conda Environment, Run command : `conda activate env_client`
  <br>&nbsp;&nbsp;NOTE: Activate conda environment with each new instance of Terminal
- STEP 2 : Verify Server IP and Port Number in `.env` file.
  <br>&nbsp;&nbsp;NOTE: If you are not using separate device as Server, do not change contents of `.env` file
- STEP 3 : Run command : `streamlit run client_ui.py`

---

#### Tested On:

- Client &nbsp;: MacBook Pro 14"
- Server : RTX 3060 12G || Ubuntu Server 24.04 LTS
- LLM &nbsp;&nbsp;&nbsp;&nbsp;: Meta-Llama-3.1-8B
