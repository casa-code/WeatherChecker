import requests
# Step 1: Get Weather Data (Using OpenWeatherMap)
def get_weather(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    weather_json = response.json()
    print(weather_json)
    return weather_json


