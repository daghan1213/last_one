import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} olarak giriş yaptı.')

@bot.command()
async def iklim(ctx):
    mesaj = (
        "Sera gazlarını azaltmanın bazı yolları şunlardır:\n"
        "1. Enerji verimli cihazlar kullanmak.\n"
        "2. Fosil yakıt kullanımını azaltmak ve yenilenebilir enerji kaynaklarına geçmek.\n"
        "3. Toplu taşıma araçlarını kullanmak veya yürümek/bisiklete binmek.\n"
        "4. Atıkları geri dönüştürmek ve azaltmak.\n"
        "5. Ağaç dikmek ve ormansızlaşmaya karşı mücadele etmek.\n"
        "6. Yerel ve mevsimlik ürünler tüketmek.\n"
        "7. Enerji tasarrufu sağlamak için ev yalıtımı yapmak.\n"
        "8. Az su tüketen ürünler kullanmak."
    )
    await ctx.send(mesaj)

bot.run('bot token')