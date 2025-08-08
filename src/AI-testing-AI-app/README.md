# 🧳 AI Travel Recommendation App (LangChain + OpenAI)

This script demonstrates how to use [LangChain](https://python.langchain.com/) and [OpenAI](https://platform.openai.com/) to generate travel requests and provide AI-powered travel recommendations.

---

## What does this script do?

1. **Loads your OpenAI API key** from a `.env` file.
2. **Defines two main functions:**
   - `generate_travel_requests`: Uses an LLM to generate example travel requests (e.g., "I want to go on a beach vacation").
   - `generate_travel_recommendations`: Uses an LLM to generate short travel recommendations for each request.
3. **Prints the generated requests and recommendations.**

---

## How it works

- **Prompt Templates:** Uses system and human message templates to guide the LLM's behavior for both generating requests and recommendations.
- **LLMChain:** Chains the prompt and LLM together for easy repeated use.
- **Interactive Flow:** First generates a list of travel requests, then generates recommendations for each request.

---

## How to Run

1. **Install dependencies:**
   ```bash
   pip install langchain langchain-openai langchain-core python-dotenv
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
['I want to go on a beach vacation.', 'I want to go hiking in the mountains.', ...]
['How about visiting the Maldives for a relaxing beach getaway?', 'Consider hiking in the Swiss Alps for breathtaking views.', ...]
```

---

## Concepts Learned
- **Prompt Engineering:** Guide the LLM to generate and respond to user requests.
- **LLMChain:** Chain prompts and LLMs for repeated, structured use.
- **System vs. Human Prompts:** Use system prompts to set context and human prompts for user input.

---

## Resources
- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)

---

Happy travels! 🌍
