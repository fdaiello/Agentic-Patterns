import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

print("🎭 Sentiment Analysis Bot")
print("Type 'quit' or 'exit' to stop")
print("-" * 40)

while True:
    user_input = input("\nEnter a phrase and we'll classify it as happy or sad: ")
    
    if user_input.lower() in ["quit", "exit"]:
        print("👋 Goodbye!")
        break
    
    if not user_input.strip():
        print("⚠️  Please enter some text.")
        continue
        
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a sentiment classification bot. Analyze the user's input and respond with only one word: either 'happy' or 'sad'."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.3,  # Lower temperature for more consistent classification
            max_tokens=10,    # Only need one word
        )

        content = response.choices[0].message.content
        if content:
            sentiment = content.strip().lower()
            
            # Add emoji based on sentiment
            if "happy" in sentiment:
                print("😊 Sentiment: Happy")
            elif "sad" in sentiment:
                print("😢 Sentiment: Sad")
            else:
                print(f"🤔 Sentiment: {sentiment.title()}")
        else:
            print("❌ No response received from the API")
            
    except Exception as e:
        print(f"❌ Error analyzing sentiment: {e}")
        print("Please try again.")
