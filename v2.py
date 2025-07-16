import re
import random

# Optional: For preprocessing
import nltk
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources (run once)
nltk.download('punkt_tab')

# Define some intents with keywords and responses
intents = {
    "greeting": {
        "keywords": ["hi", "hello", "hey", "good morning", "good evening"],
        "responses": ["Hello!", "Hi there!", "Hey! How can I help you?"]
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see you", "later"],
        "responses": ["Goodbye!", "See you later!", "Have a great day!"]
    },
    "thanks": {
        "keywords": ["thanks", "thank you", "thx"],
        "responses": ["You're welcome!", "Any time!", "Glad to help!"]
    },
    "unknown": {
        "responses": ["I'm not sure I understand.", "Can you rephrase that?", "Sorry, I don't know about that."]
    },
    "weather": {
    "keywords": ["weather", "rain", "sunny", "forecast"],
    "responses": ["I can't predict the weather yet, but you can check a forecast site!"]
    },
    "joke": {
        "keywords": ["joke", "funny", "laugh"],
        "responses": ["Why don’t scientists trust atoms? Because they make up everything! 😂"]
    }
}

# Preprocessing: Lowercase, remove punctuation
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return word_tokenize(text)

# Intent recognition
def get_intent(tokens):
    for intent, data in intents.items():
        if intent == "unknown":
            continue
        for word in tokens:
            if word in data["keywords"]:
                return intent
    return "unknown"

# Generate response
def generate_response(intent):
    return random.choice(intents[intent]["responses"])

# Main chat loop
def chatbot():
    print("🤖 ChatBot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("🧑 You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("🤖 ChatBot: Goodbye!")
            break
        tokens = preprocess(user_input)
        intent = get_intent(tokens)
        response = generate_response(intent)
        print(f"🤖 ChatBot: {response}")

# Run it
if __name__ == "__main__":
    chatbot()
