import requests 
from files.get_weather import get_weather
from files.send_to_pushover import send_to_pushover
from files.DataClass import Data



def main():
    todaysweatherdata = get_weather(city,state,country,weather_api_key)
    print(todaysweatherdata)
    msg
    if "rain" in todaysweatherdata:
        msg = "It's raining" 
    if "snow" in todaysweatherdata:
        msg = "It's snowing"
    Today = Data(todaysweatherdata, msg)
    print(msg)    
    return Today

# send_to_pushover(Today,pushover_user_key,pushover_api_token)

