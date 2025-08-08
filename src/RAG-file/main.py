
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env")

from langchain_community.document_loaders import CSVLoader
from langchain_community.vectorstores import Qdrant
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA

loader = CSVLoader(
    file_path="./src/RAG-file/dataset_small.csv", source_column="title"
)
data = loader.load()

embeddings = OpenAIEmbeddings()

qdrant_docsearch = Qdrant.from_documents(
    data,
    embeddings,
    location=":memory:",
    collection_name="book"
)

qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    chain_type="stuff",
    retriever=qdrant_docsearch.as_retriever(),
    return_source_documents=True
)

while True:
    user_input = input("Hi, I'm an AI librarian. What can I help you with?\n")
    if user_input.lower() in {"exit", "quit"}:
        print("Goodbye!")
        break
    book_request = (
        "You are a librarian. Help the user answer their question. Do not provide the ISBN."
        f"\nUser: {user_input}"
    )
    result = qa({"query": book_request})
    print(len(result['source_documents']))
    print(result["result"])
