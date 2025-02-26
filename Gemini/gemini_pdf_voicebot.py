import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

# Configure your API key
genai.configure(api_key="AIzaSyA8Dsecwk_Gt9KS5u4hk9hnw7gx-OoKIHE") # Replace with your API key

def get_audio():
    """Captures audio from the microphone and returns text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

def speak(text):
    """Converts text to speech and plays it."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def chat_with_document(document_path):
    """Voice bot that answers questions from a document."""
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')

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
            question = get_audio()
            if question:
                if question.lower() == 'exit':
                    break
                print(f"You: {question}")
                print("Bot: Thinking...")
                conversation = context + [f"User: {question}"]
                response = model.generate_content(conversation)

                if response.text:
                    print(f"Bot: {response.text}")
                    speak(response.text)
                    context.append(f"User: {question}")
                    context.append(f"Bot: {response.text}")
                else:
                    speak("I'm sorry, I couldn't understand that.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage:
document_path = 'C:/Users/sreekar/Downloads/runbook.pdf'  # Replace with your PDF file path
chat_with_document(document_path)

print("Goodbye!")