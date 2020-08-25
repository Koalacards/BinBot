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

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="bin game | !help"))


@client.command(hidden=True)
async def reloadCog(ctx, cog):
    if ctx.message.author.display_name == 'Koalacards':
        client.reload_extension(cog)
    await ctx.message.delete()

@client.command(hidden=True)
async def quit(ctx):
    if ctx.message.author.display_name == 'Koalacards':
        await client.close()
    await ctx.message.delete()

client.run(RUN_ID)