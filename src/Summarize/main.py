import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

def summarize_text(text, max_words=10):
    """
    Summarize text using OpenAI GPT-4.
    
    Args:
        text: Text to summarize
        max_words: Maximum words in summary
    
    Returns:
        Summary string
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system", 
                    "content": f"You are a summarization expert. Create a TLDR summary in exactly {max_words} words or fewer."
                },
                {
                    "role": "user", 
                    "content": f"Summarize this text:\n\n{text}"
                }
            ],
            temperature=0.3,
            max_tokens=50,
        )
        
        content = response.choices[0].message.content
        return content.strip() if content else "No response generated"
        
    except Exception as e:
        return f"Error summarizing: {e}"

def main():
    """Main function to test summarization."""
    print("📝 Text Summarization Tool")
    print("=" * 40)
    
    # Constants
    ORIGINAL_LABEL = "Original:"
    
    # Test case 1: Laws of Robotics
    robotics_laws = """
    1) A robot may not injure a human being or, through inaction,
    allow a human being to come to harm.

    2) A robot must obey orders given it by human beings except where
    such orders would conflict with the First Law.

    3) A robot must protect its own existence as long as such protection
    does not conflict with the First or Second Law.
    """
    
    print("\n🤖 Laws of Robotics:")
    print(ORIGINAL_LABEL, robotics_laws.strip())
    summary1 = summarize_text(robotics_laws, max_words=5)
    print("5-word TLDR:", summary1)
    
    # Test case 2: Laws of Thermodynamics
    thermodynamics_laws = """
    1st Law of Thermodynamics - Energy cannot be created or destroyed.
    2nd Law of Thermodynamics - For a spontaneous process, the entropy of the universe increases.
    3rd Law of Thermodynamics - A perfect crystal at zero Kelvin has zero entropy.
    """
    
    print("\n🌡️  Laws of Thermodynamics:")
    print(ORIGINAL_LABEL, thermodynamics_laws.strip())
    summary2 = summarize_text(thermodynamics_laws, max_words=8)
    print("8-word TLDR:", summary2)
    
    # Test case 3: Custom input
    custom_text = """
    Artificial Intelligence (AI) refers to the simulation of human intelligence in machines 
    that are programmed to think like humans and mimic their actions. The term may also be 
    applied to any machine that exhibits traits associated with a human mind such as learning 
    and problem-solving. The ideal characteristic of artificial intelligence is its ability 
    to rationalize and take actions that have the best chance of achieving a specific goal.
    """
    
    print("\n🧠 Artificial Intelligence Definition:")
    print(ORIGINAL_LABEL, custom_text.strip())
    summary3 = summarize_text(custom_text, max_words=6)
    print("6-word TLDR:", summary3)

if __name__ == "__main__":
    main()
