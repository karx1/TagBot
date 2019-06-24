import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

client = commands.Bot(command_prefix=":")

extensions = [
  'jishaku',
  'cogs.tags'
]

if __name__ == "__main__":
  for ext in extensions:
    client.load_extension(ext)

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name=f"Tagging! | :help"))
  print("Ready!")

keep_alive()
code = os.environ.get("BOT_TOKEN")
client.run(code)
