# 🧑‍💻 Generate Mock People Data with LangChain, OpenAI, and Pydantic

This script demonstrates how to use [LangChain](https://python.langchain.com/), [OpenAI](https://platform.openai.com/), and [Pydantic](https://docs.pydantic.dev/) to generate and parse structured mock data for a list of people.

---

## What does this script do?

1. **Loads your OpenAI API key** from a `.env` file.
2. **Defines Pydantic models** for a person and a list of people.
3. **Uses an LLM (GPT-4)** to generate a list of 10 fake people (first name, last name, date of birth).
4. **Uses a prompt and output parser** to ensure the data matches the expected schema.
5. **Prints the structured result** as a Python object.

---

## How to Run

1. **Install dependencies:**
   ```bash
   pip install langchain langchain-openai langchain-core pydantic python-dotenv
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

## Example Output

```
people=[Person(first_name='John', last_name='Doe', dob='1990-01-01'), ...]
```

---

## Concepts Learned

- **Pydantic Models:** Define and validate structured data.
- **Prompt Engineering:** Guide the LLM to output data in a specific format.
- **LangChain Output Parsers:** Automatically parse LLM output into Python objects.
- **Mock Data Generation:** Use LLMs to create realistic test data.

---

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

---

Happy generating! 🚀
