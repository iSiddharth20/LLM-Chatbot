from llama_index.llms.ollama import Ollama

llm = Ollama(model="llama3")

query = r"Hello! You up for a quick chat?"

response = llm.complete(query)

print(response)
