import json, random, datetime, re, config
import mysql.connector as db
from urllib.parse import urlparse
import discord
from discord.ext import commands
from discord.utils import find
from distutils.util import strtobool
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
                (message.author.id, 1, '異常なし')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, normal, remark) VALUES (%s, %s, %s)', health)
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
                (message.author.id, 1, '咳')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, cough, remark) VALUES (%s, %s, %s)', health)
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
                (message.author.id, 1, '息苦しさ')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, choking, remark) VALUES (%s, %s, %s)', health)
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
                (message.author.id, 1, '鼻水')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, nose, remark) VALUES (%s, %s, %s)', health)
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
                (message.author.id, 1, '喉の痛み')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, throat, remark) VALUES (%s, %s, %s)', health)
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
                (message.author.id, 1, '体のだるさ')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, tired, remark) VALUES (%s, %s, %s)', health)
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
                (message.author.id, 1, '腹痛')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, stomachache, remark) VALUES (%s, %s, %s)', health)
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
                (message.author.id, 1, '下痢')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, diarrhea, remark) VALUES (%s, %s, %s)', health)
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
                (message.author.id, 1, '頭痛')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, headache, remark) VALUES (%s, %s, %s)', health)
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
                (message.author.id, 1, '味覚障害')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, dysgeusia, remark) VALUES (%s, %s, %s)', health)
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
                (message.author.id, 1, '嗅覚障害')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into health (customer_id, dysosmia, remark) VALUES (%s, %s, %s)', health)
            conn.commit()
        except:
            conn.rollback()
            raise

    # mylist
    elif message.content == "!mylist":
        await message.channel.send('貴方のこれまでの記録')
        print(message.author.id)
        try:
            mylist = [
                (message.author.id)
            ]
            cur.executemany('select created_at as 登録日時,remark as 症状 from health where customer_id = %s', mylist)
            d = cur.fetchone()
            message.channnel.send(d)
            # cur.executemany('select created_at as 登録日時,temperature as 体温 from temp where customer_id = %s', mylist)
            #d = cur.fetchone()
            # message.channnel.send(d)
        except:
            raise


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
        \n !temp_〇〇.〇 → 現在の体温を記録する。\
        \n !elist → !healthの対応する絵文字を表示する。\
        \n !mylist → 自分が投稿した過去の情報を返す。```')

@bot.command()
async def temp(ctx, arg, message):
    if float(arg) < 35 or float(arg) > 41:
        await ctx.send('エラー \n無効の体温数値です。内容を再確認してください。')
    else:
        await ctx.send('送信できました \n一日に2回以上送った場合は最後のメッセージのみが有効です。')
        try:
            customer = [
                (message.author.id, message.author.display_name)
            ]
            temp = [
                (message.author.id, {arg})
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name) VALUES (%s, %s)', customer)
            cur.executemany('insert into temp (customer_id, temperature) VALUES (%s, %s)', temp)
            conn.commit()
        except:
            conn.rollback()
            raise

bot.run(TOKEN)
cur.close()
conn.close()
