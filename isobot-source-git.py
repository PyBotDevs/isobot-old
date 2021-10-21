### Modules ###
import os
import time
import math
import random
import pickle
import os.path
import discord
import datetime
import praw
import requests
from time import sleep
from random import randint
from discord.ext import commands
from discord.ext.commands import *
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
### Modules end ###

### Startup/variables ###
ids = [
    738290097170153472,
    796097512355266602,
    821635924039434261,
    852586561610055699,
    816941773032390676,
    705462972415213588
]
bad = [
    'fuck',
    'asshole',
    'nigga',
    'motherfucker',
    'fuckyou',
    'bitch',
    'cum',
    'shit',
    's‌hit', ### Contains special character ###
    'shi‌t',
    'dick',
    'pussy',
    'boob',
    'FUCΚ', ### Greek K ###
    'Fu‌ck',
    'fucκ', # Greek #
    'shiτ', # Greek again .-. #,
    'sex',
    'penis'
]
whitelist = [
    'document',
    'cucumber'
]
console = False
log = True
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
print('Enable logging?')
print('=====================')
print('Default is True')
print('1. Yes (recommended)')
print('2. No')
print('=====================')
con = int(input('Input: '))
if con == 1:
    pass
elif con == 2:
    log = not log
intents = discord.Intents.all()
errHandlerVer = 'v2.3'
botVer = 'v4.0.1'
currencyVer = 'v1.1'
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
owner = 'notsniped#6776'
homedir = os.path.expanduser("~")
client = commands.Bot(command_prefix=";", intents=intents)
slash = SlashCommand(client, sync_commands=True)
global startTime
startTime = time.time()
client.remove_command('help')
reddit = praw.Reddit(client_id='_pazwWZHi9JldA',
                     client_secret='1tq1HM7UMEGIro6LlwtlmQYJ1jB4vQ',
                     user_agent='idk', check_for_async=False)
### Startup/variables end ###

### Command variables ###
beg = True
fish = True
work = True
daily = True
monthly = True
weekly = True
snipe = True
edit = True
shop = True
inventory = True
buy = True
networth = True
lbin = True
ah = True
theme_color_old = 0x8124af # replace 'theme_color_old' with 'theme_color' on November 1 2021
theme_color = 0xeb6123 # Halloween special color ONLY
### Functions and classes ###
if os.name == 'nt':
    data_filename = homedir + "\\database.pickle"
else:
    data_filename = "/sdcard/Download/database.pickle"


class Data:
    def __init__(self, wallet, bank, xp, level, op):
        self.wallet = wallet
        self.bank = bank
        self.xp = xp
        self.level = level
        self.op = op

class colors:
    cyan = '\033[96m'
    red = '\033[91m'
    green = '\033[92m'
    end = '\033[0m'

def load_data():
    if os.path.isfile(data_filename):
        with open(data_filename, "rb") as file:
            return pickle.load(file)
    else:
        return dict()

def load_member_data(member_ID):
    data = load_data()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0)

    return data[member_ID]

def save_member_data(member_ID, member_data):
    data = load_data()

    data[member_ID] = member_data

    with open(data_filename, "wb") as file:
        pickle.dump(data, file)

def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")

# def consoleFunc():
#     while True:
#         cmd = input(f'{colors.cyan}[{colors.end}{colors.green}Console{colors.end}{colors.cyan}]>{colors.end}')
#         if cmd == 'shutdown':
#             conf = input('Are you sure? (y/n)')
#             if conf == 'y':
#                 # raise SystemExit
#                 exit()
#             elif conf == 'n':
#                 pass
#             else:
#                 print(f'What is {conf}')
#         elif cmd == 'clear':
#             os.system('cls')
#         elif cmd == 'viewLog':
#             os.system('notepad F:\\bot\\logs\\log.txt')
#         elif cmd == 'clearLog':
#             conf = input('Are you sure (y/n)')
#             if conf == 'y':
#                 os.system('del F:\\bot\\logs\\log.txt -f')
#                 print('Log file deleted')
#             elif conf == 'n':
#                 pass
#             else:
#                 print(f'What is {conf}')

### Functions and classes end ###

currency = True

## Events ###
@client.event
async def on_ready():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="sussy chats (;help)"))
    print('Bot is online')
    print('==================')
    print('------------------')
    print('Bot Info')
    print(f'Bot version: {colors.cyan}{botVer}{colors.end}')
    print(f'Error handler version: {colors.cyan}{errHandlerVer}{colors.end}')
    print(f'Currency system version: {colors.cyan}{currencyVer}{colors.end}')
    print(f'Username: {colors.green}{client.user.name}{colors.end}\nId: {colors.green}{client.user.id}{colors.end}\nDeveloper name: {colors.green}{owner}{colors.end}')
    print('==================')
    print('Server list:')
    print('------------------')
    for guild in client.guilds:
        guild_owner = client.get_user(guild.owner.id)
        print(f'Server name: {colors.green}{guild.name}{colors.end}\nServer id: {colors.cyan}{guild.id}{colors.end}\nMember count: {colors.green}{guild.member_count}{colors.end}\nServer owner: {colors.cyan}{guild_owner}{colors.end}')
        print('----------------')
    print('==================')
    print('Bot config:')
    print('------------------')
    print(f'Ping: {round(client.latency * 1000)}')
    print('------------------')
    boot = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    print(f'Startup time: {boot}')
    print('------------------')
    print(f'Server count: {str(len(client.guilds))}')
    print('------------------')
    if bool(currency) == True:
        print(f'Currency: {colors.green}{currency}{colors.end}')
    else:
        print(f'Currency: {colors.red}{currency}{colors.end}')
    print('------------------')
    if bool(log) == True:
        print(f'Logging: {colors.green}{log}{colors.end}')
        print('------------------')
    else:
        print(f'Logging: {colors.red}{log}{colors.end}')
        print('------------------')
    if bool(console) == True:
        print(f'Console: {colors.green}{console}{colors.end}')
        print('==================')
        threading.Thread(target=consoleFunc).start()
    else:
        print(f'Console: {colors.red}{console}{colors.end}')
        print('==================')
        pass
    print('Bot admins')
    print('------------------')
    print(colors.cyan)
    for id in ids:
        print(id)
    print(colors.end)
    print('==================')
    print('System info')
    print('Running as: ' + str(os.system("whoami")))
    print('------------------')
    print('Os name: ' + str(os.name))
    print('------------------')
    print('Current working dir: ' + str(os.getcwd()))
    print('------------------')
    try:
        botpath = 'F:\\bot\\src\\bot\.py'
        botsize = os.path.getsize(botpath)
        print('Bot file size: ' + botsize)
        print('------------------')
    except FileNotFoundError:
        if os.name == 'posix':
            try:
                 print('Bot file size: ' + os.path.getsize('/sdcard/bot/bot.py'))
                 print('------------------')
            except FileNotFoundError:
                print('Bot file size: ' + os.path.getsize(str(os.getcwd() + '/bot.py')))
                print('------------------')

# Error handler #
@client.event
async def on_command_error(ctx, error):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if isinstance(error, CommandNotFound):
        if os.name == 'nt':
            with open('F:\\bot\\logs\\errors.txt', 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at CommandNotFound. Details: This command does not exist.\n')
                f.close()
                print(f'[{current_time}] Ignoring exception at {colors.green}CommandNotFound{colors.end}. Details: This command does not exist. {colors.red}The user was not notified of this error. This error was logged at \'F:\\bot\\logs\\errors.txt\'{colors.end}')
        else:
            pass
    if isinstance(error, CommandOnCooldown):
        await ctx.send(f'This command is on cooldown. Please try after {math.ceil(error.retry_after)} seconds')
        if os.name == 'nt':
            with open('F:\\bot\\logs\\errors.txt', 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at CommandOnCooldown. Details: This command is currently on cooldown.\n')
                f.close()
                print(f'[{current_time}] Ignoring exception at {colors.green}CommandOnCooldown{colors.end}. Details: This command is currently on cooldown. {colors.red}This error was logged at \'F:\\bot\\logs\\errors.txt\'{colors.end}')
        else:
            pass
    if isinstance(error, MissingRequiredArgument):
        await ctx.send('Missing required argument(s)')
        if os.name == 'nt':
            with open('F:\\bot\\logs\\errors.txt', 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at MissingRequiredArgument. Details: The command can\'t be executed because required arguments are missing.\n')
                f.close()
                print(f'[{current_time}] Ignoring exception at {colors.green}MissingRequiredArgument{colors.end}. Details: The command can\'t be executed because required arguments are missing. {colors.red}This error was logged at \'F:\\bot\\logs\\errors.txt\'{colors.end}')
        else:
            pass
    if isinstance(error, MissingPermissions):
        await ctx.send('You dont have permissions to use this')
        if os.name == 'nt':
            with open('F:\\bot\\logs\\errors.txt', 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at MissingPermissions. Details: The user doesn\'t have the required permissions.\n')
                f.close()
                print(f'[{current_time}] Ignoring exception at {colors.green}MissingPermissions{colors.end}. Details: The user doesn\'t have the required permissions. {colors.red}This error was logged at \'F:\\bot\\logs\\errors.txt\'{colors.end}')
        else:
            pass
    if isinstance(error, BadArgument):
        await ctx.send('Invalid argument')
        if os.name == 'nt':
            with open('F:\\bot\\logs\\errors.txt', 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at BadArgument.\n')
                f.close()
                print(f'[{current_time}] Ignoring exception at {colors.green}BadArgument{colors.end}. {colors.red}This error was logged at \'F:\\bot\\logs\\errors.txt\'{colors.end}')
        else:
            pass
    if isinstance(error, BotMissingPermissions):
        await ctx.send('I don\'t have the required permissions to use this.')
        if os.name == 'nt':
            with open('F:\\bot\\logs\\errors.txt', 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at BotMissingPermissions.\n Details: The bot doesn\'t have the required permissions.\n')
                f.close()
                print(f'[{current_time}] Ignoring exception at {colors.green}BotMissingPremissions{colors.end}. Details: The bot doesn\'t have the required permissions. {colors.red}This error was logged at \'F:\\bot\\logs\\errors.txt\'{colors.end}')
        else:
            pass
# Error handler end #

snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_message_delete(message):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    guild = client.guilds[0]
    channel = message.channel
    snipe_message_author[message.channel.id] = message.author
    snipe_message_content[message.channel.id] = message.content
    if bool(log) == True:
        # with open('F:\\bot\\logs\\log.txt', 'a') as f:
        #     f.write(f'[{current_time}]Message deleted by {snipe_message_author[channel.id]}.\n   Content:{snipe_message_content[channel.id]}\n')
        #     f.close()
        if message.guild.id == 880409977074888714:
            c = client.get_channel(897387063576506379)
            em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id], color=0xFFBF00)
            em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
            await c.send(embed = em)
        elif message.guild.id == 876826249207640096:
            c = client.get_channel(881181406582165525)
            em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id], color=0xFFBF00)
            em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
            await c.send(embed = em)
        else:
            pass
    else:
        pass

@client.event
async def on_message_edit(message_before, message_after):
    global author
    author = message_before.author
    guild = message_before.guild.id
    channel = message_before.channel
    global before
    before = message_before.content
    global after
    after = message_after.content
    if any(x in message_after.content.lower() for x in bad):
        await message_after.delete()
        await channel.send(f'{message_after.author.mention} watch your language.')
    if bool(log):
        if guild == 880409977074888714:
            c = client.get_channel(897387314609786880)
            em = discord.Embed(description = f"**Message before**: {message_before.content}\n**Message after**: {message_after.content}")
            em.set_footer(text = f"This message was edited by {message_before.author} in {channel}")
            await c.send(embed = em)
        else:
            pass
    else:
        pass

@client.event
async def on_member_join(member):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    guild = member.guild.name
    if bool(log) == True:
        if os.name == 'nt':
            with open('F:\\bot\\logs\\log.txt', 'a') as f:
                f.write(f'[{current_time}]{member} joined {guild}\n')
                f.close()
            print(f'[{current_time}] {colors.cyan}{member}{colors.end} joined {colors.green}{guild}{colors.end}')
        else:
            pass
    else:
        pass

@client.event
async def on_member_remove(member):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    guild = member.guild.name
    if bool(log) == True:
        if os.name == 'nt':
            with open('F:\\bot\\logs\\log.txt', 'a') as f:
                f.write(f'[{current_time}]{member}{colors.end} left {guild}\n')
                f.close()
            print(f'[{current_time}] {colors.cyan}{member}{colors.end} left {colors.green}{guild}{colors.end}')
        else:
            pass
    else:
        pass

@client.event
async def on_message(message):
    if not message.author.bot:
        member_data = load_member_data(message.author.id)
        member_data.xp += 1
        if member_data.level == 0:
            if member_data.xp >= 25:
                member_data.xp -= member_data.xp
                member_data.level += 1
                await message.channel.send(f"<@{message.author.id}> You leveled up to level {member_data.level}")
            else:
                pass
        elif member_data.level == 1:
            if member_data.xp >= 50:
                member_data.xp -= member_data.xp
                member_data.level += 1
                await message.channel.send(f"<@{message.author.id}> You leveled up to level {member_data.level}")
            else:
                pass
        elif member_data.level == 2:
            if member_data.xp >= 100:
                member_data.xp -= member_data.xp
                member_data.level += 1
                await message.channel.send(f"<@{message.author.id}> You leveled up to level {member_data.level}")
            else:
                pass
        elif member_data.level == 3:
            if member_data.xp >= 500:
                member_data.xp -= member_data.xp
                member_data.level += 1
                await message.channel.send(f"<@{message.author.id}> You leveled up to level {member_data.level}")
        elif member_data.level == 4:
            if member_data.xp >= 750:
                member_data.xp -= member_data.xp
                member_data.level += 1
                await message.channel.send(f"<@{message.author.id}> You leveled up to level {member_data.level}")
            else:
                pass
        elif member_data.level >= 5:
            if member_data.xp >= 1000:
                member_data.xp -= member_data.xp
                member_data.level += 1
                await message.channel.send(f"<@{message.author.id}> You leveled up to level {member_data.level}")
        else:
            pass

        save_member_data(message.author.id, member_data)
        if '<@738290097170153472>' not in message.content:
            pass
        else:
            print(f'{message.author.display_name} pinged you!\n     Content: {message.content}')
    else:
        pass
    await client.process_commands(message)

@client.event
async def on_message(message):
    if not message.author.bot:
        if any(x in message.content.lower() for x in whitelist):
            pass
        elif any(x in message.content.lower() for x in bad):
            await message.delete()
            await message.channel.send(f'{message.author.mention} watch your language.')
        else:
            pass
    else:
        pass

    await client.process_commands(message)

### Events end ###

### Commands ###
# @client.command()
# async def disable(ctx):
#     def check(msg):
#         return msg.author == ctx.message.author and (msg.content)
#     msg = await client.wait_for("message", check=check)
#     if str(msg.content) == 'testcmd':
#         test = not test
#         await ctx.send('Command testcmd has been disabled')
#         if bool(log) == True:
#             print(f'{text} command has been disabled by {ctx.message.author.display_name}')
#         else:
#             pass
#     else:
#         await ctx.send('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

@client.command(aliases=['goldfish'])
async def fstab(ctx):
    await ctx.reply('https://cdn.discordapp.com/attachments/878297190576062515/879845618636423259/IMG_20210825_005111.jpg')

@client.command(aliases=['xp', 'level'])
async def rank(ctx, user : discord.User=None):
    return  ### Used because levelling is disabled. Reason for disabled levelling is that most servers have arcane or Mee6 as an alternative. ###
    if user == None:
        member_data = load_member_data(ctx.message.author.id)
        if member_data.level <= 5:
            rank = "New person"
        elif member_data.level >= 10 and member_data.level > 5:
            rank = "Active"
        elif member_data.level >= 20 and member_data.level > 10:
            rank = "Active af!!"
        if member_data.level == 0:
            e = discord.Embed(title=f"{ctx.message.author.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\25")
        elif member_data.level == 1:
            e = discord.Embed(title=f"{ctx.message.author.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\50")
        elif member_data.level == 2:
            e = discord.Embed(title=f"{ctx.message.author.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\100")
        elif member_data.level == 3:
            e = discord.Embed(title=f"{ctx.message.author.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\500")
        elif member_data.level == 4:
            e = discord.Embed(title=f"{ctx.message.author.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\750")
        elif member_data.level >= 5:
            e = discord.Embed(title=f"{ctx.message.author.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\1000")
        await ctx.send(embed=e)
    else:
        member_data = load_member_data(ctx.message.author.id)
        if member_data.level <= 5:
            rank = "New person"
        elif member_data.level >= 10 and member_data.level > 5:
            rank = "Active"
        elif member_data.level >= 20 and member_data.level > 10:
            rank = "Active af!!"
        member_data = load_member_data(user.id)
        if member_data.level == 0:
            e = discord.Embed(title=f"{user.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\25")
        elif member_data.level == 1:
            e = discord.Embed(title=f"{user.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\50")
        elif member_data.level == 2:
            e = discord.Embed(title=f"{user.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\100")
        elif member_data.level == 3:
            e = discord.Embed(title=f"{user.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\500")
        elif member_data.level == 4:
            e = discord.Embed(title=f"{user.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\750")
        elif member_data.level >= 5:
            e = discord.Embed(title=f"{user.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\1000")
        await ctx.send(embed=e)

@client.command()
async def add_xp(ctx, user : discord.User, *, arg1):
    if ctx.message.author.id not in ids:
        await ctx.reply(f'I am 101% sure this command doesn\'t exist :eyes:')
    else:
        if arg1.isdigit:
            member_data = load_member_data(user.id)
            member_data.xp += int(arg1)
            save_member_data(user.id, member_data)
        else:
            await ctx.reply(f'**{arg1}** is not a number lol')

@client.command()
async def edit_snipe(ctx):
    try:
        em = discord.Embed(description=f'**Message before**: {before}\n**Message after**:{after}', color=theme_color)
        em.set_footer(text=f'This message was edited by {author}')
        await ctx.send(embed = em)
    except:
        await ctx.reply('No recent edited messages here :eyes:')

@client.command()
async def add_lvl(ctx, user : discord.User, *, arg1):
    if ctx.message.author.id not in ids:
        await ctx.reply(f'101% sure that this command doesn\'t exist :eyes:')
    else:
        if arg1.isdigit:
            member_data = load_member_data(user.id)
            member_data.level += int(arg1)
            save_member_data(user.id, member_data)
        else:
            await ctx.reply(f'{arg1} is not a number')

@client.command()
async def invite(ctx):
    inviteLink = 'https://discord.com/api/oauth2/authorize?client_id=896437848176230411&permissions=8&scope=bot'
    await ctx.reply(f'Invite isobot to your server with this link >> {inviteLink}')

@client.command()
async def amogus(ctx):
    await ctx.reply("https://c.tenor.com/1iSARWJr-TEAAAAC/among-us-twerk.gif")

@client.command()
async def say(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(f'{text}')

@client.command()
async def uptime(ctx):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    await ctx.send(f'I have been running for {uptime}.')

@client.command()
async def snipe(ctx):
    channel = ctx.channel
    try:
        if any(x in snipe_message_content[channel.id] for x in bad):
            em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = f'||{snipe_message_content[channel.id]}||', color=0xcf1515)
            em.set_footer(text = f"WARNING! THIS MESSAGE CONTAINS PROFANE TEXT! This message was sent by {snipe_message_author[channel.id]}")
            await ctx.send(embed = em)
        else:
            em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id], color=theme_color)
            em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
            await ctx.send(embed = em)
    except:
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")

@client.command()
async def whoAmI(ctx):
    await ctx.send(f"I am: {client.user.name}\nMy id is: {client.user.id}\nMy developer is: {owner}\nMy ping is {round(client.latency * 1000)}ms\nYour name is: {'saneite#5077 (not my dev)' if ctx.message.author.id == 795986008680300565 else ctx.message.author}\nYour id is: {ctx.message.author.id}")

@client.command()
async def ping(ctx):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    await ctx.send(f'Pong! My ping is {round(client.latency * 1000)}ms')
    if bool(log) == True:
        with open('F:\\bot\\logs\\log.txt', 'a') as f:
            f.write(f'[{current_time}] Bot ping is {round(client.latency * 1000)}ms\n')
            f.close()
        pass
    else:
        return

@client.command()
async def help(ctx):
    helpEmbed = discord.Embed(title='**MY COMMAND LIST**', description='My Brackets are **;**\n\nEconomy:\nwork, beg, bal, dep, with, give, hunt, fish, daily, weekly, monthly, postmeme\n\nBot Information:\nping, invites, whoAmI, invite, uptime\n\nModeration:\nban, kick, lock, unlock, nuke\n\nMisc:\n8ball, slap, kill, uwu, snipe, edit_snipe, meme, linuxmeme, nothecker, aww, softwaregore, ihadastroke, amogus, fstab, say', color=theme_color)
    await ctx.send(embed = helpEmbed)

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
  responses = [
            "no?????",
            "when you grow a braincell, yes",
            "you stupid, of course not",
            "lol no",
            "As I see it, yes.",
            "Most likely.",
            "Yes.",
            "Try again",
            "brain.exe stopped responding.",
            "ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good."
  ]
  ballEmbed= discord.Embed(title=f':8ball: {question}', description=f'{random.choice(responses)}')
  await ctx.send(embed=ballEmbed)

@client.command()
async def eues(ctx):
    await ctx.message.delete()
    await ctx.send(':eyes:')

@client.command()
@commands.has_permissions(manage_channels=True)
async def nuke(ctx, channel: discord.TextChannel = None):
    if channel == None: 
        await ctx.send("You did not mention a channel!")
        return

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        new_channel = await nuke_channel.clone(reason="Has been Nuked!")
        await nuke_channel.delete()
        await new_channel.send("This channel has been nuked!")
        await ctx.send("Nuked the Channel sucessfully!")
        if bool(log) == True:
            with open('F:\\bot\\logs\\log.txt', 'a') as f:
                f.write(f'[{current_time}]{ctx.message.author.display_name}nuked{nuke_channel}\n')
                f.close()
            print(f'[{current_time}] {ctx.message.author.display_name} nuked {nuke_channel}')
        else:
            pass
    else:
        await ctx.reply(f"No channel named {channel.name} was found!")

@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel = None):
    if channel == None: 
        await ctx.reply("Please run this command again, but mention a channel next time.")
        return
    lock_channel = discord.utils.get(ctx.guild.channels, name=channel.name)
    if lock_channel is not None:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        perms = lock_channel.overwrites_for(ctx.guild.default_role)
        perms.send_messages=False
        await lock_channel.set_permissions(ctx.guild.default_role, overwrite=perms, reason="Moderator ran lock command.")
        # await ctx.reply('**:white_check_mark: This channel has been locked.**')
        sendEmbedLock = discord.Embed(title=f':white_check_mark: **{lock_channel}** has been locked.', color=0x6ede62)
        await ctx.channel.send(embed = sendEmbedLock)
        if bool(log) == True:
                with open('F:\\bot\\logs\\log.txt', 'a') as f:
                    f.write(f'[{current_time}] {ctx.message.author.display_name} locked {lock_channel}.\n')
                    f.close()
                print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} locked {colors.green}{lock_channel}{colors.end}.')
        else:
            pass
    else:
        await ctx.reply(f'No channel named {channel.name} was found.')
    
@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel = None):
    if channel == None: 
        await ctx.reply("Please run this command again, but mention a channel next time.")
        return
    unlock_channel = discord.utils.get(ctx.guild.channels, name=channel.name)
    if unlock_channel is not None:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        perms = unlock_channel.overwrites_for(ctx.guild.default_role)
        perms.send_messages=True
        await unlock_channel.set_permissions(ctx.guild.default_role, overwrite=perms, reason="Moderator ran unlock command.")
        # await ctx.reply('**:white_check_mark: This channel has been unlocked.**')
        sendEmbedUnlock = discord.Embed(title=f':white_check_mark: **{unlock_channel}** has been unlocked.', color=0x6ede62)
        await ctx.channel.send(embed = sendEmbedUnlock)
        if bool(log) == True:
                with open('F:\\bot\\logs\\log.txt', 'a') as f:
                    f.write(f'[{current_time}] {ctx.message.author.display_name} unlocked {unlock_channel}.\n')
                    f.close()
                print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} unlocked {colors.green}{unlock_channel}{colors.end}.')
        else:
            pass
    else:
        await ctx.reply(f'No channel named {channel.name} was found.')
    

@client.command()
async def invites(ctx, *, user : discord.User=None):
    totalInvites = 0
    if user == None:
        for i in await ctx.guild.invites():
            if i.inviter == ctx.author:
                totalInvites += i.uses
        e = discord.Embed(title=f'{ctx.message.author.display_name}\'s total invites', description=f"{totalInvites} invite{'' if totalInvites == 1 else 's'}", color=theme_color)
        await ctx.reply(embed=e)
    elif user.bot:
        await ctx.reply('This is a bot, not a user.')
        return
    else:
        for i in await ctx.guild.invites():
            if i.inviter == user:
                totalInvites += i.uses
        e = discord.Embed(title=f'{user.display_name}\'s total invites', description=f"{totalInvites} invite{'' if totalInvites == 1 else 's'}", color=theme_color)
        await ctx.reply(embed=e)

@client.command()
async def shutdown(ctx):
    if ctx.message.author.id == 738290097170153472:
        def check(msg):
            return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)
        
        await ctx.send('You sure?')
        msg = await client.wait_for("message", check=check)
        if msg.content == 'y' or msg.content == 'yes':
            await ctx.send('Shutting down the bot...')
            time.sleep(0.5)
            raise SystemExit('Bot shutdown')
        elif msg.content == 'n' or msg.content == 'no':
            await ctx.send('ok')
        else:
            await ctx.send(f'Wtf is {msg.content}? You are supposed to reply with yes or no')
    else:
        await ctx.send(f'101% that this command doesn\'t exist :eyes:')

@client.command(aliases=['hl'])
@commands.cooldown(1, 40, commands.BucketType.user)
async def highlow(ctx):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    numb = randint(1, 100)
    numb2 = randint(1, 100)
    id = ctx.message.author.id
    coins = randint(300, 1000)
    member_data = load_member_data(id)

    def check(msg):
        return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)

    await ctx.send(f'Your number is {numb} choose if the other is lower, higher or jackpot')
    msg = await client.wait_for("message", check=check)
    if msg.content == 'low':
        if numb > numb2:
            await ctx.send(f'Congrats, your number was {numb2} and you earned {coins} coins')
            member_data.wallet += coins
            save_member_data(id, member_data)
            if bool(log) == True:
                    # with open('F:\\bot\\logs\\log.txt', 'a') as f:
                    #     f.write(f'[{current_time}]{ctx.message.author.display_name} earned {coins} coins\n')
                    #     f.close()
                print(f'[{current_time}] {ctx.message.author.display_name} earned {coins} coins')
            else:
                pass
        elif numb < numb2:
            await ctx.send(f'Incorrect the number was {numb2}')
        elif numb == numb2:
            await ctx.send(f'You stupid you could won 1 mil coins if you choose jackpot')
    if msg.content == 'jackpot':
        if numb == numb2:
            coins2 = randint(1000000, 5000000)
            await ctx.send(f'Congrats, your number was {numb2} and you earned {coins2} coins gg!')
            member_data = load_member_data(id)
            member_data.wallet += coins2
            save_member_data(id, member_data)
            if bool(log) == True:
                    # with open('F:\\bot\\logs\\log.txt', 'a') as f:
                    #     f.write(f'[{current_time}] {ctx.message.author.display_name} earned {coins2} coins\n')
                    #     f.close()
                print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} earned {colors.green}{coins2}{color.end} coins.')
            else:
                pass
        else:
            await ctx.send(f'Incorrect the number was {numb2}')
    if msg.content == 'high':
        if numb < numb2:
            await ctx.send(f'Congrats, your number was {numb2} and you earned {coins} coins')
            member_data = load_member_data(id)
            member_data.wallet += coins
            save_member_data(id, member_data)
            if bool(log) == True:
                    # with open('F:\\bot\\logs\\log.txt', 'a') as f:
                    #     f.write(f'[{current_time}]{ctx.message.author.display_name} earned {coins} coins\n')
                    #     f.close()
                print(f'[{current_time}] {ctx.message.author.display_name} earned {coins} coins')
            else:
                pass
        else:
            await ctx.send(f'Incorrect your number was {numb2}')
    else:
        await ctx.send(f'{msg.content} is not an option')

@client.command()
async def thicc(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/877460877085900800/897409012134445086/THICC_TEXT.png')

@client.command()
async def kill(ctx, user : discord.User):
    if user == None:
        await ctx.send('Please tag someone to kill')
    elif user.id == ctx.message.author.id:
        await ctx.send('Ok you are dead, please tag someone else to kill')
    else:
        responses2 = [
            f"<@{user.id}> died from a dang baguette",
            f"<@{ctx.message.author.id}> strikes <@{user.id}> with the killing curse... *Avada Kedavra!*",
            f"<@{user.id}> dies from dabbing too hard",
            f"<@{ctx.message.author.id}> fstabbed the heck out of <@{user.id}>"
        ]
        await ctx.send(f'{random.choice(responses2)}')

@client.command()
async def stroke(ctx):
    await ctx.send('ug8 o\\')

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, *, member : discord.Member):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if member == ctx.message.author:
        await ctx.reply('You can\'t kick yourself, you idiot')
        return
    else:
        await member.kick()
    await ctx.send(f'{member} has been **kicked** from the server.')
    if bool(log) == True:
        # with open('F:\\bot\\logs\\log.txt', 'a') as f:
        #     f.write(f'[{current_time}]{ctx.message.author.display_name} kicked {member} from {ctx.message.guild.name}')
        #     f.close()
        print(f'[{current_time}] {ctx.message.author.display_name} kicked {member.display_name} from {ctx.message.guild.name}')
    else:
        pass

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, *, member : discord.Member):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if member == ctx.message.author:
        await ctx.reply('You can\'t ban yourself, you idiot')
        return
    else:
        await member.ban()
        await ctx.send(f'{member} has been **banned** from the server.')
        if bool(log) == True:
            print(f'[{current_time}] {ctx.message.author.display_name} banned {member.display_name} from {ctx.message.guild.name}')
        else:
            pass 

@client.command(aliases=["lm"])
async def linuxmeme(ctx):
    memes_submissions = reddit.subreddit('linuxmemes').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embed = discord.Embed(title = submission.title, color=theme_color)
    embed.set_image(url=submission.url)
    embed.set_footer(text='I use Arch BTW.')
    await ctx.send(embed = embed)

@client.command(aliases=["nh"])
async def nothecker(ctx):
    nothecker_submissions = reddit.subreddit('nothecker').hot()
    post_to_pick = random.randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in nothecker_submissions if not x.stickied)
    embed = discord.Embed(title = submission.title, color=theme_color)
    embed.set_image(url=submission.url)
    embed.set_footer(text=':eues:')
    await ctx.send(embed = embed)

@client.command(aliases=['pet'])
async def aww(ctx):
    aww_submissions = reddit.subreddit('aww').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in aww_submissions if not x.stickied)
    embed = discord.Embed(title = submission.title, color=theme_color)
    embed.set_image(url=submission.url)
    embed.set_footer(text='Meow/Woof!')
    await ctx.send(embed = embed)

@client.command(aliases=['sg'])
async def softwaregore(ctx):
    sg_submissions = reddit.subreddit('softwaregore').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in sg_submissions if not x.stickied)
    embed = discord.Embed(title = submission.title, color=theme_color)
    embed.set_image(url=submission.url)
    embed.set_footer(text='Softwaregore be like')
    await ctx.send(embed = embed)

@client.command(aliases=['meem'])
async def meme(ctx):
    memes_submissions = reddit.subreddit('memes').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embed = discord.Embed(title = submission.title, color=theme_color)
    embed.set_image(url=submission.url)
    embed.set_footer(text='Meems be like')
    await ctx.send(embed = embed)

@client.command()
async def ihadastroke(ctx):
    memes_submissions = reddit.subreddit('ihadastroke').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embed = discord.Embed(title = submission.title, color=theme_color)
    embed.set_image(url=submission.url)
    embed.set_footer(text='Stokr... Stork... Stroke.')
    await ctx.send(embed = embed)

@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def hecker_booster_claim(ctx):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if "Hecker booster" in ctx.message.author.roles:
        member_data = load_member_data(ctx.message.author.id)
        member_data.wallet += 69420
        save_member_data(ctx.message.author.id, member_data)
        await ctx.send('Thanks for boosting Hecker\'s Hub! For this, you claimed 69420 coins :sunglasses:')
        if bool(log) == True:
            print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} used {colors.green}Hecker booster{colors.end}')
        else:
            pass
    else:
        await ctx.reply('You need to boost this server to use this command!')

@commands.cooldown(1, 1800, commands.BucketType.user)
async def work(ctx):
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    member_data = load_member_data(ctx.message.author.id)
    coins = randint(1000, 25000)
    member_data.wallet += coins
    await ctx.send(f"You earned {coins} coins.")
    save_member_data(ctx.message.author.id, member_data)
    if bool(log) == True:
        print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} earned {colors.green}{coins}{colors.end} coins')
    else:
        pass

@client.command()
@commands.cooldown(1, 180, commands.BucketType.user)
async def spam(ctx, *, spammsg):
    if ctx.message.author.id == 738290097170153472 or 705462972415213588:
        await ctx.message.delete(f'{spammsg}')
        # repeat this 30 times.
        await ctx.send(f'{spammsg}')  # 1st hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 2nd hit 
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 3rd hit 
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 4th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 5th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 6th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 7th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 8th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 9th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 10th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 11th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 12th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 13th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 14th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 15th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 16st hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 17nd hit 
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 18rd hit 
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 19th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 20th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 21th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 22th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 23th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 24th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 25th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 26th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 27th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 28th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 29th hit
        time.sleep(1)
        await ctx.send(f'{spammsg}')  # 30th hit
        time.sleep(1)
    else:
        await ctx.reply('I don\'t trust you with this command :eyes:')
    
@client.command()
async def uwu(ctx, user : discord.User):
    await ctx.send(f'{ctx.message.author.mention} uwu\'ed {user}. *uwu*')

@client.command()
async def slap(ctx, user : discord.User):
    responses3 = [
        "https://cdn.weeb.sh/images/Hkw1VkYP-.gif",
        "https://cdn.weeb.sh/images/HkA6mJFP-.gif",
        "https://cdn.weeb.sh/images/Sk9mfCtY-.gif",
        "https://cdn.weeb.sh/images/HJKiX1tPW.gif"
    ]
    e = discord.Embed(title=f'{ctx.message.author} slaps {user}', color=theme_color)
    e.set_image(url=f'{random.choice(responses3)}')
    await ctx.send(embed = e)

@client.command()
async def floppa(ctx):
    responses_floppa = [
        "https://cdni.rbth.com/rbthmedia/images/2021.05/original/60b4cf1d85600a4427115b02.jpg",
        "https://i.kym-cdn.com/entries/icons/original/000/034/421/cover1.jpg",
        "https://static.wikia.nocookie.net/floppapedia-revamped/images/9/96/Floppa.jpg/revision/latest?cb=20210223180751",
        "https://pbs.twimg.com/profile_images/1417930987372257297/yk4xiTv5_400x400.jpg",
        "https://i.pinimg.com/236x/90/ff/1f/90ff1f3ec129b93c251730f838cc2d06.jpg"
    ]
    e = discord.Embed(title='Floppa', color=theme_color)
    e.set_image(url=f'{random.choice(responses_floppa)}')
    await ctx.send(embed = e)


#@client.command()                                                          ### Will Edit Later ###
#@commands.cooldown(1, 30, commands.BucketType.user)
#async def guess(ctx):
#    now = datetime.datetime.now()
#    current_time = now.strftime("%H:%M:%S")
#    if bool(currency) == False:
#        await ctx.message.channel.send('Currency is disabled')
#        return
#    else:
#        pass
#    member_data = load_member_data(ctx.message.author.id)
#    await ctx.message.channel.send('Guess a number from 1 to 10')
#
#    def check(msg):
#        return msg.author == ctx.message.author and msg.channel == ctx.message.channel and int(msg.content) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#    msg = await client.wait_for("message", check=check)
#
#    if int(msg.content) == x:
#        coins = randint(1, 100)
#        await ctx.message.channel.send(f"Correct, you earned {coins} coins")
#        member_data.wallet += coins
#        save_member_data(ctx.message.author.id, member_data)
#        if bool(log) == True:
#            print(f'[{current_time}]{colors.cyan}{ctx.message.author.display_name}{colors.end} has earned {colors.green}{x}{colors.end} coins')
#        else:
#            pass
#    else:
#        await ctx.message.channel.send(f"Nope. It was {x}")

@client.command(aliases=['sus'])
async def isSus(ctx, *, user : discord.User):
    susvar = [
        True,
        False
    ]
    sus = random.choice(susvar)
    if bool(sus) == True:
        await ctx.send(f'{user.mention} is very sus')
    elif bool(sus) == False:
        await ctx.send(f'{user.mention} isn\'t sus')
    else:
        await ctx.reply('undefined')

@client.command(aliases=['pm'])
@commands.cooldown(1, 40, commands.BucketType.user)
async def postmeme(ctx):
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    member_data = load_member_data(ctx.message.author.id)
    #if int(member_data.wallet) >= value:
    #    await ctx.reply(f'You have reached max value for your wallet ({value})')
    #    return
    #else:
    #    pass
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    await ctx.send(f'{ctx.message.author.mention} What type of meme you want to post?\n`f` Fresh meme\n`d` Dank meme\n`c` Copypasta\n*more comming soon*')

    def check(msg):
        return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content) in ['f', 'd', 'c']
    
    msg = await client.wait_for("message", check=check)

    x = randint(0, 200)
    if x == 0:
        await ctx.send(f'{ctx.message.author.mention} You earned 0 coins xD')
    else:
        await ctx.send(f'You earned {x} coins')
        member_data.wallet += x
        save_member_data(id, member_data)
        if bool(log) == True:
            print(f'[{current_time}]{colors.cyan}{ctx.message.author.display_name}{colors.end} has earned {colors.green}{x}{colors.end} coins')
        else:
            pass

@client.command()
async def stab(ctx, user : discord.User):
    e = discord.Embed(title=f':knife: {ctx.message.author} fstabbed {user}. Oof! :knife:', description='That must really fstabbing hurt...', color=theme_color)
    await ctx.send(embed = e)


@client.command()
async def afk(ctx):
    await ctx.reply('This command has been disabled')

@client.command()
async def null(ctx):
    await ctx.reply('You got **null** coins dood.')

@client.command(aliases=['gift'])
async def give(ctx, user : discord.User, *, arg1):
    if user.id == ctx.message.author.id:
        await ctx.reply('You can\'t give coins to yourself')
        return
    else:
        if arg1.isdigit:
            member_data = load_member_data(ctx.message.author.id)
            if member_data.wallet < int(arg1):
                await ctx.reply('You don\'t have that many coins in your wallet')
                return
            elif int(arg1) < 0:
                await ctx.reply('Don\'t try to break me **dood**')
            elif int(arg1) == 0:
                await ctx.reply('You can\'t gift 0 coins')
            else:
                member_data.wallet -= int(arg1)
                save_member_data(ctx.message.author.id, member_data)
                user_data = load_member_data(user.id)
                user_data.wallet += int(arg1)
                save_member_data(user.id, user_data)
                await ctx.reply(f'You gave {arg1} coins to {user.display_name}')
        else:
            await ctx.reply(f'{arg1} is not a digit **dood**')

@client.command()
async def add(ctx, user : discord.User, *, arg1=None):
    if ctx.message.author.id not in ids:
        await ctx.reply(f'101% sure that this command doesn\'t exist :eyes:')
        return
    else:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if arg1.startswith('0x') or arg1.startswith('-0x'):
            try:
                hexv = int(f'{arg1}', 16)
                member_data = load_member_data(user.id)
                member_data.wallet += int(hexv)
                save_member_data(user.id, member_data)
                await ctx.send(f'Added {hexv} coins to {user.display_name}\'s account')
                print(f'[{current_time}]{colors.cyan}{ctx.message.author.display_name}{colors.end} added {colors.green}{hexv}{colors.end} coins to {colors.cyan}{user.display_name}\'s{colors.end} account')
            except ValueError:
                await ctx.send(f'Invalid hex value')
        elif arg1.startswith('0b') or arg1.startswith('-0b'):
            try:
                binv = int(f'{arg1}', 2)
                member_data = load_member_data(user.id)
                member_data.wallet += int(binv)
                save_member_data(user.id, member_data)
                await ctx.send(f'Added {binv} coins to {user.display_name}\'s account')
                print(f'[{current_time}]{colors.cyan}{ctx.message.author.display_name}{colors.end} added {colors.green}{binv}{colors.end} coins to {colors.cyan}{user.display_name}\'s{colors.end} account')
            except ValueError:
                await ctx.send('Invalid binary value')
        elif arg1.isdigit:
            member_data = load_member_data(user.id)
            member_data.wallet += int(arg1)
            save_member_data(user.id, member_data)
            await ctx.send(f'Added {arg1} coins to {user.display_name}\'s account')
            if bool(log) == True:
                print(f"[{current_time}]{colors.cyan}{ctx.message.author.display_name}{colors.end} added {colors.green}{arg1}{colors.end} coins to {colors.cyan}{user.display_name}{colors.end}\'s account")
            else:
                pass
        elif arg1 == None:
            await ctx.reply('Usage: `;add <user> binary\\hex\\decimal`')
            return
        else:
            await ctx.send('Invalid value.')
        

@client.command()
@commands.cooldown(1, 1800, commands.BucketType.user)
async def work(ctx):
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    member_data = load_member_data(ctx.message.author.id)
    coins = randint(1000, 25000)
    member_data.wallet += coins
    await ctx.send(f"You earned {coins} coins.")
    save_member_data(ctx.message.author.id, member_data)
    if bool(log) == True:
        print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} earned {colors.green}{coins}{colors.end} coins')
    else:
        pass

@client.command()
async def e(ctx):
    await ctx.message.delete()
    await ctx.send('e')

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def beg(ctx):
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    member_data = load_member_data(ctx.message.author.id)
    coins = randint(1, 500)
    #if int(member_data.wallet) >= value:
    #    await ctx.reply(f'You reached max wallet value. ({value})')
    #    return
    #else:
    member_data.wallet += coins
    await ctx.send(f'You earned {coins} coins.')

    save_member_data(ctx.message.author.id, member_data)
    if bool(log) == True:
        print(f'[{current_time}]{colors.cyan}{ctx.message.author.display_name}{colors.end} earned {colors.green}{coins}{colors.end} coins')
    else:
        pass

@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
    if bool(currency) == False:
        await ctx.reply('Currency is disabled')
        return
    else:
        pass
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S") 
    member_data = load_member_data(ctx.message.author.id)
    member_data.wallet += 10000
    await ctx.send('You claimed 10,000 coins')
    save_member_data(ctx.message.author.id, member_data)
    if bool(log) == True:
        print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} claimed {colors.green}10000{colors.end} coins from daily command.')
    else:
        pass

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def fish(message):
    if bool(currency) == False:
        await message.channel.send('Currency is disabled')
        return
    else:
        pass
    items = [
        "nothing",
        "fish",
        "rare fish",
        "goldfish",
        "mythic fish"
    ]
    item = random.choice(items)
    if item == 'nothing':
        await message.channel.send('You got nothing XD')
    elif item == 'fish':
        await message.channel.send(f'You caught a fish and sold it for 100 coins')
        member_data = load_member_data(message.author.id)
        member_data.wallet += 100
        save_member_data(message.author.id, member_data)
    elif item == 'rare fish':
        member_data = load_member_data(message.author.id)
        await message.channel.send(f'You caught a rare fish and sold it for 300 coins')
        member_data.wallet += 300
        save_member_data(message.author.id, member_data)
    elif item == 'goldfish':
        member_data = load_member_data(message.author.id)
        await message.channel.send(f'You caught a **goldfish**, fstabbed it and sold it for 420 coins')
        member_data.wallet += 420
        save_member_data(message.author.id, member_data)
    elif item == 'mythic fish':
        member_data = load_member_data(message.author.id)
        await message.channel.send(f'You caught a **mythic** fish and sold it for 1000 coins')
        member_data.wallet += 1000
        save_member_data(message.author.id, member_data)

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def dig(message):
    if bool(currency) == False:
        await message.channel.send('Currency is disabled')
        return
    else:
        pass
    items = [
        "nothing",
        "fell",
        "rock",
        "python",
        "shovel",
        "treasure_chest"
    ]
    item = random.choice(items)
    if item == 'nothing':
        await message.channel.send('You got nothing XD')
    if item == 'fell':
        await message.channel.send('You fell into the hole and died of fall damage. You lost 300 coins.')
        member_data = load_member_data(message.author.id)
        member_data.wallet -= 300
        save_member_data(message.author.id, member_data)
    elif item == 'rock':
        await message.channel.send(f'You found a rock. You sold it and earned 100 coins.')
        member_data = load_member_data(message.author.id)
        member_data.wallet += 100
        save_member_data(message.author.id, member_data)
    elif item == 'python':
        member_data = load_member_data(message.author.id)
        await message.channel.send(f'You found a pet python. You sold it and earned 500 coins.')
        member_data.wallet += 500
        save_member_data(message.author.id, member_data)
    elif item == 'shovel':
        member_data = load_member_data(message.author.id)
        await message.channel.send(f'You found someone else\'s shovel while digging. You sold it for 1000 coins.')
        member_data.wallet += 1000
        save_member_data(message.author.id, member_data)
    elif item == 'treasure_chest':
        member_data = load_member_data(message.author.id)
        await message.channel.send(f'You found a treasure chest while digging. Turns out that it is full of gold. You sold it and earned 5000 coins.')
        member_data.wallet += 5000
        save_member_data(message.author.id, member_data)

@client.command(aliases=['dep'])
async def deposit(ctx, *, arg1):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        member_data = load_member_data(ctx.message.author.id)
        if arg1 == 'all' or arg1 == 'max':
            if member_data.wallet == 0:
                await ctx.reply('You don\'t have any coins in your wallet')
                return
            else:
                if member_data.wallet == 1:
                    await ctx.reply(f'You deposited {member_data.wallet} coin.')
                else:
                    await ctx.reply(f'You deposited {member_data.wallet} coins.')
                member_data.bank += int(member_data.wallet)
                member_data.wallet -= int(member_data.wallet)
                if bool(log) == True:
                    print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} deposited {colors.green}{member_data.wallet}{colors.end} coin\\s to their bank account.')
                else:
                    pass
                save_member_data(ctx.message.author.id, member_data)
                return
        elif arg1.isdigit:
            if int(arg1) > member_data.wallet:
                await ctx.reply('You don\'t have that many coins in your wallet')
                return
            elif int(arg1) < 0:
                await ctx.reply('Don\'t try to break me dood')
                return
            else:
                await ctx.send(f'You deposited {arg1} coins')
                member_data.wallet -= int(arg1)
                member_data.bank += int(arg1)
                if bool(log) == True:
                    print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} deposited {colors.green}{arg1}{colors.end} coin\\s to their bank account.')
                else:
                    pass
                save_member_data(ctx.message.author.id, member_data)
                return
        else:
            raise BadArgument

@client.command(aliases=['with'])
async def withdraw(ctx, *, arg1):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        member_data = load_member_data(ctx.message.author.id)
        if arg1 == 'all' or arg1 == 'max':
            if member_data.bank == 0:
                await ctx.send('You don\'t have any coins in your bank')
                return
            else:
                if member_data.bank == 1:
                    await ctx.reply(f'You withdrawn {member_data.bank} coin')
                else:
                    await ctx.reply(f'You withdrawn {member_data.bank} coins')    
                member_data.wallet += int(member_data.bank)
                member_data.bank -= int(member_data.bank)
                if bool(log) == True:
                    print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} withdrew {colors.green}{member_data.bank}{colors.end} coin\\s from their bank account.')
                else:
                    pass
                save_member_data(ctx.message.author.id, member_data)
                return
        elif arg1.isdigit:
            if int(arg1) > member_data.bank:
                await ctx.reply('You don\'t have that many coins in your bank')
                return
            elif int(arg1) < 0:
                await ctx.reply('Don\'t try to break me dood')
                return
            else:
                await ctx.reply(f'You withdrawn {arg1} coins')
                member_data.wallet += int(arg1)
                member_data.bank -= int(arg1)
                if bool(log) == True:
                    print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} withdrew {colors.green}{arg1}{colors.end} coin\\s from their bank account.')
                else:
                    pass
                save_member_data(ctx.message.author.id, member_data)
                return
        else:
            raise BadArgument

@client.command()
async def rob(ctx, *, user : discord.User):
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if ctx.message.author.id == user.id:
        await ctx.send('you cant rob yourself xd')
        return
    elif user.id == 738290097170153472:
        await ctx.send('You can\'t rob the bot developer LOL')
        return
    elif user.id == 705462972415213588:
        await ctx.send('You can\'t rob the ||other|| bot developer LOL')
        return
    else:
        vic_data = load_member_data(user.id)
        if vic_data.wallet < 500:
            save_member_data(user.id, vic_data)
            await ctx.send('This user has less than 500 coins')
        elif vic_data.wallet >= 500:
            coins = randint(500, vic_data.wallet)
            if bool(log) == True:
                print(f'[{current_time}] {ctx.message.author.display_name} stole {coins} coins from {user.display_name}')
            else:
                pass
            vic_data.wallet -= coins
            save_member_data(user.id, vic_data)
            member_data = load_member_data(ctx.message.author.id)
            member_data.wallet += coins
            save_member_data(ctx.message.author.id, member_data)
            await ctx.send(f'You stole {coins} coins from **{user.display_name}**')

@client.command()
async def whoppa(ctx):
    e = discord.Embed(title='Whoppa')
    e.set_image(url='https://upload.wikimedia.org/wikipedia/commons/b/b8/WHOPPER_with_Cheese%2C_at_Burger_King_%282014.05.04%29.jpg')
    await ctx.send(embed = e)

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def hunt(message):
    if bool(currency) == False:
        await message.channel.send('Currency is disabled')
        return
    else:
        pass
    items = [
        "nothing",
        "skunk",
        "boar",
        "dragon",
        "sniper",
        "died"
    ]
    item = random.choice(items)
    if item == 'nothing':
        await message.channel.send('You got nothing XD')
    elif item == 'skunk':
        await message.channel.send('You went for hunting and got a skunk. You sold it and earned 200 coins')
        member_data = load_member_data(message.author.id)
        member_data.wallet += 200
        save_member_data(message.author.id, member_data)
    elif item == 'boar':
        await message.channel.send('You went for hunting and got a boar. You sold it and earned 500 coins')
        member_data = load_member_data(message.author.id)
        member_data.wallet += 500
        save_member_data(message.author.id, member_data)
    elif item == 'shovel':
        await message.channel.send('You went for hunting and found a sniper, so you sold it and earned 1000 coins.')
        member_data = load_member_data(message.author.id)
        member_data.wallet += 1000
    elif item == 'dragon':
        await message.channel.send('You went for hunting and got a dragon wtf. You sold it and earned 5000 coins')
        member_data = load_member_data(message.author.id)
        member_data.wallet += 5000
        save_member_data(message.author.id, member_data)
    elif item == 'died':
        await message.channel.send('You went for hunting but you died. You lost 420 coins.')
        member_data = load_member_data(message.author.id)
        member_data.wallet -= 420
        save_member_data(message.author.id, member_data)

@client.command()
@commands.cooldown(1, 604800, commands.BucketType.user)
async def weekly(message):
    if bool(currency) == False:
        await message.channel.send('Currency is disabled')
        return
    else:
        pass
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    member_data = load_member_data(message.author.id)
    member_data.wallet += 50000
    await message.channel.send('You claimed 50,000 coins')
    save_member_data(message.author.id, member_data)
    if bool(log) == True:
        with open('F:\\bot\\logs\\errors.txt', 'a') as f:
                f.write(f'[{current_time}] {message.author.display_name} claimed 50000 coins from weekly command.\n')
                f.close()
        print(f'[{current_time}] {colors.cyan}{message.author.display_name}{colors.end} claimed {colors.green}50000{colors.end} coins from weekly command.')
    else:
        pass

@client.command()
@commands.cooldown(1, 2592000, commands.BucketType.user)
async def monthly(message):
    if bool(currency) == False:
        await message.channel.send('Currency is disabled')
        return
    else:
        pass
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    member_data = load_member_data(message.author.id)
    member_data.wallet += 100000
    await message.channel.send('You claimed 100,000 coins')
    save_member_data(message.author.id, member_data)
    if bool(log) == True:
        with open('F:\\bot\\logs\\errors.txt', 'a') as f:
            f.write(f'[{current_time}] {message.author.display_name} claimed 50000 coins from weekly command.\n')
            f.close()
        print(f'[{current_time}] {colors.cyan}{message.author.display_name}{colors.end} claimed {colors.green}100000{colors.end} coins from monthly command.')
    else:
        pass

@client.command()
async def pog(ctx):
    await ctx.send('69420')

@client.command()
async def dev_claim(message):
    if message.author.id == 705462972415213588:
        member_data = load_member_data(message.author.id)
        member_data.wallet += 69420
        await message.channel.send('You claimed 69,420 coins :sunglasses:')
        save_member_data(message.author.id, member_data)
    elif message.author.id == 738290097170153472:
        member_data = load_member_data(message.author.id)
        member_data.wallet += 50128
        await message.channel.send('You claimed 50,128 coins :knife:')
        save_member_data(message.author.id, member_data)
    elif message.author.id == 795986008680300565:
        member_data = load_member_data(message.author.id)
        member_data.wallet += 69
        await message.channel.send('You claimed 69 coins')
        save_member_data(message.author.id, member_data)
    else:
        await message.channel.send('Are you the bot developer? No, I didn\'t think so.')

@client.command()
async def wipe_user(ctx, *, user : discord.User):
    if ctx.message.author.id == 738290097170153472:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        member_data = load_member_data(user.id)
        member_data.wallet -= member_data.wallet
        member_data.bank -= member_data.bank
        await ctx.send(f"Wiped {user}'s account")
        save_member_data(user.id, member_data)
        if bool(log) == True:
            with open('F:\\bot\\logs\\errors.txt', 'a') as f:
                f.write(f'[{current_time}] {ctx.message.author.display_name} wiped {user.display_name}\'s profile.\n')
                f.close()
            print(f'[{current_time}] {ctx.message.author.display_name} {colors.red}wiped{colors.end} {user.display_name}\'s profile.')
        else:
            pass
    else:
        await ctx.reply('I dont think you are my dev')

@client.command(aliases=['bal'])
async def balance(ctx, user : discord.User=None):
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    if user == None:
        member_data = load_member_data(ctx.message.author.id)

        embed = discord.Embed(title=f"{ctx.message.author.display_name}'s Balance", color=theme_color)
        embed.add_field(name="Wallet", value=str(member_data.wallet))
        embed.add_field(name="Bank", value=str(member_data.bank))
        embed.set_footer(text=f'Currency api made by thatOneArchUser#5794, and deployed by {owner}')
        await ctx.send(embed=embed)
    else:
        member_data = load_member_data(user.id)

        embed = discord.Embed(title=f"{user.display_name}'s Balance", color=theme_color)
        embed.add_field(name="Wallet", value=str(member_data.wallet))
        embed.add_field(name="Bank", value=str(member_data.bank))
        embed.set_footer(text=f'Currency api made by thatOneArchUser#5794, and deployed by {owner}')
        await ctx.send(embed=embed)

@client.command(aliases=['inv'])
async def inventory(ctx):
    await ctx.reply(f'this command is disabled')
    return  # Must add later :>
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    member_data = load_member_data(ctx.message.author.id)

    e = discord.Embed(title=f"{ctx.message.author.display_name}'s Inventory", description=f'op item\n{member_data.op}')
    await ctx.send(embed=e)

@client.command()
async def shop(ctx):
    await ctx.reply(f'this command is disabled')
    return
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    e = discord.Embed(title='Shop', description="**Items:\nop item: 69,420 coins\nid: `op`") #will edit later
    await ctx.send(embed=e)

@client.command()
async def buy(ctx, *, arg1):
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if str(arg1) == 'op':
        member_data = load_member_data(ctx.message.author.id)
        if member_data.wallet < 69420:
            await ctx.send('You don\'t have 69,420 coins to buy this')
        else:
            member_data.wallet -= 69420
            member_data.op += 1
            save_member_data(ctx.message.author.id, member_data)
            await ctx.send(f'You bought 1 {msg.content}')
            if bool(log) == True:
                print(f'[{current_time}] {ctx.message.author.display_name} bought 1 {msg.content} from shop')
            else:
                pass
    elif str(arg1) == 'rich_person':
        await ctx.reply('This item has been removed from the shop as \'Rich Person\' role doesn\'t exist anymore.')
        return
        member_data = load_member_data(ctx.message.author.id)
        if member_data_wallet < 1000000:
            await ctx.reply('You don\'t have enough coins in your wallet to buy this')
            return
        elif "rich person" in ctx.message.author.roles:
            await ctx.reply('You already bought this')
            return
        else:
            member_data.wallet -= 1000000
            save_member_data(ctx.message.author.id, member_data)
            await ctx.message.author.add_roles("rich person")
            await ctx.reply('You bought the role \'rich person\' for 1,000,000 coins')
    else:
        await ctx.send(f'wtf is {arg1}?')

#hypixel skyblock api key: e7ca6250-5641-4e3e-ab5d-6e6c90502273
@client.command(aliases=["nw"])
async def networth(ctx, *, arg1, arg2=None):
    if arg2 == None:
        url = f'https://nariah-dev.com/api/networth/total/{arg1}/?key=e7ca6250-5641-4e3e-ab5d-6e6c90502273'
        r = requests.get(url)
        if r.status_code == 200:
            r.raise_for_status()
            jsonr = r.json()
            total = jsonr["total"]
            e = discord.Embed(title=f'{arg1}\'s Hypixel Skyblock networth', description=f'{total} coins')
            await ctx.send(embed=e)
        elif r.status_code == 500:
            await ctx.reply('An internal error occured')
        elif r.status_code == 404:
            jsonr = r.json()
            cause = jsonr["cause"]
            await ctx.reply(f'Error\nStatus code: {r.status_code}\nCause: {cause}')
        else:
            await ctx.reply(f'Undefined status code: {r.status_code}\ndm this to notsniped#6776')
    else:
        url = f'https://nariah-dev.com/api/networth/total/{arg1}/{arg2}?key=e7ca6250-5641-4e3e-ab5d-6e6c90502273'
        r = requests.get(url)
        if r.status_code == 200:
            r.raise_for_status()
            jsonr = r.json()
            total = jsonr["total"]
            e = discord.Embed(title=f'{arg1}\'s Hypixel Skyblock networth', description=f'{total} coins')
            e.set_footer(text=f'Profile: {arg2}')
            await ctx.send(embed=e)
        elif r.status_code == 500:
            await ctx.reply('An internal error occured')
        elif r.status_code == 404:
            await ctx.reply('Invalid username or profile')
        else:
            await ctx.reply(f'Undefined status code: {r.status_code}\ndm this to notsniped#6776')

@client.command(aliases=['ah'])
async def auctionhouse(ctx, *, arg1):
    url = f'https://nariah-dev.com/api/auctions/statistics/{arg1}'
    r = requests.get(url)
    if r.status_code == 200:
        r.raise_for_status()
        jsonr = r.json()
        data = jsonr["data"]
        # data of jsonr["data"]
        average = data["average"] #average price of an item
        minimum = data["min"] #minimum price of an item
        maximum = data["max"] #maximum price of an item
        item = arg1.replace("_", " ")
        e = discord.Embed(title=f'Auction house stats for {item}', description=f'Average price: {average}\nLowest price: {minimum}\nHighest price: {maximum}')
        await ctx.send(embed=e)
    elif r.status_code == 404:
        await ctx.reply(f'No such item ({id})')
    elif r.status_code == 500:
        await ctx.reply('An internal error occured')
    else:
        await ctx.reply(f'Undefined status code: {r.status_code}\nsend this to notsniped#6776') #possible status codes: 400, bad request

@client.command()
async def lbin(ctx, *, arg1):
    url = f'https://nariah-dev.com/api/auctions/statistics/{arg1}'
    r = requests.get(url)
    if r.status_code == 200:
        r.raise_for_status()
        jsonr = r.json()
        data = jsonr["data"]
        lbin = data["min"]
        item = arg1.replace("_", " ")
        e = discord.Embed(title=f'Lowest BIN for {item}', description=f'{lbin} coins')
        await ctx.send(embed=e)
    elif r.status_code == 404:
        await ctx.reply(f'No such item ({arg1})')
    elif r.status_code == 500:
        await ctx.reply('An internal error occured')
    else:
        await ctx.reply(f'Undefined status code: {r.status_code}\nsend this to notsniped#6776')

@client.command()
async def tempadmin(ctx, user : discord.User, arg1):
    if ctx.message.author.id == 738290097170153472:
        if arg1 == 'add':
            if user.id not in ids:
                ids.append(user.id)
                await ctx.reply(f'**{user.display_name}** is now a bot admin for this session')
            else:
                await ctx.reply(f'**{user.display_name}** is already a bot admin')
        elif arg1 == 'remove' or 'delete':
            if user.id not in ids:
                await ctx.reply(f'**{user.display_name}** is not a bot admin')
                return
            else:
                ids.remove(user.id)
                await ctx.reply(f'{user.display_name} is not a bot admin anymore')
    else:
        await ctx.reply('I am 101%% sure that this command doesn\'t exist :eyes:')
### Commands end ###        

### Slash commands ###
# option types:
# sub command: 1
# sub command group: 2
# string: 3
# int: 4
# bool: 5
# user: 6
# channel: 7
# role: 8

#@slash.slash(name="snipe", description="Shows the most recent deleted message")
#async def snipe(ctx: SlashContext):
#    channel = ctx.channel
#    try:
#        em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
#        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
#        await ctx.send(embed = em)
#    except:
#        await ctx.send(f"There are no recently deleted messages in #{channel.name}")

#@slash.slash(
#    name="balance",
#    description="Shows the money amount of a user",
#    options=[
#        create_option(
#            name="user",
#            description="Select a user",
#            option_type=6,
#            required=False
#        )
#    ]
#)
#async def balance(ctx: SlashContext, user:str):
#    if user == None:
#        member_data = load_member_data(ctx.message.author.id)
#
#        embed = discord.Embed(title=f"{ctx.message.author.display_name}'s Balance")
#        embed.add_field(name="Wallet", value=str(member_data.wallet))
#        embed.add_field(name="Bank", value=str(member_data.bank))
#        embed.set_footer(text=f'Currency api made by {owner}')
#        await ctx.send(embed=embed)
#    else:
#        member_data = load_member_data(user.id)
#
#        embed = discord.Embed(title=f"{user.display_name}'s Balance")
#        embed.add_field(name="Wallet", value=str(member_data.wallet))
#        embed.add_field(name="Bank", value=str(member_data.bank))
#        embed.set_footer(text=f'Currency api made by {owner}')
#        await ctx.send(embed=embed)

#@slash.slash(
#    name="edit",
#    description="Shows the most recent edited message"
#)
#async def edit(ctx: SlashContext):
#    try:
#        em = discord.Embed(description=f'**Message before**: {before}\n**Message after**:{after}')
#        em.set_footer(text=f'This message was edited by {author}')
#        await ctx.send(embed = em)
#    except:
#        await ctx.reply('No recent edited messages here :eues:')

#@slash.slash(
#    name="say",
#    description="null",
#    options=[
#        create_option(
#            name="text",
#            description="null",
#            option_type=3,
#            required=True
#        )
#    ]
#)
#async def say(ctx: SlashContext, text:str):
#    await ctx.send(text)

#@slash.slash(
#    name="sus",
#    description="tells if a user is sus",
#    options=[
#        create_option(
#            name="user",
#            description="is sus user",
#            option_type=6,
#            required=True
#        )
#    ]
#)
#async def sus(ctx: SlashContext, user:str):
#    susbool = [
#        True,
#        False
#    ]
#    isSus = random.choice(susbool)
#    if isSus == True:
#        await ctx.send(f'{user.mention} is very sus')
#    else:
#        await ctx.send(f'{user.mention} isn\'t sus')

#@slash.slash(
#    name="fstab",
#    description="fstab.goldfish"
#)
#async def fstab(ctx: SlashContext):
#    await ctx.send('https://cdn.discordapp.com/attachments/878297190576062515/879845618636423259/IMG_20210825_005111.jpg')

#@slash.slash(
#    name="ping",
#    description="shows bot ping",
#)
#async def ping(ctx: SlashContext):
#    await ctx.send(f'Pong! My ping is {round(client.latency * 1000)}ms')

#@slash.slash(
#    name="invite",
#    description="sends invite of bot"
#)
#async def invite(ctx: SlashContext):
#    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=859869941535997972&permissions=8&scope=bot")

#@slash.slash(
#    name="uptime",
#    description="shows bot uptime"
#)
#async def uptime(ctx: SlashContext):
#    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
#    await ctx.send(uptime)

#@slash.slash(
#    name="null",
#    description="null"
#)
#async def null(ctx: SlashContext):
#    await ctx.send("You got __null__ coins **dood**")

#@slash.slash(
#    name="networth",
#    description="shows the networth of a user",
#    options=[
#        create_option(
#            name="username",
#            description="show networth of a player",
#            option_type=3,
#            required=True
#        )
#    ]
#)
#async def networth(ctx: SlashContext, username:str):
#    url = f'https://nariah-dev.com/api/networth/total/{username}/?key=e7ca6250-5641-4e3e-ab5d-6e6c90502273'
#    r = requests.get(url)
#    if r.status_code == 200:
#           r.raise_for_status()      
#           jsonr = r.json()
#           total = jsonr["total"]
#           e = discord.Embed(title=f'{username}\'s Hypixel Skyblock networth', description=f'{total} coins')
#           await ctx.send(embed=e)
#    elif r.status_code == 500:
#        await ctx.send('An internal error occured')
#    elif r.status_code == 404:
#         jsonr = r.json()
#         cause = jsonr["cause"]
#         await ctx.send(f'Error\nStatus code: {r.status_code}\nCause: {cause}')
#    else:
#        await ctx.send(f'Undefined status code: {r.status_code}\ndm this to notsniped#6776')

#@slash.slash(
#    name="auction",
#    description="shows the auction house stats for an item",
#    options=[
#        create_option(
#            name="item id",
#            description="item id",
#            option_type=3,
#            required=True
#        )
#    ]
#)
#async def auction(ctx: SlashContext, id:str):
#    url = f'https://nariah-dev.com/api/auctions/statistics/{id}'
#    r = requests.get(url)
#    if r.status_code == 200:
#        r.raise_for_status()
#        jsonr = r.json()
#        data = jsonr["data"]
#        # data of jsonr["data"]
#        average = data["average"]
#        minimum = data["min"]
#        maximum = data["max"]
#        newstring = id.replace("_", " ")
#        e = discord.Embed(title=f'Auction house stats for {newstring}', description=f'Average price: {average}\nLowest price: {minimum}\nHighest price: {maximum}')
#        await ctx.send(embed=e)
#    elif r.status_code == 404:
#        await ctx.send(f'No such item ({id})')
#    elif r.status_code == 500:
#        await ctx.send('An internal error occured')
#    else:
#        await ctx.send(f'Undefined status code: {r.status_code}\ndm this to notsniped#6776')

#@slash.slash(
#    name="lbin",
#    description="shows the lowest BIN price of an item",
#    options=[
#        create_option(
#            name="item id",
#            description="item id",
#            option_type=3,
#            required=True
#        )
#    ]
#)
#async def lbin(ctx, id:str):
#    url = f'https://nariah-dev.com/api/auctions/statistics/{id}'
#    r = requests.get(url)
#    if r.status_code == 200:
#        r.raise_for_status()
#        jsonr = r.json()
#        data = jsonr["data"]
#        lbin = data["min"]
#        item = id.replace("_", " ")
#        e = discord.Embed(title=f'Lowest BIN for {item}', description=f'{lbin} coins')
#        await ctx.send(embed=e)
#    elif r.status_code == 404:
#        await ctx.send(f'No such item ({id})')
#    elif r.status_code == 500:
#        await ctx.send('An internal error occured')
#    else:
#        await ctx.send(f'Undefined status code: {r.status_code}\nsend this to notsniped#6776')

client.run('Insert token here')
