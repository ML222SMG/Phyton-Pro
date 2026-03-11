import discord
from discord.ext import commands
import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

curiosidades = [
    "El Vampiro de Energía: 🔋 ¿Sabías que los aparatos conectados pero apagados (como el cargador del celular o la TV) consumen hasta un 10% de la energía de tu hogar? A esto se le llama consumo fantasma. Desconectarlos no solo ayuda al planeta, sino que también baja la cuenta de la luz.",
    "El Poder de una Lata: 🥤 Reciclar una sola lata de aluminio ahorra suficiente energía para mantener encendida una televisión por 3 horas. El aluminio es uno de los pocos materiales que se puede reciclar infinitamente sin perder calidad.",
    "Buscadores Verdes: 🌳 Si quieres ayudar mientras navegas, existen buscadores como Ecosia que utilizan los ingresos por publicidad para plantar árboles. Es una forma sencilla de reforestar el mundo mientras haces tus tareas o buscas tutoriales.",
    "Menos Carne, Más Agua: 🥩 Para producir solo 1 kilo de carne de res se necesitan cerca de 15,000 litros de agua. Reducir el consumo de carne aunque sea un día a la semana (como los Lunes sin Carne) tiene un impacto masivo en el ahorro de recursos hídricos.",
    "Moda Rápida vs. Planeta: 👕 La industria de la moda es la segunda más contaminante del mundo. Fabricar unos jeans nuevos requiere unos 7,500 litros de agua (lo que bebe una persona promedio en 7 años). ¡Comprar ropa de segunda mano o intercambiar con amigos es una súper opción!"
]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
@bot.command()
async def meme1(ctx):
    imagenes = os.listdir("Bot_Discord/Imagenes")
    with open(f"Bot_Discord/Imagenes/{random.choice(imagenes)}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def audios(ctx):
    audios = os.listdir("Bot_Discord/Audios")
    with open(f"Bot_Discord/Audios/{random.choice(audios)}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
@bot.command()
async def limpiar(ctx):
    await ctx.channel.purge()
    await ctx.send("Mensaje Eliminados", delete_after = 3)
@bot.command()
async def Curiosidad(ctx):
    dato = random.choice(curiosidades)
    await ctx.send(f'ahí va una curiosidad,{dato}')
