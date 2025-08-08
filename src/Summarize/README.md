# 📝 OpenAI Text Summarization Example

This example demonstrates how to use the [OpenAI Python SDK](https://platform.openai.com/docs/api-reference) to summarize text using GPT-4. The script provides a function to generate a short TLDR summary for any input text, with several test cases.

---

## 📂 What does this script do?

1. **Loads your OpenAI API key** from a `.env` file.
2. **Initializes the OpenAI client** using the API key.
3. **Defines a function** to summarize text using GPT-4, with a word limit.
4. **Runs test cases** to demonstrate summarization of:
   - The Laws of Robotics
   - The Laws of Thermodynamics
   - A definition of Artificial Intelligence
5. **Prints the original text and the summary** for each test case.

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

### 2. **Summarization Function**
- Sends the input text to GPT-4 with a system prompt instructing the model to reply with a TLDR summary in a specified number of words or fewer.
- Handles errors and returns the summary or an error message.

### 3. **Test Cases**
- Summarizes the Laws of Robotics, Laws of Thermodynamics, and a definition of Artificial Intelligence, each with a different word limit.
- Prints the original and summarized text for each case.

---

## 📝 Example Output

```
📝 Text Summarization Tool
========================================

🤖 Laws of Robotics:
Original: 1) A robot may not injure a human being ...
5-word TLDR: Robots protect, obey, don't harm.

🌡️  Laws of Thermodynamics:
Original: 1st Law of Thermodynamics - Energy cannot be created ...
8-word TLDR: Energy conserved, entropy increases, zero entropy at zero.

🧠 Artificial Intelligence Definition:
Original: Artificial Intelligence (AI) refers to the simulation ...
6-word TLDR: AI: machines mimic human intelligence, learning.
```

---

## 🧠 Concepts Learned
- **OpenAI Python SDK:** Official library for accessing OpenAI models.
- **Text Summarization:** Generating short summaries (TLDRs) from longer text.
- **Prompt Engineering:** Instructing the model to reply with a specific word limit.
- **Reusable Functions:** Encapsulating API calls for easy reuse.

---

## 📚 Resources
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)

---

Happy summarizing! ✂️
