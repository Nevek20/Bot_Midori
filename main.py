import discord
from discord.ext import commands
import random
import json
import os
import aiohttp

MENTIONED_USER_ID = 0000000000000000

intents = discord.Intents.all()
intents.messages = True
intents.message_content = True
bot = commands.Bot(".", intents=intents)

PEXELS_API_KEY = "*****************************************************"
PEXELS_API_URL = "https://api.pexels.com/videos/search?query=cat&per_page=10"

#Carregar o contador JSON
def contador():
    if os.path.exists("contador.json"):
        with open ("contador.json", "r") as f:
            return json.load(f)
    return {"count": 0}

#Salvar o contador JSON
def salvar(data):
    with open ("contador.json", "w") as f:
        json.dump(data,f)

#inicia o contador
counter = contador()

@bot.event
async def on_ready():
    print("Comecou a putaria")

@bot.event
async def on_message(message):
    global counter

    if message.author.bot: 
        return
    if f"<@{MENTIONED_USER_ID}>" in message.content:
        counter["count"] += 1
        salvar(counter)
        await message.channel.send(f"O contador está em {counter['count']}!")
    await bot.process_commands(message)

@bot.command()
async def credits(ctx):
    """Créditos de quem criou o bot"""
    await ctx.reply("Este bot foi criado por Matheus Guida!! - E calma q to me esforçando pra ficar bom...")

@bot.command()
async def ola(ctx:commands.Context):
    """Da um oi pra você"""
    nome = ctx.author.name
    await ctx.reply(f"Oi, {nome}!!!!!")

@bot.command()
async def soma(ctx:commands.Context, a:int, b:int):
    """Faz uma continha básica de soma"""
    resultado = a + b
    await ctx.send(f"Sua conta:     {a} + {b} = {resultado}")

@bot.command()
async def kill(ctx, member:discord.Member): 
    """Mata alguem"""
    await ctx.send(f"O fodido do(a) {member.mention} MORREU!!! 💀💀💀")

@bot.command()
async def d6(ctx): 
    """Rola um D6"""
    resultado = random.randint(1,6)
    await ctx.send(f"🎲 | Seu D6 foi de:   {resultado}.")

@bot.command()
async def alexpimenta(ctx):
    """Conta quantas vezes o alexpimenta foi chamado"""
    await ctx.send(f"o viado do(a) alexpimenta foi mencionado {counter['count']} vezes")

@bot.command()
async def sazon(ctx:commands.Context):
    """Mostra o maior Sazon do Brasil"""
    embed1 = discord.Embed(
        title= "O MAIOR SAZON DO MUNDO!",
        description = "\u200b**Vulgo Lokinho (Lokashi)\u200b**"
    )

    imagem = discord.File("img/sazon.png" , filename="sazon.png")
    embed1.set_image(url="attachment://sazon.png")

    embed1.set_footer(text="⚠️ PROCURADO!! RECOMPENSA: 3 REAIS NO PIX ⚠️")
    await ctx.send(embed=embed1, file=imagem)

@bot.command()
async def tatikawa(ctx:commands.Context):
    """TATIKAWAAAAAAAA"""
    embed2 = discord.Embed(
        title="Motivo: estuprou viados no beco",
        description = "Recompensa: 20 mil dólares"
    )

    img2 = discord.File("img/tatikawa.png", filename="tatikawa.png")
    embed2.set_image(url="attachment://tatikawa.png")
    
    embed2.set_author(name="Policia Federal")
    embed2.set_footer(text="Qualquer informação alertar as autoridades.")
    await ctx.send(embed=embed2, file=img2)

@bot.command(name="gato")
async def gato(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(PEXELS_API_URL, headers={"Authorization": PEXELS_API_KEY}) as response:
            if response.status == 200:
                data = await response.json()
                videos = data.get("videos", [])
                
                if videos:
                    video_url = random.choice(videos)["video_files"][0]["link"]
                    await ctx.send(video_url)
                else:
                    await ctx.send("F")
            else:
                await ctx.send("F2")
        
bot.run("***************************************")