import requests

key = ""

def usernameToUUID(username):
    request = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
    data = request.json()
    return data["id"]

def playerInfo(key,uuid):
    r = requests.get(f"https://api.hypixel.net/v2/player?key={key}&uuid={uuid}")
    data = r.json()
    username = ""
    rank = ""
    currentPet = "None"
    if data["success"] == True and data["player"] != None:
        username = data["player"]["displayname"]
        for i in data["player"]:
            if i == "currentPet":
                currentPet = data["player"]["currentPet"]
    else:
        print("We couldn't find the user.")            
myuuid = usernameToUUID("PostalDude")
playerInfo(key,myuuid)   
