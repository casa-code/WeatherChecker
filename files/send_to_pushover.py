import requests
from files.DataClass import Data
def send_to_pushover(Data_obj: Data, user_key, api_token):
        requests.post(
            "https://api.pushover.net/1/messages.json",
            data = {
                "token": api_token,
                "user": user_key,
                "message": Data.msg
            }
        )
        pass 
