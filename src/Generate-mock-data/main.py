
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Person(BaseModel):
    first_name: str = Field(description="first name")
    last_name: str = Field(description="last name")
    dob: str = Field(description="date of birth")


class PeopleList(BaseModel):
    people: list[Person] = Field(description="A list of people")


model = ChatOpenAI(model="gpt-4")
parser = PydanticOutputParser(pydantic_object=PeopleList)

format_instructions = parser.get_format_instructions()

prompt = PromptTemplate(
    template="Generate a list of 10 fake people's information. Each person should have a first name, last name, and date of birth. Format the output as JSON matching this schema.\n{format_instructions}",
    input_variables=[],
    partial_variables={
        "format_instructions": format_instructions
    },
)

_input = prompt.format_prompt()
output_msg = model.invoke(_input.to_string())
output = output_msg.content if hasattr(output_msg, 'content') else str(output_msg)
if isinstance(output, list):
    output_str = "\n".join(str(x) for x in output)
elif isinstance(output, dict):
    output_str = str(output)
else:
    output_str = str(output)
parsed = parser.parse(output_str)
print(parsed)
