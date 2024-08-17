import discord
from discord.ext import commands
import stats as s
import json

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!',intents=intents)
token = ""
with open("settings.json","r") as f:
    data = json.load(f)
    token = data["token"]
    f.close()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Your stats: !stats"))
@bot.command(description="Check your Hypixel Stats!",usage="!stats <username>")
async def stats(ctx, arg: str):
    uuid = s.usernameToUUID(arg)
    data = s.playerInfo(uuid)
    namemc = f"https://namemc.com/profile/{arg}"
    skywarsWins = s.skywarsTotalWins(data)
    skywarsKills = s.skywarsTotalKills(data)
    dropperWins = s.dropperWins(data)
    bedwarsKills = s.bedwarsKills(data)
    skywarsSouls = s.skywarsSouls(data)
    murdermysteryCoins = s.murdermysteryCoins(data)
    embed = discord.Embed(title="Hypixel Stats Checker Bot",description="Here is your stats:",color=0x00ff00)
    embed.add_field(name="Username",value=arg,inline=False)
    embed.add_field(name="UUID",value=uuid,inline=False)
    embed.add_field(name="NameMc Profile",value=namemc,inline=False)
    embed.add_field(name="SkyWars Wins",value=skywarsWins,inline=False)
    embed.add_field(name="SkyWars Kills",value=skywarsKills,inline=False)
    embed.add_field(name="Dropper Wins",value=dropperWins,inline=False)
    embed.add_field(name="BedWars Kills",value=bedwarsKills,inline=False)
    embed.add_field(name="SkyWars Souls",value=skywarsSouls,inline=False)
    embed.add_field(name="MurderMystery Coins",value=murdermysteryCoins,inline=False)
    await ctx.send(embed=embed)
bot.run(token)    
