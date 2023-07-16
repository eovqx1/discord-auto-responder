
-- made by eovqx


import discord
from discord.ext import commands
import asyncio
import time

client = discord.Client()
token =  input("Token: ")



@client.event

async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id == 891837001865773097:
        await message.channel.send('<@891837001865773097> YO MASKED SHUT THE FUCK UP LIL NIGGA :rofl: :rofl: :rofl: THIS NIGGA SO ASS :rofl: :rofl: :rofl: UR A CLOWN FAGGOT ASS NIGGA :clown: :clown: :clown: COME DIE MONKEY :knife: :knife: :knife: IMA BURY U ALIVE U COON DYKE :headstone: :headstone: :headstone:  UR SO EZ LOOOOOL :joy: :joy: :joy:  UR DYING RN LMFAOOOOOOOOOO :rofl: :rofl: :rofl: ')
        

client.run(token, bot=False)