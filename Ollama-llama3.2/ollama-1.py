import subprocess
import requests
import time

def start_ollama_server():
    try:
        # Check if the Ollama server is running
        response = requests.get("http://localhost:11434/health")
        if response.status_code == 200:
            print("Ollama server is already running.")
            return
    except requests.ConnectionError:
        print("Ollama server not running. Starting it now...")
    
    # Start the Ollama server as a subprocess
    subprocess.Popen(["ollama", "serve"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("Starting Ollama server...")
    time.sleep(5)  # Wait for the server to initialize

    # Verify server is running
    try:
        response = requests.get("http://localhost:11434/health")
        if response.status_code == 200:
            print("Ollama server is running.")
        else:
            print("Failed to start Ollama server.")
    except requests.ConnectionError:
        print("Failed to connect to Ollama server.")

def query_ollama(prompt, model="llama2", system_message="You give short and best practice python code.", temperature=0):
    url = "http://localhost:11434/api/completions"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        "temperature": temperature,
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Raise an error if the request failed
    return response.json()

# Start Ollama server
start_ollama_server()

# Define your prompt
prompt = """
Write a python function that uses regex to extract emails
(including instances of 'name at email dot com') from a text.
Use pytest to write useful unit tests.
"""

# Query the Ollama model
response = query_ollama(prompt)

# Print the result
print(response['choices'][0]['message']['content'])
