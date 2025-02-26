import google.generativeai as genai
import os

# Configure your API key
genai.configure(api_key="YOUR_API_KEY")  # Replace with your actual API key.

def chat_with_document(document_path):
    """
    Creates a chatbot that answers questions based on a document (PDF).

    Args:
        document_path: Path to the PDF document.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')  # or gemini-1.5-flash

        with open(document_path, "rb") as f:
            pdf_data = f.read()

        context = [
            "Here is a document:",
            {
                "mime_type": "application/pdf",
                "data": pdf_data
            },
            "\n\nBased on the document, answer the following questions in a conversational manner."
        ]

        while True:
            question = input("You: ")
            if question.lower() == 'exit':
                break

            conversation = context + [f"User: {question}"]

            response = model.generate_content(conversation)

            if response.text:
                print(f"Bot: {response.text}\n")
                context.append(f"User: {question}")
                context.append(f"Bot: {response.text}") #Add both user and bot responses to the context
            else:
                print("Bot: I'm sorry, I couldn't understand that.\n")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage:
document_path = 'C:/Users/sreekar/Downloads/runbook.pdf'  # Replace with your PDF file path
chat_with_document(document_path)

print("Goodbye!")