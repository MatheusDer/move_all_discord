import discord
from discord.ext import commands
from discord.ext.commands import check

bot = commands.Bot(command_prefix="$")
WHITE_LIST: list[str] = ["Cargo1", "Cargo2"]


def formata_cargos_usuario(cargos) -> list[str]:
    lista_cargos = []
    for cargo in cargos:
        lista_cargos.append(str(cargo))
    
    return lista_cargos


def permissao(white_list: list[str], cargos: list[str]) -> bool:
    count = 0
    for cargo in white_list:
        if cargo in cargos:
            count += 1
    
    if count != 0:
        return True
    return False


@bot.command()
async def mover(ctx, *, canal: discord.VoiceChannel):
    cargos_user = formata_cargos_usuario(ctx.author.roles)

    if permissao(WHITE_LIST, cargos_user):
        for membros in ctx.author.voice.channel.members:
            await membros.move_to(canal)
    else:
        await ctx.channel.send("{0} não tem permissão para usar esse comando - {1} - {2} necessário"
        .format(ctx.author.name, cargos_user, WHITE_LIST))


@bot.command()
async def dc(ctx):
    await ctx.bot.logout()


bot.run('/token/')
