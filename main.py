import asyncio
import time
import json
from discord import FFmpegPCMAudio, app_commands
from openai import OpenAI
import discord
from discord.ext import commands                    ####<--------------------------------------------NEVEM KVA SE KLE SPLOH DOGAJA JUST LEAVE IT ALONE!
dict = {}
import os

glasovi = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
customlist = {}
leaderboard = {}
playtime = {}
timemute = {}
global lisenforjoin, lisennextmessig, messiges
lisennextmessig = []
lisenforjoin = {}
messiges = {}
global emojiseznam
emojiseznam = [
        "🥇 1st",
        "🥈 2nd",
        "🥉 3rd",
        "🚀 4th",
        "😎 5th",
        "😬 6th",
        "😟 7th",
        "🤢 8th",
        "💩 9th",
        "🗑️ 10th"
    ]


intents = discord.Intents.all()
from keys import openai_api, discordapi_key


# Create the bot instance with the specified command prefix and intents
client = commands.Bot(command_prefix='!', intents=intents)

# Event listener for when the bot has finished preparing
@client.event
async def on_ready():
    print(f' {client.user} (ID: {client.user.id})')
    print("work bitch garblt")
    print('------')
    global leaderboard, playtime
    with open('leaderboard.txt', 'r') as file:
        leaderboard = json.load(file)  # Load leaderboard as a dictionary
    with open('playtime.txt', 'r') as file:
        playtime = json.load(file)  # Load leaderboard as a dictionary


@client.command()
async def ponovi(ctx):
    messageaudio = FFmpegPCMAudio("speech.mp3")
    ctx.voice_client.play(messageaudio)

@client.command()
async def govori(ctx, pglas):
    global globalctx, glas
    globalctx = ctx # rab bit kle
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


@client.event #reading massages no matter what
async def on_message(message):
    await client.process_commands(message)
    message_content = message.content
    message_author = message.author
    message_words = set(message_content.split()) #splits the words (for detecting custom uwu) leave it for now

    donotread = ["!govori", "!ponovi"]
    if message_author in dict and not any(word in message_content for word in donotread): #al naredi voice file in predvaja al ne
        print(message_words)  # delite just for fun
        global custom

        custom = set(customlist).intersection(message_words)
        print(f'Cooking a new massage for -> {message_author} Rekel je: {message_content}')
        await tts(message_content, message_author)
        messageaudio = FFmpegPCMAudio("speech.mp3")

        globalctx.voice_client.play(messageaudio)
    if message_author in lisennextmessig:
        print("cuming!!!")
        messiges[message_author] = message_content
        print(messiges)
    else:
        print(f'Random New message -> {message_author} said: {message_content}')




async def tts(message_content, message_author): #dict author is needed to find in dict the voice theyuse
        client = OpenAI(api_key=openai_api)
        with client.audio.speech.with_streaming_response.create(
            model="tts-1",
            voice=dict.get(message_author),
            input=message_content,
        ) as response:
            response.stream_to_file("speech.mp3")

# @tasks.loop()
# async def anticheat(member):
#     if member.voice: POMOJE NA RABM VEČ
#         pass
#     else:
#         timemute[member.name] = None
#         anticheat.stop()

@client.command()
async def leaderboard(ctx):
    i = 0
    messig = []
    for tekmovalec in sorted(leaderboard.items(),key=lambda item:-item[1]):
        if i > 10:
            break
        messig.append(f"{emojiseznam[i]}: {tekmovalec[0]}, Minute: {tekmovalec[1]}")
        i+=1
    await ctx.send("\n".join(messig))
@client.command()
async def playtime(ctx):
    i = 0
    messig = []
    for tekmovalec in sorted(playtime.items(), key=lambda item: -item[1]):
        if i > 10:
            break
        messig.append(f"{emojiseznam[i]}: {tekmovalec[0]}, Minute: {tekmovalec[1]}")
        i += 1
    await ctx.send("\n".join(messig))


@client.event
async def on_voice_state_update(member, before, after):
    channel_id = 1235858508059119649  # Replace this with your actual channel ID
    channel = client.get_channel(channel_id)
    print(member)
    user = member.name
    if after.self_mute and not before.self_mute: # Mutes
        timemute[user] = time.time()
        print(f"{user} muted")
        # anticheat.start(member)
    if before.channel is not None and after.channel is None:
        timemute[member.name] = None
    if before.self_mute and not after.self_mute: # Unmutes
        # anticheat.stop() #stops so it doesnt erorred
        end_time = time.time()
        if timemute[user]:
            elapsed_time = end_time - timemute[user]
            elepsed_time_hour = elapsed_time / 60
            rounded_time_hour = round(elepsed_time_hour, 2)
            if user not in playtime:
                playtime[user] = 0  # Initialize to 0 if it doesn't exist
            playtime[user] += rounded_time_hour
            with open("playtime.txt", "w") as file:
                json.dump(leaderboard, file)  # Dump leaderboard dictionary as JSON
            if user not in leaderboard or rounded_time_hour > leaderboard[user]:   #thanks to chat gbt i dont know what this works but it does
                leaderboard[user] = rounded_time_hour
                await channel.send(f"""New record from {member.mention}: {rounded_time_hour} minut. Your total muted time is {playtime[user]}""")
                with open("leaderboard.txt", "w") as file:
                    json.dump(leaderboard, file)  # Dump leaderboard dictionary as JSON
            print(f"{member.name} unmuted was muted for {rounded_time_hour}")
        else:
            await channel.send(f"HAHAHAH PA SEM TE DOBU {member.mention} BADNA! NČ GULJUFANJA PR BAJTA")

    # if member.voice and user in lisenforjoin:
    #     tts()





@client.command()
async def leavemesig(ctx, ime):
    if ime:
        await ctx.send(f"Prepering a new message for {ime} please type it.")
        lisennextmessig.insert(0,ctx.author.name)
        lisenforjoin[ime] = ctx.author
        print(f"adeed to {lisennextmessig}")




client.run(discordapi_key)
