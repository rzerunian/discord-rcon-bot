import discord
from discord.ext import commands
from mcrcon import MCRcon
import os

# Defina o prefixo de comando do bot e o token do bot (usaremos variáveis de ambiente para segurança)
bot = commands.Bot(command_prefix="!")

# Configurações do RCON
RCON_HOST = os.getenv('RCON_HOST')
RCON_PORT = int(os.getenv('RCON_PORT'))
RCON_PASSWORD = os.getenv('RCON_PASSWORD')

# Função que conecta ao servidor e executa o comando /players
def get_players():
    try:
        with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
            response = mcr.command('/players')
            return response
    except Exception as e:
        print(f"Erro ao conectar ao servidor RCON: {e}")
        return None

# Evento que indica que o bot está online
@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} está online!')

# Comando para obter a lista de jogadores conectados
@bot.command()
async def players(ctx):
    players_list = get_players()
    if players_list:
        await ctx.send(f"Jogadores conectados: \n{players_list}")
    else:
        await ctx.send("Não foi possível obter a lista de jogadores.")

# Inicia o bot
bot.run(os.getenv('DISCORD_TOKEN'))
