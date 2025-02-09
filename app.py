import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
chatbot = pipeline("text-generation", model="distilgpt2")
def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "please consult doctor for accurate advice"
    elif "appointment" in user_input:
        return "Would you like to shedule appointment with the doctor?"
    elif "medication" in user_input:
        return "It's important to take prescibed medicines regularly. If you have concerns,consult your doctor"
    else:
        response=chatbot(user_input,max_length=500,num_return_sequences=2)
    return response[0]['generated_text']
def main():
    st.title("Healthcare Assistant Chatbot")
    user_input=st.text_input("how can I assist today")
    if st.button("submit"):
        if user_input:
            st.write("user :",user_input)
            with st.spinner("processing you query,please wait"):
                response=healthcare_chatbot(user_input)
            st.write("Healthcare Assistant : ",response)
            print(response)

        else:
            st.write("please enter a message to get response")

if __name__ == "__main__":
    main()
