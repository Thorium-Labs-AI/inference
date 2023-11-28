# Thorium - RAG Utility for GPT-based chat

Thorium is a REST API to provide a quick way to store documents in vector storage for multiple tenants and to use them for retrieval augmented generation in chat application.
Its capabilities have more or less been covered by recent changes made to the OpenAI API.

# Technologies

The API is a FastAPI application, served through AWS Fargate.
The semantic search and vector storage is done with Pinecone.
The embeddings and chat responses are created using the OpenAI API.
I used GitHub actions for deployment and Terraform for IaC.
