
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def generate_travel_recommendations(travel_requests):
    """
    Generate travel recommendations based on user requests
    """
    # create templates
    system_template_travel_agent = """You are travel recommendation agent. Provide a short recommendation based on the user request."""
    system_message_prompt = SystemMessagePromptTemplate.from_template(
        system_template_travel_agent)

    human_template_travel_agent = "{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(
        human_template_travel_agent)

    # create full prompt
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt])

    chain = LLMChain(
        llm=ChatOpenAI(temperature=1),
        prompt=chat_prompt
    )

    recommendations = []
    for travel_request in travel_requests:
        result = chain.invoke(travel_request)
        # If result is a dict with 'text' or 'output', extract it
        if isinstance(result, dict):
            recommendations.append(result.get('text') or result.get('output') or str(result))
        else:
            recommendations.append(str(result))
    return recommendations


def generate_travel_requests(n=5) -> list[str]:
    """ Generate travel requests
    n: number of requests
    """
    # create templates
    system_template_travel_agent = """Generate one utterance for how someone would to travel for a {text}"""
    system_message_prompt = SystemMessagePromptTemplate.from_template(
        system_template_travel_agent)

    # create full prompt
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt])

    chain = LLMChain(
        llm=ChatOpenAI(model='gpt-4'),
        prompt=chat_prompt
    )

    results = []
    for _ in range(0, n):
        result = chain.invoke("beach vacation")
        if isinstance(result, dict):
            results.append(result.get('text') or result.get('output') or str(result))
        else:
            results.append(str(result))
    return results


# generate some requests
travel_requests = generate_travel_requests()
print(travel_requests)

# get the recommendations
recommendations = generate_travel_recommendations(travel_requests)
print(recommendations)
