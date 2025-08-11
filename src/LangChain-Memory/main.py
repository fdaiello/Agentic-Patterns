
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.memory import ConversationBufferMemory

# Load environment variables from .env
# .env file should have: OPENAI_API_KEY=your_api_key
load_dotenv()


# Initialize the LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Prompt template with memory placeholder
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])

# Memory for conversation
memory = ConversationBufferMemory(return_messages=True, memory_key="history", input_key="input")

# RunnableWithMessageHistory setup
chain = prompt | llm
conversation = RunnableWithMessageHistory(
    chain,
    lambda session_id: memory.chat_memory,
    input_messages_key="input",
    history_messages_key="history",
)

# Simple REPL loop
print("🤖 Chatbot ready! Type 'exit' to quit.")
session_id = "default"
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = conversation.invoke({"input": user_input}, config={"configurable": {"session_id": session_id}})
    print("Bot:", response.content if hasattr(response, "content") else response)