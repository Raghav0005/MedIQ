from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain.vectorstores import Pinecone
import pinecone
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")

#print(PINECONE_API_KEY)

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

pinecone.Pinecone(api_key = os.getenv("PINECONE_API_KEY"))
index_name = "medical-chatbot"
docsearch = Pinecone.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)
