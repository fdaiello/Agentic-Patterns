from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

load_dotenv()

# Define a new graph
workflow = StateGraph(state_schema=MessagesState)

# Define the function that calls the model
def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}

# Define the (single) node in the graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# Add memory
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

# Model initialization
model = ChatOpenAI(model="gpt-4o-mini")

# Session configuration - this would be used if there were different threads or sessions
config = {"configurable": {"thread_id": "abc123"}}

print("💬 Start chatting with the bot! (type 'exit' or 'quit' to stop)")
while True:
    user_input = input("You: ").strip()
    if user_input.lower() in {"exit", "quit"}:
        print("👋 Goodbye!")
        break
    input_messages = [HumanMessage(user_input)]
    output = app.invoke({"messages": input_messages}, config)
    # Print the last AI message in the state
    print("Bot:", output["messages"][-1].content)







