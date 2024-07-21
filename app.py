from llama_index.llms.ollama import Ollama

class OllamaResponse:
    def __init__(self, model_name=None):
        ''' If No Model is Specified, Ollama will assume Meta-Llama-3-8B '''
        self.model_name = "llama3" if not model_name else model_name
        self.llm = Ollama(model=self.model_name)
    
    def set_query(self, query):
        ''' Get Query from Client, Set Query for Further Processing '''
        self.query = query
        # You can add Query formatting code here
    
    def get_response_from_ollama(self):
        ''' Send Query to Ollama, Get Response from Ollama '''
        self.response = self.llm.complete(self.query)
        # You can add Response formatting code here
    
    def post_response(self):
        ''' Send Response to Client '''
        return self.response


if __name__ == '__main__':

    test_run = OllamaResponse()

    query = r"Hello! You up for a quick chat?"

    test_run.set_query(query)
    test_run.get_response_from_ollama()

    response = test_run.post_response()
    print(response)

