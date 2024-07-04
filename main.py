import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands
from datetime import datetime

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command()
async def cal(ctx):
    print("test")
    date = datetime.today()
    date = date.strftime("%d.%m.%Y")

    url = f'https://wg.edubs.ch/termine/calexport_results?from={date}&to={date}'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    tag = soup.find("p")

    if tag is None:
        tag = soup.find_all('a')

        embed = discord.Embed(title=f"Termine am {date}",
                              description=f"Hier stehen alle Termine für den {date}",
                              color=0xFF5733)
        for s in tag:
            embed.add_field(name="Termin:", value=s.string,inline=False)

        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title=f"Termine am {date}",
                              description=f"Es gibt keine Termine für heute",
                              color=0xFF5733)
        await ctx.send(embed=embed)


bot.run("INSERT_TOKEN_HERE")
