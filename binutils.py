import discord
import globalvars

async def isBinned(guild, member):
    binnedRole = await getBinnedRole(guild)
    for role in member.roles:
        if role == binnedRole:
            return True
    return False

async def getBinnedRole(guild):
    role = None
    for role in guild.roles:
        if str(role) == 'binned':
            return role
    role = await guild.create_role(name='binned')
    return role

async def binAction(guild, member:discord.Member):
    ''' puts someone in the bin, returns False if they already had the binned role'''
    binnedRole = await getBinnedRole(guild)
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