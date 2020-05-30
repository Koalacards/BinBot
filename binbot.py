import discord
from discord.ext import commands
from confidential import *

client = commands.Bot(command_prefix='!')

reactionStr = '👍'

binMessages = []

numVotes = 3

bin_channel = 'bin'

bin_votes_channel = 'bin-votes'


@client.event
async def on_ready():
    print('bin bot pog')

@client.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    guild = message.guild
    if message.id in binMessages:
        if reaction.count >= numVotes:
            print('time to assign the binned role')
            toBeBinned = message.mentions[0]
            binned = await binUnbin(guild, toBeBinned)
            print('got past role assign')
            binMessages.remove(message.id)
            if binned == True:
                await message.channel.send(f'{toBeBinned.mention} has been unbinned!')
            else:
                await message.channel.send(f'{toBeBinned.mention} has been binned!')
                if len(message.mentions) == 1:
                    await message.channel.send('https://giphy.com/gifs/LJemLPJs6dBhm')

@client.command()
async def bin(ctx, member:discord.Member, *, reason:str = ''):
    if ctx.channel.name != bin_votes_channel:
        return
    guild = ctx.message.guild
    if member == client.user:
        await ctx.send(f'Silly {ctx.message.author.display_name}, you can\'t bin me!')
        return
    reasonMessage = f' for reason: `{reason}`' if reason != '' else ''
    if await isBinned(guild, member) == True:
        await ctx.send(f'{member.mention} is already in the bin!')
    else:
        message = await ctx.send(f'{member.mention} is being voted into the bin by {ctx.message.author.mention}{reasonMessage}.\nReact with a {reactionStr} to vote for binning. {numVotes} {reactionStr}\'s are needed.')
        binMessages.append(message.id)

@client.command()
async def unbin(ctx, member:discord.Member, *, reason:str = ''):
    if ctx.channel.name != bin_votes_channel:
        return
    guild = ctx.message.guild
    reasonMessage = f' for reason: `{reason}`' if reason != '' else ''
    if await isBinned(guild, member) == False:
        await ctx.send(f'{member.mention} is already out of the bin!')
    else:
        message = await ctx.send(f'{member.mention} is being voted out of the bin by {ctx.message.author.mention}{reasonMessage}. React with a {reactionStr} to vote for unbinning. {numVotes} {reactionStr}\'s are needed.')
        binMessages.append(message.id)

'''
@client.command()
async def votenum(ctx, number:int):
    if ctx.channel.name != bin_votes_channel:
        return
    if number > 0:
        global numVotes
        numVotes = number
        await ctx.send(':thumbsup:')
    else:
        await ctx.send('The vote number must be a positive integer!')
'''
        
async def binUnbin(guild, member:discord.Member):
    binnedRole = await getBinnedRole(guild)
    hasBinnedRole = False
    for role in member.roles:
        if role == binnedRole:
            hasBinnedRole = True
            break
    if hasBinnedRole == True:
        await member.remove_roles(binnedRole)
        return True
    else:
        await member.add_roles(binnedRole)
        return False


async def getBinnedRole(guild):
    role = None
    for role in guild.roles:
        if str(role) == 'binned':
            return role
    role = await guild.create_role(name='binned')
    return role

async def isBinned(guild, member):
    binnedRole = await getBinnedRole(guild)
    for role in member.roles:
        if role == binnedRole:
            return True
    return False

@client.event
async def on_message(message):
    isbinned = await isBinned(message.guild, message.author)
    if isbinned == True and message.channel.name != bin_channel:
        await message.delete() 
    await client.process_commands(message)  
    


client.run(RUN_ID)