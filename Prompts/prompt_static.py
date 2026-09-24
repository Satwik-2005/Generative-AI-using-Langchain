from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

import streamlit as st

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="openai/gpt-oss-120b", task="text-generation")

model = ChatHuggingFace(llm=llm)

st.header("Reaserch Tool")
user_input = st.text_input("Enter your Prompt here")

if st.button('summarize'):
    result = model.invoke(user_input)
    st.write(result.content)