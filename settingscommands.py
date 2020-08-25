import discord
from discord.ext import commands
import bindbfunctions

class SettingsCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def thumbsup(self, ctx, number:int):
        author = ctx.message.author
        if author.guild_permissions.administrator == True or author.guild_permissions.manage_guild == True:
            if number > 0:
                bindbfunctions.setThumbsUpVoteNum(ctx.guild.id, number)
                await ctx.send(':thumbsup:')
            else:
                await ctx.send('The vote number must be a positive integer!')
        else:
            await ctx.send('In order to change a setting, you must have the `Administrator` or `Manage Server` permission.')

    
    @commands.command()
    async def thumbsdown(self, ctx, number:int):
        author = ctx.message.author
        if author.guild_permissions.administrator == True or author.guild_permissions.manage_guild == True:
            if number > 0:
                bindbfunctions.setThumbsDownVoteNum(ctx.guild.id, number)
                await ctx.send(':thumbsup:')
            else:
                await ctx.send('The vote number must be a positive integer!')
        else:
            await ctx.send('In order to change a setting, you must have the `Administrator` or `Manage Server` permission.')
    
    @commands.command()
    async def hourcooldown(self, ctx, hours:int):
        author = ctx.message.author
        if author.guild_permissions.administrator == True or author.guild_permissions.manage_guild == True:
            if hours > 0:
                bindbfunctions.setHourCooldown(ctx.guild.id, hours)
                await ctx.send(':thumbsup:')
            else:
                await ctx.send('The number of hours must be a positive integer!')
        else:
            await ctx.send('In order to change a setting, you must have the `Administrator` or `Manage Server` permission.')
    
    @commands.command()
    async def commandprefix(self, ctx, commandPrefix:str):
        author = ctx.message.author
        if author.guild_permissions.administrator == True or author.guild_permissions.manage_guild == True:
            bindbfunctions.setCommandPrefix(ctx.guild.id, commandPrefix)
            await ctx.send(':thumbsup:')
        else:
            await ctx.send('In order to change a setting, you must have the `Administrator` or `Manage Server` permission.')

    @commands.command()
    async def thumbsupemoji(self, ctx, thumbsUpEmoji:str):
        author = ctx.message.author
        if author.guild_permissions.administrator == True or author.guild_permissions.manage_guild == True:
            try:
                await ctx.message.add_reaction(thumbsUpEmoji)
                bindbfunctions.setThumbsUpEmoji(ctx.guild.id, str(thumbsUpEmoji))
            except:
                embed = discord.Embed(
                    description='This emoji cannot be used for this guild because the bot cannot use it. Please try another emoji or check the server\'s emoji settings.',
                    colour= discord.Color.red()
                )
                await ctx.send(embed=embed)
        else:
            await ctx.send('In order to change a setting, you must have the `Administrator` or `Manage Server` permission.')

    @commands.command()
    async def thumbsdownemoji(self, ctx, thumbsDownEmoji:str):
        author = ctx.message.author
        if author.guild_permissions.administrator == True or author.guild_permissions.manage_guild == True:
            try:
                await ctx.message.add_reaction(thumbsDownEmoji)
                bindbfunctions.setThumbsDownEmoji(ctx.guild.id, str(thumbsDownEmoji))
            except:
                embed = discord.Embed(
                    description='This emoji cannot be used for this guild because the bot cannot use it. Please try another emoji or check the server\'s emoji settings.',
                    colour= discord.Color.red()
                )
                await ctx.send(embed=embed)
        else:
            await ctx.send('In order to change a setting, you must have the `Administrator` or `Manage Server` permission.')
    

def setup(bot):
    bot.add_cog(SettingsCommands(bot))