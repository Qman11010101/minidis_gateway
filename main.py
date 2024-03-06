import os

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True # メンバー管理の権限
intents.message_content = True # メッセージの内容を取得する権限

bot = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)

@bot.event
async def on_ready():
    print("ready")


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    await message.reply(message.content)


bot.run(os.environ["crsbot_token"])