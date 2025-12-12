from flask import Flask, request, jsonify, render_template
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from src.prompt import *
import os
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

# Global variables for lazy loading
embeddings = None
docsearch = None
retriever = None
rag_chain = None

def initialize_rag_chain():
    """Initialize RAG chain components lazily on first request"""
    global embeddings, docsearch, retriever, rag_chain
    
    if rag_chain is not None:
        return rag_chain
    
    print("Initializing RAG chain... This may take a moment on first request.")
    
    # Load embeddings
    embeddings = download_hugging_face_embeddings()
    
    # Connect to Pinecone
    index_name = "medical-chatbot"
    docsearch = PineconeVectorStore.from_existing_index(
        index_name=index_name,
        embedding=embeddings
    )
    retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    
    # Initialize chat model
    chatModel = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GEMINI_API_KEY,
        convert_system_message_to_human=True
    )
    
    # Create prompt
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )
    
    # Create chains
    question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    
    print("RAG chain initialized successfully!")
    return rag_chain



@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    
    # Initialize chain on first request (lazy loading)
    chain = initialize_rag_chain()
    
    response = chain.invoke({"input": msg})
    print("Response : ", response["answer"])
    return str(response["answer"])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)