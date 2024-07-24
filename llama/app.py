import google.generativeai as genai
import os
import streamlit as st

# Set your API key here
apikey="[your api key]"

# Configure the Generative AI model
genai.configure(api_key=apikey)
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to generate code
def generate_code(context, language):
    prompt = f"Generate code for the following context:\n\n{context}\n\nin {language} language."
    response = model.generate_content(prompt)
    return response.text

# Streamlit page configuration
st.set_page_config(
    page_title="Generate Code",
    page_icon='🤖',
    layout='centered',
    initial_sidebar_state='collapsed'
)

# Streamlit app interface
st.header("Generate Code")

input_text = st.text_area("Describe the context you need code for")

# Creating a dropdown to select the programming language
programming_language = st.selectbox(
    'Select the programming language', 
    ('Python', 'JavaScript', 'Java', 'C++', 'Go', 'Ruby', 'C#', 'Swift', 'PHP', 'Kotlin', 'R', 'TypeScript', 'Scala', 'Perl'), 
    index=0
)

# Button to submit the request
submit = st.button("Generate")

# Display the final response
if submit:
    generated_code = generate_code(input_text, programming_language)
    st.code(generated_code, language=programming_language.lower())
