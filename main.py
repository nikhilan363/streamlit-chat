import streamlit as st
from ollama import chat
st.title("My AI Bot: Alexa")
name= "Nikhila"
st.write("Welcome, ",name)
question = st.text_input("Ask a question")
if st.button("Ask"):
    #st.write("you asked:", question)
    response = chat(model = "Llama3.2", messages = [
        {
            "role": "system",
            "content": "You are a friendly tutor. you explain conceptsin a very simple way. Explain in 50 words max."
        },
        {
            "role": "user",
            "content": question
        }
    ])
    answer = response.message.content
    st.write(answer) 
#dropdown 
#options = ["C+", "Java", "Python"]
#choice = st.selectbox("Select your favourite language:", options)
#st.write(f"you selected {choice}")