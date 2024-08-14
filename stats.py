import requests
import datetime

key = ""

def usernameToUUID(username):
    request = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
    data = request.json()
    return data["id"]

def playerInfo(key,uuid):
    r = requests.get(f"https://api.hypixel.net/v2/player?key={key}&uuid={uuid}")
    data = r.json()
    if data["success"] == True and data["player"] != None:
        return data                      
    else:
        print("We couldn't find the user.")
        return "None"
        
def rankParser(data):
    rank = "None"
    for i in data["player"]:
            if i == "packageRank":
                rank = data["player"][i]
            if i == "newPackageRank":
                rank = data["player"][i]
            if i == "monthlyPackageRank":
                rank = data["player"][i]
            if i == "rank":
                rank = data["player"][i]
    return rank
def petParser(data):
    Currentpet = "None"
    for i in data["player"]:
        if i == "currentPet":
            Currentpet = data["player"][i]
    return Currentpet        
def petNameParser(data,pet):
    petname = "None"
    if pet != "None":
        for i in data["player"]:
            if i == "petStats":
                petname = data["player"]["petStats"][pet]["name"]
    return petname                 

def firstLogin(data):
    firstLogin = 0
    for i in data["player"]:
        if i == "firstLogin":
            firstLogin = data["player"][i]
            firstLogin = datetime.datetime.fromtimestamp(firstLogin // 1000.0)
    return firstLogin        
def lastLogin(data):
    lastLogin = 0
    for i in data["player"]:
        if i == "lastLogin":
            lastLogin = data["player"][i]
            lastLogin = datetime.datetime.fromtimestamp(lastLogin // 1000.0) 
    return lastLogin
def isOnline(data):
    if data["player"]["lastLogin"] > data["player"]["lastLogout"]:
        return True
    else:
        return False                                                                
myuuid = usernameToUUID("Narutoduck")
data = playerInfo(key,myuuid)
rank = rankParser(data)
currentPet = petParser(data)
petname = petNameParser(data,currentPet)
firstlogin = firstLogin(data)
lastlogin = lastLogin(data)
isonline = isOnline(data)
print(isonline)   
