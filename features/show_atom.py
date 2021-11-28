import discord
import json
from pathlib import Path

path = Path()
path = f"{path.parent.absolute()}/static/periodictable.json"


def analyze(message):
    #loading json
    with open(path, "r", encoding="utf8") as f:
        info = json.load(f)
    elements = info["elements"]

    #getting input
    message = message.split()
    print(message)
    num, name, specs = None, None, None

    #checks whether number or name is given
    try:
        num = int(message[1])
    except:
        name = message[1]
        name = name.capitalize()
    #getting the atom from the json
    if name:
        elem = [i for i in elements if i["name"] == name][0]
    if num:
        elem = [i for i in elements if i["number"] == num][0]
    #requirement of information from json
    try:
        specs = message[2]
    except:
        specs = "full"

    if specs == "full":
        return elem
    else:
        if specs in elem:
            return [elem["name"], specs, elem[specs]]
        return elem

async def show_data(msg, main_msg):
    try:
        data = analyze(main_msg)
        if type(data) is dict:
            embedVar = discord.Embed(title=f"{data['name']} ({data['symbol']})", color=0x0bb5cb)
            for i in data:
                embedVar.add_field(name=f"{i}", value=f"{data[i]}", inline=False)
            await msg.channel.send(embed=embedVar)
        else:
            embedVar = discord.Embed(title=f"{data[0]}", color=0x0bb5cb, description=f"{data[1]}: {data[2]}")
            await msg.channel.send(embed=embedVar)
    except:
        return

