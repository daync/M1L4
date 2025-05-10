import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hai! Saya adalah bot {bot.user}!')

@bot.command()
async def Selamatpagi(ctx):
    await ctx.send("selamat pagi juga ,love love.")

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def selamatmalam(ctx):
    await ctx.send("selamat malam juga,love love.")

bot.run("MTM2ODIwNjMyMjgxMzc2MzYyNw.G_buUa.dWb7nuqjXSWNKspubF2vrVYjj9lfUCteczjEN8")




