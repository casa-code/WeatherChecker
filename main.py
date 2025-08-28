import os
from files.get_weather import get_weather
from files.send_to_pushover import send_to_pushover
from files.DataClass import Data

weather_api_key = os.environ.get("weather_api_key")
pushover_api_token = os.environ.get("pushover_api_token")
pushover_user_key = os.environ.get("pushover_user_key")

lat="34.052235"
lon="-118.243683"


def main():
    todaysweatherdata = get_weather(lat,lon,weather_api_key)
    print(todaysweatherdata)
    msg = ":), Today it's not raining or snowing!"
    if "rain" in todaysweatherdata["main"]:
        msg = "It's raining :|" 
    if "snow" in todaysweatherdata["main"]:
        msg = "It's snowing :|"
    print(msg) 
    pass

# send_to_pushover(Today.msg,pushover_user_key,pushover_api_token)

