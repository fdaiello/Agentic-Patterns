# 📚 Advanced RAG Pipeline: Structured Book Search with LangChain, Qdrant, and OpenAI

This advanced example demonstrates a Retrieval-Augmented Generation (RAG) pipeline using [LangChain](https://python.langchain.com/), [Qdrant](https://qdrant.tech/), and [OpenAI](https://platform.openai.com/). It features structured query parsing, dynamic filtering, and interactive Q&A over a CSV of book data.

---

## 📂 What does this script do?

1. **Loads your OpenAI API key** from a `.env` file.
2. **Loads book data** from a CSV file using LangChain's community CSVLoader.
3. **Embeds the book data** using OpenAI embeddings.
4. **Stores the embeddings** in an in-memory Qdrant vector database.
5. **Defines a Pydantic model** for structured query extraction (year, genre).
6. **Uses an LLM to parse user queries** into structured search filters.
7. **Dynamically filters the vector store** using Qdrant's advanced filtering.
8. **Sets up a RetrievalQA chain** with a ChatOpenAI LLM and the filtered retriever.
9. **Lets you ask questions** about the books in an interactive loop.

---

## 🧑‍💻 Code Walkthrough

### 1. **Setup and Authentication**
- Loads your OpenAI API key from `.env` using `python-dotenv`.
- Initializes the LLM and embeddings with your API key (automatically from environment).

### 2. **Data Loading**
- Loads book data from `./src/RAG-file/dataset_small.csv` using the community CSVLoader, including metadata columns.

### 3. **Embeddings and Vector Store**
- Embeds the book data with `OpenAIEmbeddings`.
- Stores the embeddings in an in-memory Qdrant vector database.

### 4. **Structured Query Parsing**
- Defines a Pydantic model (`BookSearch`) for expected search fields (year, genre).
- Uses a `PydanticOutputParser` and a prompt template to instruct the LLM to extract these fields from user queries.

### 5. **Dynamic Filtering**
- Converts the parsed LLM output into a Qdrant filter for targeted retrieval.

### 6. **RetrievalQA Chain**
- Sets up a RetrievalQA chain with a `ChatOpenAI` LLM and the Qdrant retriever, using the dynamic filter.

### 7. **Interactive Q&A**
- Enters a loop where you can ask questions about the books.
- Type `exit` or `quit` to end the session.
- Prints the number of source documents retrieved and the answer.

---

## 🚀 How to Run

1. **Install dependencies:**
   ```bash
   pip install langchain langchain-community langchain-openai qdrant-client python-dotenv pydantic
   ```
2. **Set your OpenAI API key** in a `.env` file at the project root:
   ```env
   OPENAI_API_KEY=sk-...
   ```
3. **Ensure your CSV file** is at `./src/RAG-file/dataset_small.csv`.
4. **Run the script:**
   ```bash
   python src/RAG-file/main_advanced.py
   ```

---

## 📝 Example Output

```
Hi im an AI librarian what can I help you with?
> Find me a fantasy book from 1954
2
The Lord of the Rings is a fantasy novel written by J.R.R. Tolkien in 1954.

Hi im an AI librarian what can I help you with?
> exit
Goodbye!
```

---

## 🧠 Concepts Learned
- **RAG (Retrieval-Augmented Generation):** Combines retrieval of relevant documents with LLM generation.
- **Structured Query Parsing:** Uses LLM and Pydantic to extract structured search fields from natural language.
- **Dynamic Filtering:** Applies filters to the vector store for targeted retrieval.
- **Embeddings & Vector Store:** Converts text to vectors and stores them for similarity search.
- **RetrievalQA Chain:** Combines retriever and LLM for question answering.

---

## 🟣 What is Qdrant?

[Qdrant](https://qdrant.tech/) is an open-source vector database designed for storing and searching embeddings (vector representations of data). It enables fast and scalable similarity search, which is essential for Retrieval-Augmented Generation (RAG) and other AI applications. In this example, Qdrant is used in-memory to store and retrieve book embeddings, allowing the AI to quickly find relevant information based on your questions and filters.

---

## 📚 Resources
- [LangChain Documentation](https://python.langchain.com/)
- [Qdrant Documentation](https://qdrant.tech/documentation/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

---

Happy experimenting! 🚀
