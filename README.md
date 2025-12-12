# 🏥 End-to-End Medical Chatbot using RAG

An intelligent medical chatbot built using Retrieval-Augmented Generation (RAG) that provides accurate medical information by combining the power of vector databases, embeddings, and large language models. 

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Demo](#demo)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project implements an end-to-end medical chatbot that uses Retrieval-Augmented Generation (RAG) to answer medical queries. The system processes medical documents, stores them in a vector database, and retrieves relevant information to provide accurate, context-aware responses using Google's Gemini AI model. 

## ✨ Features

- **RAG-based Architecture**: Combines document retrieval with generative AI for accurate responses
- **Vector Database Integration**: Uses Pinecone for efficient similarity search
- **Modern UI**:  Clean and intuitive chat interface
- **Real-time Responses**: Fast query processing and response generation
- **Context-Aware**:  Retrieves relevant medical information before generating answers
- **Scalable**: Serverless vector database deployment on AWS
- **PDF Processing**: Automatically processes and indexes medical PDF documents

## 🏗️ Architecture

The system follows a RAG (Retrieval-Augmented Generation) architecture:

1. **Document Processing**: PDF documents are loaded, processed, and split into chunks
2. **Embedding Generation**: Text chunks are converted to embeddings using HuggingFace models
3. **Vector Storage**: Embeddings are stored in Pinecone vector database
4. **Query Processing**: User queries are embedded and similar documents are retrieved
5. **Response Generation**: Retrieved context is passed to Gemini AI for answer generation

## 🛠️ Technologies Used

- **LangChain**: Framework for building LLM applications
- **Google Gemini AI**: Large language model for response generation
- **Pinecone**: Vector database for similarity search
- **HuggingFace**:  Sentence transformers for embeddings
- **Flask**: Web framework for the backend
- **Python**:  Core programming language
- **PyPDF**:  PDF document processing

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/pawanchinnu17/End-to-End-Medical_chatbot_using_RAGS.git
cd End-to-End-Medical_chatbot_using_RAGS
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

1. **Create a `.env` file** in the root directory with the following variables: 

```env
PINECONE_API_KEY=your_pinecone_api_key
GEMINI_API_KEY=your_gemini_api_key
```

2. **Add your medical documents** to the `data/` directory in PDF format

3. **Create and populate the vector database**:
```bash
python store_index.py
```

## 🚀 Usage

1. **Start the Flask application**:
```bash
python app.py
```

2. **Access the application**:
Open your browser and navigate to `http://localhost:8080`

3. **Start chatting**:
Type your medical queries and get instant, context-aware responses!

## 🎬 Demo

<img width="1326" height="785" alt="demo med app" src="https://github.com/user-attachments/assets/456e394f-63e5-4f34-8ecb-a17b4b5d6ba3" />


The chatbot provides detailed medical information on various topics.  In the example above, the chatbot explains the effects of high alcohol levels and symptoms of co-alcohol dependence, demonstrating its ability to provide comprehensive medical information.

## 📁 Project Structure

```
End-to-End-Medical_chatbot_using_RAGS/
├── data/                      # Medical PDF documents
├── src/                       # Source code modules
│   ├── helper. py             # Helper functions for data processing
│   └── prompt.py             # System prompts for the chatbot
├── static/                    # Static files (CSS, JS, images)
├── templates/                 # HTML templates
│   └── chat.html             # Main chat interface
├── research/                  # Jupyter notebooks for experimentation
├── app.py                     # Flask application
├── store_index.py            # Script to create vector database
├── requirements.txt          # Python dependencies
├── setup.py                  # Package setup file
├── . gitignore               # Git ignore file
└── README.md                # This file
```

## 🔍 How It Works

### 1. Data Ingestion and Indexing
- Medical PDF documents are loaded from the `data/` directory
- Documents are filtered and split into manageable chunks
- Each chunk is converted into vector embeddings using HuggingFace models
- Embeddings are stored in Pinecone vector database for fast retrieval

### 2. Query Processing
- User submits a medical query through the web interface
- Query is converted into an embedding vector
- Pinecone performs similarity search to find the top-k relevant document chunks

### 3. Response Generation
- Retrieved documents provide context for the query
- Context + query are passed to Google's Gemini AI model
- Model generates a comprehensive, context-aware response
- Response is displayed to the user in the chat interface

### Key Components: 

- **Embeddings**: `sentence-transformers` model from HuggingFace
- **Vector Store**: Pinecone with cosine similarity metric (384 dimensions)
- **LLM**: Google Gemini 2.5 Flash model
- **Retrieval**:  Top-3 similar documents for each query

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.  For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


 
