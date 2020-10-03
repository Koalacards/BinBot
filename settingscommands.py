import discord
from discord.ext import commands
import bindbfunctions

class SettingsCommands(commands.Cog, name="Bin Voting Settings Commands (ADMIN/SERVER MANAGER PERMISSIONS ONLY)"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(brief="Number of 'thumbs-up' reactions required to bin/unbin", description="When this number is changed (Default: 5), the number of 'thumbs-up' reactions required to bin/unbin a user will be the given number.\nWARNING: This applies to older votes as well, even if the message says that it requires your old number of 'thumbs-up' reactions.")
    async def thumbsupvotes(self, ctx, number:int):
        author = ctx.message.author
        if author.guild_permissions.administrator == True or author.guild_permissions.manage_guild == True:
            if number > 0:
                bindbfunctions.setThumbsUpVoteNum(ctx.guild.id, number)
                await ctx.send(':thumbsup:')
            else:
                await ctx.send('The vote number must be a positive integer!')
        else:
            await ctx.send('In order to change a setting, you must have the `Administrator` or `Manage Server` permission.')

    
    @commands.command(brief="Number of 'thumbs-down' reactions required to stop a vote ", description="When this number is changed (Default: 5), the number of 'thumbs-down' reactions required to remove a bin/unbin vote for a user will be the given number.\nWARNING: This applies to older votes as well, even if the message says that it requires your old number of 'thumbs-down' reactions.")
    async def thumbsdownvotes(self, ctx, number:int):
        author = ctx.message.author
        if author.guild_permissions.administrator == True or author.guild_permissions.manage_guild == True:
            if number > 0:
                bindbfunctions.setThumbsDownVoteNum(ctx.guild.id, number)
                await ctx.send(':thumbsup:')
            else:
                await ctx.send('The vote number must be a positive integer!')
        else:
            await ctx.send('In order to change a setting, you must have the `Administrator` or `Manage Server` permission.')
    
    @commands.command(brief="Changes the number of hours a vote is valid for", description="When this number is changed (Default: 6), all votes will be invalid and deleted upon next reaction after the number of hours given.\nThis applies to older votes as well, even if the message says that it will be valid for your old number of hours.")
    async def validvotehours(self, ctx, hours:int):
        author = ctx.message.author
        if author.guild_permissions.administrator == True or author.guild_permissions.manage_guild == True:
            if hours > 0:
                bindbfunctions.setHourCooldown(ctx.guild.id, hours)
                await ctx.send(':thumbsup:')
            else:
                await ctx.send('The number of hours must be a positive integer!')
        else:
            await ctx.send('In order to change a setting, you must have the `Administrator` or `Manage Server` permission.')
    
    @commands.command(brief="Changes the command prefix for all commands (default: !)", description="Changes the command prefix for all commands. All commands after the entered command will use the prefix entered.")
    async def commandprefix(self, ctx, commandPrefix:str):
        author = ctx.message.author
        if author.guild_permissions.administrator == True or author.guild_permissions.manage_guild == True:
            bindbfunctions.setCommandPrefix(ctx.guild.id, commandPrefix)
            await ctx.send(':thumbsup:')
        else:
            await ctx.send('In order to change a setting, you must have the `Administrator` or `Manage Server` permission.')

    @commands.command(brief="Emoji for 'thumbs-up' reactions", description="When this emoji is changed (Default: 👍), the 'thumbs-up' emoji for bin/unbin votes will be the given emoji.\nWARNING: This applies to older votes as well, meaning that you will have to manually react with your new emoji after the change is made.")
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

    @commands.command(brief="Emoji for 'thumbs-down' reactions", description="When this emoji is changed (Default: 👎), the 'thumbs-down' emoji for bin/unbin votes will be the given emoji.\nWARNING: This applies to older votes as well, meaning that you will have to manually react with your new emoji after the change is made.")
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