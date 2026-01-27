import streamlit as st
import random
from application import temperature_of_city

# ----- page configuration -----

# ---- Helper Function ----

def get_random_quote(): 
    quotes = [
        "Believe you can and you're halfway there.",
        "Write it on your heart that every day is the best day in the year.",
        "Your futures past is your presents future - changing the past is possible!",
        "The only person you are destined to become is the person you decide to be.",
        "Clarity comes from action.",
        "You know more than you think you do.Trust Yourself.",
        "In the middle of difficulty lies opportunity.",
        "Courage is the important of all virtues, because without courage you can't practice any other virtues consistently."

    ]
    return random.choice(quotes)

def get_random_images():
    images_url = [

    ]
    return random.choice(images_url)

# ----home page descriptions ----

def Home_page():
    # Display the home papge with quote and image
    st.title("Your Morning Pal. 🌞")
    st.markdown("----")
    st.subheader("Thought of the Day.")
    st.info (f"{get_random_quote()}")
    st.image(get_random_images(), caption="A beautiful way to start your day.", use_container_width= True)
    st.markdown("----")
    st.write("Sidebar on the left -> Daily updates! ")
    


def weather_news_page():
    """Displays the page for getting weather and news by city."""
    st.header ("Get weather of the city")
    city = st.text_input("Enter your city name: ")
    
    if st.button("Fetch Information"):
        if city:
            Temperature_output = temperature_of_city(city)
            st.subheader (f"Weather Info: {Temperature_output}")
            st.success("Weather information fetched successfully!!!!!!")
        else:
            st.error("Please enter a city name.")


def interest_news_page():
   
    """Displays the page for getting news by interest."""
    st.header("Get News Based on Your Interests")
    interest = st.text_input("Enter your area of interest (e.g., Technology, Sports, Health):", "Technology")


    if st.button("Fetch News"):
        st.success("Done")


def smart_planner():
    st.header("Your smart planner")
    city = st.text_input("Emter your city")
    if st.button("Let's plan"):
        st.success("done")


# -----sidebar navigation------

st.sidebar.title("Navigation")
st.sidebar.markdown("----")
st.sidebar.subheader("choose your page: ")
st.sidebar(Home_page())

