import streamlit as st
import pandas as pd
from datetime import datetime, time

st.set_page_config(
    page_title="My app",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={"About": "Welcome to DV4S!",
                "Get Help": "https://www.polimi.it",
                "Report a bug": "https://www.polimi.it"
                }
)

# Title
st.title('My New :red[Streamlit] App!')

# Header
st.header('Welcome to :green[DV4S] !')

# Subheader
st.subheader('😀 Smile !')

# Text
st.write('Welcome to my **great** new app!')

# Markdown
st.markdown('__')
st.markdown('> Ciao!')
st.markdown('<p style="color:yellow; font-size:20px;">This is yellow text</p>', 
            unsafe_allow_html=True)


# Displaying a number
st.write("Here is a number:", 42)

# Displaying a list
my_list = ["apple", "banana", "cherry"]
st.write("My list:", my_list)

# Displaying a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
st.write("Dictionary example:", my_dict)

# Displaying a DataFrame
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
st.write("Here is a DataFrame:", df)

# Define a list containing all the sports I know
sports_list = ['soccer', 'basketball', 'tennis', 'ski', 'football']

# Check if the button is pressed, show the list
if st.button("Sports", type="primary"):
    st.write(sports_list)

# Introduce a checkbox
if st.checkbox("I like DV4S!"):
    st.write("You like it, indeed!")
else:
    st.write("Please, like DV4S...")


# Introduce a radio button
chosen_sport = st.radio("Which sport do you prefer?", sports_list)
st.write('You like ' + chosen_sport + ' , indeed!')

# Introduce a select box
chosen_sport = st.selectbox("Which sport do you prefer?", sports_list)
st.write('You like ' + chosen_sport + ' , indeed!')

# Define a dictionary with players and goals in a season
players = {"Zoff": "10", "Ronaldo": "23", "Messi": "34"}
selection = st.multiselect("Select the player to analyse:",
                         ["Zoff", "Ronaldo", "Messi"])
for player in selection:
    st.write(f':red[{player}]: {players[player]} goal!')


# Age
age = st.slider('How old are you?', 18, 67, 25)
st.write("You are", age, "years old!")

# Age ranges
age_range = st.slider('Select a range of valid ages', 18, 67, (25, 50))
st.write('You selected:', age_range)

# Datetime range
date_range = st.slider('Select a range of valid dates',
                       value=(datetime(2025, 3, 15), datetime(2025, 3, 20)),
                       min_value=datetime(2025, 3, 1),
                       max_value=datetime(2025, 3, 31),
                       format="DD/MM/YYYY")

# Unpack tuple
start_date, end_date = date_range

# Format dates correctly
st.write("Date range:", start_date.strftime("%d/%m/%Y"), "to", end_date.strftime("%d/%m/%Y"))


# Text Input
name = st.text_input("Enter your name:", placeholder="Type here...")

# Number Input
age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25, step=1)

# Display user input
if name:
    st.write(f"Hello, **{name}**! 👋")
    
if age:
    st.write(f"Your age is **{age}** years old.")

# Combining Inputs
if name and age:
    st.success(f"Welcome, {name}! You are {age} years old. 🎉")


# Data range with widgets
date = st.date_input("Select a date range",
                     value=(datetime(2025, 3, 15), datetime(2025, 3, 20)))

# Creating a form
with st.form("user_form"):
    # Text input (name)
    name = st.text_input("Full Name:", placeholder="Enter your name...")

    # Number input (age)
    age = st.number_input("Age:", min_value=1, max_value=120, value=25, step=1)

    # Select box (dropdown) for gender
    gender = st.selectbox("Gender:", ["Select an option", "Male", "Female", "Other"])

    # Submit button
    submitted = st.form_submit_button("Submit")

# Display output after submission
if submitted:
    if name and gender != "Select an option":
        st.success(f"✅ Form submitted!\n\n**Name:** {name}\n**Age:** {age}\n**Gender:** {gender}")
    else:
        st.warning("⚠️ Please fill out all fields correctly.")