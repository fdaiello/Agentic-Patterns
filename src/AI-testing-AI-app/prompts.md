# 📝 LangChain Prompt Templates Explained

This document explains the three main prompt template classes used in LangChain for chat-based LLMs:

- `ChatPromptTemplate`
- `SystemMessagePromptTemplate`
- `HumanMessagePromptTemplate`

---

## 1. `ChatPromptTemplate`

**Purpose:**
- Combines multiple message templates (system, human, AI, etc.) into a single prompt for chat-based LLMs.
- Allows you to build complex, multi-turn prompts by composing different message roles.

**Usage Example:**
```python
chat_prompt = ChatPromptTemplate.from_messages([
    system_message_prompt,
    human_message_prompt
])
```
- Here, `chat_prompt` will produce a prompt that includes both the system and human messages in the correct order for the LLM.

---

## 2. `SystemMessagePromptTemplate`

**Purpose:**
- Defines the "system" message in a chat prompt, which sets the context, rules, or persona for the LLM.
- Used to instruct the LLM on how to behave throughout the conversation.

**Usage Example:**
```python
system_template = "You are a travel recommendation agent. Provide a short recommendation based on the user request."
system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
```
- This message is typically the first in the prompt sequence and is not shown to the user.

---

## 3. `HumanMessagePromptTemplate`

**Purpose:**
- Defines the "human" (user) message in a chat prompt.
- Used to insert the user's input or question into the prompt sequence.

**Usage Example:**
```python
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
```
- This message represents what the user says to the LLM.

---

## 🧩 How They Work Together

- You create individual message templates for each role (system, human, etc.).
- Combine them using `ChatPromptTemplate.from_messages([...])` to form a complete prompt.
- Pass the combined prompt to an LLM chain (e.g., `LLMChain`) for structured, multi-turn interactions.

---

## 📚 Resources
- [LangChain Prompt Templates Documentation](https://python.langchain.com/docs/modules/model_io/prompts/)
- [LangChain Chat Prompt Guide](https://python.langchain.com/docs/modules/model_io/prompts/chat/)

---

Happy prompting! ✨
