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
        st.error("Please set your OpenAI API key in a .env file")
        return
    else:
        st.write("OpenAI API Key is set")


    chat = ChatOpenAI()

    st.header("TylerGPT")
    
    message("Hello, I'm Tyler's Chatbot, Ask me anything about him!")
    message("What are Tyler's hobbies?", is_user=True)


    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="Hello, I'm Tyler's Chatbot, Ask me anything about him!"),
        ]

    with st.sidebar:
        user_input = st.text_input("Ask away")

    if user_input:
        
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.spinner("Thinking..."):
            response = chat(st.session_state.messages)
        
        st.session_state.messages.append(AIMessage(content=response.content))

    messages = st.session_state.get("messages", [])
    for i, msg in enumerate(messages):
        if i == 0:
            pass
        elif i % 2 == 0:
            message(msg.content, is_user=True, key= str(i) + "_user")
        else:
            message(msg.content, is_user=False, key= str(i) + "_ai")



if __name__ == "__main__":
    main()