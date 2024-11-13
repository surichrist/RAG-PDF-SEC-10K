import streamlit as st
import os
from langchain_community.llms import Ollama

from models import get_list_of_models
from llm import getStreamingChain
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from document_loader import load_documents_into_database

EMBEDDING_MODEL = "nomic-embed-text"
PATH = "10k"


st.title("Alemeno RAG 📚")

if "list_of_models" not in st.session_state:
    st.session_state["list_of_models"] = get_list_of_models()

selected_model = st.sidebar.selectbox(
    "Select a model:", st.session_state["list_of_models"]
)

if st.session_state.get("ollama_model") != selected_model:
    st.session_state["ollama_model"] = selected_model
    st.session_state["llm"] = Ollama(model=selected_model)


# Folder selection
folder_path = st.sidebar.text_input("Enter the folder path:", PATH)

if folder_path:
    if not os.path.isdir(folder_path):
        st.error(
            "The provided path is not a valid directory. Please enter a valid folder path."
        )
    else:
        if st.sidebar.button("Index Documents"):
        
            with st.spinner(
                "Creating embeddings and loading documents into Chroma..."
            ):
                db = load_documents_into_database(
                    EMBEDDING_MODEL, folder_path
                )
            st.session_state["db"] = db
            st.info("All set to answer questions!")
else:
    st.warning("Please enter a folder path to load documents into the database.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
if "db" not in st.session_state:
    try:
        st.session_state["db"] = Chroma(
        embedding_function=OllamaEmbeddings(model="nomic-embed-text"),
        persist_directory="cdb"
    
)
    except ValueError:
        st.warning("No data found, please Index Documents")
        
        

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Question"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = getStreamingChain(
            prompt,
            st.session_state.messages,
            st.session_state["llm"],
            st.session_state["db"],
        )
        response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})