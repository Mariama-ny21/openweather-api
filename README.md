# OpenWeather API Python Project

This is a very small Python command-line project that gets the current weather for a city from the OpenWeather API, and it can also show a simple 3-day forecast.

## What it does

- Asks for a city name
- Asks if you want a 3-day forecast
- Calls the OpenWeather current weather API
- Calls the OpenWeather forecast API when you choose the 3-day option
- Prints the current weather, or a simple daily forecast summary for the next 3 days

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

```text
Enter a city name: London
Choose 1 for current weather or 2 for a 3-day forecast: 2
```

Choose `1` to show current weather, or `2` to show the 3-day forecast.
