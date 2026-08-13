# purpose: to build a connection to Gemini LLM
from google import genai
from dotenv import load_dotenv
import os

# get api key from .env file
load_dotenv()

def build_connection():
    """
    Builds a connection to the Gemini LLM.

    Returns:
        A client object that interacts with the Gemini LLM.
    """
    return genai.Client() 

def send_prompt(client, prompt):
    """
    Sends a prompt to the Gemini LLM.

    Args:
        client: The client object connecting to Gemini.
        prompt: The message to send to Gemini.
    Returns:
        An interaction object containing the response from Gemini.
    """
    interaction = client.interactions.create(
        model=os.getenv("GEMINI_MODEL", "gemini-3.6-flash"),
        input=prompt
    )
    return interaction

def get_text_response(interaction):
    """
    Retrieves the text response from a Gemini interaction.

    Args:
        interaction: The interaction object containing the response from Gemini.

    Returns:
        The text response from Gemini.
    """
    return interaction.output_text