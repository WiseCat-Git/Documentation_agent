import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_documentation(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Use the appropriate model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500,
        temperature=0.5,
        top_p=1,
        n=1
    )

    documentation_text = response.choices[0].message.content.strip()
    return documentation_text
