# 🤖 OpenAI GPT Chat Example (Python)

This example demonstrates how to use the official [OpenAI Python SDK](https://platform.openai.com/docs/api-reference) to interact with GPT models. It shows how to authenticate, send a chat prompt, and print the model's response.

---

## 📂 What does this script do?

1. **Loads your OpenAI API key** from a `.env` file.
2. **Initializes the OpenAI client** using the API key.
3. **Sends a chat prompt** to the GPT-3.5-turbo model.
4. **Prints the model's response** to the console.

---

## 🚀 How to Run

1. **Install dependencies:**
   ```bash
   pip install openai python-dotenv
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

## 🧑‍💻 Code Walkthrough

### 1. **Setup and Authentication**
- Loads your OpenAI API key from `.env` using `python-dotenv`.
- Initializes the OpenAI client with your API key.

### 2. **Send a Chat Prompt**
- Sends a chat completion request to the GPT-3.5-turbo model with a system and user message.
- Sets temperature and max tokens for the response.

### 3. **Print the Response**
- Extracts and prints the model's reply from the response object.

---

## 📝 Example Output

```
Hello world
```

---

## 🧠 Concepts Learned
- **OpenAI Python SDK:** Official library for accessing OpenAI models.
- **.env for secrets:** Keeps your API key out of your code.
- **Chat API:** Sending system and user messages to control the conversation.

---

## 📚 Resources
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)

---

Happy prompting! 🚀
