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

    system_prompt = "You are a helpful and knowledgeable assistant that only answers questions related to the internet, such as how it works, its protocols (HTTP, TCP/IP, etc.), history, infrastructure (like DNS, servers, ISPs), and applications. If the question is not about the internet, respond with: Sorry, I can only answer questions about the internet."

    response = groq.chat.completions.create(
        model="compound-beta",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )
    
    if not response.choices or not response.choices[0].message:
        console.print("Error: No response from Groq API.")
        return "I'm sorry, I couldn't process your request."
    
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