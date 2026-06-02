"""Simple OpenWeather API CLI app."""

# Import the standard library modules we need.
import json
import os
from collections import defaultdict
from datetime import datetime

import requests
from dotenv import load_dotenv
from requests.exceptions import HTTPError, RequestException

# Store the API endpoints in one place so they are easy to read and change.
CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

# Load variables from a local .env file before reading the process environment.
load_dotenv()


# Read the API key from the environment.
def get_api_key() -> str:
    return os.getenv("OPENWEATHER_API_KEY", "")


# Ask the user for a city name and remove extra spaces.
def get_city_name() -> str:
    city_name = input("Enter a city name: ").strip()
    return city_name


# Ask the user if they want the 3-day forecast version.
def get_forecast_choice() -> bool:
    while True:
        choice = input("Choose 1 for current weather or 2 for a 3-day forecast: ").strip()
        if choice == "1":
            return False
        if choice == "2":
            return True
        print("Please type 1 or 2.")


# Ask the user for their preferred temperature unit.
def get_temperature_unit() -> str:
    while True:
        choice = input("Choose 1 for Celsius or 2 for Fahrenheit: ").strip()
        if choice == "1":
            return "metric"
        if choice == "2":
            return "imperial"
        print("Please type 1 or 2.")


# Call the OpenWeather current weather API and return the parsed data.
def fetch_weather(city_name: str, api_key: str, units: str) -> dict:
    # Use `requests` to call the current weather endpoint with query params.
    params = {"q": city_name, "appid": api_key, "units": units}
    response = requests.get(CURRENT_WEATHER_URL, params=params, timeout=10)
    # Raise an HTTPError for bad HTTP status codes.
    response.raise_for_status()
    # Parse and return the JSON response body.
    return response.json()


# Call the OpenWeather forecast API and return the parsed data.
def fetch_forecast(city_name: str, api_key: str, units: str) -> dict:
    # Use `requests` to call the 5-day/3-hour forecast endpoint.
    params = {"q": city_name, "appid": api_key, "units": units}
    response = requests.get(FORECAST_URL, params=params, timeout=10)
    # Raise an HTTPError for bad HTTP status codes.
    response.raise_for_status()
    # Parse and return the JSON response body.
    return response.json()


# Print the weather information in a simple format.
def print_weather(weather_data: dict, units: str) -> None:
    city_name = weather_data["name"]
    country_code = weather_data["sys"]["country"]
    description = weather_data["weather"][0]["description"].title()
    temperature = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]
    
    # Determine the correct unit symbol based on units parameter.
    unit_symbol = "°C" if units == "metric" else "°F"
    wind_speed = weather_data["wind"]["speed"]
    pressure = weather_data["main"]["pressure"]

    print(f"\nWeather for {city_name}, {country_code}")
    print(f"Description: {description}")
    print(f"Temperature: {temperature}{unit_symbol}")
    print(f"Feels like: {feels_like}{unit_symbol}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Pressure: {pressure} hPa")


# Group forecast entries by day so we can show one simple summary per day.
def build_three_day_summary(forecast_data: dict) -> list[dict]:
    daily_data = defaultdict(list)

    # Collect the forecast entries for each date.
    for item in forecast_data["list"]:
        date_text = item["dt_txt"].split(" ")[0]
        daily_data[date_text].append(item)

    summary = []

    # Build a small summary for the first three days we received.
    for date_text in sorted(daily_data.keys())[:3]:
        items = daily_data[date_text]
        temperatures = [entry["main"]["temp"] for entry in items]
        descriptions = [entry["weather"][0]["description"] for entry in items]

        summary.append(
            {
                "date": date_text,
                "min_temp": min(temperatures),
                "max_temp": max(temperatures),
                "description": descriptions[0].title(),
            }
        )

    return summary


# Print the 3-day forecast in a simple format.
def print_three_day_forecast(forecast_data: dict, units: str) -> None:
    city_name = forecast_data["city"]["name"]
    country_code = forecast_data["city"]["country"]
    summary = build_three_day_summary(forecast_data)
    
    # Determine the correct unit symbol based on units parameter.
    unit_symbol = "°C" if units == "metric" else "°F"

    print(f"\n3-Day Forecast for {city_name}, {country_code}")

    # Show one simple line for each day in the forecast summary.
    for item in summary:
        date_value = datetime.strptime(item["date"], "%Y-%m-%d").strftime("%d/%m/%Y")
        print(f"{date_value}: {item['description']}")
        print(f"  Low: {item['min_temp']}{unit_symbol}")
        print(f"  High: {item['max_temp']}{unit_symbol}")


# Run the program and handle simple errors for the user.
def main() -> None:
    api_key = get_api_key()
    if not api_key:
        print("Please set the OPENWEATHER_API_KEY environment variable first.")
        return

    city_name = get_city_name()
    if not city_name:
        print("City name cannot be empty.")
        return

    wants_forecast = get_forecast_choice()
    units = get_temperature_unit()

    try:
        if wants_forecast:
            forecast_data = fetch_forecast(city_name, api_key, units)
            print_three_day_forecast(forecast_data, units)
        else:
            weather_data = fetch_weather(city_name, api_key, units)
            print_weather(weather_data, units)
    except HTTPError as error:
        # `requests.HTTPError` includes the response; show a short message.
        print(f"OpenWeather API returned an HTTP error: {error}")
    except RequestException:
        # Network-level errors from `requests`.
        print("Network error. Please check your internet connection.")
    except KeyError:
        print("Unexpected response from the API.")


# Start the app when the file is run directly.
if __name__ == "__main__":
    main()
