import requests
# Send Notification to phone (Using Pushover)
def send_to_pushover(msg, user_key, api_token):
        requests.post(
            "https://api.pushover.net/1/messages.json",
            data = {
                "token": api_token,
                "user": user_key,
                "message": msg
            }
        )
        pass 
