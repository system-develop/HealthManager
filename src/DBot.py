import json, random, re, config
import mysql.connector as db
from urllib.parse import urlparse
import discord
from discord.ext import commands
from discord.utils import find
from distutils.util import strtobool
from datetime import date, datetime, timedelta
intents = discord.Intents.default()
intents.members = True

 # コネクションの作成
conn = db.connect(
    host=config.HST,
    port=config.PRT,
    user=config.USN,
    password=config.PSW,
    database=config.DBS
)

#接続再試行
conn.ping(reconnect=True)
#接続確認
print(conn.is_connected())
#省略
cur = conn.cursor()

link_regex = re.compile(
    r'^https?://(?:(ptb|canary)\.)?discordapp\.com/channels/'
    r'(?:([0-9]{15,21})|(@me))'
    r'/(?P<channel_id>[0-9]{15,21})/(?P<message_id>[0-9]{15,21})/?$'
)

TOKEN = config.TKN

bot = commands.Bot(command_prefix='!', intents=intents)

random_contents = [
    "元気そうで何よりです。その調子で健康を維持しましょう",
    "今の時期、健康第一が何よりモットーです。その心がけをこれからも",
    "(｀･ω･´)",
]

@bot.event
async def on_message(message):

    await bot.process_commands(message)

    if message.content == "!health 😄":
        content = random.choice(random_contents)
        await message.channel.send(content)
        print(message.author.id)

        try:
            customer = [
                (message.author.id, message.author.display_name)
            ]
            health = [
                (message.author.id, 1)
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, normal) VALUES (%s, %s)', health)
            conn.commit()

        except:
            conn.rollback()
            raise

    elif message.content == "!health 😷":
        await message.channel.send('風邪を引いてしまいましたか？マスクの着用を徹底すると共に、うがいを定期的に行うようにしましょう。')
        print(message.author.id)
        try:
            customer = [
                (message.author.id, message.author.display_name)
            ]
            health = [
                (message.author.id, 1)
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, cough) VALUES (%s, %s)', health)
            conn.commit()
        except:
            conn.rollback()
            raise

    elif message.content == "!health 🤐":
        await message.channel.send('無理はせず、しんどいと感じたらすぐに申し出て早退するなど対処をとって下さい。')
        print(message.author.id)
        try:
            customer = [
                (message.author.id, message.author.display_name)
            ]
            health = [
                (message.author.id, 1)
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, choking) VALUES (%s, %s)', health)
            conn.commit()
        except:
            conn.rollback()
            raise

    elif message.content == "!health 🤧":
        await message.channel.send('気温の変化に追いつけていますか？衣類や布団などをその時の気温に合わせて調節すると共に、ひどいと感じたときは耳鼻科を受診するなどして下さい')
        print(message.author.id)
        try:
            customer = [
                (message.author.id, message.author.display_name)
            ]
            health = [
                (message.author.id, 1)
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, nose) VALUES (%s, %s)', health)
            conn.commit()
        except:
            conn.rollback()
            raise

    elif message.content == "!health 😵":
        await message.channel.send('喉を酷使した覚えがありますか？うがいを徹底すると共に、今後の体調に注意して下さい。')
        print(message.author.id)
        try:
            customer = [
                (message.author.id, message.author.display_name)
            ]
            health = [
                (message.author.id, 1)
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, throat) VALUES (%s, %s)', health)
            conn.commit()
        except:
            conn.rollback()
            raise

    elif message.content == "!health 👿":
        await message.channel.send('無理はせず、しんどいと感じたらすぐに申し出て早退するなど対処をとって下さい。')
        print(message.author.id)
        try:
            customer = [
                (message.author.id, message.author.display_name)
            ]
            health = [
                (message.author.id, 1)
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, tired) VALUES (%s, %s)', health)
            conn.commit()
        except:
            conn.rollback()
            raise

    elif message.content == "!health 🥶":
        await message.channel.send('お腹を冷やしていませんか？冬は勿論、夏もお腹に布団を掛けて寝ないと腹痛の元になります。')
        print(message.author.id)
        try:
            customer = [
                (message.author.id, message.author.display_name)
            ]
            health = [
                (message.author.id, 1)
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, stomachache) VALUES (%s, %s)', health)
            conn.commit()
        except:
            conn.rollback()
            raise

    elif message.content == "!health 🤢":
        await message.channel.send('できる限り消化の良いものを摂って下さい。また、使用した後の便器はペーパーで拭くなどして、消毒を行って下さい')
        print(message.author.id)
        try:
            customer = [
                (message.author.id, message.author.display_name)
            ]
            health = [
                (message.author.id, 1)
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, diarrhea) VALUES (%s, %s)', health)
            conn.commit()
        except:
            conn.rollback()
            raise

    elif message.content == "!health 🤕":
        await message.channel.send('無理はせず、しんどいと感じたらすぐに申し出て早退するなど対処をとって下さい。')
        print(message.author.id)
        try:
            customer = [
                (message.author.id, message.author.display_name)
            ]
            health = [
                (message.author.id, 1)
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, headache) VALUES (%s, %s)', health)
            conn.commit()
        except:
            conn.rollback()
            raise

    elif message.content == "!health 👅":
        await message.channel.send('担任の先生または保健所に相談して下さい。また、マスクや手洗いうがいなど、対策はいつも以上に徹底するようお願いします。')
        print(message.author.id)
        try:
            customer = [
                (message.author.id, message.author.display_name)
            ]
            health = [
                (message.author.id, 1)
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, dysgeusia) VALUES (%s, %s)', health)
            conn.commit()
        except:
            conn.rollback()
            raise

    elif message.content == "!health 👃":
        await message.channel.send('担任の先生または保健所に相談して下さい。また、マスクや手洗いうがいなど、対策はいつも以上に徹底するようお願いします。')
        print(message.author.id)
        try:
            customer = [
                (message.author.id, message.author.display_name)
            ]
            health = [
                (message.author.id, 1)
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, dysosmia) VALUES (%s, %s)', health)
            conn.commit()
        except:
            conn.rollback()
            raise

@bot.command()
async def mylist(message):
    await message.channel.send\
    ('``` !mylist_health → 自分が投稿した体調の過去情報を返す。\
        \n !mylist_temp → 自分が投稿した体温の過去情報を返す。```')

@bot.command()
async def mylist_health(ctx,arg = None):
    embed = discord.Embed(title="体調の過去情報", description=f"{ctx.author.name} さんが投稿した情報です。", color=0xa3a3a3)
    if arg is None:
        #sql_query = "select created_at,remark from health where customer_id = {}".format(ctx.author.id)
        sql_query = "select created_at, if(normal > 0, '😄 異常なし', ''), if(cough > 0, '😷咳', ''), if(choking > 0, '🤐息苦しさ', ''), if(nose > 0, '🤧鼻水', ''), if(throat > 0, '😫喉の痛み', ''), if(tired > 0, '😔体のだるさ', ''), if(stomachache > 0, '😰腹痛', ''), if(diarrhea > 0, '😖下痢', ''), if(headache > 0, '🤕頭痛', ''), if(dysgeusia > 0, '👅味覚異常', ''), if(dysosmia > 0, '👃嗅覚異常', '') from health where customer_id = {} order by created_at limit 100".format(ctx.author.id)
        cur.execute(sql_query)
        hlist = cur.fetchmany()
        for x in hlist:
            embed.add_field(name='健康状態',value=f'{x[0]}:{x[1]}',inline=False)
        await ctx.send(embed=embed)
    else:
        print("not none")

@bot.command()
async def mylist_temp(ctx,arg = None):
    embed = discord.Embed(title="体温の過去情報", description=f"{ctx.author.name} さんが投稿した情報です。", color=0xa3a3a3)
    if arg is None:
        sql_query = "select created_at,temperature from temp where customer_id = {}order by created_at limit 100".format(ctx.author.id)
        cur.execute(sql_query)
        tlist = cur.fetchmany()
        for x in tlist:
            embed.add_field(name='体温状態',value=f'{x[0]}:{x[1]}',inline=False)
        await ctx.send(embed=embed)
    else:
        print("not none")

@bot.command()
async def elist(message):
    await message.channel.send\
        ('```異常なし 😄\
        \n 咳 😷\
        \n 息苦しさ 🤐\
        \n 鼻水 🤧\
        \n 喉の痛み 😵\
        \n 体のだるさ 👿\
        \n 腹痛 🥶\
        \n 下痢 🤢\
        \n 頭痛 🤕\
        \n 味覚異常 👅\
        \n 嗅覚異常 👃```')

@bot.command()
async def cmdlist(message):
    await message.channel.send\
        ('``` !health_対応する絵文字 → 現在の体調を絵文字で表す。\
        \n !temp_〇〇.〇 → 現在の体温を記録する。(初めて入力する人は、!healthから入力を始めて下さい)\
        \n !elist → !healthの対応する絵文字を表示する。\
        \n !mylist_health → 自分が投稿した体調の過去情報を返す。\
        \n !mylist_temp → 自分が投稿した体温の過去情報を返す。```')

@bot.command()
async def temp(ctx, arg):
    if float(arg) < 35 or float(arg) > 41:
        embed = discord.Embed(title="体温入力", color=0xdc2502)
        embed.add_field(name='エラー ', value=f'{arg}は無効の体温数値です。内容を再確認してください。')
        await ctx.send(embed = embed)
    else:
        embed = discord.Embed(title="体温入力", color=0x3cd070)
        embed.add_field(name='送信できました。', value='もし発熱がある場合、登校は控えるようお願いします')

        cur.execute("select * from temp where customer_id = {}".format(ctx.author.id))
        cur.fetchall()
        cur.execute("insert into temp (customer_id, temperature) VALUES ({}, {})".format(ctx.author.id,arg))
        conn.commit()
        await ctx.send(embed = embed)

bot.run(TOKEN)
cur.close()
conn.close()
