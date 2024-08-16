import requests
import datetime
import json

key = ""
with open("settings.json","r") as f:
    d = json.load(f)
    key = d["key"]
    f.close()

def usernameToUUID(username):
    request = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username.strip()}")
    data = request.json()
    return data["id"]
def playerInfo(key,uuid):
    r = requests.get(f"https://api.hypixel.net/v2/player?key={key}&uuid={uuid}")
    data = r.json()
    if data["success"] == True and data["player"] != None and "null":
        return data                      
    else:
        print("We couldn't find the user.")
        return False
        
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
def simpleCustomGameStatsChecker(GameName,data,valueToCheck):
    stats = "None"
    if "stats" in data["player"]:
        if str(GameName) in data["player"]["stats"]:
            if str(valueToCheck) in data["player"]["stats"][str(GameName)]:
                stats = data["player"]["stats"][str(GameName)][str(valueToCheck)] 
    return stats    
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
def userRecivedGifts(data):
    gifts = 0
    if "giftingMeta" in data["player"]:
        if "bundlesRecieved" in data["player"]["giftingMeta"]:
            gifts = data["player"]["giftingMeta"]["bundlesRecieved"]
    return gifts
def totalDailyRewards(data):
    rewards = 0
    if "totalDailyRewards" in data["player"]:
        rewards = data["player"]["totalDailyRewards"]
    return rewards
def bedwarsExperience(data):
    xp = 0
    if "stats" in data["player"]:
        if "Bedwars" in data["player"]["stats"]:
            if "Experience" in data["player"]["stats"]["Bedwars"]:
                xp = data["player"]["stats"]["Bedwars"]["Experience"]
    return xp
def bedwarsGamesPlayed(data):
    games = 0
    if "stats" in data["player"]:
        if "Bedwars" in data["player"]["stats"]:
            if "games_played_bedwars" in data["player"]["stats"]["Bedwars"]:
                games = data["player"]["stats"]["Bedwars"]["games_played"]
    return games
def bedwarsCoins(data):
    coins = 0
    if "stats" in data["player"]:
        if "Bedwars" in data["player"]["stats"]:
            if "coins" in data["player"]["stats"]["Bedwars"]:
                coins = data["player"]["stats"]["Bedwars"]["coins"]
    return coins                        
def bedwarsTotalDeaths(data):
    death = 0
    if "stats" in data["player"]:
        if "Bedwars" in data["player"]["stats"]:
            if "deaths_bedwars" in data["player"]["stats"]["Bedwars"]:
                death = data["player"]["stats"]["Bedwars"]["deaths_bedwars"]
    return death
def bedwarsTotalLoses(data):
    loses = 0
    if "stats" in data["player"]:
        if "Bedwars" in data["player"]["stats"]:
            if "loses_bedwars" in data["player"]["stats"]["Bedwars"]:
                loses = data["player"]["stats"]["Bedwars"]["loses_bedwars"]
    return loses
def bedwarsTotalPurchasedItems(data):
    items = 0
    if "stats" in data["player"]:
        if "Bedwars" in data["player"]["stats"]:
            if "_items_purchased_bedwars" in data["player"]["stats"]["Bedwars"]:
                items = data["player"]["stats"]["Bedwars"]["_items_purchased_bedwars"]
    return items
def bedwarsKills(data):
    kills = 0
    if "stats" in data["player"]:
        if "Bedwars" in data["player"]["stats"]:
            if "kills_bedwars" in data["player"]["stats"]["Bedwars"]:
                kills = data["player"]["stats"]["Bedwars"]["Bedwars"]["kills_bedwars"]
    return kills
def bedwarsTotalBrokenBeds(data):
    beds = 0
    if "stats" in data["player"]:
        if "Bedwars" in data["player"]["stats"]:
            if "beds_broken_bedwars" in data["player"]["stats"]["Bedwars"]:
                beds = data["player"]["stats"]["Bedwars"]["beds_broken_bedwars"]
    return beds
def bedwarsWins(data):
    wins = 0
    if "stats" in data["player"]:
        if "Bedwars" in data["player"]["stats"]:
            if "wins_bedwars" in data["player"]["stats"]["Bedwars"]:
                wins = data["player"]["stats"]["Bedwars"]["wins_bedwars"]
    return wins
def bedwarsActiveIslandTopper(data):
    topper ="None"
    if "stats" in data["player"]:
        if "Bedwars" in data["player"]["stats"]:
            if "activeIslandTopper" in data["player"]["stats"]["Bedwars"]:
                topper = data["player"]["stats"]["Bedwars"]["activeIslandTopper"].split("islandtopper_")[1]
    return topper
def bedwarsActiveProjectileTrail(data):
    trail = "None"
    if "stats" in data["player"]:
        if "Bedwars" in data["player"]["stats"]:
            if "activeProjectileTrail" in data["player"]["stats"]["Bedwars"]:
                trail = data["player"]["stats"]["Bedwars"]["activeProjectileTrail"].split("projectiletrail_")[1]
    return trail
def bedwarsActiveSprays(data):
    sprays = "None"
    if "stats" in data["player"]:
        if "Bedwars" in data["player"]["stats"]:
            if "activeSprays" in data["player"]["stats"]["Bedwars"]:
                sprays = data["player"]["stats"]["Bedwars"]["activeSprays"].split("sprays_")[1]
    return sprays
def bedwarsActiveKillEffect(data):
    effect = "None"
    if "stats" in data["player"]:
        if "Bedwars" in data["player"]["stats"]:
            if "activeKillEffect" in data["player"]["stats"]["Bedwars"]:
                effect = data["player"]["stats"]["Bedwars"]["activeKillEffect"].split("killeffect_")[1].replace("_"," ")
    return effect            
def bedwarsActiveGlyph(data):
    glyph = "None"
    if "stats" in data["player"]:
        if "Bedwars" in data["player"]["stats"]:
            if "activeGlyph" in data["player"]["stats"]["Bedwars"]:
                glyph = data["player"]["stats"]["Bedwars"]["activeGlyph"].split("glyph_")[1]
    return glyph
def bedwarsActiveDeathCry(data):
    deathCry = "None"
    if "stats" in data["player"]:
        if "Bedwars" in data["player"]["stats"]:
            if "activeDeathCry" in data["player"]["stats"]["Bedwars"]:
                deathCry = data["player"]["stats"]["Bedwars"]["activeDeathCry"].split("deathcry")[1]
    return deathCry
def bedwarsVictoryDance(data):
    victoryDance = "None"
    if "stats" in data["player"]:
        if "Bedwars" in data["player"]["stats"]:
            if "activeVictoryDance" in data["player"]["stats"]["Bedwars"]:
                victoryDance = data["player"]["stats"]["Bedwars"]["activeVictoryDance"].split("victorydance_")[1].replace("_"," ")
    return victoryDance
def bedwarsActiveNPCSkin(data):
    skin = "None"
    if "stats" in data["player"]:
        if "Bedwars" in data["player"]["stats"]:
            if "activeNPCSkin" in data["player"]["stats"]["Bedwars"]:
                skin = data["player"]["stats"]["Bedwars"]["activeNPCSkin"].split("skin_")[1]
    return skin
def skywarsHighestWinStreak(data):
    streak = 0
    if "stats" in data["player"]:
        if "SkyWars" in data["player"]["stats"]:
            if "highestWinstreak" in data["player"]["stats"]["SkyWars"]:
                streak = data["player"]["stats"]["SkyWars"]["highestWinstreak"]
    return streak
def skywarsHighestKillStreak(data):
    streak = 0
    if "stats" in data["player"]:
        if "SkyWars" in data["player"]["stats"]:
            if "highestKillstreak" in data["player"]["stats"]["SkyWars"]:
                streak = data["player"]["stats"]["SkyWaras"]["highestKillstreak"]
    return streak
def skywarsTotalLosses(data):
    losses = 0
    if "stats" in data["player"]:
        if "SkyWars" in data["player"]["stats"]:
            if "losses" in data["player"]["stats"]["SkyWars"]:
                losses = data["player"]["stats"]["SkyWars"]["losses"]
    return losses
def skywarsTotalDeaths(data):
    deaths = 0
    if "stats" in data["player"]:
        if "SkyWars" in data["player"]["stats"]:
            if "deaths" in data["player"]["stats"]["SkyWars"]:
                deaths = data["player"]["stats"]["SkyWars"]["deaths"]
    return deaths
def skywarsTotalEggsThrown(data):
    eggs = 0
    if "stats" in data["player"]:
        if "SkyWars" in data["player"]["stats"]:
            if "egg_thrown" in data["player"]["stats"]["SkyWars"]:
                eggs = data["player"]["stats"]["SkyWars"]["egg_thrown"]
    return eggs
def skywarsActiveDeathCry(data):
    deathcry = "None"
    if "stats" in data["player"]:
        if "SkyWars" in data["player"]["stats"]:
            if "active_deathcry" in data ["player"]["stats"]["SkyWars"]:
                deathcry = data["player"]["stats"]["SkyWars"]["active_deathcry"].split("deathcry_")[1]
                
def skywarsAssists(data):
    assists = 0
    if "stats" in data["player"]:
        if "SkyWars" in data["player"]["stats"]:
            if "assists" in data["player"]["stats"]["SkyWars"]:
                assists = data["player"]["stats"]["SkyWars"]["assists"]
    return assists            
def skywarsSoloActiveKit(data):
    kit = "None"
    if "stats" in data["player"]:
        if "SkyWars" in data["player"]["stats"]:
            if "activeKit_SOLO" in data["player"]["stats"]["SkyWars"]:
                kit = data["player"]["stats"]["SkyWars"]["activeKit_SOLO"].split("_solo_")[1]
    return kit
def skywarsTeamsActiveKit(data):
    kit = "None"
    if "stats" in data["player"]:
        if "SkyWars" in data["player"]["stats"]:
            if "activeKit_TEAMS" in data["player"]["stats"]["SkyWars"]:
                kit = data["player"]["stats"]["SkyWars"]["activeKit_TEAMS"].split("_team_")[1]
    return kit
def skywarsEnderPearlsThrown(data):
    pearls = 0
    if "stats" in data["player"]:
        if "SkyWars" in data["player"]["stats"]:
            if "enderpearls_thrown" in data["player"]["stats"]["SkyWars"]:
                pearls = data["player"]["stats"]["SkyWars"]["enderpearls_thrown"]
    return pearls
def skywarsTotalHeads(data):
    heads = 0
    if "stats" in data["player"]:
        if "SkyWars" in data["player"]["stats"]:
            if "heads" in data["player"]["stats"]["SkyWars"]:
                heads = data["player"]["stats"]["SkyWars"]["heads"]
    return heads 
def skywarsActiveCage(data):
    cage = "None"
    if "stats" in data["player"]:
        if "SkyWars" in data["player"]["stats"]:
            if "active_cage" in data["player"]["stats"]["SkyWars"]:
                cage = data["player"]["stats"]["SkyWars"]["active_cage"].split("cage_")[1].replace("_"," ")
    return cage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
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
print(skywarsSoloActiveKit(data))
