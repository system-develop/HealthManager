import discord
import sqlite3
from discord.ext import commands

TOKEN = ''
client = discord.Client()


# 起動時に動作する
@client.event
async def on_ready():
    print('ログインしました')
    print('等BOTの使い方に関しましては、コマンド(/help)を参照')

#コマンド処理
@client.event
async def on_message(message):
     if not message.content.startswith('!'): return
     if message.content.startswith('!help'):
        return await body_help(message)
    if message.content.startswith('!temp'):
        return await body_temp(message)
    if message.content.startswith('!list'):
        return await body_list(message)

async def body_help(message):
    return await client.send_message(
        message.channel,
        """
        !help : コマンドを参照する
        !temp : 体温を記録 [!temp 数値]
        !lest : 記録した体温を表示[!list 名前 日付1 日付2]
        """
    )

async def body_temp(message):
    body_message = message.content.split(" ")
    if len(body_temp) < 35:
        return await client.send_message(
            message.channel,
            "体温が低過ぎます。入力可能な体温は35-41までです。"
        )
    body_content = message.content.sqlit(" ")
    if len(body_content) > 41:
        return await client.send_message(
            message.channel,
            "体温が高過ぎます。入力可能な体温は35-41までです。"
        )
    return await client.send_message(
        message.channel,
        "登録しました。"
    )


# Botの起動とDiscordサーバーへの接続
client.run('TOKEN')
