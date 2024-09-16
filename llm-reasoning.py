
from openai import AzureOpenAI

# Define constants
AZURE_OPENAI_ENDPOINT = ""
AZURE_OPENAI_API_KEY = "" 
az_client = AzureOpenAI(azure_endpoint=AZURE_OPENAI_ENDPOINT,api_version="2023-07-01-preview",api_key=AZURE_OPENAI_API_KEY)
ai_response = az_client.chat.completions.create(
    model="gpt-35-turbo",
    messages=[
        {"role": "user", "content": "Count the occurrences of the letter 'r' in the word 'strawberry'."},
    ]
)
print("gpt-35-turbo")
print(ai_response.choices[0].message.content)
print("------------")
ai_response = az_client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Count the occurrences of the letter 'r' in the word 'strawberry'."},
        {"role": "system", "content": """         
<chain of thought>
EXAMPLE: Count the occurrences of the letter 'p' in the word 'apple'.
To determine the number of occurrences of the letter 'p' in the word 'apple', we scan through the word letter by letter: 
        'a' (0), 'p' (1), 'p' (2), 'l' (0), 'e' (0). 
Therefore, the letter 'p' appears 2 times.
</chain of thought>
IMPORTANT! USE ABOVE CHAIN OF THOUGHT TO GENERATE YOUR RESPONSE!
"""}
    ]
)
print("gpt-35-turbo with CoT")
print(ai_response.choices[0].message.content)
print("------------")
