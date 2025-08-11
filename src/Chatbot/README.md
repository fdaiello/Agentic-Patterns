# LangGraph Chatbot Example

This example demonstrates how to build a simple conversational chatbot using LangGraph and LangChain with OpenAI models.


## How the Code Works

1. **Environment Setup**
   - Loads environment variables (like API keys) from a `.env` file using `load_dotenv()`.

2. **Model Initialization**
   - Instantiates a chat model with `ChatOpenAI(model="gpt-4o-mini")`.

3. **LangGraph Workflow Structure**
   - The workflow is defined as a directed graph using LangGraph's `StateGraph`.
   - You add nodes (steps) and edges (transitions) to the graph:
     - `workflow.add_node("model", call_model)` adds a node named `"model"` that runs the `call_model` function. Each node represents a step in your application.
     - `workflow.add_edge(START, "model")` creates a directed edge from the special `START` node to your `"model"` node, telling LangGraph to start execution at the `"model"` node.
   - This structure allows you to build modular, stateful applications with clear control flow. For a simple chatbot, a single node is sufficient, but you can add more nodes and edges for more complex workflows.

4. **Memory**
   - Uses `MemorySaver` to persist conversation history between turns.

5. **App Compilation**
   - Compiles the workflow graph into an executable app with memory support.

6. **Interactive Chat Loop**
   - Prompts the user for input in a loop.
   - Sends each user message to the chatbot, which responds using the LLM and conversation history.
   - Exits the loop if the user types `exit` or `quit`.

## Key Code Snippet
```python
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

load_dotenv()

workflow = StateGraph(state_schema=MessagesState)

def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}

workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

model = ChatOpenAI(model="gpt-4o-mini")

config = {"configurable": {"thread_id": "abc123"}}

print("💬 Start chatting with the bot! (type 'exit' or 'quit' to stop)")
while True:
    user_input = input("You: ").strip()
    if user_input.lower() in {"exit", "quit"}:
        print("👋 Goodbye!")
        break
    input_messages = [HumanMessage(user_input)]
    output = app.invoke({"messages": input_messages}, config)
    print("Bot:", output["messages"][-1].content)
```

## How It Works
- Each user message is wrapped in a `HumanMessage` and sent to the app.
- The app maintains conversation history using memory, so the bot can remember previous turns.
- The LLM generates a response based on the full conversation context.
- The loop continues until the user types `exit` or `quit`.

## Requirements
- `langchain-openai`
- `langchain-core`
- `langgraph`
- `python-dotenv`

Install dependencies with:
```sh
pip install -r requirements.txt
```

## Notes
- Make sure your `.env` file contains your OpenAI API key (e.g., `OPENAI_API_KEY=sk-...`).
- You can change the model by editing the `ChatOpenAI(model=...)` line.
- This pattern can be extended with more nodes, tools, or custom memory for advanced chatbots.
