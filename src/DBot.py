import discord
import json
import random
import re
import mysql.connector as db
import config
from urllib.parse import urlparse

from discord.ext import commands
from discord.utils import find
intents = discord.Intents.all()
intents.members = True

 # コネクションの作成
conn = db.connect(
    host = config.HST,
    port = config.PRT,
    user = config.USN,
    password = config.PSW,
    database = config.DBS
)
    
#接続再試行
conn.ping(reconnect=True)
#接続確認
print(conn.is_connected())

link_regex = re.compile(
    r'^https?://(?:(ptb|canary)\.)?discordapp\.com/channels/'
    r'(?:([0-9]{15,21})|(@me))'
    r'/(?P<channel_id>[0-9]{15,21})/(?P<message_id>[0-9]{15,21})/?$'
)

#Bot起動
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
            cur.execute('INSERT INTO health_manager(manager_id, date_create, customer_id) VALUES (default,sysdate,%d)')
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
        ('```異常なし 😄\
        \n 咳 😷\
        \n 鼻水 🤧\
        \n 喉の痛み 😫\
        \n 体のだるさ 😔\
        \n 腹痛 😰\
        \n 下痢 😖\
        \n 頭痛 🤕\
        \n 味覚異常 👅\
        \n 嗅覚異常 👃```')


client.run(config.TKN)
conn.close()
