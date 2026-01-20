from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

api_key= os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError ("API key not found.")

client = genai.client(api_key=api_key)

# function to get weather of the city

def get_weather(city:str):
    '''
    featches current weather of the city

    args:
    city(str): city(name)

    returns:
    dict: data in jason format
    '''

