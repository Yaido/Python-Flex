import discord
intents = discord.Intents.default()
intents.messages= True
client = discord.Client(intents=intents)

filepointer=open("C:/Users/ywalt/OneDrive/Bureaublad/MA/Jaar 1/Periode1/FLEX/Python/04-DiscordBot/Geheim", "r")
bottoken=filepointer.readline()
filepointer.close()

client.run(bottoken)

