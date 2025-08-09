
# LangSmith: Monitoring & Observability for LLM Apps

LangSmith is a platform by LangChain that helps developers **debug**, **monitor**, and **evaluate** Large Language Model (LLM) applications — especially those built with LangChain.

It acts as an **observability layer** for AI-powered apps, giving you detailed insights into:
- Which prompts were sent to the model
- How the model responded
- How tools were used during execution
- Performance metrics like latency and token usage
- User feedback and evaluation results

---

## ✨ Key Features

### 1. **Tracing**
Record every step of an AI application's execution.
- See each input, output, and intermediate step
- Inspect prompt templates and final rendered prompts
- Debug issues faster when the app misbehaves

### 2. **Evaluation**
Test different versions of prompts, tools, and chains.
- Compare model responses
- Use automated scoring or human feedback
- Identify which changes improve results

### 3. **Monitoring**
Track real-time usage and quality.
- Watch latency and token consumption
- Spot performance regressions
- Identify failure patterns early

---

## 🚀 Why Use LangSmith?

Without LangSmith:
- You have little visibility into how the LLM made a decision
- Debugging is slow and painful
- You can’t easily compare changes

With LangSmith:
- You get full traceability, monitoring, and evaluation tools for your LLM apps
- Debug and optimize faster
- Build more reliable and production-ready AI systems

---

## 📝 Getting Started

### 1. **Create a LangSmith Account**

Go to [smith.langchain.com](https://smith.langchain.com/) and sign up for a free account.

### 2. **Get Your API Key**

After logging in, go to your account settings and generate a new API key.

### 3. **Set Environment Variables**

Add the following to your `.env` file (or your environment):

```env
LANGSMITH_TRACING="true"
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY="<your key>"
LANGSMITH_PROJECT="<your project name>"
```

Replace `<your key>` with your actual LangSmith API key, and `<your project name>` with any project name you want to use for grouping traces.

### 4. **Install Dependencies**

```sh
pip install langchain langchain-openai langsmith python-dotenv
```

---

## 💡 Example: Hello World with LangSmith

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()
response = llm.invoke("Hello, world!")
print(response)
```

When you run this script, the LLM call will be traced and visible in your LangSmith dashboard.

---

## 📊 Where to View Traces

Go to [smith.langchain.com](https://smith.langchain.com/) and log in. You’ll see your project and all LLM calls, with full details and visualizations.

---

## 🔗 More Resources
- [LangSmith Documentation](https://docs.smith.langchain.com/)
- [LangChain Documentation](https://python.langchain.com/docs)
