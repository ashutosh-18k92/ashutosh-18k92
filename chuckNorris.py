import requests
X_RapidAPI_Key = os.getenv("X_RapidAPI_Key")
url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

headers = {
    'accept': "application/json",
    'x-rapidapi-key': X_RapidAPI_Key,
    'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

print(response.text)