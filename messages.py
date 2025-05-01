import asyncio
import random
import discord
from discord import Message
from main import bot

def goofyAnswers(user_message_lower, message):
    if user_message_lower.endswith("di"):
        return message.channel.send("manche")
    
    if user_message_lower.endswith("ni"):
        return message.channel.send("gger")

    elif user_message_lower.endswith("toi"):
        return message.channel.send("lette")

    elif user_message_lower.endswith("1"):
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

reactions = [   "https://tenor.com/view/snowman-mewing-speech-bubble-discord-mod-gif-8892238637966534022",
                "https://tenor.com/view/speech-bubble-ishowspeed-scream-gif-25326093",
                "https://tenor.com/view/dentedhead-speech-bubble-hldmbrnet-gif-25216740",
                "https://tenor.com/view/dentedhead-speech-bubble-hldmbrnet-gif-25216740",
                "https://tenor.com/view/among-us-sus-discord-speech-bubble-among-us-discord-speech-bubble-ok-man-gif-7378430653913901797",
                "https://tenor.com/view/discord-mod-speech-bubble-gif-12034805688750074605"];

Haerin = "https://tenor.com/view/haerin-newjeans-newjeans-haerin-haerin-react-kang-haerin-gif-11086638272767305507"
Chaewon = "https://tenor.com/view/chaewon-le-sserafim-kpop-pretty-gif-4861479788048137214"
kidLooking = "https://tenor.com/view/awkward-look-away-gif-5084935"
magesty = "https://tenor.com/view/kneel-down-my-queen-your-majesty-gif-17663021"
getthisN = "https://cdn.discordapp.com/attachments/576672116561281034/1358634299129331722/getthisniggaout.gif"

# Jifo Haerin gif + goofy ahh gifs
async def jeffReaction(message):
        if (message.content == getthisN):
            await message.channel.send("nuh uh")
        if ("haerin" in message.content.lower()):
            await message.channel.send(kidLooking)
        else:
            if random.random() < 0.05:
                await message.channel.send(Haerin)
            elif random.random() < 0.25:
                await message.channel.send(random.choice(reactions))


# Matteo Chaewon gif
async def matteoReaction(message):
    if ("chaewon" in message.content.lower()):
        await message.channel.send(kidLooking)
    else:
        if random.random() < 0.05:
            await message.channel.send(Chaewon)

# Yara et Lea emoji and gif reaction
async def yaraAndLeaReaction(message):
    if random.random() < 0.5:
            emojis = ['💀', '🤡', '👑', '🫦']
            weights = [85, 10, 4.9, 0.1]
            chosen_emojis = random.choices(emojis, weights=weights, k=1)

            for emoji in chosen_emojis:
                await message.add_reaction(emoji)

    if random.random() < 0.05:
        await message.channel.send(magesty)

async def ramiReaction(message):
    if random.random() < 0.35:
        await message.channel.send("beh ich")

async def myReaction(message: Message):
    if message.content.lower().startswith("cha"):
        await message.add_reaction('🐈')
        message_sent = await message.channel.send("beb")
        if message_sent.author == bot.user:
            await message_sent.add_reaction('🚪')
        # await message.channel.send("beb")