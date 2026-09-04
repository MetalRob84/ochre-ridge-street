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
llama3.1:8b
Cold: Hello! How can I assist you today? response time: 7.77 seconds
Hot: Hello! How can I assist you today? response time: 3.94 seconds

mistral:7b
Cold: Hello there! How can I assist you today? response time: 4.13 seconds
Hot: Hello there! How can I assist you today? response time: 2.61 seconds

Phi3.5
Cold: Hello! I'm Phi, your language model assistant. How can I help you today? response time: 2.82 seconds
Hot: Hello! I'm Phi, an AI here to assist you with any questions or tasks you might have. How can I help you today? response time: 2.24 seconds

smollm2:135m
Cold: Hello! I'm here to help you navigate the world. What's on your mind? Do you have a question about a place, a situation, or perhaps a challenge you're facing? response time: 1.74 seconds
Hot: Hello! How can I assist you today? response time: 1.27 seconds
"""
