import discord
from discord.ext import commands


class StartCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
        
        await binChannel.set_permissions(binnedRole, send_messages=True)

def setup(bot):
    bot.add_cog(StartCommand(bot))