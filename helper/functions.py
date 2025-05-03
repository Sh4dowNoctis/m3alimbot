import re
from discord import Message
from db.db import  increment_word, get_word_count
from helper.messages import *
from helper.ids import *
    
async def emoji_milestone(message: Message, count, word):
    if (count % 10 == 0):
            level = min(count // 10, len(milestone_levels)) - 1
            emoji, comment = milestone_levels[level]
            
            message_sent = await message.channel.send(f"{emoji}The Chabeb have achieved the {count // 10}th milestone for the word **{word}**!{emoji} {comment}")
            await message_sent.add_reaction(emoji)

async def search_increment_word(message: Message, wordInList: str, word: str):
    pattern = r"\b" + re.escape(wordInList) + r"\b"
    if re.search(pattern, message.content, re.IGNORECASE) and "m3alim" not in message.content:
        count = increment_word(word)
        await message.channel.send(f"📈 The word **{word}** has now been said {count} times!", delete_after=3)
        emoji_milestone(message, count, word)
        
async def word_counter(message: Message):
    if message.content.lower().endswith("ni"):
        word = "nigga"
        count = increment_word(word)
        await message.channel.send(f"📈 The word **{word}** has now been said {count} times!", delete_after=3)
        emoji_milestone(message, count, word)
    
    nigga_words = [ "nigger", "niggers", "niggi", "nigg", "niga", "nga", "nick gurr", "nyaka" ]
    for word in nigga_words:
        await search_increment_word(message, word, "nigga")
        

    tracked_words = ["haerin", "chaewon", "chabeb", "based", "cho", "nigga", "fobar"]
    for word in tracked_words:
        await search_increment_word(message, word, word)
    

        
async def user_specific_reactions(message: Message):
    if message.author.id == jeff_id:
        await jeffReaction(message)

    if message.author.id == matteo_id:
        await matteoReaction(message);

    if message.author.id == yara_id:
        await yaraReaction(message)

    # if message.author.id == rami_id:
    #     await ramiReaction(message)

    if message.author.id == my_id:
        await myReaction(message)


def log_user(message: Message):
    username = str(message.author)
    channel = str(message.channel)

    print(f'[{channel}] {username} "{username}"')
    
async def nino(message: Message, bot):
    if message.content == "nino":
        guild: discord.guild = bot.get_guild(nino_server_id)

        if not guild:
            await message.channel.send("❌ Bot is not in that guild or guild ID is wrong.")
            return

        nino_sticker = await guild.fetch_sticker(nino_sticker_id)
        await message.channel.send(stickers=[nino_sticker])