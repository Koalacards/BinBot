import discord
from discord.ext import commands
from confidential import *
import globalvars

client = commands.Bot(command_prefix=globalvars.command_prefix)

client.load_extension('bincommands')
client.load_extension('binlisteners')

@client.command()
async def reloadCog(ctx, cog):
    if ctx.message.author.display_name == 'Koalacards':
        client.reload_extension(cog)

@client.command()
async def quit(ctx):
    if ctx.message.author.display_name == 'Koalacards':
        await client.close()

client.run(RUN_ID)