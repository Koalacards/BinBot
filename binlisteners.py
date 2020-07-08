import discord
from discord.ext import commands
import globalvars
import binutils
from datetime import datetime, timedelta

class BinListeners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_message(self, message):
        isbinned = await binutils.isBinned(message.guild, message.author)
        if isbinned == True and message.channel.name != globalvars.bin_channel:
            await message.delete()
  

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        message = reaction.message
        guild = message.guild

        
        if message.author == self.bot.user and 'is being voted into the bin' in message.content:
            if message.created_at < datetime.now() - timedelta(hours=12):
                await message.delete()
            if reaction.count >= globalvars.numVotes and str(reaction.emoji) == globalvars.thumbsUp:
                toBeBinned = message.mentions[0]
                binned = await binutils.binAction(guild, toBeBinned)
                if binned == True:
                    await message.channel.send(f'{toBeBinned.mention} has been binned!')
                    if len(message.mentions) == 1:
                        await message.channel.send('https://giphy.com/gifs/LJemLPJs6dBhm')
                    await message.delete()
                else:
                    await message.channel.send(f'{toBeBinned.mention} was supposed to be binned, but they are already binned!')
            if reaction.count >= globalvars.numVotes and str(reaction.emoji) == globalvars.thumbsDown:
                await message.delete()
        if message.author == self.bot.user and 'is being voted out of the bin' in message.content:
            if message.created_at < datetime.now() - timedelta(hours=12):
                await message.delete()
            if reaction.count >= globalvars.numVotes and str(reaction.emoji) == globalvars.thumbsUp:
                toBeUnBinned = message.mentions[0]
                unbinned = await binutils.unbinAction(guild, toBeUnBinned)
                if unbinned == True:
                    await message.channel.send(f'{toBeUnBinned.mention} has been unbinned!')
                    await message.delete()
                else:
                    await message.channel.send(f'{toBeUnBinned.mention} was supposed to be unbinned, but they are already unbinned!')
            if reaction.count >= globalvars.numVotes and str(reaction.emoji) == globalvars.thumbsDown:
                await message.delete()

def setup(bot):
    bot.add_cog(BinListeners(bot))