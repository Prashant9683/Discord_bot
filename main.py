import discord
from discord.ext import commands
import os
from cog_commands import cog_commands

client = commands.Bot(command_prefix='!')

client.remove_command('help')

client.add_cog(cog_commands(client))

TOKEN = os.getenv("BOT_TOKEN")
client.run(TOKEN)