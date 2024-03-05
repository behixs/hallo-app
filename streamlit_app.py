import streamlit as st
import pandas as pd
import requests

def fetch_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    st.title("Wettervorhersage App")

    # Eingabefeld für den Städtenamen
    city = st.text_input("Gib den Namen einer Stadt ein:", "Berlin")

    # Button zum Abrufen der Wetterdaten
    if st.button("Wettervorhersage abrufen"):
        weather_data = fetch_weather_data(city)

        # Wenn Daten erfolgreich abgerufen wurden, visualisiere sie
        if weather_data.get("cod") == 200:
            st.subheader(f"Wetter in {city}:")
            st.write(f"Temperatur: {weather_data['main']['temp']} °C")
            st.write(f"Luftfeuchtigkeit: {weather_data['main']['humidity']} %")
            st.write(f"Windgeschwindigkeit: {weather_data['wind']['speed']} m/s")
        else:
            st.write("Wetterdaten konnten nicht abgerufen werden. Bitte überprüfe den Städtenamen.")

if __name__ == "__main__":
    main()


