import os
import requests
from flask import Flask
app=Flask(__name__)

@app.route('/')
def index:
    X_RapidAPI_Key = os.getenv("X_RapidAPI_Key")
    url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

    headers = {
        'accept': "application/json",
        'x-rapidapi-key': X_RapidAPI_Key,
        'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    return response.text

if __name__ == "__main__":
    app.run(debug=true)