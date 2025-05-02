# -------------------- System Imports / APIs -------------------- #
import os
import random
import asyncio
import requests
import signal
import sys
import discord
from discord import Intents, Client, Message
from discord.ext import commands
from dotenv import load_dotenv
from db import init_db, increment_word
# -------------------- My imports -------------------- #
from messages import goofyAnswers, jeffReaction, matteoReaction,  yaraAndLeaReaction, ramiReaction, myReaction
from keep_alive import keep_alive
from ids import *

# -------------------- Clean Shutdown -------------------- #

def handle_shutdown(sig, frame):
    print("🛑 Shutdown signal received.")
    bot.loop.create_task(bot.close())  # Let the bot exit gracefully

signal.signal(signal.SIGINT, handle_shutdown)
signal.signal(signal.SIGTERM, handle_shutdown)

# -------------------- Startup -------------------- #

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
init_db()

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="m3alim ", intents=intents)

@bot.event
async def on_ready():
    id = random.randint(1000, 9999)
    print(f"Bot started [ID: {id}] as {bot.user}")
    channel = bot.get_channel(log_channel_id)
    if channel:
        await channel.send(f"🟢 Bot instance `{id}` started as **{bot.user}**")
    

# -------------------- Events -------------------- #

@bot.event
async def on_message(message: Message):
    # Always allow commands to be processed
    await bot.process_commands(message)

    # Ignore self
    if message.author == bot.user:
        return
    

    # User-specific reactions
    if message.author.id == jeff_id:
        await jeffReaction(message)

    if message.author.id == matteo_id:
        await matteoReaction(message);

    if message.author.id in [yara_id, lea_id]:
        await yaraAndLeaReaction(message)

    if message.author.id == rami_id:
        await ramiReaction(message)

    if message.author.id == my_id:
        await myReaction(message)


    username = str(message.author)
    user_message: str = message.content
    channel = str(message.channel)

    print(f'[{channel}] {username} "{username}"')

    await goofyAnswers(user_message.lower(), message)


    nigga_words = ["nigga", "nigger", "niggers", "niggi", "nigg", "niga", "nga", "nick gurr", "nyaka" ]
    
    if user_message.lower().endswith("ni"):
        count = increment_word("nigga")
        await message.channel.send(f"📈 The word nigga w l'chabibet has now been said {count} times!")
        
    for word in nigga_words:
        if word in user_message.lower():
            count = increment_word("nigga")
            await message.channel.send(f"📈 The word nigga w l'chabibet has now been said {count} times!")

    tracked_words = ["haerin", "chaewon", "chabeb", "based", "cho"]
    for word in tracked_words:
        if word in user_message.lower():
            count = increment_word(word)
            await message.channel.send(f"📈 The word '{word}' has now been said {count} times!")
    


# -------------------- Commands -------------------- #

@bot.command(name="chabeb")
async def chabeb(ctx):
    await ctx.send('🐈🚪')
    await ctx.channel.last_message.add_reaction('🐈')
    await ctx.channel.last_message.add_reaction('🚪')
    

@bot.command(name="purge")
async def purge(ctx, number: int, *authors: discord.Member):
    """
    Purges the last `number` messages. If authors are specified, only deletes messages from them.
    """

    if number > 50:
        return

    def check(msg):
        return (not authors) or (msg.author in authors)

    deleted = await ctx.channel.purge(limit=number+1, check=check)
    await ctx.send(f"🧹 Deleted {len(deleted)-1} messages.", delete_after=3)

# -------------------- Future - Commands -------------------- #
"""

de NWordCounter();

def mockingLeBotDeJeffPuisDeleteSonLastMessage(message) MoCkInG jEFf BoT aNd Matteo

def russianRoulette

def sendNinoStickers()

"""
# -------------------- Main -------------------- #
def main():
    keep_alive()
    bot.run(TOKEN)

if __name__ == '__main__':
    main()

