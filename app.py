import os
from dotenv import load_dotenv
import streamlit as st
from query_func import *
from upload_func import *

load_dotenv()
pinecone_apikey = os.getenv("PINECONE_APIKEY")
pinecone_environment = os.getenv("PINECONE_ENV")
pinecone_index_name = os.getenv("PINECONE_INDEX")

st.set_page_config(page_title="Your personal local LLM")
st.title("LLM at your fingertips")

tab_titles = ['Queries', 'Upload Data']
tabs = st.tabs(tab_titles)

#Query LLM
with tabs[0]:
    def main():

        st.header("Query Your Own Data")
        st.write("Enter question here:")
        user_input = st.text_input("🔍")

        if user_input:

            embeddings=create_embeddings()

            index = pull_from_pinecone(pinecone_apikey, pinecone_environment, pinecone_index_name, embeddings)

            relavant_docs=get_similar_docs(index,user_input)

            response=get_answer(relavant_docs,user_input)

            st.write(response)

    if __name__ == '__main__':
        main()

#Uploading Data
with tabs[1]:

    def main():

        st.header("Upload your files...📁 ")

        pdf = st.file_uploader("Only PDF files allowed", type=["pdf"])

        if pdf is not None:
            with st.spinner('Wait for it...'):
                text = read_pdf_data(pdf)
                st.write("👉Reading PDF done")

                docs_chunks = split_data(text)

                st.write("👉Splitting data into chunks done")

                embeddings = create_embeddings_load_data()
                st.write("👉Creating embeddings instance done")

                push_to_pinecone(pinecone_apikey, pinecone_environment, pinecone_index_name, embeddings, docs_chunks)

            st.success("Successfully pushed the embeddings to Pinecone")

    if __name__ == '__main__':
        main()



