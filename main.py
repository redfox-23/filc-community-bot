import discord
import latex
import horoscope
import catto

client = discord.Client()
token = open("token.txt", "r").read()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!horoszkop") and message.channel.id == 992728004373524520:
        try:
            await message.channel.send(horoscope.fetch(message.content.replace("!horoszkop ", "")))
        except Exception:
            await message.channel.send("Nem létező horoszkóp!")
    elif message.content.startswith("!horoszkop") and not message.channel.id == 992728004373524520:
        await message.channel.send(f"Kérlek használd a megfelelő csatornát: <#992728004373524520> :)")
    
    elif message.content.startswith("!latex"):
        latex.save_image_from_latex(message.content.replace("!latex", ""))
        await message.channel.send(file=discord.File("compiled_latex.png"))
    
    elif message.content.startswith("!cat"):
        catto.fetch(message.content.replace("!cat ", ""))
        await message.channel.send(file=discord.File("cat.gif"))

client.run(token)