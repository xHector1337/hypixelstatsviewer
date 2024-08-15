import requests
import datetime

key = ""

def usernameToUUID(username):
    request = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username.strip()}")
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
def giftsStats(data):
    Gifted = 0
    if "giftingMeta" in data["player"]:
        if "giftsGiven" in data["player"]["giftingMeta"]:
            Gifted = data["player"]["giftingMeta"]["giftsGiven"]
    return Gifted
def skywarsTotalWins(data):
    wins = 0
    if "stats" in data["player"]:
       if "SkyWars" in data["player"]["stats"]:
           if "wins" in data["player"]["stats"]["SkyWars"]:
               wins = data["player"]["stats"]["SkyWars"]["wins"]
    return wins
def skywarsTotalKills(data):
    kills = 0
    if "stats" in data["player"]:
        if "SkyWars" in data["player"]["stats"]:
            if "kills" in data["player"]["stats"]["SkyWars"]:
                kills = data["player"]["stats"]["SkyWars"]["kills"]
    return kills
def skywarsTeamsKills(data):
    kills = 0
    if "stats" in data["player"]:
        if "SkyWars" in data["player"]["stats"]:
            if "kills_team" in data["player"]["stats"]["SkyWars"]:
                kills = data["player"]["stats"]["SkyWars"]["kills_team"]
    return kills
def skywarsSoloKills(data):
    kills = 0
    if "stats" in data["player"]:
        if "SkyWars" in data["player"]["stats"]:
            if "kills_solo" in data["player"]["stats"]["SkyWars"]:
                kills = data["player"]["stats"]["SkyWars"]["kills_solo"]
    return kills
def skywarsSoloWins(data):
    wins = 0
    if "stats" in data["player"]:
        if "SkyWars" in data["player"]["stats"]:
            if "wins_solo" in data["player"]["stats"]["SkyWars"]:
                wins = data["player"]["stats"]["SkyWars"]["wins_solo"]
    return wins
def skywarsTeamsWins(data):
    wins = 0
    if "stats" in data["player"]:
        if "SkyWars" in data["player"]["stats"]:
            if "wins_team" in data["player"]["stats"]["SkyWars"]:
                wins = data["player"]["stats"]["SkyWars"]["wins_team"]
    return wins                                                            
def skywarsSouls(data):
    souls = 0
    if "stats" in data["player"]:
        if "SkyWars" in data["player"]["stats"]:
            if "souls" in data["player"]["stats"]["SkyWars"]:
                souls = data["player"]["stats"]["SkyWars"]["souls"]
    return souls
def buildbattleTotalWins(data):
    wins = 0
    if "stats" in data["player"]:
        if "BuildBattle" in data["player"]["stats"]:
            if "wins" in data["player"]["stats"]["BuildBattle"]:
                wins = data["player"]["stats"]["BuildBattle"]["wins"]
    return wins
def buildbattleCoins(data):
    coins = 0
    if "stats" in data["player"]:
        if "BuildBattle" in data["player"]["stats"]:
            if "coins" in data["player"]["stats"]["BuildBattle"]:
                coins = data["player"]["stats"]["BuildBattle"]["coins"]
    return coins
def buildbattleSelectedHat(data):
    newSelectedHat = "None"
    if "stats" in data["player"]:
        if "BuildBattle" in data["player"]["stats"]:
            if "new_selected_hat" in data["player"]["stats"]["BuildBattle"]:
                newSelectedHat = data["player"]["stats"]["BuildBattle"]["new_selected_hat"]
    if newSelectedHat == "hats_none":
        newSelectedHat = "None"
    return newSelectedHat.replace("_"," ")
def buildbattleSelectedBackground(data):
    background = "None"
    if "stats" in data["player"]:
        if "BuildBattle" in data["player"]["stats"]:
            if "selected_backdrop" in data["player"]["stats"]["BuildBattle"]:
                background = data["player"]["stats"]["BuildBattle"]["selected_backdrop"].split("backdrops_")[1].replace("_"," ")
    return background            
def buildbattleSoloWins(data):
    wins = 0
    if "stats" in data["player"]:
        if "BuildBattle" in data["player"]["stats"]:
            if "wins_solo_normal" in data["player"]["stats"]["BuildBattle"]:
                wins = data["player"]["stats"]["BuildBattle"]["wins_solo_normal"]
    return wins
def buildbattleTeamsWins(data):
    wins = 0
    if "stats" in data["player"]:
        if "BuildBattle" in data["player"]["stats"]:
            if "wins_teams_normal" in data["player"]["stats"]["BuildBattle"]:
                wins = data["player"]["stats"]["BuildBattle"]["wins_teams_normal"]
    return wins
def buildbattleLastPurchasedSong(data):
    song = "None"
    if "stats" in data["player"]:
        if "BuildBattle" in data["player"]["stats"]:
            if "last_purchased_song" in data["player"]["stats"]["BuildBattle"]:
                song = data["player"]["stats"]["BuildBattle"]["last_purchased_song"]
    return song
def userRecentGameType(data):
    game = "None"
    if "mostRecentGameType" in data["player"]:
        game = data["player"]["mostRecentGameType"]
    return game
def buildbattleSoloMostPoints(data):
    points = 0
    if "stats" in data["player"]:
        if "BuildBattle" in data["player"]["stats"]:
            if "solo_most_points" in data["player"]["stats"]["BuildBattle"]:
                points = data["player"]["stats"]["BuildBattle"]["solo_most_points"]
    return points                                                
                                                                                                                                                                                                                                                       
myuuid = usernameToUUID("IamSaulGoodman")
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
gifts = giftsStats(data)
print(userRecentGameType(data))

