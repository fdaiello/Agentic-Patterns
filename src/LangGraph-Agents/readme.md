# LangGraph "Hello, World!" Agent Example

A minimal demonstration of building a **LangGraph** agent in Python that greets users.  
This example uses the **`create_react_agent`** helper to quickly spin up an agent without manually wiring all graph components.

---

## 📌 What is `create_react_agent`?

`create_react_agent` is a **prebuilt LangGraph constructor** that creates an agent using the **ReAct** reasoning framework.  
It automatically:
1. Wraps your chosen LLM in an **agent executor**.
2. Integrates any tools you pass in (e.g., Python functions, APIs).
3. Handles the **reasoning + acting** loop, so the agent:
   - Reads the user message.
   - Decides whether to respond directly or call a tool.
   - Processes tool output and continues reasoning.
4. Manages conversation state and passes context between steps.

Essentially, it’s the fastest way to get a **working tool-using agent** without manually defining:
- StateGraph nodes
- Message handling
- Tool-calling logic

---

## 💡 Why use `create_react_agent`?

- **Rapid prototyping** → Perfect for small demos and quick experiments.
- **Less boilerplate** → No need to wire LLM, tool logic, and message flow manually.
- **Built-in ReAct** → Uses the proven "Reasoning + Acting" pattern.
- **Tool integration** → Pass Python functions, APIs, or LangChain tools directly.
- **Stateful** → Maintains context through the conversation.

---

## 📂 Project Setup

**Project structure** (example):