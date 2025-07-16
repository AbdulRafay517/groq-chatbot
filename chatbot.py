import os
import requests
from dotenv import load_dotenv
from rich.console import Console
from groq import Groq

# Load environment variables from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize the console for rich output
console = Console()

def ask_groq(question):
    """
    Send a question about the internet to the Groq API and return the response.
    """
    
    groq = Groq(api_key=GROQ_API_KEY)
    response = groq.chat.completions.create(
        model="compound-beta",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )
    return response.choices[0].message.content

def main():
    console.print("Welcome to the Groq Chatbot!")
    while True:
        question = console.input("You: ")
        if question.lower() in ["exit", "quit"]:
            console.print("Goodbye!")
            break
        reply = ask_groq(question)
        console.print(f"Groq: {reply}")

if __name__ == "__main__":
    main()