# 🪑 Furniture Information Extraction with LangChain & Pydantic

This example demonstrates how to use [LangChain](https://python.langchain.com/) and [Pydantic](https://docs.pydantic.dev/) to extract structured information from natural language using an LLM (OpenAI GPT).

---

## 📂 What does this script do?

1. **Loads your OpenAI API key** from a `.env` file.
2. **Defines a Pydantic model** (`Furniture`) for structured output.
3. **Creates a prompt** to instruct the LLM to extract furniture details from a user request.
4. **Uses LangChain's PydanticOutputParser** to generate format instructions and parse the LLM's output.
5. **Sends the prompt to the LLM** and parses the response into a Python object.
6. **Prints debug information** at each step for transparency.

---

## 🧑‍💻 Code Walkthrough

### 1. **Setup and Authentication**
- Loads your OpenAI API key from `.env` using `python-dotenv`.
- Initializes the LLM with the API key.

### 2. **Pydantic Model**
- Defines a `Furniture` class with fields: `type`, `style`, and `color`.
- Each field has a description to guide the LLM.

### 3. **Prompt Construction**
- Uses `PromptTemplate` to create a prompt that asks the LLM to extract furniture info and format it as JSON.
- Uses `PydanticOutputParser` to generate format instructions for the LLM.

### 4. **Model Invocation & Parsing**
- Sends the prompt to the LLM.
- Parses the LLM's output into a `Furniture` object using the parser.
- Prints the parsed structure.

---

## 🧠 What is Pydantic?

[Pydantic](https://docs.pydantic.dev/) is a Python library for data validation and settings management using Python type annotations. It lets you define data models (classes) with type hints, and automatically validates and parses data into those models. In this script, Pydantic is used to define the expected structure of the extracted information, and to parse the LLM's output into a Python object.

---

## 🚀 How to Run

1. **Install dependencies:**
   ```bash
   pip install langchain openai pydantic python-dotenv
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

## 📝 Example Output

```
🔧 Format Instructions Generated:
... (format instructions for the LLM) ...
📝 Complete Prompt Sent to AI:
... (full prompt with instructions and user request) ...
🤖 Raw AI Response:
{
  "type": "chair",
  "style": "mid century",
  "color": "blue"
}
✅ Parsed Structure:
Type: chair
Style: mid century
Colour: blue
blue
```

---

## 🧠 Concepts Learned
- **Pydantic Models:** Define and validate structured data.
- **Prompt Engineering:** Guide the LLM to output data in a specific format.
- **LangChain Output Parsers:** Automatically parse LLM output into Python objects.

---

## 📚 Resources
- [LangChain Documentation](https://python.langchain.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)

---

Happy extracting! 🪑
