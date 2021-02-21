import discord
import os
from discord.ext import commands
import price_util as pu

client = discord.Client()
bot = commands.Bot(command_prefix='-doge')


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(msg):

    if msg.author == client.user:
        return

    msgContent = msg.content
    msgArr = msgContent.split()
    channel = msg.channel

    if msgContent.startswith('-doge'):
        if len(msgArr) == 2:
            [price, timestamp, logo_url] = pu.currentPrice(msgArr[1])
            curl = pu.getUrl(msgArr[1])
            embed = discord.Embed(title=msgArr[1], url=curl,
                                  description="price: "+str(round(float(price), 3))+" (USD)\nTimestamp: "+timestamp, color=discord.Color.blue())
            # pu.saveImg(logo_url, "svg.svg");
            # cairosvg.svg2png(url="./svg.svg",write_to='./logo.png')
            embed.set_thumbnail(
                url='https://cryptoicons.org/api/white/btc/400')
            embed.set_footer(text="\U000027A1Go Right for Sparkline\U000027A1")

            chanMsg = await channel.send(embed=embed)
            await chanMsg.add_reaction('\U00002B05')
            await chanMsg.add_reaction('\U000027A1')
            await msg.add_reaction('\U0001F4B0')
        else:
            await channel.send('GG!')
    await bot.process_commands(msg)


# @client.command()
# async def embed(ctx):

#     embed = discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/",
#                           description="This is an embed that will show how to build an embed and the different components", color=discord.Color.blue())
#     await ctx.send(embed=embed)


client.run(os.getenv('DISCORD_TOKEN'))
