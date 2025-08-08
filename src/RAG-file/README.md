# 📚 RAG Pipeline: AI Librarian with LangChain, Qdrant, and OpenAI

This example demonstrates a simple Retrieval-Augmented Generation (RAG) pipeline using [LangChain](https://python.langchain.com/), [Qdrant](https://qdrant.tech/), and [OpenAI](https://platform.openai.com/). It loads a CSV of book data, embeds it, stores it in a vector database, and lets you ask questions about the books interactively.

---

## 📂 What does this script do?

1. **Loads your OpenAI API key** from a `.env` file.
2. **Loads book data** from a CSV file using LangChain's CSVLoader.
3. **Embeds the book data** using OpenAI embeddings.
4. **Stores the embeddings** in an in-memory Qdrant vector database.
5. **Sets up a RetrievalQA chain** with a ChatOpenAI LLM and the retriever.
6. **Lets you ask questions** about the books in an interactive loop.

---

## 🧑‍💻 Code Walkthrough

### 1. **Setup and Authentication**
- Loads your OpenAI API key from `.env` using `python-dotenv`.
- Initializes the LLM and embeddings with your API key (automatically from environment).

### 2. **Data Loading**
- Loads book data from `./src/RAG-file/dataset_small.csv` using `CSVLoader`.

### 3. **Embeddings and Vector Store**
- Embeds the book data with `OpenAIEmbeddings`.
- Stores the embeddings in an in-memory Qdrant vector database.

### 4. **RetrievalQA Chain**
- Sets up a RetrievalQA chain with a `ChatOpenAI` LLM and the Qdrant retriever.

### 5. **Interactive Q&A**
- Enters a loop where you can ask questions about the books.
- Type `exit` or `quit` to end the session.
- Prints the number of source documents retrieved and the answer.

---

## 🚀 How to Run

1. **Install dependencies:**
   ```bash
   pip install langchain langchain-community langchain-openai qdrant-client python-dotenv
   ```
2. **Set your OpenAI API key** in a `.env` file at the project root:
   ```env
   OPENAI_API_KEY=sk-...
   ```
3. **Ensure your CSV file** is at `./src/RAG-file/dataset_small.csv`.
4. **Run the script:**
   ```bash
   python src/RAG-file/main.py
   ```

---

## 📝 Example Output

```
Hi, I'm an AI librarian. What can I help you with?
> Who wrote The Hobbit?
2
J.R.R. Tolkien wrote The Hobbit.

Hi, I'm an AI librarian. What can I help you with?
> exit
Goodbye!
```

---


## 🧠 Concepts Learned
- **RAG (Retrieval-Augmented Generation):** Combines retrieval of relevant documents with LLM generation.
- **Embeddings:** Converts text to vectors for similarity search.
- **Vector Store:** Fast retrieval of relevant chunks using Qdrant.
- **RetrievalQA Chain:** Combines retriever and LLM for question answering.

---

## 🟣 What is Qdrant?

[Qdrant](https://qdrant.tech/) is an open-source vector database designed for storing and searching embeddings (vector representations of data). It enables fast and scalable similarity search, which is essential for Retrieval-Augmented Generation (RAG) and other AI applications. In this example, Qdrant is used in-memory to store and retrieve book embeddings, allowing the AI to quickly find relevant information based on your questions.

---

## 📚 Resources
- [LangChain Documentation](https://python.langchain.com/)
- [Qdrant Documentation](https://qdrant.tech/documentation/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)

---

Happy experimenting! 🚀
