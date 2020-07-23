from binmodels import *
from peewee import *
import globalvars

def getThumbsUpVoteNum(guild_id:int):
    guildQuery = GuildProperties.select().where(GuildProperties.guild_id == guild_id)
    if len(guildQuery) == 0:
        return globalvars.defaultThumbsUpCount
    elif len(guildQuery) == 1:
        for row in guildQuery:
            if row.thumbsup is None:
                return globalvars.defaultThumbsUpCount
            else:
                return row.thumbsup
    else:
        print('There is more than one result for the guild')

def setThumbsUpVoteNum(guild_id:int, thumbsUpVoteNum:int):
    guildQuery = GuildProperties.select().where(GuildProperties.guild_id == guild_id)
    if len(guildQuery) == 0:
        GuildProperties.create(guild_id=guild_id, thumbsup=thumbsUpVoteNum)
    elif len(guildQuery) == 1:
        for query in guildQuery:
            query.thumbsup = thumbsUpVoteNum
            query.save()
    else:
        print('There is more than one result for the guild')



def getThumbsDownVoteNum(guild_id:int):
    guildQuery = GuildProperties.select().where(GuildProperties.guild_id == guild_id)
    if len(guildQuery) == 0:
        return globalvars.defaultThumbsDownCount
    elif len(guildQuery) == 1:
        for row in guildQuery:
            if row.thumbsdown is None:
                return globalvars.defaultThumbsDownCount
            else:
                return row.thumbsdown
    else:
        print('There is more than one result for the guild')

def setThumbsDownVoteNum(guild_id:int, thumbsDownVoteNum:int):
    guildQuery = GuildProperties.select().where(GuildProperties.guild_id == guild_id)
    if len(guildQuery) == 0:
        GuildProperties.create(guild_id=guild_id, thumbsdown=thumbsDownVoteNum)
    elif len(guildQuery) == 1:
        for query in guildQuery:
            query.thumbsdown = thumbsDownVoteNum
            query.save()
    else:
        print('There is more than one result for the guild')

def getHourCooldown(guild_id:int):
    guildQuery = GuildProperties.select().where(GuildProperties.guild_id == guild_id)
    if len(guildQuery) == 0:
        return globalvars.invalidated_hours
    elif len(guildQuery) == 1:
        for row in guildQuery:
            if row.hourcooldown is None:
                return globalvars.invalidated_hours
            else:
                return row.hourcooldown
    else:
        print('There is more than one result for the guild')

def setHourCooldown(guild_id:int, hourCooldownNum:int):
    guildQuery = GuildProperties.select().where(GuildProperties.guild_id == guild_id)
    if len(guildQuery) == 0:
        GuildProperties.create(guild_id=guild_id, hourcooldown=hourCooldownNum)
    elif len(guildQuery) == 1:
        for query in guildQuery:
            query.hourcooldown = hourCooldownNum
            query.save()
    else:
        print('There is more than one result for the guild')

def getThumbsUpEmoji(guild_id:int):
    guildQuery = GuildProperties.select().where(GuildProperties.guild_id == guild_id)
    if len(guildQuery) == 0:
        return globalvars.thumbsUp
    elif len(guildQuery) == 1:
        for row in guildQuery:
            if row.thumbsupemoji is None:
                return globalvars.thumbsUp
            else:
                return row.thumbsupemoji
    else:
        print('There is more than one result for the guild')

def setThumbsUpEmoji(guild_id:int, thumbsUpEmoji:str):
    guildQuery = GuildProperties.select().where(GuildProperties.guild_id == guild_id)
    if len(guildQuery) == 0:
        GuildProperties.create(guild_id=guild_id, thumbsupemoji=thumbsUpEmoji)
    elif len(guildQuery) == 1:
        for query in guildQuery:
            query.thumbsupemoji = thumbsUpEmoji
            query.save()
    else:
        print('There is more than one result for the guild')

def getThumbsDownEmoji(guild_id:int):
    guildQuery = GuildProperties.select().where(GuildProperties.guild_id == guild_id)
    if len(guildQuery) == 0:
        return globalvars.thumbsDown
    elif len(guildQuery) == 1:
        for row in guildQuery:
            if row.thumbsdownemoji is None:
                return globalvars.thumbsDown
            else:
                return row.thumbsdownemoji
    else:
        print('There is more than one result for the guild')

def setThumbsDownEmoji(guild_id:int, thumbsDownEmoji:str):
    guildQuery = GuildProperties.select().where(GuildProperties.guild_id == guild_id)
    if len(guildQuery) == 0:
        GuildProperties.create(guild_id=guild_id, thumbsdownemoji=thumbsDownEmoji)
    elif len(guildQuery) == 1:
        for query in guildQuery:
            query.thumbsdownemoji = thumbsDownEmoji
            query.save()
    else:
        print('There is more than one result for the guild')

def getCommandPrefix(guild_id:int):
    guildQuery = GuildProperties.select().where(GuildProperties.guild_id == guild_id)
    if len(guildQuery) == 0:
        return globalvars.command_prefix
    elif len(guildQuery) == 1:
        for row in guildQuery:
            if row.command_prefix is None:
                return globalvars.command_prefix
            else:
                return row.command_prefix
    else:
        print('There is more than one result for the guild')

def setCommandPrefix(guild_id:int, commandPrefix:str):
    guildQuery = GuildProperties.select().where(GuildProperties.guild_id == guild_id)
    if len(guildQuery) == 0:
        GuildProperties.create(guild_id=guild_id, command_prefix=commandPrefix)
    elif len(guildQuery) == 1:
        for query in guildQuery:
            query.command_prefix = commandPrefix
            query.save()
    else:
        print('There is more than one result for the guild')

