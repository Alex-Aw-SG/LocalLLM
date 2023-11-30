import pinecone
from langchain.vectorstores import Pinecone
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.llms import CTransformers
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
import joblib


#Function to pull index data from Pinecone
def pull_from_pinecone(pinecone_apikey,pinecone_environment,pinecone_index_name,embeddings):

    pinecone.init(
    api_key=pinecone_apikey,
    environment=pinecone_environment
    )

    index_name = pinecone_index_name

    index = Pinecone.from_existing_index(index_name, embeddings)
    return index

def create_embeddings():
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings

#This function will help us in fetching the top relevent documents from Pinecone Index
def get_similar_docs(index,query,k=1):

    similar_docs = index.similarity_search(query, k=k)
    return similar_docs

#Function to query local LLM
def get_answer(docs,user_input):
    config = {'max_new_tokens': 4098, 'temperature': 0, 'context_length': 4098}

    llm = CTransformers(model='enter/model/path/llama-2.gguf', model_type='llama', config=config)

    chain = load_qa_chain(llm=llm, chain_type="stuff")

    response = chain.run(input_documents=docs, question=user_input, token_max=4000)

    return response

