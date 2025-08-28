import os
from dotenv import load_dotenv
from files.get_weather import get_weather
from files.send_to_pushover import send_to_pushover

load_dotenv()
weather_api_key = os.environ.get("weather_api_key")
pushover_api_token = os.environ.get("pushover_api_token")
pushover_user_key = os.environ.get("pushover_user_key")

lon="-118.243683"
lat="34.052235"

def main():
    todays_weather_data = get_weather(lat,lon,weather_api_key)
    weather_condition = todays_weather_data.get("weather", [{}])[0].get("main", "")
    msg = ":)"
    if "Rain" in weather_condition:
        msg = "It's raining :|" 
    if "Snow" in weather_condition:
        msg = "It's snowing :|"
    send_to_pushover(msg,pushover_user_key,pushover_api_token)    
    pass


if __name__ == "__main__":
    main()