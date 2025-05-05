# -------------------- System Imports / APIs -------------------- #
import os
import random
import asyncio
import requests
import signal
import sys
import re
import discord
from discord import Intents, Client, Message
from discord.ext import commands
from dotenv import load_dotenv
from db.db import init_db, increment_word, get_word_count
# -------------------- My imports -------------------- #
import discord.ext
from helper.functions import *
from helper.messages import *
from helper.ids import *
from keep_alive import keep_alive
from components.buttons import *

# -------------------- Global Variable -------------------- #

russian_roulette_limit = 5
INSTANCE_ID = random.randint(1000, 9999)
FFMPEG_PATH = "./bin/ffmpeg.exe"

# -------------------- Handle Shutdown -------------------- #

# Shutdown logging
async def graceful_shutdown():
    embed = discord.Embed(
        title=f"{ENV_LABEL} Bot Shutdown",
        description=f"🔴 Instance `{INSTANCE_ID}` is shutting down.",
        color=discord.Color.red()
    )

    for channel_id in [log_channel_nino_id, log_channel_chabeb_id]:
        channel = bot.get_channel(channel_id)
        if channel:
            await channel.send(embed=embed)

    await bot.close()

def handle_shutdown(sig, frame):
    bot.loop.create_task(graceful_shutdown())

signal.signal(signal.SIGINT, handle_shutdown)
signal.signal(signal.SIGTERM, handle_shutdown)

# -------------------- Startup -------------------- #

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
init_db()

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="m3alim ", intents=intents)


ENV_LABEL = "DEV" if os.getenv("LOCAL_DEV") == "1" else "PROD"

@bot.event
async def on_ready():
    print(f"Bot [{ENV_LABEL}] started [ID: {INSTANCE_ID}] as {bot.user}")

    embed = discord.Embed(
        title=f"{ENV_LABEL} Bot Started",
        description=f"🟢 Instance `{INSTANCE_ID}` launched as **{bot.user}**",
        color=discord.Color.green()
    )

    for channel_id in [log_channel_nino_id, log_channel_chabeb_id]:
        channel = bot.get_channel(channel_id)
        if channel:
            await channel.send(embed=embed)
    

# -------------------- Events -------------------- #

@bot.event
async def on_message(message: Message):
    
    # --------------- Setup --------------- #
    # Ignore self
    if message.author == bot.user or message.guild.id == squad_server_id:
        return
    # Always allow commands to be processed
    await bot.process_commands(message)
    # Log User
    log_user(message)
    

    # --------------- Features --------------- #
    await user_specific_reactions(message) # Reacts depending on what the people type

    await nino(message, bot) # literally just sends a nino sticker

    await goofyAnswers(message.content.lower(), message) # Cho Colat
    
    await word_counter(message) # tracked_words = ["haerin", "chaewon", "chabeb", "based", "cho", "nigga"]


@bot.event
async def on_voice_state_update(member: discord.member, before: discord.VoiceState, after: discord.VoiceState):
    if after.channel == None:
        return
    if after.channel.id == russian_roullette_channel_id and len(after.channel.members) > russian_roulette_limit:
        list_of_members = after.channel.members
        await random.choice(list_of_members).move_to(bot.get_channel(fobar_nation_id))


# -------------------- Commands -------------------- #

@bot.command(name="chabeb")
async def chabeb(ctx):
    """
    Sends 🐈🚪
    """
    await ctx.send('🐈🚪')
    await ctx.channel.last_message.add_reaction('🐈')
    await ctx.channel.last_message.add_reaction('🚪')
    

@bot.command(name="purge")
async def purge(ctx: commands.context.Context, number: int, *authors: discord.Member):
    """
    Purges the last `number` messages. If authors are specified, only deletes messages from them.
    """
    if number > 50:
        await ctx.send("❌ Limit is 50 messages.", delete_after=3)
        return

    def check(msg):
        return (not authors) or (msg.author in authors)
    
    messages = [message async for message in ctx.channel.history(limit=number+1)]
    filtered = list(filter(check, messages))

    if not filtered:
        await ctx.send("No messages matched.", delete_after=3)
        return

    target_msg = filtered[-1]
    view = ConfirmPurgeView(ctx, filtered)
    await ctx.send(
        f"Delete messages until:\n**{target_msg.author.display_name}:** {target_msg.content}",
        view=view,
        delete_after=10
    )
    
@bot.command(name="counter")
async def counter(ctx: commands.context.Context, word):
    """
    Gives the counter of the specified word ["haerin", "chaewon", "chabeb", "based", "cho", "nigga", "fobar"]
    """
    if not word:
        return
    
    tracked_words = ["haerin", "chaewon", "chabeb", "based", "cho", "nigga", "fobar"]
    if word in tracked_words:
        count = get_word_count(word)
        
    await ctx.channel.send(f"📈 The word {word} has now been said {count} times!", delete_after=5)
    
    
@bot.command(name="roulette")
async def roulette(ctx, value: int):
    """
    Set roulette variable to the value
    """
    global russian_roulette_limit
    russian_roulette_limit = value
    await ctx.send(f"✅ Variable set to {russian_roulette_limit}", delete_after=3)

@bot.command(name="check")
async def check(ctx):
    """
    Shows current roulette variable
    """ 
    await ctx.send(f"📦 Current value: {russian_roulette_limit}")

# -------------------- Future - Commands -------------------- #
"""

def mockingLeBotDeJeffPuisDeleteSonLastMessage(message) MoCkInG jEFf BoT aNd Matteo

"""
# -------------------- Main -------------------- #
def main():
    keep_alive()
    bot.run(TOKEN)

if __name__ == '__main__':
    main()

