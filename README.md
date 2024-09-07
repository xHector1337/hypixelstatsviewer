![Ekran görüntüsü 2024-09-07 170424](https://github.com/user-attachments/assets/e45dd8e3-f6a6-4412-a8a6-fd477e6b6f36)
# Hypixel Stats Viewer in Python

`stats.py` is a hypixel library written in python and `bot.py` is a discord bot written with `discord.py` and `stats.py`

# Discord Bot Installation and Usage:

Install every dependencies using `pip install -r requirements.txt` then edit `settings.json` and write your own Discord Bot Token and Hypixel Api Key.
Then you are ready to go! Check your stats by typing `!stats ` with username as your argument. After that your stats will be waiting for you!

# Hypixel Stats Viewer Installation and Usage:

If you are only going to use this library, you **don't need to install discord.py** dependency.

## Basic Usage:

```
myuuid = usernameToUUID("IamSaulGoodman")
data = playerInfo(myuuid)
myBedwarsWins = bedwarsWins(data)
print(myBedwarsWins)
```
All of the checker functions take playerInfo data as argument. If you want to check a value that the library doesn't have a function for.
You can use simpleCustomGameStatsChecker or simpleCustomGameStatsCheckerEx functions.

Example usage of simpleCustomGameStatsChecker:
```
myuuid = usernameToUUID("IamSaulGoodman")
data = playerInfo(myuuid)
GameName = "SkyWars"
valueToCheck = "kills"
myKills = simpleCustomGameStatsChecker(GameName,data,valueToCheck)
print(myKills)
```
It'll print your SkyWars kills.

Example usage of simpleCustomGameStatsCheckerEx:
```
def dropperFails(data): # It is a function to demonstrate usage of simpleCustomGameStatsCheckerEx function.
    fails = simpleCustomGameStatsCheckerEx("Arcade",data,"dropper","fails")
    return fails
```

Happy coding!

## Disclaimer

Please don't make too many requests to Hypixel API and don't use the library for illegal purposes.
