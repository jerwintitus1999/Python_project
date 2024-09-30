import streamlit as st

st.title("Hello World with Balloons!")
st.write("Click the button to celebrate.")

if st.button('Celebrate!'):
    st.balloons()

# import streamlit as st

st.title("User Input Example")
st.title("User Input Example")

name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}! Welcome to Streamlit!")

# import streamlit as st
import pandas as pd

st.title("Map of Chennai")

# Coordinates for Chennai (latitude, longitude)
chennai_coordinates = pd.DataFrame({
    'lat': [12.925947999046729],
    'lon': [80.23581106680246]
})

# Display the map with Chennai's coordinates
st.map(chennai_coordinates)

checkBox = st.radio(
    "What is your favourite food",
    ["Pizza", "Burger", "Dosa"],
    index= None,
)

st.write("You selected: ", checkBox)
