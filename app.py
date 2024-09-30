import streamlit as st

import requests

import pandas as pd

st.title("Find the country")

country = st.text_input("Enter the country name")

if country:
    st.write(f"The country name is {country}")
    API_KEY = '48283f18b28b40898d94a008bbf9ca65'
    url = f"https://api.opencagedata.com/geocode/v1/json?q={country}&key={API_KEY}"

    response = requests.get(url)
    data = response.json()

    if data['results']:
        lat = data['results'][0]['geometry']['lat']
        lon = data['results'][0]['geometry']['lng']
        print(f"Latitude: {lat}, Longitude: {lon}")

        # Coordinates for the given country (latitude, longitude)
        coordinates = pd.DataFrame({
            'lat': [lat],
            'lon': [lon]
        })

        # Display the countrys coordinates
        st.map(coordinates)
    else:
        print("Location not found")
