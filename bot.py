import discord
import os

from discord.ext import commands


TokenFile = open("./data/Token.txt", "r")
TOKEN = TokenFile.read()

OWNERID = 674701053425352714

bot = commands.Bot(command_prefix = ".", case_insensitive=True)

@bot.event
async def on_ready():
    print("Бот готовий")


@bot.event
async def on_command_error(ctx,error):
    embed = discord.Embed(
    title='',
    color=discord.Color.red())
    if isinstance(error, commands.CommandNotFound):
        pass
    if isinstance(error, commands.MissingPermissions):
        embed.add_field(name=f'Помилка доступу', value=f'Ти не маєш {error.missing_perms} дозвіл.')
        await ctx.send(embed=embed)
    else:
        embed.add_field(name = f':x: Помилка в терміналі:', value = f"```{error}```")
        await ctx.send(embed = embed)
        raise error

@bot.command()
async def load(ctx, extension):
    if ctx.author.id == OWNERID:
        bot.load_extension(f'Сogs:{extension}')
        await ctx.send(f"Сogs включено!")
    else:
        await ctx.send(f"Ти ще не настільки крутий для цієї команди")

@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == OWNERID:
        bot.unload_extension(f'Cogs.{extension}')
        await ctx.send(f"Cog відключено!")
    else:
        await ctx.send(f"Ти ще не настільки крутий для цієї команди")


@bot.command(name = "reload")
async def reload_(ctx, extension):

    if ctx.author.id == OWNERID:
        bot.reload_extension(f'Cogs.{extension}')
        await ctx.send(f"Cog перезапущено!")
    else:
        await ctx.send(f"Ти ще не настільки крутий для цієї команди")


for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        try:
            bot.load_extension(f'Cogs.{filename[:-3]}')
        except Exception:
            raise Exception

bot.run(str(TOKEN))