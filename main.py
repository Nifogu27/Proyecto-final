import discord
import random
import requests
from discord.ext import commands
from settings import settings
from discord.ui import View, Select
import google.generativeai as genai
import deepl

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Envia un saludo al usuario
@bot.command()
async def hola(ctx):
    await ctx.send(f'¡Hola!, soy un bot {bot.user}! Si quieres conocer mis funciones envíame "$ayuda"')

# El bot repite lo que escribes
@bot.command()
async def test(ctx, *arg):
    respuesta = " ".join(arg)
    await ctx.send(respuesta)

# El bot se ríe jajaja
@bot.command()
async def jaj(ctx, count_heh = 5):
    await ctx.send("ja" * count_heh)

# Dice la fecha en la que un usuario se unió
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

# Suma dos números
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

# Escoge entre las opciones que le das
@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


# Verifica si la imagen adjuntada es una paloma o un gorrión
@bot.command()
async def check(ctx):
    """Verifica si la imagen adjunta es una paloma o un gorrión."""
    if len(ctx.message.attachments) > 0:
        image_url = ctx.message.attachments[0].url
        # Aquí iría el código para analizar la imagen y determinar si es una paloma o un gorrión.
        # Por ejemplo, usar un modelo de machine learning o una API externa para el reconocimiento de imágenes.
        await ctx.send(f"Imagen recibida: {image_url}. Realizando análisis...")
        # Respuesta final dependiendo del análisis realizado:
        await ctx.send("Es una paloma.")  # O "Es un gorrión" según el análisis.
    else:
        await ctx.send("Por favor, adjunta una imagen para realizar la verificación.")


#Envia imágenes aleatorias de pokemones
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

# Envia imágenes aleatorias de perros
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

# Envia imágenes aleatorias de zorros
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


# El bot te habla de contaminación
@bot.command()
async def contaminacion(ctx):
    await ctx.send(f"""Hola, soy un bot {bot.user}!""")# esta linea saluda
    await ctx.send(f'Te voy hablar un poco sobre la contaminación')
    await ctx.send(f'La contaminación es un gran problema a nivel mundial, muchos paises sufren a diario')
    # Enviar una pregunta al usuario
    await ctx.send("Quieres consejos sobre cómo combatir la contaminación? Responde con 'sí' o 'no'.")
# Esperar la respuesta del usuario
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['sí', 'si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content in ['sí', 'si', "Si", "Sí"]:
            await ctx.send("1. No arrojar basura en los rios")
            await ctx.send("2. Dejar de quemar basuras")
            await ctx.send("3. No usar plásticos")
            await ctx.send("4. No usar productos con químicos")
            await ctx.send("Entre otras más")
            
        else:
            await ctx.send("Está bien, si alguna vez necesitas consejos, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
    await ctx.send("Quieres saber la definición de contaminación, responde 'sí' o 'no'.")
    response1 = await bot.wait_for('message', check=check)
    if response1:
        if response1.content in ['sí', 'si', "Si", "Sí"]:
            await ctx.send("La contaminación es la introducción de sustancias o energías dañinas en el medio ambiente, alterando su equilibrio y afectando la salud de los seres vivos.") 
        else:
            await ctx.send("Está bien, si alguna vez tienes curiosidad te ayudaré con mucho gusto.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")

# El bot te recomienda películas        
@bot.command()
async def peliculas(ctx):
    await ctx.send(f"Hola, soy un bot {bot.user}!")  # esta línea saluda
    await ctx.send("Te voy a hablar un poco sobre las películas.")
    await ctx.send("Las películas son una forma de entretenimiento y de pasar un buen rato, con amigos, familia, etc.")
    # Enviar una pregunta al usuario
    await ctx.send("¿Quieres que te recomiende una película? Responde con 'sí' o 'no'.")

    # Esperar la respuesta del usuario
    def check2(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() in ['sí', 'si', "Si", "Sí", "No", 'no']

    response2 = await bot.wait_for('message', check=check2)
    if response2:
        if response2.content.lower() in ['sí', 'si', "Si", "Sí"]:
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
        if response3.content.lower() in ['sí', 'si', "Si", "Sí"]:
            await ctx.send("Netflix, Amazon Prime Video, HBO Max, Disney+, YouTube, Paramount+, etc.")
        else:
            await ctx.send("Está bien, si alguna vez necesitas saber dónde, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")


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
    retos = ["Dibuja un carro", "Dibuja a un ser querido", "Dibuja un famoso", "Dibuja un paisaje", "Dibuja tu personaje animado"]
    await ctx.send(random.choice(retos))


# Información sobre el clima de la ciudad que desees
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

# Noticias
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

#Chatbot de Gemini
genai.configure(api_key="AIzaSyBIRjbs_w7graezF9xzG5GK92F-z6cf7gc")
# Modelo Gemini
model = genai.GenerativeModel("gemini-1.5-flash")
# Generar respuesta
@bot.command()
async def gemini(ctx, *, pregunta: str):
    """Comando para preguntar a Gemini"""
    await ctx.send("⏳ Pensando...")
    response = model.generate_content(pregunta)
    await ctx.send(response.text)

# Configuración de DeepL
DEEPL_API_KEY = "a095f285-5f80-4e4b-a1cb-ed41938284c1:fx"
translator = deepl.Translator(DEEPL_API_KEY)
# Lista de idiomas disponibles
IDIOMAS = {
    "Inglés (US)": "EN-US",
    "Inglés (GB)": "EN-GB",
    "Español": "ES",
    "Francés": "FR",
    "Alemán": "DE",
    "Japonés": "JA",
    "Portugués (PT)": "PT-PT",
    "Portugués (BR)": "PT-BR",
    "Chino": "ZH",
    "Italiano": "IT"
}
# Menú de selección de idioma
class TranslateSelect(discord.ui.Select):
    def __init__(self, text):
        self.text = text
        options = [discord.SelectOption(label=lang, value=code, emoji="🌍") for lang, code in IDIOMAS.items()]
        super().__init__(placeholder="Selecciona un idioma...", options=options)
    async def callback(self, interaction: discord.Interaction):
        try:
            # Traducir el texto seleccionado por el usuario
            translated_text = translator.translate_text(self.text, target_lang=self.values[0])
            await interaction.response.send_message(f"**Traducción a {self.values[0]}:** {translated_text.text}")
        except Exception as e:
            await interaction.response.send_message(f"⚠️ Error al traducir: {e}")
# Vista con el menú interactivo
class TranslateView(View):
    def __init__(self, text):
        super().__init__()
        self.add_item(TranslateSelect(text))
# Comando para traducir
@bot.command()
async def traducir(ctx, *, texto: str):
    """Traduce un texto usando un menú interactivo."""
    await ctx.send("Selecciona un idioma para traducir:", view=TranslateView(texto))

# Borrar todos los mensajes con el bot
@bot.command()
async def limpiar(ctx):
    await ctx.channel.purge()
    await ctx.send("Mensajes eliminados", delete_after = 3)

@bot.command()
async def ayuda(ctx):
    """Muestra las funciones del bot organizadas por número y sección."""
    help_text = """
**Funciones del Bot:**

**Funciones Simples** 🟢:
1. **$hola**: Envia un saludo al usuario.
2. **$test <mensaje>**: El bot repite lo que escribes.
3. **$ja**: Responde con una risa, normalmente usada para responder en tono divertido.

**Funciones Matemáticas** ➗:
4. **$add <número1> <número2>**: Suma dos números.

**Funciones de Elección** 🤔:
5. **$choose <opción1> <opción2> ...**: Elige una opción entre varias.

**Funciones de Verificación** ✅:
6. **$check**: Verifica si la imagen adjuntada es una paloma o un gorrión.
7. **$joined <usuario>**: Dice la fecha en la que un usuario se unió.

**Funciones de Imágenes** 🖼️:
8. **$duck**: Envía una imagen aleatoria de un pato.
9. **$dog**: Envía una imagen aleatoria de un perro.
10. **$fox**: Envía una imagen aleatoria de un zorro.
11. **$poke <pokemón>**: Muestra la imagen de un pokemón (requiere el nombre del pokemón).

**Funciones Informativas** ℹ️:
12. **$contaminacion**: Habla sobre la contaminación y da consejos para combatirla.
13. **$peliculas**: Te recomienda películas según tu preferencia.
14. **$clima <ciudad>**: Muestra el clima de la ciudad que indiques.
15. **$noticias**: Muestra las noticias del día.

**Funciones de Juegos** 🎮:
16. **$ppt**: Juega una partida de piedra, papel o tijera.
17. **$dado**: Lanza un dado y te dice el número que salió.
18. **$adivina**: Adivina un número del 1 al 10.
19. **$dibujo**: Te reta a dibujar algo al azar.

**Chatbot** 🤖:
20. **$gemini <pregunta>**: Responde preguntas utilizando el chatbot Gemini.

**Funciones de Traducción** 🌍:
21. **$traducir <texto>**: Traduce el texto dado al idioma que selecciones.

**Funciones de Moderación** ⚙️:
22. **$limpiar <número>**: Elimina el número de mensajes especificado del canal (solo administradores).
    """
    await ctx.send(help_text)

# Iniciar el bot
bot.run(settings["TOKEN"])
