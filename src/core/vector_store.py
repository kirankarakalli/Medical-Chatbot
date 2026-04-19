from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from src.config.settings import PINECONE_API_KEY, INDEX_NAME


def get_vector_store(embeddings):
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(INDEX_NAME)
    vector_store = PineconeVectorStore(index=index, embedding=embeddings)
    return vector_store

