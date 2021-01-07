
import discord
import json
import config
import mysql.connector
from mysql.connector import errorcode
from discord.ext import commands
from discord.utils import find
from datetime import date, datetime, timedelta
from distutils.util import strtobool
intents = discord.Intents.default()
intents.members = True

# connect to mysql ----------------------------------------------------------------------------

print("mysqlサーバーに直接: ",end="\n")
try :
    mydb = mysql.connector.connect(
    host=config.hst,
    user=config.usn,
    password=config.psw
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("ユーザー名かパスワードが違っています。")
    else:
        print(err)
else:
    print("OK")

# mycursor = mydb.cursor()
    # mydb.close()
#create database^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
db_name = config.db_name
# create database
def create_db(mycursor, db_name):
    mycursor = mydb.cursor()
    mycursor.execute("show databases like '{}'".format(db_name))
    a = mycursor.fetchone()
    if a is not None:
        print("{} 存在しています。".format(db_name))
        return
    else: 
        try:
            mycursor.execute("create database {}".format(db_name))
            mydb.database = db_name
            mydb.commit()
            print("{} 作成できました。".format(db_name))
        except mysql.connector.Error as err:
            print("データベースの作成の失敗: {}".format(err))
            exit(1)
       
# health_record　データベースを使う
print("データベースのに直接：")
try:
    mycursor = mydb.cursor()
    mycursor.execute("use {}".format(db_name))
except mysql.connector.Error as err:
    print("{} 存在していません。".format(db_name))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        cr_db = input("{} 作成しますか。(はい　/　いいえ)".format(db_name))
        if cr_db == "はい":
            create_db(mycursor, db_name)
            mydb.database = db_name
           
        else:
            print("{} 作成していない。".format(db_name))

    else:
        print(err)
        exit(1)
else:
    print("OK")

# mycursor.execute("delete from temp")
# mydb.commit()
# create table^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# get sql command from create db.json file
with open("create db.json") as json_file:
    # mycursor = mydb.cursor()
    table = json.load(json_file)
    for table_name in table:
        sql_str = ""
        for element in table[table_name]:
            sql_str += element
        try:
            print("{} テーブルの作成：".format(table_name))
            mycursor.execute(sql_str)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("{} テーブルが存在しています。".format(table_name))
            else:
                print(err)
        else:
            print("OK")

mycursor.close()
# mydb.close()
# insert database-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^--^-^-^-^-^-^-^-^-^-^-^-^-^-^-
# add database

add_customer = ("insert into customer (customer_id, customer_name, admin_flag, remark) values (%s, %s, %s, %s)")
add_temp = ("insert into temp (created_at, customer_id, temperature, remark) values (%s, %s, %s, %s)")
add_health = ("insert into health (managed_id, created_at, customer_id, fine, cough, choking, nose, throat, tired, stomachache, diarrhea, headache, dysgeusia, dysosmia, remark) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s)")

# 自分のBotのアクセストークン
TOKEN = config.token_id
# client = discord.Client()
#コマンドの最初の文字を指定し
bot = commands.Bot(command_prefix = '!', intents=intents)
#自分のチャンネルID
# CHANNEL_ID = 776673735380828161
# set admin------------------=========================================================
# 761114010640187403
def set_admin(id):
    mycursor = mydb.cursor()
    mycursor.execute("update customer set admin_flag = True where customer_id = {}".format(id))
    mydb.commit()
    print("{} をadmin_flag = Trueにしました。".format(id))
# set_admin(761114010640187403)
#  function check existence customer_id +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def check_id(id):
    mycursor = mydb.cursor()
    mycursor.execute("select * from customer where customer_id = {}".format(id))
    mycursor.fetchall()
    rc = mycursor.rowcount
    return rc
# サーバーのメンバーをcustomerテーブルに挿入する+++++++++++++++++++++++++++++++++++++++++++++++++++
data_customers = []
@bot.command()
async def member_record(ctx):
    # print(ctx.author.id)
    mycursor = mydb.cursor()
    try: 
        mycursor.execute("select * from customer where customer_id = {} and admin_flag = True".format(ctx.author.id))
        mycursor.fetchall()
        check_admin = mycursor.rowcount
    except mysql.connector.Error as err:
        print(err)
    else: 
        embed = discord.Embed(title='メンバーをデータベースに挿入', color=0xcc00c0)
        if check_admin != 0:
            mems = ctx.guild.members
            for i in mems:
                if not check_id(i.id):
                    data_customers.append((i.id, i.name, False, ""))
            # print("all members are existing")
            # return
            mycursor.executemany(add_customer, data_customers)
            mydb.commit()
            mycursor.close()
            # mydb.close()
            embed.add_field(name='OK', value='メンバーをデータベースに挿入完了')
            await ctx.send(embed = embed)
        else:
            embed.add_field(name='エラー', value='このコマンドは制限されています。')
            await ctx.send(embed = embed)
    

#botが起動の時の挨拶^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
@bot.event
async def on_ready():
    print("bot is ready")

#サーバーは入るとき、初期の挨拶と使い方-------------------------------------------------------
@bot.event
async def on_guild_join(guild):
    embed = discord.Embed(title='こんにちは！、Heath Managerです。\nよろしくお願いいたします。', color=0xdc2502)
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embed.add_field(name='使い始めるのに!cmdlistコマンドを実行してください。', value='©TN31 Enjoy')
        await channel.send(embed = embed)
        break

# 新規メンバーを歓迎する関数\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


@bot.event
async def on_member_join(member):
    embed = discord.Embed(title=f"{member.name} Health Managerへようこそ", description=f"{member.id}", color=0xdc2502)
    if check_id(member.id) == 0:
        mycursor.execute(add_customer, (member.id, member.name, False, ""))
        mydb.commit()
        mycursor.close()
        print(f"{member.name} added into server")
    else:
        print(f"{member.name} are existing")
        return

    await member.send(embed=embed)

# !cmdlist command 作成し-----------------------------------------------------------
# jsonファイルから読み込み
with open('help.json', encoding='utf-8') as help_manual:
    help_data = json.load(help_manual)
@bot.command()
async def cmdlist(ctx):
    embed = discord.Embed(title='利用方法をご案内いたします。', color=0xcc00c0, timestamp= ctx.message.created_at)
    for cmd in help_data["help_manual"]:
        embed.add_field(name=f'コマンド名: {cmd["name"]}', value=f'説明:\n{cmd["describe"]}', inline=False)
    await ctx.send(embed=embed)

#!elist command 作成し------------------------------------------------------------------

#elist.txt というファイルを開く
with open("elist.json", encoding="utf-8") as elist_json:
    elist_data = json.load(elist_json)

@bot.command()
async def elist(ctx):
    # await ctx.send("コマンド：!" + str(ctx.command) )
    embed = discord.Embed(title="対応する絵文字", color=0xcc00c0, timestamp= ctx.message.created_at)
    for e in elist_data["elist"]:
        embed.add_field(name=f'{e["icon"]}', value=f'{e["describe"]}',  inline=True)
    await ctx.send(embed = embed)

# temp command 作成し---------------------------------------------------------------------------


@bot.command()
async def temp(ctx, arg):
    if float(arg) < 35 or float(arg) > 41:
        embed = discord.Embed(title="体温入力", color=0xdc2502)
        embed.add_field(name='エラー ', value=f'{arg}は無効の体温数値です。内容を再確認してください。')
        await ctx.send(embed = embed)
    else:
        embed = discord.Embed(title="体温入力", color=0x3cd070)
        embed.add_field(name='送信できました。', value='一日に2回以上送った場合は最後のメッセージのみが有効です。')
        # 1日に何回目かチェック
        mycursor = mydb.cursor()
        mycursor.execute("select * from temp where created_at = '{}' and customer_id = {}".format(datetime.now().date(), ctx.author.id))
        mycursor.fetchall()
        check = mycursor.rowcount
        # 1回目場合　insert into temp テーブル
        if check == 0:
            mycursor.execute("alter table temp auto_increment = 1")
            data_temp = (datetime.now().date(), ctx.author.id, arg, "")
            mycursor.execute(add_temp, data_temp)
            mydb.commit()
            # mycursor.close()
        # 2回目以上場合　update into temp with same customer id
        else:
            mycursor.execute("update temp set temperature = {} where created_at = '{}' and customer_id = {}".format(arg, datetime.now().date(), ctx.author.id))
            mydb.commit()
        mycursor.close()
        await ctx.send(embed = embed)

# temp別の書き方--------------------
# @bot.command()
# async def temp(ctx, arg):
#     if float(arg) < 35 or float(arg) > 41:
#         await ctx.send('エラー \n無効の体温数値です。内容を再確認してください。')
#     else:
#         await ctx.send('送信できました \n一日に2回以上送った場合は最後のメッセージのみが有効です。')

# mylist^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
@bot.command()
async def mylist(ctx, arg = None):
    embed = discord.Embed(title="過去情報", description=f"{ctx.author.name} さんが投稿した情報です。", color=0xa3a3a3, timestamp=ctx.message.created_at)
    if arg is None:
        mycursor = mydb.cursor()
        sql_query = "select t.created_at, t.temperature, if(h.fine > 0, '😄 異常なし', ''), if(h.cough > 0, '😷咳', ''), if(h.choking > 0, '🤐息苦しさ', ''), if(h.nose > 0, '🤧鼻水', ''), if(h.throat > 0, '😫喉の痛み', ''), if(h.tired > 0, '😔体のだるさ', ''), if(h.stomachache > 0, '😰腹痛', ''), if(h.diarrhea > 0, '😖下痢', ''), if(h.headache > 0, '🤕頭痛', ''), if(h.dysgeusia > 0, '👅味覚異常', ''), if(h.dysosmia > 0, '👃嗅覚異常', '') from temp as t inner join health as h on t.customer_id = {} and t.created_at = h.created_at order by t.created_at".format(ctx.author.id)
        # sql_query = "select created_at, temperature from temp where customer_id = {}".format(ctx.author.id)
        mycursor.execute(sql_query)
        mlist = mycursor.fetchall()
        # print(mlist)
        for x in mlist:
            # print(
            embed.add_field(name=f'{x[0]}', value=f'体温：{x[1]} || 体調： {x[2]} {x[3]} {x[4]} {x[5]} {x[6]} {x[7]} {x[8]} {x[9]} {x[10]} {x[11]} {x[12]}', inline=False)
        await ctx.send(embed = embed)
    else:
        print("not none")

# health emoji^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# function check emoji in elist data?? 

@bot.command()
async def health(ctx, *arg):
    embed = discord.Embed(title="当該絵文字", color=0x3cd070, timestamp=ctx.message.created_at)
    status_dict = {"U+1F604":"0", "U+1F637":"0", "U+1F910":"0", "U+1F927":"0", "U+1F62B":"0", "U+1F61E":"0", "U+1F630":"0", "U+1F616":"0", "U+1F915":"0", "U+1F445":"0", "U+1F443":"0"}
    # print(status_dict)
    for x in arg:
        # x_of_unicode = 'U+{:X}'.format(ord(x))
        x_of_unicode = f'U+{ord(x):X}'
        # print(type(status_dict[x_of_unicode]))
        for k in elist_data["elist"]:
            if x_of_unicode == k["unicode"]:
                embed.add_field(name=f"{k['describe']}", value=f"{x}", inline=True)
                status_dict[x_of_unicode] = 1
                # print(type(status_dict[x_of_unicode]))
    embed.add_field(name="送信できました。", value="一日に２回以上送った場合は最後のメッセージのみが有効です。", inline=False)
    mycursor = mydb.cursor()
    mycursor.execute("select * from health where customer_id = {} and created_at = '{}'".format(ctx.author.id, datetime.now().date()))
    mycursor.fetchall()
    check_exist = mycursor.rowcount
    if check_exist == 0:
        mycursor.execute("alter table health auto_increment = 1")
        add_health = "insert into health (created_at, customer_id, fine, cough, choking, nose, throat, tired, stomachache, diarrhea, headache, dysgeusia, dysosmia, remark) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data_health = (datetime.now().date(), ctx.author.id, int(status_dict["U+1F604"]), int(status_dict["U+1F637"]), int(status_dict["U+1F910"]), int(status_dict["U+1F927"]), int(status_dict["U+1F62B"]), int(status_dict["U+1F61E"]), int(status_dict["U+1F630"]), int(status_dict["U+1F616"]), int(status_dict["U+1F915"]), int(status_dict["U+1F445"]), int(status_dict["U+1F443"]), " ")
        mycursor.execute(add_health, data_health)
        mydb.commit()
    else:
        add_health = "update health set fine = %s, cough = %s, choking = %s, nose = %s, throat = %s, tired = %s, stomachache = %s, diarrhea = %s, headache = %s, dysgeusia = %s, dysosmia = %s where customer_id = {} and created_at = '{}'".format(ctx.author.id, datetime.now().date())
        data_health = (int(status_dict["U+1F604"]), int(status_dict["U+1F637"]), int(status_dict["U+1F910"]), int(status_dict["U+1F927"]), int(status_dict["U+1F62B"]), int(status_dict["U+1F61E"]), int(status_dict["U+1F630"]), int(status_dict["U+1F616"]), int(status_dict["U+1F915"]), int(status_dict["U+1F445"]), int(status_dict["U+1F443"]))
        mycursor.execute(add_health, data_health)
        mydb.commit()
        
    await ctx.send(embed = embed)
    mycursor.close()
            
            



#health manager呼ばれるとき---------------------------------------------------------------------
# 返信する非同期関数を定義
async def reply(message):
    reply = f'{message.author.mention} さん。ご用件は何でしょうか？\n使い方について!cmdlistコマンドを実行してください。' # 返信メッセージの作成
    await message.channel.send(reply) # 返信メッセージを送信
    await bot.process_commands(reply)

# 発言時に実行されるイベントハンドラを定義
@bot.event
async def on_message(message):
    if bot.user in message.mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行
    await bot.process_commands(message)
# @bot.event
# async def on_message(message):
#     await message.channel.send("hello")
bot.run(TOKEN)