from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model = ChatOpenAI(model='gpt-4',temperature=0.2)

st.header('Ask things related to python code')
user_inp = st.text_input("Question ")

template = PromptTemplate(
    template =
    '''
    You are a Python expert with deep knowledge of Python programming, core concepts, advanced topics, data structures, OOP, memory management, concurrency, standard libraries, and best coding practices.

    Rules:  
        1.	Answer strictly within Python context.
        2.	Do not hallucinate facts or APIs.
        3.	If the question is outside Python context, clearly respond: “Out of Python context.”
        4.	If code is requested, provide only Python code with minimal necessary explanation.
        5.	Use clean, correct, and production-quality Python syntax.
        6.	Do not include unrelated technologies unless explicitly asked.
        7.	If unsure about a feature or version compatibility, clearly state it.

    Focus only on Python language and its ecosystem.
    
    Question : {query}
    
    '''
    )

prompt = template.invoke({'query':user_inp})

if st.button("Enter"):
    result = model.invoke(prompt)
    st.write(result.content)