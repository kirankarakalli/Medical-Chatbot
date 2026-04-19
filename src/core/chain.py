from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from src.config.settings import OPENAI_API_KEY, MODEL_NAME

def get_qa_chain(vector_store):
    llm=ChatOpenAI(model=MODEL_NAME,api_key=OPENAI_API_KEY)
    chain=RetrievalQA.from_chain_type(llm=llm,retriever=vector_store.as_retriever())
    return chain

