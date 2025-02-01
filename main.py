import discord
import os, random
import time 
import requests
from discord.ext import commands
from settings import settings

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi!, I am a bot {bot.user}!')

@bot.command()
async def test(ctx, *arg):
    respuesta = " ".join(arg)
    await ctx.send(respuesta)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def poke(ctx,arg):
    try:
        pokemon = arg.split(" ", 1)[0].lower()
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        if result.text == "Not Found":
            await ctx.send("Pokemón no encontrado")
        else: 
            image_url = result.json()["sprites"]["front_default"]
            print(image_url)
            await ctx.send(image_url)
    except Exception as e:
        print("Error:", e)
@poke.error
async def error_type(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send("Tienes que darme un pokemón")

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''The duck command returns the photo of the duck'''
    print("hello")
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def dog(ctx):
    '''The dog command returns the photo of the dog'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

def get_fox_image_link():    
    link = 'https://randomfox.ca/floof/'
    res = requests.get(link)
    data = res.json()
    return data['image']

@bot.command('fox')
async def fox(ctx):
    '''The fox command returns the photo of the fox'''
    image_link= get_fox_image_link()
    await ctx.send(image_link)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
    
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path = "labels.txt", image_path = f"./{attachment.filename}"))
    else:
        await ctx.send("You forgot to upload the image :(")

@bot.command()
async def contaminacion(ctx):
    await ctx.send(f"""Hola, soy un bot {bot.user}!""")# esta linea saluda
    await ctx.send(f'Te voy hablar un poco sobre la contaminacion')
    await ctx.send(f'La contaminación es un gran problema a nivel mundial, muchos paises sufren a diario')
    # Enviar una pregunta al usuario
    await ctx.send("Quieres consejos sobre cómo combatir la contaminación? Responde con 'sí' o 'no'.")
# Esperar la respuesta del usuario
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['sí', 'si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content in ['sí', 'si']:
            await ctx.send("1. No arrojar basura en los rios")
            await ctx.send("2. Dejar de quemar basuras")   
        else:
            await ctx.send("Está bien, si alguna vez necesitas consejos, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
    await ctx.send("Quieres saber la definicion de contaminacion, responde si o no")
    response1 = await bot.wait_for('message', check=check)
    if response1:
        if response1.content in ['sí', 'si']:
            await ctx.send("Arrojar basura") 
        else:
            await ctx.send("Está bien, si alguna vez necesitas consejos, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
        
@bot.command()
async def peliculas(ctx):
    await ctx.send(f"Hola, soy un bot {bot.user}!")  # esta línea saluda
    time.sleep(1)
    await ctx.send("Te voy a hablar un poco sobre las películas.")
    time.sleep(1)
    await ctx.send("Las películas son una forma de entretenimiento y de pasar un buen rato, con amigos, familia, etc.")
    # Enviar una pregunta al usuario
    await ctx.send("¿Quieres que te recomiende una película? Responde con 'sí' o 'no'.")

    # Esperar la respuesta del usuario
    def check2(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() in ['sí', 'si', 'no']

    response2 = await bot.wait_for('message', check=check2)
    if response2:
        if response2.content.lower() in ['sí', 'si']:
            await ctx.send("Interestelar - Ciencia ficción")
            await ctx.send("La vida es bella - Drama")
            await ctx.send("Son como niños - Comedia")
            await ctx.send("El resplandor - Terror")
            await ctx.send("Coco - Animación")
        else:
            await ctx.send("Está bien, si alguna vez necesitas alguna recomendación, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")

    await ctx.send("¿Quieres saber dónde ver películas? Responde 'sí' o 'no'.")
    response3 = await bot.wait_for('message', check=check2)
    if response3:
        if response3.content.lower() in ['sí', 'si']:
            await ctx.send("Netflix, Amazon Prime Video, HBO Max, Disney+, YouTube, Paramount+, etc.")
        else:
            await ctx.send("Está bien, si alguna vez necesitas saber dónde, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")

@bot.command()
async def limpiar(ctx):
    await ctx.channel.purge()
    await ctx.send("Mensajes eliminados", delete_after = 3)

@bot.command()
async def ayuda(ctx):
    ayuda_texto = """
    Aquí están los comandos que puedes usar con este bot:

    1. **$hello**: Saluda al bot.
    2. **$test [argumentos]**: Devuelve los argumentos que se pasen.
    3. **$heh [count_heh]**: Envía "he" repetido por el número indicado (por defecto, 5).
    4. **$poke [pokemón]**: Muestra la imagen del pokemón indicado.
    5. **$duck**: Muestra una imagen aleatoria de un pato.
    6. **$dog**: Muestra una imagen aleatoria de un perro.
    7. **$fox**: Muestra una imagen aleatoria de un zorro.
    8. **$add [número1] [número2]**: Suma dos números.
    9. **$joined [miembro]**: Muestra la fecha en que un miembro se unió al servidor.
    10. **$choose [opciones]**: Elige aleatoriamente entre las opciones dadas.
    11. **$check**: Verifica si se subió una imagen y la procesa.
    12. **$contaminacion**: Habla sobre la contaminación y ofrece consejos para combatirla.
    13. **$peliculas**: Habla sobre películas y ofrece recomendaciones.
    14. **$limpiar**: Elimina mensajes en el canal.

    Si necesitas más ayuda, no dudes en preguntar.
    """
    await ctx.send(ayuda_texto)


bot.run(settings["TOKEN"])
