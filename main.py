import asyncio
import random
import time
import json
from asyncio import tasks
import re
from discord import Intents
from discord import FFmpegPCMAudio
from openai import OpenAI
import discord
from discord.ext import commands
from OrnkOkvara import NormalOkvara, OrnkOkvara
global NormalOkvara, OrnkOkvara
dict = {}
import os
glasovi = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
customlist = {}
leaderboard = {}
playtime = {}
timemute = {}
global lisenforjoin, lisennextmessig, messiges, userincall, timegable, randomgamblevalue
userincall = {}
lisennextmessig = {}
lisenforjoin = {}
messiges = {}
timegable = 0
randomgamblevalue = 0
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
client = commands.Bot(command_prefix='!', intents=intents)
# Event listener for when the bot has finished preparing

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await errorsound(ctx)


async def errorsound(ctx):
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client:
        print("allready connected")
    else:  # If the bot is not connected
        await voice_channel.connect()  # Connect to the voice channel
    if random.random() < 0.2:
        if random.random() < 0.5:
            ctx.voice_client.play(FFmpegPCMAudio("./Errors/OrnkOkvara.mp3"))
            while ctx.voice_client.is_playing():
                await asyncio.sleep(1)
            await ctx.voice_client.disconnect()
            await ctx.send(random.choice(OrnkOkvara))
        else:
            ctx.voice_client.play(FFmpegPCMAudio("./Errors/OrnkOkvara2.mp3"))
            while ctx.voice_client.is_playing():
                await asyncio.sleep(1)
            await ctx.voice_client.disconnect()
            await ctx.send(random.choice(OrnkOkvara))
    else:
        if random.random() < 0.3:
            ctx.voice_client.play(FFmpegPCMAudio("./Errors/NormalOkvara.mp3"))
            await ctx.send(random.choice(NormalOkvara))
        elif random.random() < 0.3:
            ctx.voice_client.play(FFmpegPCMAudio("./Errors/NormalOkvara2.mp3"))
            await ctx.send(random.choice(NormalOkvara))
        else:
            ctx.voice_client.play(FFmpegPCMAudio("./Errors/NormalOkvara3.mp3"))
            await ctx.send(random.choice(NormalOkvara))

#oneliner V trust
async def randommedic(ctx): #oneliner trust
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client:
        print("allready connected")
    else:  # If the bot is not connected
        await voice_channel.connect()  # Connect to the voice channel
    folders = [name for name in os.listdir("./medic") if os.path.isdir(os.path.join("./medic", name))]  # THNAKS CHAD GBT NO IDEA WHAT THIS CODE DOES
    random_folder = random.choice(folders)
    randomchosingfilefolder = f"./medic/{random_folder}"
    gambledmedicvoses = os.listdir(randomchosingfilefolder)
    randomgambledvoice = random.choice(gambledmedicvoses)
    finalgambledvoice = f"./medic/{random_folder}/{randomgambledvoice}"
    if os.path.isfile(finalgambledvoice):
        print(f"{finalgambledvoice} is a file.")
        ctx.voice_client.play(FFmpegPCMAudio(finalgambledvoice))
    # Check if it's a folder
    else:
        print(f"{finalgambledvoice} is a folder.")
        folders2 = [name for name in os.listdir(f"./medic/{finalgambledvoice}") if os.path.isdir(os.path.join(f"./medic/{finalgambledvoice}", name))]  # THNAKS CHAD GBT NO IDEA WHAT THIS CODE DOES
        randomgambledvoice2 = random.choice(folders2)
        finalgambledvoice2 = f"./medic/{random_folder}/{randomgambledvoice}/{randomgambledvoice2}"
        if os.path.isfile(finalgambledvoice):
            print(f"{finalgambledvoice} is a file.")
            ctx.voice_client.play(FFmpegPCMAudio(finalgambledvoice2))
        # Check if it's a folder
        else:
            print(f"{finalgambledvoice} is a folder.")
            folders3 = [name for name in os.listdir(f"./medic/{finalgambledvoice}/{finalgambledvoice2}") if os.path.isdir(os.path.join(f"./medic/{finalgambledvoice}/{finalgambledvoice2}", name))]  # THNAKS CHAD GBT NO IDEA WHAT THIS CODE DOES
            randomgambledvoice3 = random.choice(folders3)
            finalgambledvoice3 = f"./medic/{random_folder}/{randomgambledvoice}/{randomgambledvoice2}/{randomgambledvoice3}"
            ctx.voice_client.play(FFmpegPCMAudio(finalgambledvoice3))
            if os.path.isfile(finalgambledvoice):
                ctx.voice_client.play(FFmpegPCMAudio(finalgambledvoice3))
            else:
                print("wtf?") #oneliner

def sanitize_filename(filename):
    """
    Sanitize the filename by removing invalid characters for a file path.
    """
    # Replace characters not allowed in file names with underscores
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

@client.event
async def on_ready():
    print(f' {client.user} (ID: {client.user.id})')
    print("work bitch garblt ziga gaming")
    print('------')
    game = discord.Game("https://github.com/JozeJan/jozetova-igracka")
    await client.change_presence(status=discord.Status.idle, activity=game)
    global leaderboard, playtime
    with open('/data/leaderboard.txt', 'r+') as file:
        file.seek(0)  # Move the cursor to the beginning of the file
        try:
            leaderboard = json.load(file)  # Load leaderboard as a dictionary
        except json.JSONDecodeError:
            leaderboard = {}
    with open('/data/playtime.txt', 'r+') as file:
        file.seek(0)  # Move the cursor to the beginning of the file
        try:
            playtime = json.load(file)  # Load leaderboard as a dictionary
        except json.JSONDecodeError:
            playtime = {}

#
@client.command()
async def medic(ctx):
    await randommedic(ctx)

@client.command()
async def join(ctx):
    if ctx.author.voice is None:
        return await ctx.send("You are not connected to a voice channel")
    else:
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client:
            ctx.voice_client.play(FFmpegPCMAudio(f"./intro songs/{random.randint(1, 55)}.mp3"))
        else:  # If the bot is not connected
            await voice_channel.connect()  # Connect to the voice channel
            ctx.voice_client.play(FFmpegPCMAudio(f"./intro songs/{random.randint(1, 55)}.mp3"))


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
    sanitized_message_content = sanitize_filename(message_content)
    sanitized_message_author = sanitize_filename(message_author.name)
    message_words = set(message_content.split()) #splits the words (for detecting custom uwu) leave it for now

    donotread = ["!govori", "!ponovi"]
    # while globalctx.voice_client.is_playing():
    #     await asyncio.sleep(1)  # Check every second if the bot is still playing
    #     print(f"Fixing overlap from {message_author}")
    if message_author in dict and not any(word in message_content for word in donotread): #al naredi voice file in predvaja al ne
        if not globalctx.voice_client.is_playing():
            print(message_words)  # delite just for fun
            global custom
            custom = set(customlist).intersection(message_words)
            print(f'Cooking a new massage for -> {message_author} Rekel je: {message_content}')
            await tts(message_content, message_author)
            messageaudio = FFmpegPCMAudio(f"./TTSR/{sanitized_message_content}:{sanitized_message_author}.mp3")
            globalctx.voice_client.play(messageaudio)
    if message_author.name in lisennextmessig and "!leavenote" not in message_content:
        name = lisennextmessig[message_author.name]
        lisenforjoin[name] = [message_content]
        print(f" printing lisen for join {lisenforjoin}")
        del lisennextmessig[message_author.name]

    else:
        print(f'{message_author} said: {message_content}')

openai_client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

async def speak(text, voice):  # dict author is needed to find in dict the voice theyuse
    with openai_client.audio.speech.with_streaming_response.create(
            model="tts-1",
            voice=voice,
            input=text,
    ) as response:
        response.stream_to_file(f"{text}:{voice}.mp3")

async def tts(message_content, message_author): #dict author is needed to find in dict the voice theyuse
    with openai_client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice=dict.get(message_author),
        input=message_content,
    ) as response:
        sanitized_message_content = sanitize_filename(message_content)
        sanitized_message_author = sanitize_filename(message_author.name)
        tts_filepath = f"./TTSR/{sanitized_message_content}:{sanitized_message_author}.mp3"
        response.stream_to_file(tts_filepath)

# @tasks.loop(seconds=60)
# async def timegamble():
#     timegable += 1
#     if randomgamblevalue is None:
#         randomgamblevalue = random.randint(900, 1440)
#     if timegamble == randomgamblevalue:
#         timegamble.stop()

@client.command()
async def leaderboard(ctx):
    i = 0
    messig = []
    for tekmovalec in sorted(leaderboard.items(),key=lambda item:-item[1]):
        if i > 9:
            break
        messig.append(f"{emojiseznam[i]}: {tekmovalec[0]}, Minute: {round(tekmovalec[1], 2)}")
        i+=1
    await ctx.send("\n".join(messig))
@client.command()
async def playtime(ctx):
    i = 0
    messig = []
    for tekmovalec in sorted(playtime.items(), key=lambda item: -item[1]):
        if i > 9:
            break
        messig.append(f"{emojiseznam[i]}: {tekmovalec[0]}, Minute: {round(tekmovalec[1], 2)}")
        i += 1
    await ctx.send("\n".join(messig))


@client.event
async def on_voice_state_update(member, before, after):
    #does the leaderboard biznis
    channel_id = 1235858508059119649  # Replace this with your actual channel ID
    channel = client.get_channel(channel_id)
    user = member.name
    if after.self_mute and not before.self_mute: # Mutes
        timemute[user] = time.time()
        print(f"{user} muted")
        # anticheat.start(member)
    if before.channel is not None and after.channel is None:
        timemute[member.name] = None
        del userincall[user]
        print(f"{userincall} left")
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
            playtime[user] = round(playtime[user], 2)
            print(f"zaokrožil na {playtime[user]}")
            with open("/data/playtime.txt", "w+") as file:
                json.dump(playtime, file)  # Dump leaderboard dictionary as JSON
            if user not in leaderboard or rounded_time_hour > leaderboard[user]:   #thanks to chat gbt i dont know what this works but it does
                leaderboard[user] = rounded_time_hour
                await channel.send(f"""New record from {member.mention}: {rounded_time_hour} minut. Your total muted time is {playtime[user]}""")
                with open("/data/leaderboard.txt", "w+") as file:
                    json.dump(leaderboard, file)  # Dump leaderboard dictionary as JSON
            print(f"{member.name} unmuted was muted for {rounded_time_hour}")
        else:
            await channel.send(f"HAHAHAH PA SEM TE DOBU {member.mention} BADNA! NČ GULJUFANJA PR BAJTA")
    #does the leavemesig



    if after.channel is not None and before.channel is None:
        userincall[user] = after.channel.name
        print(f"{userincall} joined")
    if after.channel is not None and before.channel is None:
        print(f"{user} joined the channel")
        if user in lisenforjoin:
            list = lisenforjoin[user]
            voice_channel = after.channel
            print(f"waiting out {list}")
            await speak(f"Novo sporočilo za {user}: {list}", "echo")
            await asyncio.sleep(random.uniform(3, 5))
            print(f"reading out {list}")
            await voice_channel.connect()
            if not member.guild.voice_client:  # If the bot is not connected to any channel
                voice_client = await voice_channel.connect()
            else:
                voice_client = member.guild.voice_client
            yougotmail = FFmpegPCMAudio("yougotmail.wav")
            voice_client.play(yougotmail)
            while voice_client.is_playing():
                await asyncio.sleep(1)
            messageaudio = FFmpegPCMAudio("speech.mp3")
            voice_client.play(messageaudio)
            while voice_client.is_playing():
                await asyncio.sleep(1)
            await voice_client.disconnect()
            del lisenforjoin[user]
    if  before.channel != after.channel:
        userincall[user] = after.channel.name
        print(f"{userincall} swiched")

@client.command()
async def deepseek(ctx, *, message: str):
    from irot import deepseekf
    """Stores the message after !deepseek"""
    print(f"recived an masssage for deepseek: {message}")
    ai_response = await deepseekf(message)  # Await API call
    await ctx.send(ai_response)  # Send extracted response



@client.command()
async def leavenote(ctx, ime):
    if ime:
        await ctx.send(f"Prepering a new message for {ime} the next message you send will be deliverd to him!")
        lisennextmessig[ctx.author.name] = ime
        lisenforjoin[ime] = ""


@client.event
async def on_presence_update(before, after):
    if before.status != after.status:
        channel = client.get_channel(1235339151218577499)
        user_mention = f"<@{after.id}>"
        await channel.send(f"{user_mention} has gone {after.status}", allowed_mentions=discord.AllowedMentions(users=False))



# @client.event
# async def on_member_update(before, after):
#     # specific_user_name = "joze3.0"  # Replace with the specific user's name
#     if before.status != after.status:
#         channel = client.get_channel(1235339151218577499)
#         await channel.send(f"{after.name} has gone {after.status}")




discordtoekn = os.environ.get("DISCORD_TOKEN")




client.run(discordtoekn)







#simulate typing:
# async with channel.typing():
#     # simulate something heavy
#     await asyncio.sleep(20)
#
# await channel.send('Done!')
