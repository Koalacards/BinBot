import discord
from discord.ext import commands


class StartCommand(commands.Cog, name="Start Command"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='Do this command first!', help="This command will set up the role, category and channels necessary to run Binbot!")
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
            await ctx.send("The `binned` role has been created, which will be given to users that you vote into the bin!")
        
        #next, check to see if there is a bin category. if there is, the bin channels will be put in there.
        binCategory = None
        for category in guild.categories:
            if category.name == 'Bin':
                binCategory = category
        
        if binCategory is None:
            binCategory = await guild.create_category('Bin')
            await ctx.send("The `Bin` category has been created! This category will house the two channels, `#bin` and `#bin-votes`, that are used by Binbot!")
        

        #then, adds the #bin and #bin-votes channels if they are already not in the category
        binChannel = None
        binVotesChannel = None
        for channel in binCategory.channels:
            if channel.name == 'bin':
                binChannel = channel
            if channel.name == 'bin-votes':
                binVotesChannel = channel
        
        if binVotesChannel is None:
            binVotesChannel = await guild.create_text_channel('bin-votes', category=binCategory, topic='Use this channel to start all of your binning/unbinning votes!')
            await ctx.send("The `#bin-votes` channel has been created! Use this channel to start all of your binning/unbinning votes!")
        
        if binChannel is None:
            binChannel = await guild.create_text_channel('bin', category=binCategory, topic='This is the channel where binned members can speak in, but nobody else can!')
            await ctx.send("The `#bin` channel has been created! This is the only channel that binned people will be able to talk in, and other members of the server cannot talk in this channel.")

        for channel in guild.channels:
            if channel.name != 'bin':
                await channel.set_permissions(binnedRole, send_messages=False)
        
        await binChannel.set_permissions(binnedRole, send_messages=True)
        await binChannel.set_permissions(guild.default_role, send_messages=False)
        await ctx.send("Channel permissions have been set up such that users with the `binned` role cannot speak in any other channel besides `#bin`.\nRegular users also cannot talk in `#bin`.")
        await ctx.send("Binbot is now set up, enter the help command for more help and have fun!")

def setup(bot):
    bot.add_cog(StartCommand(bot))