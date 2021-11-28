import discord
from TOKEN import TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print(f"\033[31mLogged in as {client.user}\033[39m")

@client.event
async def on_message(message):
    if message.content.startswith("$pwd"):
        await message.channel.send(os.getcwd())

client.run(TOKEN)

