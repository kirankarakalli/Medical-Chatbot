from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
INDEX_NAME = os.getenv('INDEX_NAME', 'medical-chatbot')
MODEL_NAME = os.getenv('MODEL_NAME', 'gpt-3.5-turbo')

if not PINECONE_API_KEY or not OPENAI_API_KEY:
    raise ValueError("Missing required API keys in .env")
