import discord
intents = discord.Intents.default()
intents.messages= True
client = discord.Client(intents=intents)

filepointer=open("C:/Geheim/DiscordBot.txt", "r")
bottoken=filepointer.readline()
filepointer.close()

client.run(bottoken)

async def on_ready():
    guild = client.guilds[0]
    print(guild.name, "is de naam van deze server")
    print(client.user, "is geconnect aan de server")

on_ready