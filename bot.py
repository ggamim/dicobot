import discord
import os

from discord.ext import commands
bot = commands.Bot(command_prefix='!')
TOKEN = 'access_token'

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('생각 안'))
    print('실행중')

@bot.event
async def on_message(msg):
    if msg.author.bot: return None
    await bot.process_commands(msg)

@bot.command()
async def 놀자에요(ctx):
    await  ctx.channel.send('https://cdn.discordapp.com/attachments/933336072082034738/933336198414491668/KakaoTalk_20211216_170411961.jpg')

@bot.command()
async def 인삼(ctx):
    await  ctx.channel.send('https://cdn.discordapp.com/attachments/933336072082034738/933336225438375957/KakaoTalk_20220119_211810662_01.jpg')

@bot.command()
async def 몰루(ctx):
    await  ctx.channel.send('https://cdn.discordapp.com/attachments/933336072082034738/933336265502375966/KakaoTalk_20220119_211810662_10.png')

@bot.command()
async def 줘(ctx):
    await  ctx.channel.send('https://cdn.discordapp.com/attachments/933336072082034738/933336355667341422/KakaoTalk_20220119_211854882_01.jpg')

@bot.command()
async def 안줘(ctx):
    await  ctx.channel.send('https://cdn.discordapp.com/attachments/933336072082034738/933336355570855997/KakaoTalk_20220119_211854882_02.jpg')

@bot.command()
async def 크크(ctx):
    await  ctx.channel.send('https://cdn.discordapp.com/attachments/933336072082034738/934408524329525278/01F1E9A3-4008-4866-9E1E-36F8E05AE82A.png')

@bot.command()
async def 불편(ctx):
    await  ctx.channel.send('https://cdn.discordapp.com/attachments/933336072082034738/948969928168452156/i15930144628.png')

@bot.command()
async def 편안(ctx):
    await  ctx.channel.send('https://cdn.discordapp.com/attachments/933336072082034738/948969928386551868/i14918434366.png')

@bot.command()
async def 엄지(ctx):
    await  ctx.channel.send('https://cdn.discordapp.com/attachments/963303414723399690/963304112630411324/01_coconut.gif')

@bot.command()
async def 헤으응(ctx):
    await  ctx.channel.send('https://cdn.discordapp.com/attachments/963303414723399690/963304213440520212/05_coconut.gif')

@bot.command()
async def 못참지(ctx):
    await  ctx.channel.send('https://cdn.discordapp.com/attachments/963303414723399690/963304388192002088/28_2_.gif')

@bot.command()
async def 눈나(ctx):
    await  ctx.channel.send('https://cdn.discordapp.com/attachments/963303414723399690/963304515862421564/10__100.gif')

@bot.command()
async def 제발(ctx):
    await  ctx.channel.send('https://cdn.discordapp.com/attachments/963303414723399690/963304572896571392/04_.gif')

@bot.command()
async def 팝콘(ctx):
    await  ctx.channel.send('https://cdn.discordapp.com/attachments/963303414723399690/963305142948626442/01.gif')

















access_token = os.environ['BOT_TOKEN']
bot.run(TOKEN)
