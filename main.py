import discord
from discord.ext import commands
import os
from cog_commands import cog_commands

client = commands.Bot(command_prefix='!')

client.remove_command('help')

client.add_cog(cog_commands(client))

client.run("OTMzNTYyNTkwOTM4OTQ3NjM3.YejV6g.zvuiw5A3WRVfzfMW8kstz1mgUDQ")