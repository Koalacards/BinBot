import discord
import globalvars

async def isBinned(guild, member):
    binnedRole = await getBinnedRole(guild)
    if binnedRole is None:
        return False
    for role in member.roles:
        if role == binnedRole:
            return True
    return False

async def getBinnedRole(guild):
    for role in guild.roles:
        if str(role) == 'binned':
            return role
    return None

async def binAction(guild, member:discord.Member):
    ''' puts someone in the bin, returns False if they already had the binned role'''
    binnedRole = await getBinnedRole(guild)
    if binnedRole == None:
        return None
    hasBinnedRole = False
    for role in member.roles:
        if role == binnedRole:
            hasBinnedRole = True
            break
    if hasBinnedRole == True:
        return False
    else:
        await member.add_roles(binnedRole)
        return True

async def unbinAction(guild, member:discord.Member):
    '''Takes someone out of the bin, returns False if they are already out of the bin'''
    binnedRole = await getBinnedRole(guild)
    if binnedRole == None:
        return None
    hasBinnedRole = False
    for role in member.roles:
        if role == binnedRole:
            hasBinnedRole = True
            break
    if hasBinnedRole == True:
        await member.remove_roles(binnedRole)
        return True
    else:
        return False