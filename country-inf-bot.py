import discord
import requests
import random
import pandas as pd
from discord.ext import commands
import discord, datetime, time
from datetime import date, datetime

times_used = 0

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


df = pd.read_html("https://worldpopulationreview.com/continents/capitals/world")
df1 = (df[0])
df2 = pd.DataFrame(df1)
df3 = df2["Country"].str.lower()
del df2["Country"]
df2.insert(1, "Country", df3, True)

dp = pd.read_html("https://worldpopulationreview.com/countries")
dp1 = (dp[0])
dp2 = pd.DataFrame(dp1)
dp3 = dp2.iloc[:, 1:3]
dp4 = dp3["Country"].str.lower()
del dp3["Country"]
dp3.insert(0, "Country", dp4, True)

da2 = pd.DataFrame(dp1)
da3 = da2[["Country", "Area"]]
da4 = da3["Country"].str.lower()
del da3["Country"]
da3.insert(0, "Country", da4, True)

dd1 = (dp[0])
dd2 = pd.DataFrame(dd1)
dd3 = dd2[["Country", "Density (km²)"]]
dd4 = dd3["Country"].str.lower()
del dd3["Country"]
dd3.insert(0, "Country", dd4, True)


@client.command(name="capitals")
async def _command(ctx):
    global times_used
    await ctx.send(f"tell me a country")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await client.wait_for("message", check=check)
    count = msg.content
    country = count.lower()
    try:
        c = df2.loc[df2["Country"] == country, "Capital"]
        d = "".join(c)
        await msg.channel.send(d)
    except:
        await msg.channel.send("there is no such country")

    times_used = times_used + 1


@client.command(name="populations")
async def _command(ctx):
    global times_used
    await ctx.send(f"tell me a country")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await client.wait_for("message", check=check)
    count = msg.content
    country = count.lower()
    try:
        c = dp3.loc[dp3["Country"] == country]
        await msg.channel.send(int(c["2021 Population"]))

    except:
        print("there is no such country")

    times_used = times_used + 1


@client.command(name="density")
async def _command(ctx):
    global times_used
    await ctx.send(f"tell me a country")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await client.wait_for("message", check=check)
    count = msg.content
    country = count.lower()
    try:
        c = dd3.loc[dd3["Country"] == country]
        d = "".join(c["Density (km²)"])
        await msg.channel.send(d)

    except:
        await msg.channel.send("there is no such country")

    times_used = times_used + 1


@client.command(name="areas")
async def _command(ctx):
    global times_used
    await ctx.send(f"tell me a country")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await client.wait_for("message", check=check)
    count = msg.content
    country = count.lower()
    try:
        c = da3.loc[da3["Country"] == country]
        await msg.channel.send(int(c["Area"]))

    except:
        await msg.channel.send("there is no such country")

    times_used = times_used + 1


client.run("TOKEN")