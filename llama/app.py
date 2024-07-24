import google.generativeai as genai
import os
import streamlit as st


apikey="AIzaSyCqO6PIgY80nLSW1iJyI4BvCe2PflVsloY"

genai.configure(api_key=apikey)

model = genai.GenerativeModel('gemini-1.5-flash')


def generate(text,style):
    response = model.generate_content("Genrate a story of the context"+text+"in the style of"+style)
    return response.text

st.set_page_config(
    page_title="Generate Code Snippets",
    page_icon='🤖',
    layout='centered',
    initial_sidebar_state='collapsed'
)

st.header("Generate Story")

input_text = st.text_area("Describe the context you need story for")

## Creating a dropdown to select the programming language
writingStyle = st.selectbox('Select the writing style',( '15th century', '5yr olds', 'Modern', 'simple'), index=0)

# Button to submit the request
submit = st.button("Generate")

## Display the final response
if submit:
    st.code(generate(input_text,writingStyle))