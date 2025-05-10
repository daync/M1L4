import discord
from bot_logic import gen_pass

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$halo'):
        await message.channel.send("Hai!")
    elif message.content.startswith('$sampai jumpa'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send("Password kamu " + gen_pass(10))

client.run("MTM2ODIwNjMyMjgxMzc2MzYyNw.G_buUa.dWb7nuqjXSWNKspubF2vrVYjj9lfUCteczjEN8")

