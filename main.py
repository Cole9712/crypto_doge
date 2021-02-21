import discord
import os
from discord.ext import commands
import price_util as pu
import util
from sigfig import round

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
            displayLeftArrow = False
            [name, rank, price, timestamp, price_change_pct,
                price_change, high, logo_url] = pu.getBasic(msgArr[1])
            [desp, coinUrl] = pu.getUrl(msgArr[1])
            if len(desp)>=400:
                showDesp = desp[:400]+"......(for more information, react with \U00002B05 in bottom)"
                displayLeftArrow = True
            else:
                showDesp = desp

            embed = discord.Embed(title=msgArr[1]+" ("+name+")", url=coinUrl,
                        description=showDesp, color=discord.Color.blue())
            embed.add_field(name="Current Price",
                            value=str(round(float(price), sigfigs=7))+" USD", inline=True)
            embed.add_field(name="Timestamp", value=util.convertTimestamp(timestamp), inline=True)
            embed.add_field(name="Price Change in 1 Day", value=str(round(float(price_change), sigfigs=7)), inline=False)
            embed.add_field(name=f"Price Change % in 1 Day", value=str(round(float(price_change_pct), sigfigs=5))+"%", inline=False)
            embed.add_field(name="Rank by Market Cap", value=rank, inline=True)
            embed.add_field(name="All Time High Price", value=str(round(float(high), sigfigs=7))+" USD", inline=True)
            embed.set_thumbnail(
                url=logo_url)
            leftString = ""
            if displayLeftArrow:
                leftString = "\U00002B05Go Left for Description    "

            embed.set_footer(text=leftString+"Go Right for Sparkline\U000027A1")

            chanMsg = await channel.send(embed=embed)
            await chanMsg.add_reaction('\U00002B05')
            await chanMsg.add_reaction('\U000027A1')
            await msg.add_reaction('\U0001F4B0')
        else:
            await channel.send('GG!')
    await bot.process_commands(msg)

@client.event
async def on_reaction_add(reaction, user):
    if user == client.user:
        return
    if reaction.emoji == '\U00002B05':
        
        await reaction.message.delete()
        pass
    elif reaction.emoji == '\U000027A1':
        
        pass



client.run(os.getenv('DISCORD_TOKEN'))
