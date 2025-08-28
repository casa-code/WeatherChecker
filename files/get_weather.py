import requests
# Step 1: Get Weather Data (Using OpenWeatherMap)
def get_weather(city_name,state_code,country_code, api_key):
    #url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={api_key}"
    response = requests.get(url)
    weather_instance = response.json()
    print(weather_instance)
    return weather_instance
