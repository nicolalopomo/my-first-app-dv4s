import streamlit as st

st.set_page_config(
    page_title="My App",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("My New STREAMLIT app")

st.write("Welcome to my new app!!!")


data = st.slider("Select a value", 0, 100, 50)

st.write("You selected :", data)
