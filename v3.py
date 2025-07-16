import re
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd

# Load the data csv
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Split the data into text and labels
def split_data(data):
    texts = data['text'].tolist()
    intents = data['intent'].tolist()
    return texts, intents

# Preprocessing: lowercase and remove special characters
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

# Apply preprocessing to all texts
def preprocess_texts(texts):
    return [preprocess_text(text) for text in texts]

# Vectorize texts
def vectorize_texts(texts):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    return tfidf_matrix, vectorizer

# Train the model using logistic regression
def train_model(texts, intents):
    # Vectorize the texts
    tfidf_matrix, vectorizer = vectorize_texts(texts)
    
    # Train a logistic regression model
    model = LogisticRegression(max_iter=1000)
    model.fit(tfidf_matrix, intents)
    
    return model, vectorizer

# Intent-to-response mapping
def intent_to_response(intent, confidence):
    responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Any time!"],
    "help": ["I'm here to help. What do you need?", "Sure, how can I assist?"],
    "capabilities": ["I'm a chatbot built to answer simple questions!", "I can chat and help you!"],
    "unknown": ["Sorry, I don't understand that."]
    }
    
    # Set confidence threshold
    confidence_threshold = 0.2
    
    # if the confidence is below the threshold, return a unknown response, else a random response from the intent
    if (max(confidence[0]) < confidence_threshold):
        return random.choice(responses["unknown"])
    else:
        return random.choice(responses[intent])

# Chat loop
def chat_loop(model, vectorizer):
    print("Chatbot is ready! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        # Preprocess user input
        preprocessed_input = preprocess_text(user_input)
        
        # Transform input using the vectorizer
        input_tfidf = vectorizer.transform([preprocessed_input])
        
        # Predict intent
        intent = model.predict(input_tfidf)[0]
        
        # Get response based on intent
        response = intent_to_response(intent, model.predict_proba(input_tfidf))
        
        print(f"Chatbot: {response}")
        
# Main function to run the chatbot
if __name__ == "__main__":
    # Load and preprocess data
    data = load_data('intents.csv')
    texts, intents = split_data(data)
    preprocessed_texts = preprocess_texts(texts)
    
    # Train the model
    model, vectorizer = train_model(preprocessed_texts, intents)

    # Start the chat loop
    chat_loop(model, vectorizer)