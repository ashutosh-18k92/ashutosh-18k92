import http.client

conn = http.client.HTTPSConnection("matchilling-chuck-norris-jokes-v1.p.rapidapi.com")

headers = {
    'accept': "application/json",
    'x-rapidapi-key': "7df969622bmsh6a457d47f217115p1ec357jsnb206217e8717",
    'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
    }

conn.request("GET", "/jokes/random", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
