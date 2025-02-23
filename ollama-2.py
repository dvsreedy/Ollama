from ollama import chat
from ollama import ChatResponse


response: ChatResponse = chat(model='llama3.2', messages=[
    {"role": "system", "content": "You give short and best practice python code."},
    {"role": "user", "content": """
      Write a python function that uses regex to extract emails
       (including instances of 'name at email dot com') from a text.
      Use pytest to write useful unit tests.
      """
}
  ],
)

print(response.message.content)