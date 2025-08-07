"""
Super Simple LangChain Example
The absolute simplest way to use LangChain - perfect for beginners!
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Load your API key from .env file
load_dotenv()

# Step 1: Create a language model
llm = ChatOpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    model="gpt-3.5-turbo",
    temperature=0.7
)

print("🚀 Super Simple LangChain Example")
print("=" * 40)

# Example 1: Ask a direct question
print("\n💡 Example 1: Direct Question")
response = llm.invoke("What is Python programming?")
print("Question: What is Python programming?")
print("Answer:", response.content)

# Example 2: Use a template
print("\n🎯 Example 2: Using Templates")
prompt = ChatPromptTemplate.from_template("Explain {topic} in simple terms.")

# Create a chain (template + model)
chain = prompt | llm

response = chain.invoke({"topic": "machine learning"})
print("Topic: machine learning")
print("Explanation:", response.content)

# Example 3: Multiple questions with the same template
print("\n🔄 Example 3: Reusing Templates")
topics = ["artificial intelligence", "blockchain", "quantum computing"]

for topic in topics:
    response = chain.invoke({"topic": topic})
    print(f"\n{topic.title()}:")
    print(response.content)

print("\n✅ That's it! You've used LangChain!")
print("🎉 You learned: LLMs, Prompts, and Chains")
