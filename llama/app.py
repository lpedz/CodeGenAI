import streamlit as st  # Streamlit is a library used for creating web applications with simple Python scripts.
from langchain.prompts import PromptTemplate  # Used to give prompts to the LLM
from langchain.llms import CTransformers

## Function To get response from LLaMA 2 model
def getLLamaResponse(input_text, programming_language):
    ### LLaMA2 model
    llm = CTransformers(
        model='TheBloke/Llama-2-7B-Chat-GGML',
        model_type='llama',
        config={'max_new_tokens': 256, 'temperature': 0.5}
    )  # CTransformers is used to call the LLaMA 2 model.

    ## Prompt Template: the prompt that is given to the LLaMA-2 model, which is then processed to generate the output
    template = """
        Write a functional code snippet in {programming_language} for the following task:
        {input_text}
    """
    prompt = PromptTemplate(input_variables=["programming_language", "input_text"], template=template)

    ## Generate the response from the LLaMA 2 model
    response = llm(prompt.format(programming_language=programming_language, input_text=input_text))
    print(response)
    return response

# Setting Streamlit UI
st.set_page_config(
    page_title="Generate Code Snippets",
    page_icon='🤖',
    layout='centered',
    initial_sidebar_state='collapsed'
)

st.header("Generate Code Snippets")

input_text = st.text_area("Describe the task for which you need a code snippet")

## Creating a dropdown to select the programming language
programming_language = st.selectbox('Select the Programming Language', ('Python', 'JavaScript', 'Java', 'C++'), index=0)

# Button to submit the request
submit = st.button("Generate")

## Display the final response
if submit:
    st.code(getLLamaResponse(input_text, programming_language), language=programming_language.lower())
