import google.generativeai as genai
import os

# Configure your API key
genai.configure(api_key="YOUR_API_KEY")  # Replace with your actual API key.

def ask_gemini_with_document(document_path, question):
    """
    Asks Gemini questions based on the content of a document (PDF).

    Args:
        document_path: Path to the PDF document.
        question: The question to ask.

    Returns:
        The answer from Gemini, or None if an error occurs.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')  # or gemini-1.5-flash

        with open(document_path, "rb") as f:
            pdf_data = f.read()

        response = model.generate_content([
            "Here is a document:",
            {
                "mime_type": "application/pdf",
                "data": pdf_data
            },
            f"\n\nBased on the document, answer this question: {question}"
        ])

        return response.text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example Usage:
document_path = 'C:/Users/sreekar/Downloads/runbook.pdf'  # Replace with your PDF file path

while True:
    question = input("Enter your question (or type 'exit' to quit): ")
    if question.lower() == 'exit':
        break
    
    print("Asking Gemini...\n")
    print(f"Question: {question}\n")
    answer = ask_gemini_with_document(document_path, question)

    if answer:
        print(f"Question: {question}")
        print(f"Answer: {answer}\n")
    else:
        print("Could not get an answer.\n")

print("Goodbye!")