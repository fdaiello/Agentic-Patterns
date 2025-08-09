# Tool-based Agent Example (`main.py`)

This example demonstrates how to build a simple tool-using agent with LangChain and OpenAI, using the latest API patterns.

## Overview
- **Defines a custom tool** using the `@tool` decorator.
- **Initializes a ChatOpenAI LLM** (e.g., GPT-4o-mini).
- **Creates an agent** that can use the tool via OpenAI function-calling.
- **Invokes the agent** with a user query, and prints only the final output.

## Code Walkthrough

```python
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import initialize_agent, AgentType

load_dotenv()

# 1️⃣ Define your tool
@tool
def say_hello(name: str) -> str:
    """Say hello to a person by name."""
    return f"Hello, {name}! Nice to meet you."

# 2️⃣ Create the LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",  # or "gpt-4o"
    temperature=0
)

# 3️⃣ Initialize the agent with the tool
agent = initialize_agent(
    tools=[say_hello],
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,  # uses function calling
    verbose=True
)

# 4️⃣ Run a query that will make the model use the tool
result = agent.invoke("Please greet a person named Felipe.")
# Print only the agent's final output, not the full result object
if isinstance(result, dict) and 'output' in result:
    print(result['output'])
else:
    print(result)
```

## How it Works
1. **Tool Definition:**
   - The `say_hello` function is decorated with `@tool`, making it available to the agent.
2. **LLM Initialization:**
   - Uses OpenAI's GPT-4o-mini (or GPT-4o) as the language model.
3. **Agent Setup:**
   - The agent is initialized with the tool and LLM, using OpenAI's function-calling agent type.
   - `verbose=True` enables detailed reasoning traces in the console.
4. **Agent Invocation:**
   - The agent is asked to greet a person by name. It decides to use the `say_hello` tool.
   - Only the final output is printed, avoiding duplicate responses.

## Requirements
- `langchain`
- `langchain-openai`
- `langchain-core`
- `langchain-community`
- `python-dotenv`

Install dependencies with:
```sh
pip install -r requirements.txt
```

## Notes
- Make sure your OpenAI API key is set in a `.env` file as `OPENAI_API_KEY=...`.
- This pattern is future-proof for OpenAI function-calling agents in LangChain.
- For more advanced agentic patterns, see other modules in this repository.
