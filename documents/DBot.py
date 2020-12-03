import discord
import json
from urllib.parse import urlparse
import mysql.connector
from discord.ext import commands
from discord.utils import find
intents = discord.Intents.default()
intents.members = True
import random
import re

url = urlparse('mysql://user:pass@localhost:3306/health_manager')

 # コネクションの作成
    conn = mysql.connector.connect(
        host="localhost",
        port='3306'
        user="root",
        password="health_manager428",
        database="health_manager"
    )

    conn.ping(reconnect=True)

    print(conn.is.connected())


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
    print(message.author.id)

    if message.author == client.user:
        return

    if message.content == "!health 😄":
        content = random.choice(random_contents)
        # メッセージが送られてきたチャンネルに送る
        await message.channel.send(content)
        print("%d" % (message.author.id))

        try:
        cur.execute('INSERT INTO health_manager(manager_id,date_create,customer_id) VALUES (default,sysdate,%d)')
        conn.commit()
        except:
        conn.rollback()
        raise

    elif message.content == "!health 😷":

        await message.channel.send('咳メッセージ')
        print("%d" % (message.author.id))

        try:
        cur.execute('INSERT INTO health_manager(manager_id,date_create,customer_id,cough) VALUES (default,sysdate,%d,yes);')
        conn.commit()
        except:
        conn.rollback()
        raise

    elif message.content == "!health 🤐":

        await message.channel.send('息苦しさメッセージ')
        print("%d" % (message.author.id))

        try:
        cur.execute('INSERT INTO health_manager(manager_id,date_create,customer_id,choking) VALUES (default,sysdate,%d,yes);')
        conn.commit()
        except:
        conn.rollback()
        raise

    elif message.content == "!health 🤧":

        await message.channel.send('鼻水メッセージ')
        print("%d" % (message.author.id))

        try:
        cur.execute('INSERT INTO health_manager(manager_id,date_create,customer_id,nose) VALUES (default,sysdate,%d,yes);')
        conn.commit()
        except:
        conn.rollback()
        raise

    elif message.content == "!health 😵":

        await message.channel.send('喉の痛みメッセージ')
        print("%d" % (message.author.id))

        try:
        cur.execute('INSERT INTO health_manager(manager_id,date_create,customer_id,throat) VALUES (default,sysdate,%d,yes);')
        conn.commit()
        except:
        conn.rollback()
        raise

    elif message.content == "!health 👿":

        await message.channel.send('体のだるさメッセージ')
        print("%d" % (message.author.id))

        try:
        cur.execute('INSERT INTO health_manager(manager_id,date_create,customer_id,listness) VALUES (default,sysdate,%d,yes);')
        conn.commit()
        except:
        conn.rollback()
        raise

    elif message.content == "!health 🥶":

        await message.channel.send('腹痛メッセージ')
        print("%d" % (message.author.id))

        try:
        cur.execute('INSERT INTO health_manager(manager_id,date_create,customer_id,stomachache) VALUES (default,sysdate,%d,yes);')
        conn.commit()
        except:
        conn.rollback()
        raise

    elif message.content == "!health 🤢":

        await message.channel.send('下痢メッセージ')
        print("%d" % (message.author.id))

        try:
        cur.execute('INSERT INTO health_manager(manager_id,date_create,customer_id,diarrhea) VALUES (default,sysdate,%d,yes);')
        conn.commit()
        except:
        conn.rollback()
        raise

    elif message.content == "!health 🤕":

        await message.channel.send('頭痛メッセージ')
        print("%d" % (message.author.id))

        try:
        cur.execute('INSERT INTO health_manager(manager_id,date_create,customer_id,headache) VALUES (default,sysdate,%d,yes);')
        conn.commit()
        except:
        conn.rollback()
        raise

    elif message.content == "!health 👅":

        await message.channel.send('味覚異常メッセージ')
        print("%d" % (message.author.id))

        try:
        cur.execute('INSERT INTO health_manager(manager_id,date_create,customer_id,dysgeusia) VALUES (default,sysdate,%d,yes);')
        conn.commit()
        except:
        conn.rollback()
        raise

    elif message.content == "!health 👃":

        await message.channel.send('嗅覚異常メッセージ')
        print("%d" % (message.author.id))

        try:
        cur.execute('INSERT INTO health_manager(manager_id,date_create,customer_id,dysosmia) VALUES (default,sysdate,%d,yes);')
        conn.commit()
        except:
        conn.rollback()
        raise

    if message.content == '!cmdlist':
        await message.channel.send\
        ('``` !health_対応する絵文字 → 現在の体調を絵文字で表す。\
        \n !temp_〇〇.〇 → 現在の体温を記録する。\
        \n !elist → !healthの対応する絵文字を表示する。\
        \n !mylist → 自分が投稿した過去の情報を返す。```')

    if message.content == '!elist':
        await message.channel.send\
        ('``` 異常なし 😄\
        \n 咳 😷\
        \n 鼻水 🤧\
        \n 喉の痛み 😫\
        \n 体のだるさ 😔\
        \n 腹痛 😰\
        \n 下痢 😖\
        \n 頭痛 🤕\
        \n 味覚異常 👅\
        \n 嗅覚異常 👃```')


client.run('')

# gitにあげる前にトークンは消すように