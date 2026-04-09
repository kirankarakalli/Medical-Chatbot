from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from typing import List
from langchain.schema import Document

def load_pdf_files(data):
    loader=DirectoryLoader(data,glob="*.pdf",loader_cls=PyPDFLoader)
    documents=loader.load()
    return documents


def filter_to_minimal_docs(docs:List[Document])->List[Document]:
    """
    Given a liast of document objects,return a
    new List of document objects containing only 
    source in metedata and the original page content
    """

    minimal_docs: List[Document]=[]
    for doc in docs:
        src=doc.metadata.get('source')
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source":src}
            )
        )
    return minimal_docs


def text_split(docs):
    text_spliiter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100)
    text_chunk=text_spliiter.split_documents(docs)
    return text_chunk


def download_embeddings():
    """
    Download and return the huggingface embeddings model.
    """
    model_name="sentence-transformers/all-MiniLM-L6-V2"
    embeddings=HuggingFaceBgeEmbeddings(
        model_name=model_name
    )
    return embeddings

