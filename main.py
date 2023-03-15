import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
# Run the bot
bot.run("MTA4NTUzNzQ2ODM3MzI4Mjg5Nw.Gak3UT.WjQYajhWoM0X83--Q2-ggWEUMMcQFKeL3bTXQM")


