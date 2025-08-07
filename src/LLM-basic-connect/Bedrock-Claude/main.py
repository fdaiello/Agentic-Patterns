import os
import json
import boto3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Bedrock client
bedrock_client = boto3.client(
    'bedrock-runtime',
    region_name=os.getenv('AWS_REGION', 'us-east-1'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

# Prepare the request payload for Claude
request_body = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 150,
    "temperature": 0.7,
    "messages": [
        {
            "role": "user",
            "content": "Say 'Hello world'"
        }
    ]
}

# Make the request to Bedrock
response = bedrock_client.invoke_model(
    modelId="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
    body=json.dumps(request_body),
    contentType='application/json'
)

# Parse the response
response_body = json.loads(response['body'].read())
response_message = response_body['content'][0]['text']
print(response_message)