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
