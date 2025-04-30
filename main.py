import os
from dotenv import load_dotenv
import discord
import asyncio
from discord import Intents, Client, Message
from discord.ext import commands
import random
from messages import goofyAnswers, jeffReaction, matteoReaction,  yaraAndLeaReaction, ramiReaction, myReaction
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="m3alim ", intents=intents)

my_id = 411654562819211275
jeff_id = 532728104322465815
yara_id = 1314032768543359069
lea_id = 765228868671242250
matteo_id = 437187631009234944
rami_id = 342008936960098305

@bot.event
async def on_ready():
    print(f'{bot.user} is now running')

@bot.event
async def on_message(message):
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
    

# Example command — you can add more like this
@bot.command(name="chabeb")
async def ping(ctx):
    await ctx.send('🐈🚪')
    await ctx.channel.last_message.add_reaction('🐈')
    await ctx.channel.last_message.add_reaction('🚪')


# bot = commands.Bot(command_prefix="!")
def main():
    keep_alive()
    bot.run(TOKEN)

if __name__ == '__main__':
    main()