# 🟣 How Filtering Works in Advanced RAG (Qdrant + LangChain)

This document explains how filtering is used in the advanced Retrieval-Augmented Generation (RAG) pipeline with Qdrant, LangChain, and OpenAI.

---

## 1. User Query → Structured Fields
- The user enters a natural language query (e.g., “Find me a fantasy book from 1954”).
- The LLM (via a prompt and PydanticOutputParser) extracts structured fields from the query, such as:
  - `genre`: "fantasy"
  - `year`: "1954"

## 2. Create Qdrant Filter
- The extracted fields are used to build a Qdrant filter object.
- This filter specifies conditions like:
  - `metadata.categories` must match the genre.
  - `metadata.published_year` must match the year.
- The filter is passed as `search_kwargs` to the Qdrant retriever.

## 3. Filtered Vector Search
- Qdrant uses the filter to only consider documents (books) that match the specified genre and year.
- It then performs a similarity search (using embeddings) within this filtered subset.

---

## 🔄 Flow: User Query → Filter → Vector Search → LLM

1. **User Query:**
   - User types a question (e.g., “Show me a science fiction book from 1965”).
2. **LLM Parses Query:**
   - The LLM, guided by a prompt and Pydantic schema, extracts structured search fields (e.g., `genre="science fiction"`, `year="1965"`).
3. **Filter Construction:**
   - The code builds a Qdrant filter using these fields.
4. **Vector Search (Qdrant):**
   - Qdrant retrieves only those book documents whose metadata matches the filter.
   - Among these, it uses vector similarity (embeddings) to find the most relevant ones.
5. **LLM Answer Generation:**
   - The filtered, relevant documents are passed to the LLM (ChatOpenAI) via the RetrievalQA chain.
   - The LLM uses these documents to generate a final, contextually accurate answer for the user.

---

## **Summary**
- The filter ensures only relevant documents (by metadata) are considered.
- The vector search finds the most similar among those.
- The LLM uses the filtered, relevant context to answer the user’s question.

---

## 📚 Resources
- [Qdrant Filtering Documentation](https://qdrant.tech/documentation/concepts/filtering/)
- [LangChain Retrieval Docs](https://python.langchain.com/docs/modules/data_connection/retrievers/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

---

Happy filtering! 🟣
