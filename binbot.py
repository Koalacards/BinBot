import discord
from discord.ext import commands
from confidential import *
import globalvars
import bindbfunctions

def _guild_prefix(bot, message):
    guild = message.guild
    if guild is None:
        return globalvars.command_prefix
    else:
        return bindbfunctions.getCommandPrefix(guild.id)

client = commands.Bot(command_prefix=_guild_prefix)

client.load_extension('startcommand')
client.load_extension('bincommands')
client.load_extension('settingscommands')
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