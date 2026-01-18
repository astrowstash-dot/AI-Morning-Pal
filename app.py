import streamlit as st
import random

# ----- page configuration -----

# ---- Helper Function ----

def get_random_quote(): 
    quotes = [
        "Todays goal: Coffee and Kindness. Maybe two coffees, and then kindndess",
        "Write it on your heart that every day is the best day in the year."
    ]
    return random.choice(quotes)

def get_random_images():
    images_url = [

    ]
    return random.choice(images_url)

def weather_news_page():
    """Displays the page for getting weather and news by city."""
    st.header ("Get weather of the city")
    city = st.text_input("Enter your city name: ")