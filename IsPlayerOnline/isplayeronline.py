import requests
import os

player = input("What player would you like to check the online status of? ")
apikey = os.getenv("HYPIXEL_API_KEY")
if apikey is None:
    apikey = input("Since there was no API key found from Environment Variable HYPIXEL_API_KEY, please enter your API key. ")
if len(player) <= 16:
    resp = requests.get("https://api.mojang.com/users/profiles/minecraft/{0}".format(player)) 
    assert resp.status_code == 200, "Player does not exist."
    resp = resp.json()
    player = resp["id"]
resp = requests.get("https://api.hypixel.net/player?key={0}&uuid={1}".format(apikey, player))
assert resp.status_code == 200, "Something went wrong, response code: {0}".format(resp.status_code)
resp = resp.json()
assert "player" in resp and "lastLogin" in resp["player"], "Player has never played on Hypixel"
if "lastLogout" not in resp["player"]:
    print("Player is online")
if resp["player"]["lastLogin"] < resp["player"]["lastLogout"]:
    print("Player is not online")
else:
    print("Player is online")