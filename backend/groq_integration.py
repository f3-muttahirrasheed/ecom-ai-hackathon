import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()


# Initialize the Groq client using the API key from environment variable
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def ask_groq(question, system_prompt="How are you and what is the day today."):
    """
    Sends a question to Groq and returns the response.
    """
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ],
            model="llama3-70b-8192",  # You can also use: mixtral-8x7b-32768 or gemma-7b-it
        )
        response = chat_completion.choices[0].message.content
        return response
    except Exception as e:
        print(f"Error in Groq integration: {e}")
        return None
