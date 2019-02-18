import discord
import datetime

TOKEN = "NTQ3MDUzOTk5NTYwNTg5MzMy.D0xOjQ.PJnnm9TGNRTMSd9PysBRSbQWvUE"

client = discord.Client()


memory = {}


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    tokens = message.content.split(' ')
    cmd = tokens[0]

    print(cmd)

    if cmd == "!hello":
        msg = "Hello {0.author.mention}".format(message)
        await client.send_message(message.channel, msg)
    elif cmd == "!learn":
        msg = ""
        if len(tokens) >= 3:
            command = "!"+tokens[1]
            response = " ".join(tokens[2:])
            if command in memory:
                msg = "I already know this one. Use !forget [command] to make me forget!"
            else:
                memory[command] = response
                msg = "Learning..."
                print("Current memory:")
                print(memory)
        else:
            msg = "I don't understand."
        await client.send_message(message.channel, msg)
    elif cmd == "!forget":
        if len(tokens) >= 2:
            command = "!"+tokens[1]
            if command in memory:
                memory.pop(command, None)
                msg = "Forgot '" + command + "'."
            else:
                msg = "I didn't even know that."
        else:
            msg = "I don't understand."
        await client.send_message(message.channel, msg)
    elif cmd == "!memory":
        await client.send_message(message.channel, "I know...")
        msg = ""
        if len(memory) == 0:
            msg = "...nothing  -JS"
        else:
            for key, value in memory.items():
                msg += "\nIf I see '" + key + "' I respond with '" + value + "'."
        await client.send_message(message.channel, msg)
    elif cmd == "!countdown":
        today = datetime.datetime.now()
        target = datetime.datetime(2019, 11, 8)
        days_remaining = target - today
        msg = "Modern Warfare 4 will release in " + str(days_remaining.days) + " days!"
        await client.send_message(message.channel, msg)
    elif cmd == "!help":
        msg = "Hi! I am a very much intelligent bot with porper speling!\n"
        msg += "Here's what I can do!\n"
        msg += "!memory - shows what I know\n"
        msg += "!learn [command] [text] - I learn to say [text] upon seeing [command]\n"
        msg += "!forget [command] - make me forget a !learn [command]"
        msg += "!memory - I tell you what I know!\n"
        msg += "!help - this"
        await client.send_message(message.channel, msg)
    elif cmd in memory:
        await client.send_message(message.channel, memory[cmd])

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")


client.run(TOKEN)