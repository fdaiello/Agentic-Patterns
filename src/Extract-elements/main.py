from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv("../.env")


class Furniture(BaseModel):
    type: str = Field(
        description="the type of furniture (e.g., chair, table, sofa, desk)"
    )
    style: str = Field(
        description="the design style of the furniture (e.g., modern, vintage, mid-century, minimalist)"
    )
    color: str = Field(
        description="the color of the furniture (e.g., blue, red, white, black)"
    )


furniture_request = "I'd like a blue mid century chair"

parser = PydanticOutputParser(pydantic_object=Furniture)

# Debug: See what format instructions are generated
format_instructions = parser.get_format_instructions()
print("🔧 Format Instructions Generated:")
print(format_instructions)
print("-" * 50)

prompt = PromptTemplate(
    template="Extract the furniture information from the user's request and format it as JSON.\n{format_instructions}\n\nUser request: {query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": format_instructions},
)

_input = prompt.format_prompt(query=furniture_request)

# Debug: See the complete prompt sent to AI
print("📝 Complete Prompt Sent to AI:")
print(_input.to_string())
print("-" * 50)

model = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
output = model.predict(_input.to_string())

# Debug: See raw AI response
print("🤖 Raw AI Response:")
print(output)
print("-" * 50)

parsed = parser.parse(output)

# Debug: See parsed structure
print("✅ Parsed Structure:")
print(f"Type: {parsed.type}")
print(f"Style: {parsed.style}")
print(f"Colour: {parsed.color}")
print("-" * 50)
print(parsed.color)
