import ollama
import os
from dotenv import load_dotenv

load_dotenv()

remote_ip = os.getenv("OLLAMA_REMOTE_IP", "NOT SET")
print(f"IP from env: {remote_ip}")

host = f"http://{remote_ip}:11434"
print(f"Connecting to: {host}")

client = ollama.Client(host=host)

# Test 1: Can we reach Ollama at all?
models = client.list()
print("Models available:", [m.model for m in models.models])

# Test 2: Can we generate?
resp = client.generate(model="gemma3:1b", prompt="say hello")
print("Response:", resp['response'])