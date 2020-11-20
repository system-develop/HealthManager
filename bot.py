
import discord
import json
import mysql.connector
from discord.ext import commands
from discord.utils import find
intents = discord.Intents.default()
intents.members = True
# connect to database
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Re2devils",
#   database="discord_botDb"
# )

# 自分のBotのアクセストークン
TOKEN = ''
# client = discord.Client()
#コマンドの最初の文字を指定し
bot = commands.Bot(command_prefix = '!')  
#自分のチャンネルID
# CHANNEL_ID = 776673735380828161 

#挨拶関数
# async def greet():
#     channel = bot.get_channel(CHANNEL_ID)
#     await channel.send('おはよう！')
#botが起動の時の挨拶
# @bot.event 
# async def on_ready():
#     await greet()

#サーバーは入るとき、初期の挨拶と使い方-------------------------------------------------------
# @bot.event
# async def on_guild_join(guild):
#     embed = discord.Embed(title='こんにちは！、Heath Managerです。\nよろしくお願いいたします。', color=0xdc2502)
#     for channel in guild.text_channels:
#         if channel.permissions_for(guild.me).send_messages:
#             embed.add_field(name='使い始めるのに!cmdlistコマンドを実行してください。', value='©TN31 Enjoy')
#         await channel.send(embed = embed)
#         break

# 新規メンバーを歓迎する関数
# @bot.event
# async def on_member_join(member):
#     embed = discord.Embed(title="ようこそ", color=0xdc2502)
#     # await member.send(f'{member.mention}さん、ようこそ')
#     await member.send(embed=embed)

#!cmdlist command 作成し-----------------------------------------------------------
#jsonファイルから読み込み
# with open('help.json', encoding='utf-8') as help_manual:
#     data = json.load(help_manual)
# @bot.command()
# async def cmdlist(ctx):
#     embed = discord.Embed(title='案内いたします。', color=0xcc00c0)
#     for cmd in data["help_manual"]:
#         embed.add_field(name=f'コマンド名: {cmd["name"]}', value=f'説明:\n{cmd["describe"]}', inline=False)
#     await ctx.send(embed=embed)

#!elist command 作成し------------------------------------------------------------------

#elist.txt というファイルを開く
# get_elist = open("elist.txt", encoding="utf-8", errors="ignore")
#elist.txtのデータを保存するために空くリストを定義し
# elists = []
#elistsリストにデータを一つずつ挿入し
# for line in get_elist:
#     word = line.strip()
#     elists.append(word)

# @bot.command()
# async def elist(ctx):
#     # await ctx.send("コマンド：!" + str(ctx.command) )   
#     embed = discord.Embed(title="対応する絵文字", color=0xdc2502, timestamp= ctx.message.created_at)
#     for word in elists:
#         embed.add_field(name=f'{elists.index(word) + 1}', value=f'{word}',  inline=True)
#     await ctx.send(embed = embed)

# temp command 作成し---------------------------------------------------------------------------
@bot.command()
async def temp(ctx, arg):
    
    if float(arg) < 35 or float(arg) > 41:
        # print("aacc")
        embed = discord.Embed(title="体温入力", color=0xdc2502)
        embed.add_field(name='エラー ', value=f'{arg}は無効の体温数値です。内容を再確認してください。')
        await ctx.send(embed = embed)
    else:
        embed = discord.Embed(title="体温入力", color=0x3cd070)
        embed.add_field(name='送信できました。', value='一日に2回以上送った場合は最後のメッセージのみが有効です。')
        await ctx.send(embed = embed)

# temp別の書き方--------------------
# @bot.command()
# async def temp(ctx, arg):
#     if float(arg) < 35 or float(arg) > 41:
#         await ctx.send('エラー \n無効の体温数値です。内容を再確認してください。')
#     else:
#         await ctx.send('送信できました \n一日に2回以上送った場合は最後のメッセージのみが有効です。')

#health manager呼ばれるとき---------------------------------------------------------------------
# 返信する非同期関数を定義
# async def reply(message):
#     reply = f'{message.author.mention} 呼びましたか？\n使い方を忘れる場合は!cmdlistコマンドを実行してください。' # 返信メッセージの作成
#     await message.channel.send(reply) # 返信メッセージを送信
#     # await bot.process_commands(reply)

# # 発言時に実行されるイベントハンドラを定義
# @bot.event
# async def on_message(message):
#     if bot.user in message.mentions: # 話しかけられたかの判定
#         await reply(message) # 返信する非同期関数を実行
#     await bot.process_commands(message)
bot.run(TOKEN)