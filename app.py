import os
import streamlit as st

# Force install nltk if missing
os.system("pip install nltk")

import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load chatbot model
chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    """
    Simple rule-based chatbot with AI-generated responses.
    """
    user_input = user_input.lower()  # Normalize input for better matching

    if "symptom" in user_input:
        return "Please consult a doctor for accurate advice."
    elif "appointment" in user_input:
        return "Would you like to schedule an appointment with the doctor?"
    elif "medication" in user_input:
        return "It's important to take prescribed medicines regularly. If you have concerns, consult your doctor."
    else:
        response = chatbot(user_input, max_length=100, num_return_sequences=1)
        return response[0]['generated_text']

def main():
    """
    Streamlit app for the Healthcare Assistant Chatbot.
    """
    st.title("Healthcare Assistant Chatbot")

    user_input = st.text_input("How can I assist you today?")
    
    if st.button("Submit"):
        if user_input.strip():  # Check if input is not empty
            with st.spinner("Processing your query, please wait..."):
                response = healthcare_chatbot(user_input)
            st.write("**Healthcare Assistant:**", response)
        else:
            st.warning("Please enter a message to get a response.")

if __name__ == "__main__":
    main()
