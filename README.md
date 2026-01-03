AI Customer Service Agent using Retrieval-Augmented Generation (RAG)
Overview

This project implements an AI-based Customer Service Agent that answers common telecom support queries using a Retrieval-Augmented Generation (RAG) approach. The system retrieves relevant historical customer–agent conversations and support tickets from a FAISS vector database and generates accurate, context-aware responses using the Perplexity API.

To ensure reliability and safety, the system applies simple escalation rules that route uncertain or complex queries to a human support agent.

Problem Statement

Telecom customer support teams handle a large number of repetitive queries related to internet connectivity, SIM activation, billing issues, and service configuration. Manually resolving these issues is time-consuming and inefficient.

The goal of this project is to build an intelligent assistant that can automatically answer common queries using historical data, while escalating unresolved or low-confidence cases to human agents.

Key Features

Semantic retrieval over telecom tickets and agent–customer dialogues

Retrieval-Augmented Generation (RAG) architecture

FAISS-based vector search for fast similarity retrieval

Perplexity API for high-quality answer generation

Source ticket/dialogue ID tracking

Rule-based escalation to human agents

REST API endpoint for query handling

Datasets

Telecom Agent–Customer Interaction Text
Contains real-world conversational data between telecom agents and customers.

Customer Support Ticket Dataset (Optional)
Includes structured customer issues and resolutions.

These datasets form the knowledge base indexed in FAISS.
System Architecture
User Query
   |
   v
Query Embedding
   |
   v
FAISS Vector Index
   |
   v
Relevant Tickets and Dialogues
   |
   v
Context Construction
   |
   v
Perplexity API (Answer Generation)
   |
   v
Answer with Source IDs
   |
   v
Escalation Decisionechnology Stack

Programming Language: Python

RAG Framework: LangChain

Vector Database: FAISS

Embedding Model: SentenceTransformers

Language Model for Generation: Perplexity API (Sonar)

API Framework: FastAPI

Workflow:

Historical telecom tickets and conversations are cleaned and converted into documents.

Each document is embedded using a sentence transformer model.

Embeddings are stored and indexed using FAISS.

When a user submits a query:

The query is embedded.

FAISS retrieves the most relevant tickets and dialogues.

Retrieved content is used as context for answer generation.

The Perplexity API generates a response grounded in the retrieved context.

Escalation rules determine whether the query should be forwarded to a human agent.

Escalation Logic:

A query is escalated to a human agent when:

No relevant documents are retrieved from FAISS

The generated answer indicates uncertainty or insufficient information

The query is outside the scope of the available historical data

API Endpoint:
POST /ask

Request Body

{
  "query": "Why is my mobile data not working?"
}


Response

{
  "question": "Why is my mobile data not working?",
  "answer": "The issue may be caused by temporary network problems or incorrect data settings.",
  "sources": ["ticket_245", "ticket_812"],
  "escalate_to_human": false
}

Use Cases:

Telecom customer support automation

Reduction of repetitive support tickets

Self-service customer assistance portals

Intelligent ticket triaging systems

Advantages:

Faster response time for customer queries

Reduced workload for human support agents

Answers grounded in real historical data

Efficient and scalable retrieval using FAISS

Future Enhancements:

Confidence scoring based on FAISS similarity distance

Multi-language support

Multi-turn conversation handling

Analytics dashboard for escalated queries

Integration with CRM and ticketing platforms

Project Summary:

This project demonstrates a practical application of Retrieval-Augmented Generation by combining FAISS-based semantic retrieval with Perplexity-powered answer generation to build an effective and reliable AI customer service assistant for telecom support.
