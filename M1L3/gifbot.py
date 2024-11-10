import discord
from discord.ext import commands

# Botunuzu oluşturun
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True 

bot = commands.Bot(command_prefix='gf!', intents=intents)

@bot.command()
async def Ask(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send("Lütfen etiketlemek istediğiniz bir kullanıcıyı belirtin.")
        return
    emb = discord.Embed(
        title=" ",
        description=f"{ctx.author.mention},kullanıcısı {member.mention} sana aşık oldu! ",
        color=discord.Color.blue()
    )

    await ctx.send(embed=emb)
    await ctx.send("https://tenor.com/tr/view/milkandmocha-hug-cute-kawaii-love-gif-11955240341230810481")


@bot.command()
async def Tebrik(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send("Lütfen etiketlemek istediğiniz bir kullanıcıyı belirtin.")
        return
    emb = discord.Embed(
        title=" ",
        description=f"{ctx.author.mention},kullanıcısı {member.mention} sani tebrik etti ",
        color=discord.Color.blue()
    )

    await ctx.send(embed=emb)
    await ctx.send("https://tenor.com/tr/view/sekerpare-senersen-sener-sen-ilyassalman-gif-9857171")


@bot.command()
async def Kizgin(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send("Lütfen etiketlemek istediğiniz bir kullanıcıyı belirtin.")
        return
    emb = discord.Embed(
        title=" ",
        description=f"{ctx.author.mention},kullanıcısı {member.mention} sana kızdı! ",
        color=discord.Color.blue()
    )

    await ctx.send(embed=emb)
    await ctx.send("https://tenor.com/tr/view/gjirlfriend-gif-16348084597044947976")


bot.run('TOKEN')