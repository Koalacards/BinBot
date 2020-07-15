import discord
from discord.ext import commands
import globalvars
import binutils

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
                description=f'{member.mention} is being voted into the bin by {ctx.message.author.display_name}{reasonMessage}.\nReact with a {globalvars.thumbsUp} to vote for binning. {globalvars.numVotes} {globalvars.thumbsUp}\'s are needed.',
                colour=discord.Color.red()
            )
            embed.set_footer(text=f'This vote will be invalidated in {globalvars.invalidated_hours} hours!')
            message = await ctx.send(embed=embed)
            await message.add_reaction(globalvars.thumbsUp)
    
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
                description=f'{member.mention} is being voted out of the bin by {ctx.message.author.display_name}{reasonMessage}.\nReact with a {globalvars.thumbsUp} to vote for unbinning. {globalvars.numVotes} {globalvars.thumbsUp}\'s are needed.',
                colour=discord.Color.green()
            )
            embed.set_footer(text=f'This vote will be invalidated in {globalvars.invalidated_hours} hours!')
            message = await ctx.send(embed=embed)
            await message.add_reaction(globalvars.thumbsUp)

    @commands.command()
    async def votenum(self, ctx, number:int):
        author = ctx.message.author
        if author.display_name == 'Koalacards' or author.guild_permissions.administrator == True:
            if number > 0:
                globalvars.numVotes = number
                await ctx.send(':thumbsup:')
            else:
                await ctx.send('The vote number must be a positive integer!')
    
    @commands.command()
    async def invalidhours(self, ctx, hours:int):
        author = ctx.message.author
        if author.display_name == 'Koalacards' or author.guild_permissions.administrator == True:
            if hours > 0:
                globalvars.invalidated_hours = hours
                await ctx.send(':thumbsup:')
            else:
                await ctx.send('The number of hours must be a positive integer!')

    @commands.command()
    async def start(self, ctx):
        guild = ctx.guild

        #first create a role if there is not a binned role
        binnedRole = None
        for role in guild.roles:
            if str(role) == 'binned':
                binnedRole = role
                break
        
        if binnedRole is None:
            binnedRole = await guild.create_role(name='binned')
        
        #next, check to see if there is a bin category. if there is, the bin channels will be put in there.
        binCategory = None
        for category in guild.categories:
            if category.name == 'Bin':
                binCategory = category
        
        if binCategory is None:
            binCategory = await guild.create_category('Bin')
        

        #then, adds the #bin and #bin-votes channels if they are already not in the category
        binChannel = None
        binVotesChannel = None
        for channel in binCategory.channels:
            if channel.name == 'bin':
                binChannel = channel
            if channel.name == 'bin-votes':
                binVotesChannel = channel
        
        if binVotesChannel is None:
            binVotesChannel = await guild.create_text_channel('bin-votes', category=binCategory)
        
        if binChannel is None:
            binChannel = await guild.create_text_channel('bin', category=binCategory)

        for channel in guild.channels:
            if channel.name != 'bin':
                await channel.set_permissions(binnedRole, send_messages=False)


def setup(bot):
    bot.add_cog(BinCommands(bot))