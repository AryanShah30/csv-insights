import streamlit as st
from langchain_helper import create_vector_db, get_qa_chain


st.set_page_config(page_title="CSV Insight", page_icon="📈", layout="centered")
st.title("📈🔍 CSV Insight: Interactive Data Explorer and Q&A")

file_upload = st.file_uploader("Upload your file", type=['csv'])

btn = st.button("Create a Knowledge Base")
if btn:
    if file_upload is not None:
        with open("uploaded_file.csv", "wb") as f:
            f.write(file_upload.getbuffer())
        create_vector_db("uploaded_file.csv")
        st.success("Knowledge Base Created")
    else:
        st.error("Please upload a file first.")

st.write("")

question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.success(response["result"])
