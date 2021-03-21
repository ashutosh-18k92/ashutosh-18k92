import http.client
X_RapidAPI_Key = os.getenv("X_RapidAPI_Key")
conn = http.client.HTTPSConnection("matchilling-chuck-norris-jokes-v1.p.rapidapi.com")

headers = {
    'accept': "application/json",
    'x-rapidapi-key': X_RapidAPI_Key,
    'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
    }

conn.request("GET", "/jokes/random", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
