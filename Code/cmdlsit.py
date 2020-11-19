# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = ''

# 接続に必要なオブジェクトを生成
client = discord.Client()

#BOTのサーバー加入  時に流すメッセージ用
gjoin = discord.on_guild_join()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
# サーバー加入時の自動メッセージ
#@client.event
#async def on_guild_join():
 #   channel = client.get_channel(12324234183172)
  #  await channel.send('!cmdlistでコマンドリストが見れます。')


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「!cmdlist」と発言したら「対応するコマンド」が返る処理
    if message.content == '!cmdlist':
        await message.channel.send\
        ('``` !health_対応する絵文字 → 現在の体調を絵文字で表す。\
        \n !temp_〇〇.〇 → 現在の体温を記録する。\
        \n !elist → !healthの対応する絵文字を表示する。\
        \n !mylist → 自分が投稿した過去の情報を返す。```')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)