import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))


st.markdown(
    "<h1 style='text-align:center;'>Chatbot Form</h1>",
    unsafe_allow_html=True
)


user_input = st.text_input("Enter your query:")

if st.button("Submit"):
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=user_input
    )

    st.write(response.text)