import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": ""},
        {"role": "user", "content": "Say 'Hello world'"}
    ],
    temperature=0.7,
    max_tokens=150,
)

response_message = response.choices[0].message
print(response_message.content)
