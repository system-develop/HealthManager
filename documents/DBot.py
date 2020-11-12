import discord
import random
import re
link_regex = re.compile(
            r'^https?://(?:(ptb|canary)\.)?discordapp\.com/channels/'
            r'(?:([0-9]{15,21})|(@me))'
            r'/(?P<channel_id>[0-9]{15,21})/(?P<message_id>[0-9]{15,21})/?$'
        )
client = discord.Client()

random_contents = [
    "元気そうで何よりです。その調子で健康を維持しましょう",
    "今の時期、健康第一が何よりモットーです。その心がけをこれからも",
    "(｀･ω･´)(｀･ω･´)(｀･ω･´)(｀･ω･´)",
]

@client.event
async def on_ready():
    print('私は {0.user} で活動を始めたぞ。おや？ご不満かい？'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!health 😄":
        content = random.choice(random_contents)
        # メッセージが送られてきたチャンネルに送る
        await message.channel.send(content)

    elif message.content == "!health 😷":

        await message.channel.send('咳メッセージ')

    elif message.content == "!health 🤐":

        await message.channel.send('息苦しさメッセージ')

    elif message.content == "!health 🤧":

        await message.channel.send('鼻水メッセージ')

    elif message.content == "!health 😵":

        await message.channel.send('喉の痛みメッセージ')

    elif message.content == "!health 👿":

        await message.channel.send('体のだるさメッセージ')

    elif message.content == "!health 🥶":

        await message.channel.send('腹痛メッセージ')

    elif message.content == "!health 🤢":

        await message.channel.send('下痢メッセージ')

    elif message.content == "!health 🤕":

        await message.channel.send('頭痛メッセージ')

    elif message.content == "!health 👅":

        await message.channel.send('味覚異常メッセージ')

    elif message.content == "!health 👃":

        await message.channel.send('嗅覚異常メッセージ')


client.run('NzY2MTczNDg2Nzc0NjE2MDc1.X4fgqg.QFiMQHxjWoRF6ZH6S3FDzNwqUxk')