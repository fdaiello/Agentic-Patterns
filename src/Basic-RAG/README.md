# 🧑‍💻 Basic Retrieval-Augmented Generation (RAG) Example with LangChain

This example demonstrates how to build a simple Retrieval-Augmented Generation (RAG) pipeline using [LangChain](https://python.langchain.com/) and OpenAI. It loads a Wikipedia article, splits it into chunks, embeds the text, stores it in a vector database, and lets you ask questions about the content interactively.

---

## 📂 What This Code Does

1. **Loads environment variables** (your OpenAI API key) from a `.env` file.
2. **Fetches a Wikipedia article** (about tea) using a web loader.
3. **Splits the article** into overlapping text chunks for better retrieval.
4. **Embeds the chunks** using OpenAI embeddings.
5. **Stores the embeddings** in a FAISS vector database for fast similarity search.
6. **Sets up a RetrievalQA chain** with a ChatOpenAI LLM and the retriever.
7. **Lets you ask questions** about the article in an interactive loop.

---

## 🚀 How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Set your OpenAI API key** in a `.env` file:
   ```env
   OPENAI_API_KEY=sk-...
   ```
3. **Run the script:**
   ```bash
   python main.py
   ```

---

## 🧩 Code Walkthrough

### 1. **Setup and API Key**
- Loads your OpenAI API key from `.env`.
- Prints debug info to confirm the key is loaded.

### 2. **Document Loading**
- Loads the Wikipedia page on tea using `WebBaseLoader`.
- Prints document info and a content preview.

### 3. **Text Splitting**
- Splits the document into 1000-character chunks with 200-character overlap using `RecursiveCharacterTextSplitter`.
- Prints chunk stats and a preview.

### 4. **Embeddings**
- Creates OpenAI embeddings for the chunks.
- Prints embedding info and a sample embedding.

### 5. **Vector Store**
- Stores the embeddings in a FAISS vector database for fast retrieval.

### 6. **RetrievalQA Chain**
- Sets up a RetrievalQA chain with a ChatOpenAI LLM and the retriever.

### 7. **Interactive Q&A**
- Enters a loop where you can ask questions about tea, and the LLM will answer using the Wikipedia content.

---

## 📝 Example Output

```
API Key loaded: Yes
API Key starts with: sk-...
📄 Number of documents loaded: 1
📝 First 500 characters of content:
Tea is an aromatic beverage ...
🔪 Original documents: 1
🧩 Split into chunks: 12
🧮 Embedding dimensions: 1536
Ask a question about tea
> What is green tea?
Green tea is ...
```

---

## 🧠 Concepts Learned
- **RAG (Retrieval-Augmented Generation):** Combines retrieval of relevant documents with LLM generation.
- **Chunking:** Splitting documents for better context and retrieval.
- **Embeddings:** Converting text to vectors for similarity search.
- **Vector Store:** Fast retrieval of relevant chunks.
- **RetrievalQA Chain:** Combines retriever and LLM for question answering.

---

## 📚 Resources
- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [FAISS](https://github.com/facebookresearch/faiss)

---

Happy experimenting! 🚀
