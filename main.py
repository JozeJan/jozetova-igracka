import asyncio
import time

from discord import FFmpegPCMAudio, app_commands
from openai import OpenAI
import discord
from discord.ext import commands
from typing import List
global dict
dict = {}
import os

global glasovi
glasovi = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
global customlist
customlist = {}













# Define the bot's intents
intents = discord.Intents.all()

# Create the bot instance with the specified command prefix and intents
client = commands.Bot(command_prefix='!', intents=intents)

# Event listener for when the bot has finished preparing
@client.event
async def on_ready():
    print(f' {client.user} (ID: {client.user.id})')
    print("work bitch garblt")
    print('------')


@client.command()
async def govori(ctx, pglas):
    global globalctx
    globalctx = ctx
    global glas
    glas = pglas

    if glas in glasovi:
        global dict
        ctxmauthor = ctx.message.author #sets it to a varible (for somereason it fails to make a dict without it.
        dict[ctxmauthor] = glas
        if ctx.author.voice is None:
            return await ctx.send("You are not connected to a voice channel")
        if ctx.author.voice is True:
            await ctx.send(f"You are already connected to a voice channel")
        else:
            global voice_channel
            voice_channel = ctx.author.voice.channel #sets the voice cahnel author to a shorter thingy so its nice!
            await voice_channel.connect()
            await ctx.send(f"Connected to voice channel: '{voice_channel}'")
    else:
        await ctx.send(f"Uporabite eden izmed teh glasov: {glasovi}")



#
# @client.command()
# async def utihni(ctx):
#     global author
#     author = []
#     await voice_channel.disconnect() makes leave


@client.event #reading massages no matter what
async def on_message(message):
    await client.process_commands(message)
    message_content = message.content
    message_author = message.author
    message_words = set(message_content.split()) #splits the words (for detecting custom uwu)

    if message_author in dict and "!govori" not in message_content:
        print(message_words)  # delite just for fun
        global custom

        custom = set(customlist).intersection(message_words)
        print(f'Cooking a new massage for -> {message_author} Rekel je: {message_content}')
        await tts(message_content, message_author)
        messageaudio = FFmpegPCMAudio("/home/joze/PycharmProjects/JožetovaIgračkaV4/speech.mp3")
        globalctx.voice_client.play(messageaudio)
    else:
        print(f'Random New message -> {message_author} said: {message_content}')







async def tts(message_content, message_author): #dict author is needed to find in dict the voice theyuse
        client = OpenAI(api_key="sk-proj-3MgyxneFDiT5LWBACL53T3BlbkFJEMjkjxj8DoisympUGuCl")
        with client.audio.speech.with_streaming_response.create(
            model="tts-1",
            voice=dict.get(message_author),
            input=message_content,
        ) as response:
            response.stream_to_file("speech.mp3")


global leaderboard, timeboard
leaderboard = {}
timeboard = {}
@client.event
async def on_voice_state_update(member, prev, cur):
    global start_time

    user = member.name
    if cur.self_mute and not prev.self_mute: # Would work in a push to talk channel
        print(f"{user} stopped talking!")


        timeboard[user] = time.time()

    if prev.self_mute and not cur.self_mute: # As would this one
        print(f"{user} started talking!")


        print(timeboard[user])
        end_time = time.time()
        elapsed_time = end_time - timeboard[user]
        rounded_time = round(elapsed_time, 2)



        channel_id = 1235858508059119649  # Replace this with your actual channel ID
        channel = client.get_channel(channel_id)
        await channel.send(f"Hello, črnc {user} je bil mutan {rounded_time} sekund!")
        # if rounded_time > leaderboard:
        #     leaderboard[user] = rounded_time











@client.command()
async def mrg(ctx, ocena):
    import datetime
    now = datetime.datetime.now()
    time = (f"{now.hour}:{now.minute}")
    import matplotlib.pyplot as plt

    # line 1 points
    x1 = [1,2,3]
    y1 = [2,4,1]
    # plotting the line 1 points
    plt.plot(x1, y1, label = "line 1")

    # line 2 points
    x2 = [1,2,3]
    y2 = [4,1,3]
    # plotting the line 2 points
    plt.plot(x2, y2, label = "line 2")

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
    # giving a title to my graph
    plt.title('Two lines on same graph!')

    # show a legend on the plot
    plt.legend()

    plt.savefig('plot.png')  # Save as PNG file










client.run('MTIzNTE0MTA2ODExNTQxNTA0MA.G3NQff.opEc4DgTeQKbv6viIFZS_O-eh7rtgP5X4rccMM')