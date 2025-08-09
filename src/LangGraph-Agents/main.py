import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

# Try loading .env (safe for local dev)
# In ECS, if .env does not exist, load_dotenv() will simply do nothing
env_path = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
if os.path.exists(env_path):
    load_dotenv(dotenv_path=env_path)

# Get API key from environment
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise EnvironmentError("OPENAI_API_KEY is not set in environment variables.")

@tool(description="Return a friendly greeting for the given name.")
def say_hello(name: str) -> str:
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}!"


agent = create_react_agent(
    model="gpt-4o-mini",       # Or your preferred LLM
    tools=[say_hello],
    prompt="You are a friendly assistant that greets users."
)

# Use prompt templates
system_template = "You are a friendly assistant."
human_template = "Say hello to {name}."

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template(human_template)
])

formatted_prompt = prompt.format_prompt(name="Felipe")

response = agent.invoke({
    "messages": formatted_prompt.to_messages()
})
print(response)
# Extract the final AIMessage content from the response['messages']
final_message = None
if isinstance(response, dict) and "messages" in response:
    # Find the last AIMessage with non-empty content
    for msg in reversed(response["messages"]):
        if hasattr(msg, "content") and isinstance(msg.content, str) and msg.content.strip():
            final_message = msg.content
            break
print(final_message or response)