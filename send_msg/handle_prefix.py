import json
from pathlib import Path
from .send_message import main

path = Path()
path = f"{path.parent.absolute()}\\bot.json"

with open(path, "r") as prefixes:
    custom_prefixes = json.load(prefixes)

def set_prefix(prefix):
    custom_prefixes["custom_prefix"] = prefix
    with open(path, "w") as f:
        json.dump(custom_prefixes, f)

async def handle(msg):
    msg_content = msg.content
    setprefix = custom_prefixes["set_prefix"]
    resetprefix = custom_prefixes["reset_prefix"]

    if msg_content.startswith(setprefix):
        prefix = msg_content[len(setprefix)+1:]
        set_prefix(prefix)
        await msg.channel.send(f"Custom prefix set to: {prefix}")
    
    if msg_content.startswith(resetprefix):
        prefix = msg_content[len(resetprefix)+1:]
        set_prefix(custom_prefixes["default_prefix"])
        await msg.channel.send(f"Default prefix restored")

    if msg_content.startswith(custom_prefixes["custom_prefix"]):
        await main(msg, custom_prefixes["custom_prefix"])