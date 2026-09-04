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
