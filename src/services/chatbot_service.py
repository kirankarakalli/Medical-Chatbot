from src.core.embeddings import get_embeddings
from src.core.vector_store import get_vector_store
from src.core.chain import get_qa_chain


def get_chain():
    embeddings=get_embeddings()
    vector_store=get_vector_store(embeddings)
    qa_chain=get_qa_chain(vector_store)
    return qa_chain

def get_response(question, chain):
    response=chain.invoke({"query":question})
    return response["result"]
