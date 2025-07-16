import os
import cohere
from dotenv import load_dotenv

load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

if not COHERE_API_KEY:
    raise ValueError("❌ Please set your COHERE_API_KEY in .env file.")

co = cohere.Client(COHERE_API_KEY)

def generate_cohere_reply(messages, model="command-r-plus", temperature=0.7):
    """Format messages and call Cohere's chat endpoint."""
    # Build chat history for Cohere format
    chat_history = []
    for msg in messages[:-1]:
        role = "USER" if msg["role"] == "user" else "CHATBOT"
        chat_history.append({"role": role, "message": msg["content"]})
    
    # Last user message
    latest_user_message = messages[-1]["content"]

    response = co.chat(
        model=model,
        chat_history=chat_history,
        message=latest_user_message,
        temperature=temperature,
        max_tokens=500
    )
    return response.text
