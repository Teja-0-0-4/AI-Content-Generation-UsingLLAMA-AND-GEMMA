## front end to interact with the API

import requests
import streamlit as st


def get_llama_response(input_text):
    response = requests.post("http://localhost:8000/essay_llama/invoke", json={'input': {'topic': input_text}})
    try:
        response_json = response.json()
        return response_json['output']['content']  # Navigate to the content field explicitly
    except Exception as e:
        st.error(f"Error parsing LLAMA response: {e}")
        return "No content available"


def get_gemma_response(input_text):
    response = requests.post("http://localhost:8000/poem_gemma/invoke", json={'input': {'topic': input_text}})
    try:
        response_json = response.json()
        return response_json['output']['content']  # Navigate to the content field explicitly
    except Exception as e:
        st.error(f"Error parsing GEMMA response: {e}")
        return "No content available"


st.title("Langchain demo with LLAMA and GEMMA")
input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write a poem on")

if input_text:
    st.write(get_llama_response(input_text))
if input_text1:
    st.write(get_gemma_response(input_text1))
