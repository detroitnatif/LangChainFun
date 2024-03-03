import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os

from langchain_community.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)



def main():
    st.set_page_config(
        page_title="TylerGPT",
        page_icon="♓︎",
    
    )

    load_dotenv()
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        st.error("You need to set your OpenAI API key in a .env file")
        return
    else:
        st.write("OpenAI API Key is set")


    chat = ChatOpenAI()

    st.header("TylerGPT")
    
    message("Hello, I'm Tyler's Chatbot, Ask me anything about him!")
    message("What are Tyler's hobbies?", is_user=True)


    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful assistant to answer questions about Tyler"),
        ]

    with st.sidebar:
        user_input = st.text_input("Ask away")

    if user_input:
        message(user_input, is_user=True)
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.spinner:
            response = chat(st.session_state.messages)
        message(response.content)



if __name__ == "__main__":
    main()