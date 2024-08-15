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
                rank = data["player"][i].replace("_PLUS","+")
            if i == "monthlyPackageRank" and data["player"][i] != "NONE":
                rank = data["player"][i].replace("_PLUS","+")
            if i == "rank":
                rank = data["player"][i].replace("SUPERSTAR","MVP++")
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
        if pet in data["player"]["petStats"]:
            if "name" in data["player"]["petStats"][pet]:
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
    Status = False
    if "lastLogin" and "lastLogout" in data["player"]:
        if data["player"]["lastLogin"] > data["player"]["lastLogout"]:
            Status = True
    return Status
def karmaParser(data):
    karma = 0
    for i in data["player"]:
        if i == "karma":
            karma = data["player"][i]
    return karma
def totalXP(data):
    xp = 0
    for i in data["player"]:
        if i == "networkExp":
            xp = data["player"][i]
    return xp        
def currentGadget(data):
    Gadget = "None"
    for i in data["player"]:
        if i == "currentGadget":
            Gadget = data["player"][i].replace("_"," ")
    return Gadget
def userLanguage(data):
    Language = "None"
    if "userLanguage" in data["player"]:
        Language = data["player"]["userLanguage"]
    return Language    
def Favourites(data):
    fav = "None"
    for i in data["player"]:
        if i == "vanityFavorites":
            fav = data["player"][i].replace("_"," ").replace(";"," & ")
    return fav
def currentCloak(data):
    Cloak = "None"
    for i in data["player"]:
        if i == "currentCloak":
            Cloak = data["player"][i]
    return Cloak
def currentClickEffect(data):
    Effect = "None"
    for i in data["player"]:
        if i == "currentClickEffect":
            Effect = data["player"][i]
    return Effect
def socialMediaParser(data):
    Socials = ""
    if "socialMedia" in data["player"]:
        if "links" in data["player"]["socialMedia"]:
            for i in data["player"]["socialMedia"]["links"]:
                Socials += f"{i}: {data['player']['socialMedia']['links'][i]}\n"
    if len(Socials) == 0:
        Socials = "None"        
    return Socials                                                                                                                                  
myuuid = usernameToUUID("IamHomelander")
data = playerInfo(key,myuuid)
rank = rankParser(data)
currentPet = petParser(data)
petname = petNameParser(data,currentPet)
firstlogin = firstLogin(data)
lastlogin = lastLogin(data)
isonline = isOnline(data)
karma = karmaParser(data)
xp = totalXP(data)
Gadget = currentGadget(data)
favourites = Favourites(data)
Cloak = currentCloak(data)
ClickEffect = currentClickEffect(data)
Socials = socialMediaParser(data)
Language = userLanguage(data)
