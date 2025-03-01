import discord
import os, random, time
import requests
from discord.ext import commands
from settings import settings
import deepl

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Comandos existentes
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

# Piedra, papel o tijera
@bot.command()
async def ppt(ctx):
    await ctx.send("¡Hola! Juguemos piedra, papel o tijera. Escribe tu elección: piedra, papel o tijera.")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ["piedra", "papel", "tijera"]
    
    msg = await bot.wait_for("message", check=check)
    opciones = ["piedra", "papel", "tijera"]
    bot_choice = random.choice(opciones)
    eleccion = msg.content.lower()
    
    if eleccion == bot_choice:
        resultado = "Empate"
    elif (eleccion == "piedra" and bot_choice == "tijera") or (eleccion == "papel" and bot_choice == "piedra") or (eleccion == "tijera" and bot_choice == "papel"):
        resultado = "¡Ganaste!"
    else:
        resultado = "¡Perdiste!"
    
    await ctx.send(f'Yo elegí {bot_choice}. {resultado}')

# Lanzar dados
@bot.command()
async def dado(ctx):
    await ctx.send(f'Sacaste un {random.randint(1, 6)}')

# Adivinar el número
@bot.command()
async def adivina(ctx):
    numero = random.randint(1, 10)
    await ctx.send("Adivina un número del 1 al 10")
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    while True:
        msg = await bot.wait_for("message", check=check)
        try:
            guess = int(msg.content)
            if guess == numero:
                await ctx.send("¡Correcto! 🎉")
                break
            else:
                await ctx.send("Intenta de nuevo")
        except ValueError:
            await ctx.send("Ingresa un número válido")

# Reto de dibujo
@bot.command()
async def dibujo(ctx):
    retos = ["Dibuja un dragón", "Dibuja un paisaje futurista", "Dibuja tu personaje favorito en otro estilo"]
    await ctx.send(random.choice(retos))

API_KEY = "cb2e23087a914f5e924161055252202"
BASE_URL = "http://api.weatherapi.com/v1/current.json"
@bot.command()
async def clima(ctx, *, ciudad: str):
    """Obtiene el clima de una ciudad usando WeatherAPI"""
    try:
        params = {
            "key": API_KEY,
            "q": ciudad,
            "lang": "es"
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if response.status_code == 200:
            nombre_ciudad = data["location"]["name"]
            pais = data["location"]["country"]
            temperatura = data["current"]["temp_c"]
            humedad = data["current"]["humidity"]
            viento = data["current"]["wind_kph"]
            descripcion = data["current"]["condition"]["text"]
            mensaje = (f"🌍 *Clima en {nombre_ciudad}, {pais}:*\n"
                       f"🌡️ *Temperatura:* {temperatura}°C\n"
                       f"💧 *Humedad:* {humedad}%\n"
                       f"🌬️ *Viento:* {viento} km/h\n"
                       f"⛅ *Descripción:* {descripcion}")
        else:
            mensaje = f"❌ No se encontró la ciudad '{ciudad}'."
        await ctx.send(mensaje)
    except Exception as e:
        await ctx.send("⚠️ Ocurrió un error al obtener el clima.")
        print(f"Error: {e}")


DEEPL_API_KEY = "a095f285-5f80-4e4b-a1cb-ed41938284c1:fx"
translator = deepl.Translator(DEEPL_API_KEY)
@bot.command()
async def traducir(ctx, idioma_destino: str, *, texto: str):
    """Traduce un texto al idioma especificado"""
    try:
        resultado = translator.translate_text(texto, target_lang=idioma_destino.upper())
        await ctx.send(f"*Traducción ({idioma_destino}):* {resultado.text}")
    except Exception as e:
        await ctx.send(f"⚠️ Error al traducir: {e}")


API_KEY_NEWS = "7d804aaae84d487b9f1153d58ceab275"
@bot.command()
async def noticias(ctx):
    """Obtiene las noticias del día."""
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY_NEWS}"
    try:
        response = requests.get(url)
        news = response.json()
        if news["status"] == "ok":
            articles = news["articles"][:5]  # Obtener las 5 primeras noticias
            for article in articles:
                title = article["title"]
                description = article["description"]
                url = article["url"]
                await ctx.send(f"**{title}**\n{description}\nMás información: {url}\n")
        else:
            await ctx.send("Lo siento, no pude obtener las noticias.")
    except Exception as e:
        await ctx.send(f"Error al obtener noticias: {e}")

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
    12. **$contaminacion**: Informa sobre la contaminación y ofrece consejos para combatirla.
    13. **$peliculas**: Da recomendaciones de películas y lugares para verlas.
    14. **$limpiar**: Elimina mensajes en el canal.
    15. **$ppt**: Juega piedra, papel o tijera con el bot.
    16. **$dado**: Lanza un dado (número aleatorio entre 1 y 6).
    17. **$adivina**: Adivina un número entre 1 y 10.
    18. **$dibujo**: Da un reto de dibujo aleatorio.
    19. **$clima [ciudad]**: Muestra el clima actual de la ciudad proporcionada.
    20. **$traducir [idioma_destino] [texto]**: Traduce un texto al idioma especificado.
    21. **$noticias**: Muestra las últimas noticias.
    """
    await ctx.send(ayuda_texto)


# Iniciar el bot
bot.run(settings["TOKEN"])
