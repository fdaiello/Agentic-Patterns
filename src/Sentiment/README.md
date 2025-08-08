# 🎭 Sentiment Analysis Bot (OpenAI)

This example demonstrates a simple interactive sentiment analysis bot using the [OpenAI Python SDK](https://platform.openai.com/docs/api-reference). The bot classifies user input as either "happy" or "sad" using GPT-4.

---

## 📂 What does this script do?

1. **Loads your OpenAI API key** from a `.env` file.
2. **Initializes the OpenAI client** using the API key.
3. **Prompts the user** for input in a loop.
4. **Sends the input** to GPT-4 for sentiment classification.
5. **Prints the sentiment** (with emoji) as "happy" or "sad".
6. **Handles errors and allows exit** with 'quit' or 'exit'.

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

### 2. **Interactive Loop**
- Prompts the user for a phrase.
- Sends the phrase to GPT-4 with a system prompt instructing the model to reply with only "happy" or "sad".
- Prints the result with an emoji.
- Handles empty input, errors, and allows the user to exit.

---

## 📝 Example Output

```
🎭 Sentiment Analysis Bot
Type 'quit' or 'exit' to stop
----------------------------------------

Enter a phrase and we'll classify it as happy or sad: I love sunny days!
😊 Sentiment: Happy

Enter a phrase and we'll classify it as happy or sad: I lost my keys.
😢 Sentiment: Sad

Enter a phrase and we'll classify it as happy or sad: quit
👋 Goodbye!
```

---

## 🧠 Concepts Learned
- **OpenAI Python SDK:** Official library for accessing OpenAI models.
- **Sentiment Analysis:** Classifying text as positive or negative.
- **Prompt Engineering:** Instructing the model to reply with only one word.
- **Interactive CLI:** Building a simple command-line bot.

---

## 📚 Resources
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)

---

Happy analyzing! 🚦
