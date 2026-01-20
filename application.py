from dotenv import load_dotenv
import os
from google import genai
import requests

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
    try:
        api_key = "5422c8018545fe4491659752823b9931"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error":str(e)}

