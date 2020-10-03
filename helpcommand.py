import discord
from discord.ext import commands
import globalvars
import bindbfunctions

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx, cmdname = ''):
        prefix = bindbfunctions.getCommandPrefix(ctx.guild.id)
        lower = cmdname.lower()
        if lower == 'start':
            embed = discord.Embed(
                title=f'{prefix}start',
                description = "This command will set up the role, category and channels necessary to run Binbot!",
                colour= discord.Color.orange()
            )
            await ctx.send(embed=embed)
        elif lower == 'bin':
            embed = discord.Embed(
                title=f'{prefix}bin <user> [reason]',
                description = "**[NOTE: Only works in the channel #binvotes]** This command will bring up a vote to bin the given discord member (if applicable).\n An embed will be created, and your thumbs-up and thumbs-down emotes of choice will be reacted.\n When the number of votes (either for-binning or against-binning) is reached, the embed will change into a 'vote over' embed, and the votes will not count.\nThe embed will also delete itself if a reaction is given after a set-number of hours have passed.",
                colour= discord.Color.orange()
            )
            await ctx.send(embed=embed)
        elif lower == 'unbin':
            embed = discord.Embed(
                title=f'{prefix}unbin <user> [reason]',
                description = "**[NOTE: Only works in the channel #binvotes]** This command will bring up a vote to unbin the given discord member (if applicable).\n An embed will be created, and your thumbs-up and thumbs-down emotes of choice will be reacted.\n When the number of votes (either for-unbinning or against-unbinning) is reached, the embed will change into a 'vote over' embed, and the votes will not count.\nThe embed will also delete itself if a reaction is given after a set-number of hours have passed.",
                colour= discord.Color.orange()
            )
            await ctx.send(embed=embed)
        elif lower == 'commandprefix':
            embed = discord.Embed(
                title=f'{prefix}commandprefix <prefix>',
                description = "Changes the command prefix for all commands (Default: !). All commands after the entered command will use the prefix entered.",
                colour= discord.Color.orange()
            )
            await ctx.send(embed=embed)
        elif lower == 'validvotehours':
            embed = discord.Embed(
                title=f'{prefix}validvotehours <hours>',
                description = "When this number is changed (Default: 6), all votes will be invalid and deleted upon next reaction after the number of hours given.\n**WARNING**: This applies to older votes as well, even if the message says that it will be valid for your old number of hours.",
                colour= discord.Color.orange()
            )
            await ctx.send(embed=embed)
        elif lower == 'thumbsdownvotes':
            embed = discord.Embed(
                title=f'{prefix}thumbsdownvotes <votes>',
                description = "When this number is changed (Default: 5), the number of 'thumbs-down' reactions required to remove a bin/unbin vote for a user will be the given number.\n**WARNING**: This applies to older votes as well, even if the message says that it requires your old number of 'thumbs-down' reactions.",
                colour= discord.Color.orange()
            )
            await ctx.send(embed=embed)
        elif lower == 'thumbsupvotes':
            embed = discord.Embed(
                title=f'{prefix}thumbsupvotes <votes>',
                description = "When this number is changed (Default: 5), the number of 'thumbs-up' reactions required to bin/unbin a user will be the given number.\n**WARNING**: This applies to older votes as well, even if the message says that it requires your old number of 'thumbs-up' reactions.",
                colour= discord.Color.orange()
            )
            await ctx.send(embed=embed)
        elif lower == 'thumbsupemoji':
            embed = discord.Embed(
                title=f'{prefix}thumbsupemoji <emoji>',
                description = "When this emoji is changed (Default: 👍), the 'thumbs-up' emoji for bin/unbin votes will be the given emoji.\n**WARNING**: This applies to older votes as well, meaning that you will have to manually react with your new emoji after the change is made.",
                colour= discord.Color.orange()
            )
            await ctx.send(embed=embed)
        elif lower == 'thumbsdownemoji':
            embed = discord.Embed(
                title=f'{prefix}thumbsdownemoji <emoji>',
                description = "When this emoji is changed (Default: 👎), the 'thumbs-down' emoji for bin/unbin votes will be the given emoji.\n**WARNING**: This applies to older votes as well, meaning that you will have to manually react with your new emoji after the change is made.",
                colour= discord.Color.orange()
            )
            await ctx.send(embed=embed)
        elif lower == 'about':
            embed = discord.Embed(
                title=f'{prefix}about',
                description = "Explains what BinBot does and the concept of binning!",
                colour= discord.Color.orange()
            )
            await ctx.send(embed=embed)
        elif lower == '':
            embed = discord.Embed(
                title="Binbot Commands",
                description=f"Below you can find all of the commands needed to run binbot.\n For more help on a command, use `{prefix}help <command name>`.",
                colour = discord.Color.orange()
            )
            embed.add_field(name='Starting Commands- **Do these first**', value=f'{prefix}start\n{prefix}about', inline=False)
            embed.add_field(name='Bin Commands- **Only work in #bin-votes**', value = f'{prefix}bin <user> [reason]\n{prefix}unbin <user> [reason]', inline=False)
            embed.add_field(name='Settings Commands- **Only useable with Admin or Server Manager permissions**', value= f'{prefix}thumbsupvotes <votes>\n{prefix}thumbsupvotes <votes>\n{prefix}validvotehours <hours>\n{prefix}commandprefix <prefix>\n{prefix}thumbsupemoji <emoji>\n{prefix}thumbsdownemoji <emoji>', inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Sorry, the name of the command you are looking for was not found. Type `{prefix}help` for more help.',
                colour = discord.Color.red()
            )
            await ctx.send(embed=embed)
    
    @commands.command()
    async def about(self, ctx):
        prefix = bindbfunctions.getCommandPrefix(ctx.guild.id)
        embed = discord.Embed(
            title="About BinBot!",
            description=f'Have you ever wanted a punishment system in your server to keep all your pesky members in check? Introducing BinBot, a bot that automates the fun punishment system called binning!\n'\
                '**What is Binning?**\nBinning a user involves giving them a role that only allows them to type in one channel, #bin, while seeing all of the other channels in the server.'\
                'At the same time, the users that are not \'binned\' are not allowed to talk in #bin, making #bin a discord prison of sorts, where only binned members can talk to each other.\n'\
                f'**What does BinBot do?**\nBinBot automates the process of binning, first by creating the binned role and two channels, #bin and #bin-votes upon `{prefix}start`.'\
                f'After that, users can use `{prefix}bin` and {prefix}`unbin` to create votes to bin or unbin a user. If there are enough votes in favor or against the decision, the user will be binned/unbinned or the vote will be removed.'\
                f'The votes can also be customized to your liking! There are a number of options that server leaders can change, all of which can be found in `{prefix}help`.\n'\
                'Happy binning, everyone!',
            colour=discord.Color.orange()
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(HelpCommand(bot))