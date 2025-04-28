import asyncio
import random
import discord

async def goofyAnswers(user_message_lower, message):
    if user_message_lower.endswith("di"):
        return message.channel.send("manche")

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

async def jeffReactions(message):
    media = random.choice(reactions)
    
    if media.endswith(('.png', '.jpg', '.jpeg', '.gif')):
        embed = discord.Embed()
        embed.set_image(url=media)
        await message.channel.send(embed=embed)
    else:
        await message.channel.send(content=media)

