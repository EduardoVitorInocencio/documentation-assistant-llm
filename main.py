from venv import create

from numpy import source
from backend.core import run_llm
from streamlit_chat import message
import streamlit as st

st.header("LangChain Chatbot - Documentation helper bot")


prompt  = st.text_input("Prompt", placeholder="Ask me anything about LangChain...")

if "user_prompt_history" not in st.session_state:
    st.session_state['user_prompt_history'] = []

if "chat_answer_history" not in st.session_state:
    st.session_state['chat_answer_history'] = []

def create_sources_string(source_urls: set[str]) -> str:
    if not source_urls:
        return ""
    
    source_list = list(source_urls)
    source_list.sort()
    sources_string = "sources:\n"
    
    for i, source in enumerate(source_list):
        sources_string += f"{i+1}. {source}\n"
    return sources_string


if prompt:
    with st.spinner("Gerating response..."):
        generate_response = run_llm(query=prompt)
        sources = set([doc.metadata["source"] for doc in generate_response["source_documents"]])
        st.text(generate_response["result"])

        formatted_response = f"{generate_response['result']}\n\n {create_sources_string(sources)}"

        st.session_state['user_prompt_history'].append(prompt)
        st.session_state['chat_answer_history'].append(formatted_response)

if st.session_state['chat_answer_history']:
    for generated_response, user_query in zip(st.session_state['chat_answer_history'], st.session_state['user_prompt_history']):
        message(user_query, is_user=True)
        message(generated_response, is_user=False)