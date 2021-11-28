import discord
from send_msg import handle_prefix


client = discord.Client()
TOKEN = "OTEzMjY3NTE5NTI2MTcwNjU0.YZ8AqA.fbgfPWEZOCvQoP7OHC8yolrr2SM"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await handle_prefix.handle(message)

client.run(TOKEN)