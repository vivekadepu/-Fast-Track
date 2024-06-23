import streamlit as st
from langchain.llms import OpenAI

# App title
st.title('🚀Fast Track')

# Directly define your OpenAI API key here
openai_api_key = st.secrets['openai_api_key']

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    response = llm(input_text)
    return response

# Main form for user input
with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')

    # Initialize the response variable
    response = None
    
    # API Key validation
    if not openai_api_key:
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    elif not openai_api_key.startswith('sk-'):
        st.error('The API key should start with "sk-"', icon='🚫')
    elif submitted:
        response = generate_response(text)
    
    # Display the response if available
    if response:
        st.info(response)
        
