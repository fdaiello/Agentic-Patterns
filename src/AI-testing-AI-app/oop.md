# 🧑‍💻 Object-Oriented Programming (OOP) in This Project

This document explains the object-oriented design patterns and OOP concepts used in the code for the AI Travel Recommendation App.

---

## What is Object-Oriented Programming (OOP)?

OOP is a programming paradigm based on the concept of "objects", which can contain data (attributes) and code (methods). OOP helps organize code, promote reuse, and model real-world concepts.

**Key OOP Concepts:**
- **Class:** A blueprint for creating objects (instances) with specific attributes and methods.
- **Object:** An instance of a class.
- **Encapsulation:** Bundling data and methods that operate on that data within one unit (class).
- **Abstraction:** Hiding complex implementation details and exposing only what is necessary.
- **Inheritance:** Creating new classes from existing ones, inheriting attributes and methods (not directly used in this code, but common in OOP).
- **Polymorphism:** The ability to use a unified interface for different data types (not directly used here, but common in OOP).

---

## OOP in This Code

### 1. **Classes from LangChain**

- **`ChatOpenAI`**
  - Represents a chat-based language model. Encapsulates all logic for interacting with OpenAI's chat API.
- **`LLMChain`**
  - Represents a chain that combines a language model and a prompt. Encapsulates the logic for running prompts through the LLM.
- **`ChatPromptTemplate`, `SystemMessagePromptTemplate`, `HumanMessagePromptTemplate`**
  - Each is a class that encapsulates the logic for building different parts of a chat prompt.

These classes are used to create objects (instances) that manage the state and behavior of the AI pipeline.

### 2. **Encapsulation and Abstraction**
- The code uses classes to encapsulate complex logic (e.g., prompt formatting, LLM interaction) behind simple interfaces.
- For example, you don't need to know how `LLMChain` works internally; you just create an instance and call `.invoke()`.

### 3. **Functions as Behaviors**
- The functions `generate_travel_requests` and `generate_travel_recommendations` act as behaviors that use these objects to perform tasks.
- They demonstrate how OOP objects can be composed and orchestrated to build more complex workflows.

### 4. **No Custom Classes Defined**
- In this particular script, all classes are imported from libraries. You could extend this by defining your own classes for more complex logic or data structures.

---

## Example: Using a Class

```python
from langchain_openai import ChatOpenAI

# Create an instance (object) of the ChatOpenAI class
llm = ChatOpenAI(temperature=1)

# Use the object to interact with the LLM
response = llm.invoke("Hello!")
```

---

## Why Use OOP Here?
- **Modularity:** Each class handles a specific responsibility (LLM, prompt, chain).
- **Reusability:** You can reuse and compose these objects in different ways.
- **Maintainability:** Encapsulation makes the code easier to maintain and extend.

---

## Further Reading
- [Python OOP Tutorial](https://realpython.com/python3-object-oriented-programming/)
- [LangChain Documentation](https://python.langchain.com/)

---

Happy learning! 🧑‍💻
