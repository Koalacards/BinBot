import discord
from discord.ext import commands
import globalvars
import binutils
from datetime import datetime, timedelta
import bindbfunctions
import re

class BinListeners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_message(self, message):
        isbinned = await binutils.isBinned(message.guild, message.author)
        if isbinned == True and message.channel.name != globalvars.bin_channel:
            await message.delete()
  

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = await self.bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        guild = message.guild
        content = None
        if len(message.embeds) == 1:
            content = message.embeds[0].description
        elif len(message.embeds) == 0:
            content = message.content
        else:
            return

        
        if message.author == self.bot.user and 'is being voted into the bin' in content:
            if message.created_at < datetime.now() - timedelta(hours=bindbfunctions.getHourCooldown(guild.id)):
                await message.delete()
            for reaction in message.reactions:
                if reaction.count >= bindbfunctions.getThumbsUpVoteNum(guild.id) and str(reaction.emoji) == bindbfunctions.getThumbsUpEmoji(guild.id):
                    votedID = self._getIDFromMessage(content)
                    votedMember = guild.get_member(votedID)
                    if votedMember is None:
                        await message.channel.send(f'The user being voted in has either left the server or could not be found.')
                        await message.delete()
                    binned = await binutils.binAction(guild, votedMember)
                    if binned == True:
                        if len(message.embeds) == 0:
                            await message.edit(content=f'{votedMember.mention} has been binned!')
                        elif len(message.embeds) == 1:
                            embed = discord.Embed(
                                title='Vote Over',
                                description=f'{votedMember.mention} has been binned!',
                                colour=discord.Color.orange()
                            )
                            await message.edit(embed=embed)
                    else:
                        await message.edit(content=f'{votedMember.mention} was supposed to be binned, but they are already binned!', embed=None)
                    break
                if reaction.count >= bindbfunctions.getThumbsDownVoteNum(guild.id) and str(reaction.emoji) == bindbfunctions.getThumbsDownEmoji(guild.id):
                    await message.delete()
                    break
        if message.author == self.bot.user and 'is being voted out of the bin' in content:
            if message.created_at < datetime.now() - timedelta(hours=bindbfunctions.getHourCooldown(guild.id)):
                await message.delete()
            for reaction in message.reactions:
                if reaction.count >= bindbfunctions.getThumbsUpVoteNum(guild.id) and str(reaction.emoji) == bindbfunctions.getThumbsUpEmoji(guild.id):
                    votedID = self._getIDFromMessage(content)
                    votedMember = guild.get_member(votedID)
                    if votedMember is None:
                        await message.channel.send(f'The user being voted out has either left the server or could not be found.')
                        await message.delete()
                    unbinned = await binutils.unbinAction(guild, votedMember)
                    if unbinned == True:
                        if len(message.embeds) == 0:
                            await message.edit(content=f'{votedMember.mention} has been unbinned!')
                        elif len(message.embeds) == 1:
                            embed = discord.Embed(
                                title='Vote Over',
                                description=f'{votedMember.mention} has been unbinned!',
                                colour=discord.Color.orange()
                            )
                            await message.edit(embed=embed)
                    else:
                        await message.edit(content=f'{votedMember.mention} was supposed to be unbinned, but they are already unbinned!', embed=None)
                    break
                if reaction.count >= bindbfunctions.getThumbsDownVoteNum(guild.id) and str(reaction.emoji) == bindbfunctions.getThumbsDownEmoji(guild.id):
                    await message.delete()
                    break
    

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        guild = channel.guild
        binnedRole = None
        for role in guild.roles:
            if str(role) == 'binned':
                binnedRole = role
                break
        
        if binnedRole is not None and channel.name != 'bin':
            await channel.set_permissions(binnedRole, send_messages=False)
            
    
    def _getIDFromMessage(self, content:str):
        firstStep = content.split()[0]
        pattern = re.compile(r'[<@!>]')
        secondStep = pattern.sub('', firstStep)
        return int(secondStep)
        



def setup(bot):
    bot.add_cog(BinListeners(bot))