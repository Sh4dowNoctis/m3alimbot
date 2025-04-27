import asyncio
import random

def goofyAnswers(user_message_lower, message):
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

reactions = ["https://images-ext-1.discordapp.net/external/Cy3ugvgCm5_vWe8NhmUKjnb6MoG8uOw2hWChqdknaJ0/https/media.tenor.com/pwQ4AsLMau0AAAPo/discord-mod-speech-bubble.mp4",
             "https://images-ext-1.discordapp.net/external/I_-meTJXqDyG3n7lZrK8OgSBaKt6pNYWfOgzkWKRmSY/https/media.tenor.com/e2eT7Zn_pYYAAAPo/snowman-mewing.mp4",
             "https://images-ext-1.discordapp.net/external/1cWJUtUPTzxgZN8gG6p0QjA7mPswSqmZQhrQrAEfNHA/https/media.tenor.com/b7mnVHUXvsAAAAPo/speech-bubble-ishowspeed.mp4",
             "https://images-ext-1.discordapp.net/external/VrkN3D77_xdrKFiDZnewFbGSrRkZLRe3RmwvvENM2qk/https/media.tenor.com/pPd2u3Q-5_UAAAPo/dentedhead-speech-bubble.mp4",
             "https://media.discordapp.net/attachments/807641026188542014/1349129359771959318/yea_man.gif?ex=67d1fa20&is=67d0a8a0&hm=898c83a3f0c6341044edaf26c81ab4ac01a26ffd1d07066e35b0704ca1712abb&=&width=540&height=525",
             "https://images-ext-1.discordapp.net/external/BSxLOsRodxnN0dJDgdEe7Jgu1g_1DqdgWUZ12-dZ4Jo/https/media.tenor.com/ZmVzlk5kKuUAAAPo/among-us-sus.mp4"];

def jeffReactions(message):
    return message.channel.send(content=random.choice(reactions))