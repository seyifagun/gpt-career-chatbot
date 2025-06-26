import cohere
import os
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT

load_dotenv()
co = cohere.ClientV2(os.getenv("COHERE_API_KEY"))

def get_chat_response(messages):
    try:
        if not messages:
            return "Please provide a message."

        # Format messages for Cohere API
        chat_history = [{
            "role": "user" if msg["role"] == "user" else "assistant",
            "content": msg["content"]
        } for msg in messages[:-1]]

        # Get the latest message
        current_message = messages[-1]["content"]

        # Format messages for Cohere API
        messages = [{
            "role": "assistant",
            "content": SYSTEM_PROMPT
        }] + chat_history + [{
            "role": "user",
            "content": current_message
        }]

        # Make API call with proper formatting
        response = co.chat(
            messages=messages,
            model="command-a-03-2025",
        )

        return response.message.content[0].text

    except Exception as e:
        return f"An error occurred: {str(e)}"
