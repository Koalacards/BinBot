import discord
from discord.ext import commands
import globalvars
import binutils
import bindbfunctions

class BinCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bin(self, ctx, member:discord.Member, *, reason:str = ''):
        if ctx.channel.name != globalvars.bin_votes_channel:
            return
        guild = ctx.message.guild
        if member == self.bot.user:
            await ctx.send(f'Silly {ctx.message.author.display_name}, you can\'t bin me!')
            return
        reasonMessage = f' for reason: `{reason}`' if reason != '' else ''
        if await binutils.isBinned(guild, member) == True:
            await ctx.send(f'{member.mention} is already in the bin!')
        else:
            embed = discord.Embed(
                title="Bin Vote",
                description=f'{member.mention} is being voted into the bin by {ctx.message.author.display_name}{reasonMessage}.\nReact with a {bindbfunctions.getThumbsUpEmoji(guild.id)} to vote for binning. {bindbfunctions.getThumbsUpVoteNum(guild.id)} {bindbfunctions.getThumbsUpEmoji(guild.id)}\'s are needed.\nIf {bindbfunctions.getThumbsDownVoteNum(guild.id)} {bindbfunctions.getThumbsDownEmoji(guild.id)}\'s are provided, the message will delete itself.',
                colour=discord.Color.red()
            )
            embed.set_footer(text=f'This vote will be invalidated in {bindbfunctions.getHourCooldown(guild.id)} hours!')
            message = await ctx.send(embed=embed)
            try:
                await message.add_reaction(bindbfunctions.getThumbsUpEmoji(guild.id))
            except:
                await message.delete()
                embed = discord.Embed(
                    description='The thumbs-up emoji cannot be used for this guild because the bot cannot use it. Please try another emoji or check the server\'s emoji settings.',
                    colour= discord.Color.red()
                )
                await ctx.send(embed=embed)

            try:
                await message.add_reaction(bindbfunctions.getThumbsDownEmoji(guild.id))
            except:
                await message.delete()
                embed = discord.Embed(
                    description='The thumbs-down emoji cannot be used for this guild because the bot cannot use it. Please try another emoji or check the server\'s emoji settings.',
                    colour= discord.Color.red()
                )
                await ctx.send(embed=embed) 
    
    @commands.command()
    async def unbin(self, ctx, member:discord.Member, *, reason:str = ''):
        if ctx.channel.name != globalvars.bin_votes_channel:
            return
        guild = ctx.message.guild
        reasonMessage = f' for reason: `{reason}`' if reason != '' else ''
        if await binutils.isBinned(guild, member) == False:
            await ctx.send(f'{member.mention} is already out of the bin!')
        else:
            embed = discord.Embed(
                title="Unbin Vote",
                description=f'{member.mention} is being voted out of the bin by {ctx.message.author.display_name}{reasonMessage}.\nReact with a {bindbfunctions.getThumbsUpEmoji(guild.id)} to vote for unbinning. {bindbfunctions.getThumbsUpVoteNum(guild.id)} {bindbfunctions.getThumbsUpEmoji(guild.id)}\'s are needed.\nIf {bindbfunctions.getThumbsDownVoteNum(guild.id)} {bindbfunctions.getThumbsDownEmoji(guild.id)}\'s are provided, the message will delete itself.',
                colour=discord.Color.green()
            )
            embed.set_footer(text=f'This vote will be invalidated in {bindbfunctions.getHourCooldown(guild.id)} hours!')
            message = await ctx.send(embed=embed)
            await message.add_reaction(bindbfunctions.getThumbsUpEmoji(guild.id))
            await message.add_reaction(bindbfunctions.getThumbsDownEmoji(guild.id))

def setup(bot):
    bot.add_cog(BinCommands(bot))