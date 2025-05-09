import asyncio
import random
import discord
from discord import Message
from helper.ids import *
from helper.lists import *


def goofyAnswers(user_message_lower: str, message):
    if user_message_lower.endswith("di"):
        return message.channel.send("manche")
    
    if user_message_lower.endswith("ni"):
        return message.channel.send("gger")

    elif user_message_lower.endswith("toi"):
        return message.channel.send("lette")

    elif user_message_lower.endswith("1") and "m3alim" not in user_message_lower:
        return message.channel.send("2")

    elif user_message_lower.endswith("chou"):
        return message.channel.send("fleur")

    elif user_message_lower.endswith("quand"):
        return message.channel.send("tine")

    elif user_message_lower.endswith("sa"):
        return message.channel.send("blier")

    elif user_message_lower.endswith("si"):
        return message.channel.send("fler")
    
    elif user_message_lower.endswith("lou"):
        return message.channel.send("té")

    elif user_message_lower.endswith("ou"):
        return message.channel.send("blier")
    
    elif user_message_lower.endswith("cho"):
        return message.channel.send("colat")
    
    elif user_message_lower.endswith("voc"):
        return message.channel.send("abulaire")
    
    elif user_message_lower.endswith("qui") or user_message_lower.endswith("ki"):
        return message.channel.send("proquo")
    
    elif user_message_lower.endswith("quoi"):
        return message.channel.send("feur")
    
    elif user_message_lower.endswith("no"):
        return message.channel.send("vembre")
    else:
        return asyncio.sleep(0)
    

# Jifo Haerin gif + goofy ahh gifs
async def jeffReaction(message):
        if (message.content == reactions_people["getthisN"]):
            await message.channel.send("nuh uh")
        if ("haerin" in message.content.lower()):
            await message.channel.send(reactions_people["kidLooking"])
        else:
            if random.random() < 0.05:
                await message.channel.send(reactions_people["Haerin"])
            elif random.random() < 0.10:
                await message.channel.send(random.choice(reactions_gifs))


# Matteo Chaewon gif
async def matteoReaction(message):
    if ("chaewon" in message.content.lower()):
        await message.channel.send(reactions_people["kidLooking"])
    else:
        if random.random() < 0.05:
            await message.channel.send(reactions_people["Chaewon"])

# Yara et Lea emoji and gif reaction
async def yaraReaction(message):
    if random.random() < 0.5:
            emojis = ['💀','👑', '🫦']
            weights = [90, 9.9, 0.1]
            chosen_emojis = random.choices(emojis, weights=weights, k=1)

            for emoji in chosen_emojis:
                await message.add_reaction(emoji)

    if random.random() < 0.05:
        await message.channel.send(reactions_people["magesty"])

# async def ramiReaction(message):
#     if random.random() < 0.35:
#         await message.channel.send("beh ich")

async def patateReaction(message):
    mesi_sticker = await message.guild.fetch_sticker(mesi_sticker_id)
    await message.channel.send(stickers=[mesi_sticker])

async def myReaction(message: Message):
    if message.content.lower().startswith("cha"):
        await message.add_reaction('🐈')
        message_sent = await message.channel.send("beb")
        if message_sent.author.id == m3alim_bob_id:
            await message_sent.add_reaction('🚪')