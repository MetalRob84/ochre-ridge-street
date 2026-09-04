from ollama import generate
import time

start = time.perf_counter()

thing = generate(stream=False, 
                 model="llama3.1:8b",
                 #model="mistral:7b",
                 #model="Phi3.5",                 
                 #model="smollm2:135m",
                 prompt="Say Hello",
                 keep_alive=0)

end = time.perf_counter()
total = end - start

print(f"{thing.response} response time: {total:.2f} seconds")

"""
Results:

llama3.1:8b
Cold: Hello! How are you today? response time: 5.79 seconds
Hot: Hello! How are you today? response time: 3.63 seconds

mistral:7b
Cold: Hello there! How can I assist you today? response time: 6.17 seconds
Hot: Hello there! How can I assist you today? response time: 2.57 seconds

Phi3.5
Cold: Hello! I'm Phi, your AI assistant. How can I help you today? response time: 6.49 seconds
Hot: Hello! I'm Phi, an AI language model here to assist you. How can I help you today? response time: 2.08 seconds

smollm2:135m
Cold: (looking at you with a gentle smile) Ah, hello, how can I help you today? response time: 1.63 seconds
Hot: Hello. How can I assist you today? response time: 1.21 seconds
"""
