# 🚀 Super Simple LangChain Example

This example demonstrates the absolute basics of using [LangChain](https://python.langchain.com/) with OpenAI's GPT models. It's designed for beginners who want to understand how to:

- Connect to an LLM (Language Model)
- Use prompt templates
- Build simple chains

---

## 📂 What does this script do?

1. **Loads your OpenAI API key** from a `.env` file
2. **Creates a language model** using `ChatOpenAI`
3. **Runs three simple examples:**
   - Direct question to the LLM
   - Using a prompt template
   - Reusing the template for multiple topics

---

## 🚀 How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt