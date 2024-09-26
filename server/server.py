from llama_index.llms.ollama import Ollama
from fastapi import FastAPI

app = FastAPI()

class OllamaResponse:
    def __init__(self, model_name=None):
        ''' If No Model is Specified, Ollama will assume Meta-Llama-3.1-8B '''
        self.model_name = "llama3.1" if not model_name else model_name
        self.llm = Ollama(model=self.model_name)
        self.query = None
        self.response = None
        self.memory_chain = []
    
    def set_query(self, query):
        ''' Get Query from Client, Set Query for Further Processing '''
        self.query = query
        self.memory_chain.append({"role": "user", "content": query})
    
    def get_response_from_ollama(self):
        ''' Send Query and Memory to Ollama, Get Response from Ollama '''
        if not len(self.memory_chain) == 1: 
            query = "\n".join([f"{msg['role']}: {msg['content']}" for msg in self.memory_chain])
            self.response = self.llm.complete(query)            
        else:
            self.response = self.llm.complete(self.query)
        self.memory_chain.append({"role": "assistant", "content": self.response})
    

chatbot = OllamaResponse()

@app.get("/query/")
def receive_query(query: str):
    ''' Receive Query from Client '''
    chatbot.set_query(query)
    chatbot.get_response_from_ollama()

@app.post("/response/")
def send_response():
    ''' Send Response to Client '''
    return chatbot.response


if __name__ == '__main__':

    test_run = OllamaResponse()

    query = r"Hello! You up for a quick chat?"

    test_run.set_query(query)
    test_run.get_response_from_ollama()

    print(test_run.response)
