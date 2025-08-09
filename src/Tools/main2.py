from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import initialize_agent, AgentType
import random

load_dotenv()

# 1️⃣ Define your tools
@tool
def say_hello(name: str) -> str:
    """Say hello to a person by name. Use this when the user asks for a greeting."""
    return f"Hello, {name}! Nice to meet you."

@tool
def get_current_weather(city: str) -> str:
    """
    Get the current weather for a given city.
    Use this when the user asks about temperature or weather conditions.
    """
    # Fake weather for demonstration
    temperature = random.randint(15, 35)
    condition = random.choice(["sunny", "cloudy", "rainy"])
    return f"The current weather in {city} is {temperature}°C and {condition}."

# 2️⃣ Create the LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",  # or "gpt-4o"
    temperature=0
)

# 3️⃣ Initialize the agent with both tools
agent = initialize_agent(
    tools=[say_hello, get_current_weather],
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,  # function calling agent
    verbose=True
)

# 4️⃣ Try different requests
print("\n--- Greeting Example ---")
response1 = agent.invoke("Please greet a person named Alice.")
print("Agent output:", response1)

print("\n--- Weather Example ---")
response2 = agent.invoke("What is the weather in Rio de Janeiro?")
print("Agent output:", response2)
