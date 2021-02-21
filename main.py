import discord
import os
from discord.ext import commands
import price_util as pu

client = commands.Bot(command_prefix='-doge')


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
            jsonObj = pu.currentPrice(msgArr[1])
            await channel.send(jsonObj)
        else:
            await channel.send('GG!')
    await client.process_commands(msg)


@client.command()
async def embed(ctx):
    embed = discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/",
                          description="This is an embed that will show how to build an embed and the different components", color=discord.Color.blue())
    await ctx.send(embed=embed)


client.run(os.getenv('DISCORD_TOKEN'))
