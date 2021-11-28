import discord
import io
import aiohttp
from features import show_atom

async def send_picture(url, message):
    async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return await message.channel.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await message.channel.send(file=discord.File(data, 'cool_image.png'))

async def main(msg, prefix):
    msg_content = msg.content
    main_msg = msg_content[len(prefix)+1:]

    if main_msg.startswith("atom"):
        await show_atom.show_data(msg, main_msg)

