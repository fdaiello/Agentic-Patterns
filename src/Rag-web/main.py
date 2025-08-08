from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import WebBaseLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Debug: Check if API key is loaded
api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key loaded: {'Yes' if api_key else 'No'}")
print(f"API Key starts with: {api_key[:10] if api_key else 'None'}...")

loader = WebBaseLoader("https://en.wikipedia.org/wiki/Tea")
documents = loader.load()

# Debug: Inspect the documents object
print(f"📄 Number of documents loaded: {len(documents)}")
print(f"📋 Type of documents: {type(documents)}")
print(f"📋 Type of first document: {type(documents[0])}")
print(f"🔍 Document attributes: {dir(documents[0])}")
print("📝 First 500 characters of content:")
print(documents[0].page_content[:500])
print(f"📊 Document metadata: {documents[0].metadata}")
print("-" * 50)

# Better splitter for Wikipedia content
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,  # Add overlap for better context
    separators=["\n\n", "\n", ". ", " ", ""],  # Try these separators in order
)
texts = text_splitter.split_documents(documents)

# Debug: Inspect the splitting results
print(f"🔪 Original documents: {len(documents)}")
print(f"🧩 Split into chunks: {len(texts)}")
print(f"📏 First chunk length: {len(texts[0].page_content)}")
print("📝 First chunk content preview:")
print(texts[0].page_content[:200] + "...")
print(f"📊 First chunk metadata: {texts[0].metadata}")
print("-" * 50)

embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

# Debug: Inspect the embeddings object
print("🔬 Embeddings Object Analysis:")
print(f"📋 Type: {type(embeddings)}")
print(
    f"🔍 Available methods: {[method for method in dir(embeddings) if not method.startswith('_')]}"
)
print(f"📊 Model being used: {getattr(embeddings, 'model', 'Not specified')}")

# Test embedding a small text
sample_embedding = embeddings.embed_query("tea")
print(f"🧮 Embedding dimensions: {len(sample_embedding)}")
print(f"🔢 First 5 values: {sample_embedding[:5]}")
print("-" * 50)

docsearch = FAISS.from_documents(texts, embeddings)

qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY")),
    chain_type="stuff",
    retriever=docsearch.as_retriever(),
)

while True:
    query = input("Ask a question about tea (or type 'exit' to quit):\n")
    if query.lower() in {"exit", "quit"}:
        print("Goodbye!")
        break
    print(qa.run(query))
