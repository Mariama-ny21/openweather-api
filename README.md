# OpenWeather API Python Project

This is a very small Python command-line project that gets the current weather for a city from the OpenWeather API, and it can also show a simple 3-day forecast.

## What it does

- Asks for a city name
- Asks if you want a 3-day forecast
- Asks for your preferred temperature unit (Celsius or Fahrenheit)
- Calls the OpenWeather current weather API
- Calls the OpenWeather forecast API when you choose the 3-day option
- Prints the current weather (with temperature, feels-like, humidity, wind speed, and pressure) or a simple daily forecast summary for the next 3 days, all in your selected temperature unit

## Setup

1. Get an API key from OpenWeather.
2. Copy `.env.example` to `.env` in the project root.
3. Put your real API key in `.env`:

```env
OPENWEATHER_API_KEY=your_real_key_here
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the app with Python.

## Run

```bash
python app.py
```

## Example

**Current Weather in Celsius (option 1):**
```text
Enter a city name: London
Choose 1 for current weather or 2 for a 3-day forecast: 1
Choose 1 for Celsius or 2 for Fahrenheit: 1

Weather for London, GB
Description: Partly Cloudy
Temperature: 15.2°C
Feels like: 14.8°C
Humidity: 65%
Wind Speed: 3.5 m/s
Pressure: 1013 hPa
```

**Current Weather in Fahrenheit:**
```text
Enter a city name: London
Choose 1 for current weather or 2 for a 3-day forecast: 1
Choose 1 for Celsius or 2 for Fahrenheit: 2

Weather for London, GB
Description: Partly Cloudy
Temperature: 59.4°F
Feels like: 58.6°F
Humidity: 65%
Wind Speed: 3.5 m/s
Pressure: 1013 hPa
```

**3-Day Forecast in Celsius (option 2):**
```text
Enter a city name: London
Choose 1 for current weather or 2 for a 3-day forecast: 2
Choose 1 for Celsius or 2 for Fahrenheit: 1

3-Day Forecast for London, GB
01/06/2026: Partly Cloudy
  Low: 12.1°C
  High: 16.5°C
02/06/2026: Rainy
  Low: 10.3°C
  High: 14.2°C
03/06/2026: Sunny
  Low: 11.8°C
  High: 18.9°C
```

**3-Day Forecast in Fahrenheit:**
```text
Enter a city name: London
Choose 1 for current weather or 2 for a 3-day forecast: 2
Choose 1 for Celsius or 2 for Fahrenheit: 2

3-Day Forecast for London, GB
01/06/2026: Partly Cloudy
  Low: 53.8°F
  High: 61.7°F
02/06/2026: Rainy
  Low: 50.5°F
  High: 57.6°F
03/06/2026: Sunny
  Low: 53.2°F
  High: 66.0°F
```
