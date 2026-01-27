from dotenv import load_dotenv
import os
from google import genai
import requests
from google.genai import types


load_dotenv()

Google_api_key= os.getenv("GOOGLE_API_KEY")
Weather_api_key = os.getenv("WEATHER_API_KEY")

if not Google_api_key:
    raise ValueError ("API key not found.")
if not Weather_api_key:
    raise ValueError("API key not found.")

client = genai.Client(api_key=Google_api_key)

# function to get weather of the city

def get_weather(city:str):  # Type hint
    '''    
    featches current weather of the city

    args:
    city(str): city(name)(eg. mumbai)

    returns:
    dict: data in jason format
    '''
    try:
        #api_key = ""
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={Weather_api_key}"
        response = requests.get(url)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error":str(e)}
    
# gemini code to use the function to get details of the city
def temperature_of_city (city):
    system_instruction = '''
        You are given weather data in json format from the OpenWeather API
        Your job is to convert it into a clear, human-friendly weather update.  
    
       Guidelines:
       1. Always mention the city and country.
       2. Convert temperature from Kelvin to Celsius (°C), rounded to 1 decimal.
       3. Include: current temperature, feels-like temperature, main weather description,
          humidity, wind speed, and sunrise/sunset times (converted from UNIX timestamp).
       4. Use natural, conversational language.
       5. Based on the current conditions, suggest what the person should carry or wear.
          - If rain/clouds: suggest umbrella/raincoat.
          - If very hot (>30°C): suggest light cotton clothes, sunglasses, stay hydrated.
          - If cold (<15°C): suggest warm clothes, jacket.
          - If windy: suggest windbreaker, secure loose items.
          - If humid: suggest breathable clothes, water bottle.
       6. If any field is missing, gracefully ignore it.
       '''
    response = client.models.generate_content(
       model = "gemini-2.5-flash",
       contents= f"Generate a clear, weather report with temperature in celcius, humidity, wind, sunrise/sunset for the {city} and practical suggestions on what to were and carry.",
       config= types.GenerateContentConfig(system_instruction = system_instruction,tools=[get_weather])
    )

    return(response.candidates[0].content.parts[0].text)


 # FUNCTION TO GET NEWS OF INTEREST
def get_news(topic: str):
    """
    fetches latest news headlines from an API

    args:
    topic(str):topic top search news for(eg- technology , cricket etc)
    """
    try:
        api_key=""
        url= f""
        response =requests.get(url)
        return response.json().get("articles",[])
    except requests.exceptions.RequestException as e:
        return{"error": str(e)}

