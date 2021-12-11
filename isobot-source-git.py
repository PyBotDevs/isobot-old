### Modules ###
import os
import time
import math
import pickle
import os.path
import discord
import datetime
import praw
import nekos
import nacl
import ffmpeg
import json
import aiohttp
import timefetch
import shutil
import threading
import clientmaster as cm
import helpdb.helpdb as helpdb
from random import randint
from random import choice
from discord import Embed
from discord import User
from discord.ext import commands
from discord.ext.commands import *
from discord.ext import tasks
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
### Modules end ###

### Startup/variables ###
ids = [
    # Your Discord ID here #
]
bad = [
    'fuck',
    'asshole',
    'nigga',
    'nigger',
    'motherfucker',
    'fuckyou',
    'cunt',
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
    'cock',
    'anus',
    'anal',
    'sex',
    'fucκ', # Greek #
    'shiτ', # Greek again .-. #,
    'penis'
]
whitelist = [
    'document',
    'cucumber',
    'sussex',
    'brainfuck',
    'sexy'
]
toLog = [
    # Your Discord Server ID here #
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
errHandlerVer = 'v2.4'
botVer = 'v4.1.7'
currencyVer = 'v2.5'
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
owner = 'notsniped#6776'
homedir = os.path.expanduser("~")
def get_prefix(client, message):
    with open('C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]
client = commands.Bot(command_prefix=(get_prefix), intents=intents)
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
buy = False
networth = True
lbin = True
ah = True
welcomer = True
theme_color = 0x8124af
color_success = 0x77b255
color_fail = 0xc92424
loggerHandler_path = 'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\log.txt'
errorHandler_path = 'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\errors.txt'
mainDB_path = '\\database.pickle'
configDB_path = '\\config.pickle'
error_display = '<:Isobot_Error:914807604511924224>'
warning_display = '<:Isobot_Warning:914807514837708852>'
### Functions and classes ###
if os.name == 'nt':
    data_filename = homedir + mainDB_path
    config_filename = homedir + configDB_path
else:
    data_filename = "/sdcard/Download/database.pickle"
    config_filename = '/sdcard/Download/config.pickle'


class Data:
    def __init__(self, wallet, bank, xp, level, rifle, bronze, silver, gold, platinum, shovel, fishingpole):
        self.wallet = wallet
        self.bank = bank
        self.xp = xp
        self.level = level
        self.rifle = rifle
        self.bronze = bronze
        self.silver = silver
        self.gold = gold
        self.platinum = platinum
        self.shovel = shovel
        self.fishingpole = fishingpole

class GData:
    def __init__(self, swearfilter, robX, giftX, levelingsystem):
        self.swearfilter = swearfilter
        self.rob = robX
        self.gift = giftX
        self.levelingsystem = levelingsystem

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
    
def load_config_data():
    if os.path.isfile(config_filename):
        with open(config_filename, "rb") as file2:
            return pickle.load(file2)
    else:
        return dict()

def load_member_data(member_ID):
    data = load_data()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]

def load_guild_data(guild_ID):
    data = load_config_data()

    if guild_ID not in data:
        return GData(1, 1, 1, 1)

    return data[guild_ID]

def save_member_data(member_ID, member_data):
    data = load_data()

    data[member_ID] = member_data

    with open(data_filename, "wb") as file:
        pickle.dump(data, file)

def save_config_data(guild_ID, guild_data):
    data = load_config_data()

    data[guild_ID] = guild_data

    with open(config_filename, "wb") as file:
        pickle.dump(data, file)

def get_time():
    current_time = timefetch.timenow

def consoleFunc():
    input('Bot> ')

### Functions and classes end ###

currency = True

## Events ###
@client.event
async def on_ready():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"chats (;help) | {str(len(client.guilds))} servers!"), status=discord.Status.online)
    print('Bot is online')
    print('==================')
    print('------------------')
    print('Bot Info')
    print(f'Bot version: {colors.cyan}{botVer}{colors.end}')
    print(f'Error handler version: {colors.cyan}{errHandlerVer}{colors.end}')
    print(f'Currency system version: {colors.cyan}{currencyVer}{colors.end}')
    print(f'Username: {colors.green}{client.user.name}{colors.end}\nId: {colors.green}{client.user.id}{colors.end}\nDeveloper name: {colors.green}{owner}{colors.end}')
    print('==================')
    try:
        client.load_extension("cogs.Music")
        print(f'Cogs loaded: {colors.green}SUCCESS{colors.end}')
    except:
        print(f'Cogs loaded: {colors.red}FAIL{colors.end}')
    print('==================')
    print('Server list:')
    print('------------------')
    for guild in client.guilds:
        guild_owner = client.get_user(guild.owner.id)
        print(f'Server name: {colors.green}{guild.name}{colors.end}\nServer id: {colors.cyan}{guild.id}{colors.end}\nMember count: {colors.green}{guild.member_count}{colors.end}\nServer owner: {colors.cyan}{guild_owner}{colors.end}\nServer owner id: {colors.green}{guild_owner.id}{colors.end}')
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
        botpath = 'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botcode.py'
        botsize = os.path.getsize(botpath)
        print(f'Bot file size: {botsize}b')
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
    current_time = timefetch.timenow
    if isinstance(error, CommandNotFound):
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at CommandNotFound. Details: This command does not exist.\n')
                f.close()
                print(f'[{current_time}] Ignoring exception at {colors.green}CommandNotFound{colors.end}. Details: This command does not exist. {colors.red}The user was not notified of this error. This error was logged at \'F:\\bot\\logs\\errors.txt\'{colors.end}')
        else:
            pass
    if isinstance(error, CommandOnCooldown):
        await ctx.send(f':stopwatch: Not now! Please try after **{str(datetime.timedelta(seconds=int(round(error.retry_after))))}**')
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at CommandOnCooldown. Details: This command is currently on cooldown.\n')
                f.close()
                print(f'[{current_time}] Ignoring exception at {colors.green}CommandOnCooldown{colors.end}. Details: This command is currently on cooldown. {colors.red}This error was logged at \'F:\\bot\\logs\\errors.txt\'{colors.end}')
        else:
            pass
    if isinstance(error, MissingRequiredArgument):
        await ctx.send('Missing required argument(s)', delete_after=8)
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at MissingRequiredArgument. Details: The command can\'t be executed because required arguments are missing.\n')
                f.close()
                print(f'[{current_time}] Ignoring exception at {colors.green}MissingRequiredArgument{colors.end}. Details: The command can\'t be executed because required arguments are missing. {colors.red}This error was logged at \'F:\\bot\\logs\\errors.txt\'{colors.end}')
        else:
            pass
    if isinstance(error, MissingPermissions):
        await ctx.send('You dont have permissions to use this command.', delete_after=8)
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at MissingPermissions. Details: The user doesn\'t have the required permissions.\n')
                f.close()
                print(f'[{current_time}] Ignoring exception at {colors.green}MissingPermissions{colors.end}. Details: The user doesn\'t have the required permissions. {colors.red}This error was logged at \'F:\\bot\\logs\\errors.txt\'{colors.end}')
        else:
            pass
    if isinstance(error, BadArgument):
        await ctx.send('Invalid argument.', delete_after=8)
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at BadArgument.\n')
                f.close()
                print(f'[{current_time}] Ignoring exception at {colors.green}BadArgument{colors.end}. {colors.red}This error was logged at \'F:\\bot\\logs\\errors.txt\'{colors.end}')
        else:
            pass
    if isinstance(error, BotMissingPermissions):
        await ctx.send('I don\'t have the required permissions to use this.')
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at BotMissingPermissions.\n Details: The bot doesn\'t have the required permissions.\n')
                f.close()
                print(f'[{current_time}] Ignoring exception at {colors.green}BotMissingPremissions{colors.end}. Details: The bot doesn\'t have the required permissions. {colors.red}This error was logged at \'F:\\bot\\logs\\errors.txt\'{colors.end}')
        else:
            pass
# Error handler end #

snipe_message_author = {}
snipe_message_content = {}

editsnipe_message_author = {}
editsnipe_messagebefore_content = {}
editsnipe_messageafter_content = {}
commandsIssued = 0
afk_messageset = {}

@client.event
async def on_message_delete(message):
    if not message.author.bot:
        server_actionlog = f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{message.guild.id}.txt'
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        guild = client.guilds[0]
        channel = message.channel
        snipe_message_author[message.channel.id] = message.author
        snipe_message_content[message.channel.id] = message.content
        if bool(log) == True:
            with open(server_actionlog, 'a') as f:
                f.write(f'[{current_time}] Message deleted by {snipe_message_author[channel.id]}.\n   Content: {snipe_message_content[channel.id]}\n')
                f.close()
            if message.guild.id == 880409977074888714:
                c = client.get_channel(897387063576506379)
                em = Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id], color=0xFFBF00)
                em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
                await c.send(embed = em)
            elif message.guild.id == 907212927076032513:
                c = client.get_channel(908591681459327006)
                em = Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id], color=0xFFBF00)
                em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
                await c.send(embed = em)
            else:
                pass
        else:
            pass
    else:
        pass

@client.event
async def on_message_edit(message_before, message_after):
    server_actionlog = f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{message_after.guild.id}.txt'
    gd_data = load_guild_data(message_after.guild.id)
    if not message_after.author.bot:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        editsnipe_message_author[message_before.channel.id] = message_before.author
        guild = message_before.guild.id
        channel = message_before.channel
        editsnipe_messagebefore_content[channel.id] = message_before.content
        editsnipe_messageafter_content[channel.id] = message_after.content
        if any(x in message_after.content.lower() for x in bad):
            if gd_data.swearfilter == 0:
                pass
            elif guild == 881865721754316822:
                pass
            else:
                await message_after.delete()
                await channel.send(f'{message_after.author.mention} watch your language.', delete_after=5)
        if bool(log):
            with open(server_actionlog, 'a') as f:
                f.write(f'[{current_time}] Message edited by {editsnipe_message_author[channel.id]}.\n   Message Before: {editsnipe_messagebefore_content[channel.id]}\n   Message After: {editsnipe_messageafter_content[channel.id]}')
                f.close()
            if guild == 880409977074888714:
                c = client.get_channel(897387314609786880)
                em = Embed(description = f"**Message before**: {message_before.content}\n**Message after**: {message_after.content}")
                em.set_footer(text = f"This message was edited by {message_before.author} in {channel}")
                await c.send(embed = em)
            else:
                pass
        else:
            pass
    else:
        pass
    

@client.event
async def on_member_join(member):
    server_actionlog = f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{member.guild.id}.txt'
    current_time = timefetch.timenow
    guild = member.guild.name
    guildID = member.guild.id
    if bool(log) == True:
        if os.name == 'nt':
            print(f'[{current_time}] {colors.cyan}{member}{colors.end} joined {colors.green}{guild}{colors.end}')
            try:
                with open(server_actionlog, 'a') as f:
                    f.write(f'[{current_time}] {member} joined {guild}\n')
                    f.close()
            except:
                print(f'[{current_time}] Ignoring exception at {colors.green}UnableToLog{colors.end}. {colors.red}This error was logged at C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\logs\\errors.txt{colors.end}')
        else:
            pass
    else:
        pass

@client.event
async def on_member_remove(member):
    server_actionlog = f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{member.guild.id}.txt'
    current_time = timefetch.timenow
    guild = member.guild.name
    if bool(log) == True:
        if os.name == 'nt':
            print(f'[{current_time}] {colors.cyan}{member}{colors.end} left {colors.green}{guild}{colors.end}')
            try:
                with open(server_actionlog, 'a') as f:
                    f.write(f'[{current_time}] {member} left {guild}\n')
                    f.close()
            except:
                print(f'[{current_time}] Ignoring exception at {colors.green}UnableToLog{colors.end}. {colors.red}This error was logged at C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\logs\\errors.txt{colors.end}')
        else:
            pass
    else:
        pass

@client.event
async def on_guild_join(guild):
    with open('C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = ';'
    with open('C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))
    with open('C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_message(message):
    gd_data = load_guild_data(message.guild.id)
    if bool(log) == True:
        if message.guild.id not in toLog:
            pass
        else:
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f'[{current_time}] {colors.cyan}{message.author.display_name}{colors.end} messaged in {colors.green}{message.guild.name} <#{message.channel.name}>{colors.end}: {message.content}')
    else:
        pass
    if '<@!738290097170153472>' not in message.content:
        pass
    else:
        print(f'{colors.cyan}{message.author.display_name}{colors.end} pinged you!\n     Content: {message.content}')
    if not message.author.bot:
        if message.content == '<@896437848176230411>':
            embedrescue = Embed(title='Bot not working?', description='If not commands aren\'t working, just type in `@isobot resetprefix`.', color=theme_color)
            message.channel.send(embed=embedrescue)
        else:
            pass
    else:
        pass
    if not message.author.bot:
        if message.content == '<@!896437848176230411> resetprefix':
            with open('C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\prefixes.json', 'r') as f:
                prefixes = json.load(f)
            prefixes[str(message.guild.id)] = ';'
            with open('C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\prefixes.json', 'w') as f:
                json.dump(prefixes, f, indent=4)
            await message.channel.send(f'Prefix successfully reset back to `;`')
        else:
            pass
    else:
        pass
    if not message.author.bot:
        if gd_data.swearfilter == 0:
            pass
        elif message.channel.id == 898358336804782182: # Swear channel in Taco Server #
            pass
        elif message.channel.id == 910071842159616010:
            pass
        else:
            if any(x in message.content.lower() for x in whitelist):
                pass
            elif any(x in message.content.lower() for x in bad):
                try:
                    await message.delete()
                except discord.errors.NotFound:
                    print(f'{colors.red}Error: Failed to delete message.{colors.end} Description: Message couldn\'t be found.')
                await message.channel.send(f'{message.author.mention} watch your language.', delete_after=5)
            else:
                pass
    else:
        pass
    if not message.author.bot:
        if gd_data.levelingsystem == 0:
            pass
        else:
            member_data = load_member_data(message.author.id)
            member_data.xp += randint(1, 5)
            if message.guild.id == 874160923860955136:
                channel_id = client.get_channel(912009910663909407)
                if member_data.level == 0:
                    if member_data.xp >= 25:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 1:
                    if member_data.xp >= 50:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 2:
                    if member_data.xp >= 100:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 3:
                    if member_data.xp >= 500:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 4:
                    if member_data.xp >= 750:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 5:
                    if member_data.xp >= 1000:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 6:
                    if member_data.xp >= 1200:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 7:
                    if member_data.xp >= 1400:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 8:
                    if member_data.xp >= 1600:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 9:
                    if member_data.xp >= 1800:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 10:
                    if member_data.xp >= 2000:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 11:
                    if member_data.xp >= 2200:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 12:
                    if member_data.xp >= 2400:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 13:
                    if member_data.xp >= 2600:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 14:
                    if member_data.xp >= 2800:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 15:
                    if member_data.xp >= 3000:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 16:
                    if member_data.xp >= 3200:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 17:
                    if member_data.xp >= 3400:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 18:
                    if member_data.xp >= 3600:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 19:
                    if member_data.xp >= 3800:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level >= 20:
                    if member_data.xp >= 4000:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                else:
                    pass
            else:
                if member_data.level == 0:
                    if member_data.xp >= 25:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 1:
                    if member_data.xp >= 50:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 2:
                    if member_data.xp >= 100:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 3:
                    if member_data.xp >= 500:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                elif member_data.level == 4:
                    if member_data.xp >= 750:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 5:
                    if member_data.xp >= 1000:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 6:
                    if member_data.xp >= 1200:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 7:
                    if member_data.xp >= 1400:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 8:
                    if member_data.xp >= 1600:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 9:
                    if member_data.xp >= 1800:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 10:
                    if member_data.xp >= 2000:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 11:
                    if member_data.xp >= 2200:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 12:
                    if member_data.xp >= 2400:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 13:
                    if member_data.xp >= 2600:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 14:
                    if member_data.xp >= 2800:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 15:
                    if member_data.xp >= 3000:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 16:
                    if member_data.xp >= 3200:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 17:
                    if member_data.xp >= 3400:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 18:
                    if member_data.xp >= 3600:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level == 19:
                    if member_data.xp >= 3800:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                    else:
                        pass
                elif member_data.level >= 20:
                    if member_data.xp >= 4000:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await message.channel.send(f"<@{message.author.id}>, you are now level **{member_data.level}**!")
                else:
                    pass
            save_member_data(message.author.id, member_data)
    else:
        pass
    await client.process_commands(message)

### Events end ###

### Commands ###

@client.command(aliases=['goldfish'])
async def fstab(ctx):
    global commandsIssued
    commandsIssued += 1
    await ctx.reply('https://cdn.discordapp.com/attachments/878297190576062515/879845618636423259/IMG_20210825_005111.jpg')

@client.command(aliases=['xp', 'level', 'lvl'])
async def rank(ctx, user:User=None):
    global commandsIssued
    commandsIssued += 1
    if user == None:
        member_data = load_member_data(ctx.message.author.id)
        e = Embed(title=f"{ctx.message.author.display_name}'s XP")
        if member_data.level == 0:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/25'))
        elif member_data.level == 1:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/50'))
        elif member_data.level == 2:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/100'))
        elif member_data.level == 3:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/500'))
        elif member_data.level == 4:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/750'))
        elif member_data.level == 5:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1000'))
        elif member_data.level == 6:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1200'))
        elif member_data.level == 7:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1400'))
        elif member_data.level == 8:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1600'))
        elif member_data.level == 9:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1800'))
        elif member_data.level == 10:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2000'))
        elif member_data.level == 11:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2200'))
        elif member_data.level == 12:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2400'))
        elif member_data.level == 13:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2600'))
        elif member_data.level == 14:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2800'))
        elif member_data.level == 15:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3000'))
        elif member_data.level == 16:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3200'))
        elif member_data.level == 17:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3400'))
        elif member_data.level == 18:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3600'))
        elif member_data.level == 19:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3800'))
        elif member_data.level >= 20:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/4000'))
        e.set_footer(text='To level up, keep on chatting!')
        await ctx.send(embed=e)
    else:
        member_data = load_member_data(user.id)
        e = Embed(title=f"{user.display_name}'s XP")
        if member_data.level == 0:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/25'))
        elif member_data.level == 1:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/50'))
        elif member_data.level == 2:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/100'))
        elif member_data.level == 3:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/500'))
        elif member_data.level == 4:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/750'))
        elif member_data.level == 5:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1000'))
        elif member_data.level == 6:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1200'))
        elif member_data.level == 7:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1400'))
        elif member_data.level == 8:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1600'))
        elif member_data.level == 9:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1800'))
        elif member_data.level == 10:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2000'))
        elif member_data.level == 11:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2200'))
        elif member_data.level == 12:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2400'))
        elif member_data.level == 13:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2600'))
        elif member_data.level == 14:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2800'))
        elif member_data.level == 15:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3000'))
        elif member_data.level == 16:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3200'))
        elif member_data.level == 17:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3400'))
        elif member_data.level == 18:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3600'))
        elif member_data.level == 19:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3800'))
        elif member_data.level >= 20:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/4000'))
        e.set_footer(text='To level up, keep on chatting!')
        await ctx.send(embed=e)

@client.command()
async def add_xp(ctx, user:User, *, arg1):
    global commandsIssued
    commandsIssued += 1
    if ctx.message.author.id not in ids:
        await ctx.reply(f'I am 101% sure this command doesn\'t exist :eyes:')
    else:
        if arg1.isdigit:
            member_data = load_member_data(user.id)
            member_data.xp += int(arg1)
            save_member_data(user.id, member_data)
        else:
            await ctx.reply(f'**{arg1}** is not a number.')

@client.command()
async def edit_snipe(ctx):
    global commandsIssued
    commandsIssued += 1
    try:
        em = Embed(description=f'**Message before**: {editsnipe_messagebefore_content[ctx.channel.id]}\n**Message after**:{editsnipe_messageafter_content[ctx.channel.id]}', color=theme_color)
        em.set_footer(text=f'This message was edited by {editsnipe_message_author[ctx.channel.id]}')
        await ctx.send(embed = em)
    except:
        await ctx.reply('No recent edited messages here :eyes:')

@client.command()
async def add_lvl(ctx, user : User, *, arg1):
    global commandsIssued
    commandsIssued += 1
    if ctx.message.author.id not in ids:
        await ctx.reply(f'101% sure that this command doesn\'t exist :eyes:')
    else:
        if arg1.isdigit:
            member_data = load_member_data(user.id)
            member_data.level += int(arg1)
            save_member_data(user.id, member_data)
        else:
            await ctx.reply(f'{arg1} is not a number lmao')

@client.command(aliases=['unload_pkg'])
async def unload_cog(ctx, pkg):
    global commandsIssued
    commandsIssued += 1
    if ctx.message.author.id not in ids:
        await ctx.reply('You aren\'t allowed to use this command.')
    else:
        if pkg == 'music':
            client.unload_extension('cogs.Music')
            e = Embed(title=f':white_check_mark: Package \'{pkg}\' successfully unloaded.', color=color_success)
            await ctx.send(embed=e)
        else:
            await ctx.reply(f'Package \'{pkg}\' could not be detected.')

@client.command(aliases=['load_pkg'])
async def load_cog(ctx, pkg):
    global commandsIssued
    commandsIssued += 1
    if ctx.message.author.id not in ids:
        await ctx.reply('You aren\'t allowed to use this command.')
    else:
        if pkg == 'music':
            client.load_extension('cogs.Music')
            e = Embed(title=f':white_check_mark: Package \'{pkg}\' successfully loaded.', color=color_success)
            await ctx.send(embed=e)
        else:
            await ctx.reply(f'Package \'{pkg}\' could not be detected.')

@client.command()
async def commandsissued(ctx):
    await ctx.send(f'**{commandsIssued}** total commands were issued during this session.')

@client.command()
async def invite(ctx):
    global commandsIssued
    commandsIssued += 1
    inviteLink = 'https://discord.com/oauth2/authorize?client_id=896437848176230411&permissions=8&scope=bot%20applications.commands'
    await ctx.reply(f'Invite isobot to your server with this link >> {inviteLink}')

@client.command()
async def say(ctx, *, text):
    global commandsIssued
    commandsIssued += 1
    await ctx.message.delete()
    await ctx.send(f'{text}')

@client.command()
async def uptime(ctx):
    global commandsIssued
    commandsIssued += 1
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    await ctx.send(f'I have been running for {uptime}.')

@client.command()
async def setmaintainance(ctx, status):
    global commandsIssued
    commandsIssued += 1
    if ctx.message.author.id not in ids:
        await ctx.send(f'{ctx.message.author.mention}, you cannot use this command.')
        return
    else:
        pass
    if status == 'true':
        await ctx.reply(':white_check_mark: Maintainance mode set.')
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"maintainance.exe"), status=discord.Status.dnd)
    elif status == 'false':
        await ctx.reply(':white_check_mark: Maintainance mode removed.')
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"chats (;help) | Servicing {str(len(client.guilds))} guilds"), status=discord.Status.online)
    else:
        await ctx.reply(f'{status} is not a valid argument. You can only use \'true\' or \'false\'')

@client.command()
async def snipe(ctx):
    global commandsIssued
    commandsIssued += 1
    channel = ctx.channel
    try:
        if any(x in snipe_message_content[channel.id] for x in bad):
            em = Embed(name = f"Last deleted message in #{channel.name}", description = f'||{snipe_message_content[channel.id]}||', color=0xcf1515)
            em.set_footer(text = f"WARNING! This message contains profane text.\nThis message was sent by {snipe_message_author[channel.id]}")
            await ctx.send(embed = em)
        else:
            em = Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id], color=theme_color)
            em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
            await ctx.send(embed = em)
    except:
        await ctx.send(f"There are no recently deleted messages in <#{channel.id}>")

@client.command()
async def whoAmI(ctx):
    global commandsIssued
    commandsIssued += 1
    embedWhoAmI = Embed(title='Who Am I', description=f'**I am:** {client.user.name}\n**My Discord id is:** {client.user.id}\n**My developer is:** {owner}\n**My ping is:** {round(client.latency * 1000)}ms\n**Your name is:** {ctx.message.author}\n**Your Discord id is:** {ctx.message.author.id}', color=theme_color)
    await ctx.send(embed = embedWhoAmI)

@client.command(aliases=['pong'])
async def ping(ctx):
    global commandsIssued
    commandsIssued += 1
    current_time = timefetch.timenow
    await ctx.send(f'Pong! My ping is `{round(client.latency * 1000)}ms`.')
    if bool(log) == True:
        with open(loggerHandler_path, 'a') as f:
            f.write(f'[{current_time}] Bot ping is {round(client.latency * 1000)}ms\n')
            f.close()
        print(f'[{current_time}] Bot ping is {colors.green}{round(client.latency * 1000)}ms{colors.end}')
        pass
    else:
        return

@client.command()
async def session(ctx):
    serverCount = str(len(client.guilds))
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    ping = int(round(client.latency * 1000))
    emb39 = Embed(title='Session Info', description='Information gets reset after the bot restarts', color=theme_color)
    emb39.add_field(name='Uptime', value=uptime)
    emb39.add_field(name='Ping (Current)', value=f'{ping}ms')
    emb39.add_field(name='Commands Issued', value=commandsIssued)
    emb39.add_field(name='Server Count', value=f'{serverCount} servers')
    await ctx.send(embed=emb39)

@client.command()
async def help(ctx, cmdhelp=None):
    global commandsIssued
    commandsIssued += 1
    if cmdhelp == 'work':
        cooldownTime = 1800
        cmdDisplay = helpdb.work1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'beg':
        cooldownTime = 30
        cmdDisplay = helpdb.beg1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'balance':
        cooldownTime = 0
        cmdDisplay = helpdb.bal1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'deposit':
        cooldownTime = 0
        cmdDisplay = helpdb.dep1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'withdraw':
        cooldownTime = 0
        cmdDisplay = helpdb.with1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'sell':
        cooldownTime = 0
        cmdDisplay = helpdb.sell1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'give':
        cooldownTime = 0
        cmdDisplay = helpdb.give1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'rob':
        cooldownTime = 40
        cmdDisplay = helpdb.rob1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'hunt':
        cooldownTime = 30
        cmdDisplay = helpdb.hunt1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'fish':
        cooldownTime = 15
        cmdDisplay = helpdb.fish1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'daily':
        cooldownTime = '1 day'
        cmdDisplay = helpdb.daily1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime}\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'weekly':
        cooldownTime = '1 week'
        cmdDisplay = helpdb.weekly1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime}\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'monthly':
        cooldownTime = '1 month'
        cmdDisplay = helpdb.monthly1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime}\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'postmeme':
        cooldownTime = 35
        cmdDisplay = helpdb.postmeme1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'dig':
        cooldownTime = 10
        cmdDisplay = helpdb.dig1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'kick':
        cooldownTime = 0
        cmdDisplay = helpdb.kick1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: moderators\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'ban':
        cooldownTime = 0
        cmdDisplay = helpdb.ban1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: moderators\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'say':
        cooldownTime = 0
        cmdDisplay = helpdb.say1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'nuke':
        cooldownTime = 0
        cmdDisplay = helpdb.nuke1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: moderators with **Manage Channel Permissions**\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'purge':
        cooldownTime = 0
        cmdDisplay = helpdb.purge1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: moderators\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'lock':
        cooldownTime = 0
        cmdDisplay = helpdb.lock1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: moderators with **Manage Channels Permission**\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'unlock':
        cooldownTime = 0
        cmdDisplay = helpdb.unlock1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: moderators with **Manage Channels Permission**\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'ping':
        cooldownTime = 0
        cmdDisplay = helpdb.ping1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'invites':
        cooldownTime = 0
        cmdDisplay = helpdb.invites1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'uptime':
        cooldownTime = 0
        cmdDisplay = helpdb.uptime1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'invite':
        cooldownTime = 0
        cmdDisplay = helpdb.invite1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'slap':
        cooldownTime = 0
        cmdDisplay = helpdb.slap1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'hug':
        cooldownTime = 0
        cmdDisplay = helpdb.hug1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'stare':
        cooldownTime = 0
        cmdDisplay = helpdb.stare1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'kill':
        cooldownTime = 0
        cmdDisplay = helpdb.kill1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'uwu':
        cooldownTime = 0
        cmdDisplay = helpdb.uwu1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'snipe':
        cooldownTime = 0
        cmdDisplay = helpdb.snipe1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'edit_snipe':
        cooldownTime = 0
        cmdDisplay = helpdb.edit_snipe1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'meme':
        cooldownTime = 0
        cmdDisplay = helpdb.meme1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'nothecker':
        cooldownTime = 0
        cmdDisplay = helpdb.nothecker1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'ihadastroke':
        cooldownTime = 0
        cmdDisplay = helpdb.ihadastroke1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'aww':
        cooldownTime = 0
        cmdDisplay = helpdb.aww1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'softwaregore':
        cooldownTime = 0
        cmdDisplay = helpdb.softwaregore1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'linuxmeme':
        cooldownTime = 0
        cmdDisplay = helpdb.linuxmeme1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'sus':
        cooldownTime = 0
        cmdDisplay = helpdb.sus1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == '8ball':
        cooldownTime = 0
        cmdDisplay = helpdb._8ball1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'amogus':
        cooldownTime = 0
        cmdDisplay = helpdb.amogus1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'fstab':
        cooldownTime = 0
        cmdDisplay = helpdb.fstab1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'whoAmI':
        cooldownTime = 0
        cmdDisplay = helpdb.whoAmI1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'warn':
        cooldownTime = 0
        cmdDisplay = helpdb.warn1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: moderators with **Manage Messages Permissions**\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'avatar':
        cooldownTime = 0
        cmdDisplay = helpdb.avatar1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'inventory':
        cooldownTime = 0
        cmdDisplay = helpdb.inventory1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'buy':
        cooldownTime = 0
        cmdDisplay = helpdb.buy1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'shop':
        cooldownTime = 0
        cmdDisplay = helpdb.shop1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'claimcatgirl':
        cooldownTime = 0
        cmdDisplay = helpdb.cg1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'viewsettings':
        cooldownTime = 0
        cmdDisplay = helpdb.vs1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'setfeature':
        cooldownTime = 0
        cmdDisplay = helpdb.sf1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: server administrators\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'scout':
        cooldownTime = 25
        cmdDisplay = helpdb.scout1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'networth':
        cooldownTime = 0
        cmdDisplay = helpdb.nw1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'roll':
        cooldownTime = 0
        cmdDisplay = helpdb.roll1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'serverinfo':
        cooldownTime = 0
        cmdDisplay = helpdb.si1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'play':
        cooldownTime = 0
        cmdDisplay = helpdb.play1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'pause':
        cooldownTime = 0
        cmdDisplay = helpdb.pause1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'skip':
        cooldownTime = 0
        cmdDisplay = helpdb.skip1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'stop':
        cooldownTime = 0
        cmdDisplay = helpdb.stop1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'loop':
        cooldownTime = 0
        cmdDisplay = helpdb.loop1
        helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: everyone\n\n*Note: Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
        await ctx.send(embed = helpSubCmdEmbed)
    elif cmdhelp == 'help':
        await ctx.reply('I think you already know how to use this command...')
    elif cmdhelp == None:
        helpEmbed = Embed(title='**MY COMMAND LIST**', description=f'My main prefix is **;**\nMy server prefix is **{(get_prefix)}**\n\n**Economy:**\n`work`, `beg`, `balance`, `deposit`, `withdraw`, `shop`, `buy`, `inventory`, `give`, `rob`, `hunt`, `fish`, `daily`, `weekly`, `monthly`, `postmeme`, `scout`\n\n**Music:**\n`join`, `play`, `skip`, `stop`, `volume`, `current`, `pause`, `queue`, `shuffle`, `remove`, `loop`\n\n**Bot Information:**\n`ping`, `invites`, `avatar`, `userinfo`, `whoAmI`, `invite`, `uptime`\n\n**Moderation:**\nban, kick, warn, purge, lock, unlock, viewsettings, setfeature, nuke\n\n**Misc:**\n8ball, slap, kill, hug, stare, uwu, snipe, edit_snipe, meme, linuxmeme, nothecker, aww, softwaregore, ihadastroke, amogus, fstab, say\n\nTo get help on a specific command, type in `;help [command name]`.', color=theme_color)
        await ctx.send(embed = helpEmbed)
    else:
        await ctx.reply(f'I can\'t find a command called {cmdhelp}.')

@client.command()
@commands.has_permissions(administrator=True)
async def actionloginfo(ctx):
    global commandsIssued
    commandsIssued += 1
    logname = f'{ctx.guild.id}.txt'
    logsize_raw = os.path.getsize(f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{ctx.guild.id}.txt')
    logsize_clean = f'{logsize_raw/1000}kb'
    emb1034 = Embed(title='Server Action Log File', color=theme_color)
    emb1034.add_field(name='Action Log File Name', value=str(f'{logname}'))
    emb1034.add_field(name='Action Log Size', value=f'{logsize_raw} bytes')
    emb1034.add_field(name='Action Log Size (KB)', value=f'{logsize_clean}')
    emb1034.set_thumbnail(url='https://notsniped.github.io/iso.bot/icons8-document-240.png')
    emb1034.set_footer(text='To view log content, do `;actionlog`\nTo archive the log, do `;archiveactionlog`')
    await ctx.send(embed = emb1034)

@client.command()
@commands.has_permissions(administrator=True)
async def actionlog(ctx):
    global commandsIssued
    commandsIssued += 1
    await ctx.send(file=discord.File(f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{ctx.guild.id}.txt'))

@client.command()
@commands.has_permissions(administrator=True)
async def archiveactionlog(ctx):
    global commandsIssued
    commandsIssued += 1
    logSize = os.path.getsize(f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{ctx.guild.id}.txt')
    src_path = f"C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{ctx.guild.id}.txt"
    dst_path = f"C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\archived\\{ctx.guild.id}.txt"
    shutil.move(src_path, dst_path)
    await ctx.send(f'Action log of size **{logSize} bytes** has been archived and cannot be viewed anymore.')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    global commandsIssued
    commandsIssued += 1
    responses = [
            "no?????",
            "When you grow a braincell, yes",
            "You stupid, of course not",
            "lol no",
            "Absolutely!",
            "Bet on it",
            "As I see it, yes.",
            "Most likely.",
            "Yes.",
            "Idfk",
            "Try again",
            "Not today.",
            "I\'m not very sure, but I think the answer is no.",
            "I\'m not very sure, but I think the answer is yes!",
            "brain.exe stopped responding.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Its a secret :>"
    ]
    ballEmbed= Embed(title=f':8ball: {question}', description=f'{choice(responses)}')
    await ctx.send(embed=ballEmbed)

@client.command(aliases=['hex', 'hexv', 'randhex'])
async def randomhex(ctx):
    global commandsIssued
    commandsIssued += 1
    r = lambda: randint(0,255)
    randhexv = '#%02X%02X%02X' % (r(),r(),r())
    emb0 = Embed(title='Random Hex Code', description=f'Hex Value: {randhexv}')
    await ctx.send(embed=emb0)

@client.command(aliases=['av'])
async def avatar(ctx, username:User=None):
    global commandsIssued
    commandsIssued += 1
    if username == None:
        userAvatar = ctx.message.author.avatar_url
        embed182 = Embed(title=f'{ctx.message.author}\'s avatar')
        embed182.set_image(url=userAvatar)
        await ctx.send(embed = embed182)
    else:
        userAvatar = username.avatar_url
        embed182 = Embed(title=f'{username}\'s avatar')
        embed182.set_image(url=userAvatar)
        await ctx.send(embed = embed182)

@client.command()
async def eues(ctx):
    global commandsIssued
    commandsIssued += 1
    await ctx.message.delete()
    await ctx.send(':eyes:')

@client.command()
async def cat(ctx):
    global commandsIssued
    commandsIssued += 1
    async with aiohttp.ClientSession() as session:
        async with session.get('http://aws.random.cat/meow') as r:
            if r.status == 200:
                js = await r.json()
                await ctx.send(js['file'])

@client.command()
async def fact(ctx):
    global commandsIssued
    commandsIssued += 1
    rand_fact = nekos.fact()
    await ctx.send(f'**A random fact**\n> {rand_fact}')

@client.command()
@commands.has_permissions(manage_channels=True)
async def nuke(ctx, channel: discord.TextChannel = None):
    global commandsIssued
    commandsIssued += 1
    server_actionlog = f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{ctx.guild.id}.txt'
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
            with open(server_actionlog, 'a') as f:
                f.write(f'[{current_time}] {ctx.message.author.display_name} nuked {nuke_channel}\n')
                f.close()
            print(f'[{current_time}] {ctx.message.author.display_name} nuked {nuke_channel}')
        else:
            pass
    else:
        await ctx.reply(f"No channel named {channel.name} was found!")

@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel = None):
    global commandsIssued
    commandsIssued += 1
    server_actionlog = f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{ctx.guild.id}.txt'
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
        sendEmbedLock = Embed(title=f':white_check_mark: **{lock_channel}** has been locked.', color=color_success)
        await ctx.channel.send(embed = sendEmbedLock)
        if bool(log) == True:
                with open(server_actionlog, 'a') as f:
                    f.write(f'[{current_time}] {ctx.message.author.display_name} locked {lock_channel}.\n')
                    f.close()
                print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} locked {colors.green}{lock_channel}{colors.end}.')
        else:
            pass
    else:
        await ctx.reply(f'No channel named {channel.name} was found.')

@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount:int, user:User=None):
    global commandsIssued
    commandsIssued += 1
    server_actionlog = f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{ctx.guild.id}.txt'
    if amount > 550:
        await ctx.reply('You have gone over the purge limit of `550` messages. Please try to purge less messages next time.')
        pass
    elif amount <= 0:
        await ctx.reply('You can\'t reverse purge messages.')
        pass
    else:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        await ctx.message.delete()
        if user == None:
            await ctx.channel.purge(limit=amount)
            embedSuccessPurge = Embed(title=':white_check_mark: Purge Successful', description=f'Purged {amount} messages from <#{ctx.channel.id}>.', color=color_success)
            await ctx.send(embed = embedSuccessPurge, delete_after=5)
        else:
            await ctx.user.purge(limit=amount)
            embedSuccessPurge = Embed(title=':white_check_mark: Purge Successful', description=f'Purged {amount} messages from user <@!{user.id}> in <#{ctx.channel.id}>.', color=color_success)
            await ctx.send(embed = embedSuccessPurge, delete_after=5)
        if bool(log) == True:
                with open(server_actionlog, 'a') as f:
                    f.write(f'[{current_time}] {ctx.message.author.display_name} purged {amount} from #{ctx.channel.name}.\n')
                    f.close()
                print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} purged {colors.green}{amount}{colors.end} messages from {colors.green}#{ctx.channel.name}{colors.end}.')
        else:
            pass

@client.command(aliases=['sp'])
@commands.has_permissions(manage_messages=True)
async def silentpurge(ctx, amount:int):
    global commandsIssued
    commandsIssued += 1
    server_actionlog = f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{ctx.guild.id}.txt'
    if amount > 550:
        await ctx.reply('You have gone over the purge limit of `550` messages. Please try to purge less messages next time.')
        pass
    elif amount <= 0:
        await ctx.reply('You can\'t reverse purge messages.')
        pass
    else:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
        if bool(log) == True:
                with open(server_actionlog, 'a') as f:
                    f.write(f'[{current_time}] {ctx.message.author.display_name} purged {amount} from #{ctx.channel.name}.\n')
                    f.close()
                print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} silent-purged {colors.green}{amount}{colors.end} messages from {colors.green}#{ctx.channel.name}{colors.end}.')
        else:
            pass

@client.command()
async def notify(ctx):
    await ctx.send(f'{error_display} This command has been removed.')

@client.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, user:User = None, *, warn_reason=None):
    global commandsIssued
    commandsIssued += 1
    server_actionlog = f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{ctx.guild.id}.txt'
    if user == None:
        await ctx.reply('Please mention a user when you want to warn someone next time.')
        return
    try:
        if warn_reason == None:
            warn_reason = '*Not provided*'
        embed67 = Embed(title=f'You were warned in {ctx.guild}.', description=f'Reason: {warn_reason}', color=theme_color)
        await user.send(embed = embed67)
        embed70 = Embed(title=f':white_check_mark: I successfully warned **{user}**.', color=color_success)
        await ctx.channel.send(embed = embed70)
    except:
        embed71 = Embed(title=f':x: Hold up!', description=f'I was unable to warn {user}.\nThis is usually caused due to the user not accepting DMs.', color=color_fail)
        await ctx.send(embed = embed71)

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel = None):
    global commandsIssued
    commandsIssued += 1
    server_actionlog = f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{ctx.guild.id}.txt'
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
        sendEmbedUnlock = Embed(title=f':white_check_mark: **{unlock_channel}** has been unlocked.', color=color_success)
        await ctx.channel.send(embed = sendEmbedUnlock)
        if bool(log) == True:
                with open(server_actionlog, 'a') as f:
                    f.write(f'[{current_time}] {ctx.message.author.display_name} unlocked {unlock_channel}.\n')
                    f.close()
                print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} unlocked {colors.green}{unlock_channel}{colors.end}.')
        else:
            pass
    else:
        await ctx.reply(f'No channel named {channel.name} was found.')

@client.command()
@commands.cooldown(1, 25, commands.BucketType.user)
async def scout(ctx):
    global commandsIssued
    commandsIssued += 1
    outcomes = [
        'found1',
        'found2',
        'notfound'
    ]
    outcome = choice(outcomes)
    if outcome == 'notfound':
        await ctx.reply('You searched the area, but you found nothing')
        return
    else:
        pass
    member_data = load_member_data(ctx.message.author.id)
    found = randint(100, 2000)
    member_data.wallet += found
    save_member_data(ctx.message.author.id, member_data)
    await ctx.reply(f'{ctx.message.author.mention} scouted the area and found **{found}** coins.')

@client.command()
async def invites(ctx, *, user : User=None):
    global commandsIssued
    commandsIssued += 1
    totalInvites = 0
    if user == None:
        for i in await ctx.guild.invites():
            if i.inviter == ctx.author:
                totalInvites += i.uses
        e = Embed(title=f'{ctx.message.author.display_name}\'s total invites', description=f"{totalInvites} invite{'' if totalInvites == 1 else 's'}", color=theme_color)
        await ctx.reply(embed=e)
    elif user.bot:
        await ctx.reply('This is a bot, not a user.')
        return
    else:
        for i in await ctx.guild.invites():
            if i.inviter == user:
                totalInvites += i.uses
        e = Embed(title=f'{user.display_name}\'s total invites', description=f"{totalInvites} invite{'' if totalInvites == 1 else 's'}", color=theme_color)
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
            await ctx.send('Ok')
        else:
            await ctx.send(f'Wtf is {msg.content}? You are supposed to reply with yes or no')
    else:
        await ctx.send(f'101% that this command doesn\'t exist :eyes:')

@client.command(aliases=['hl'])
@commands.cooldown(1, 40, commands.BucketType.user)
async def highlow(ctx):
    global commandsIssued
    commandsIssued += 1
    server_actionlog = f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{ctx.guild.id}.txt'
    current_time = timefetch.timenow
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
                with open(server_actionlog, 'a') as f:
                    f.write(f'[{current_time}]{ctx.message.author.display_name} won {coins} coins.\n')
                    f.close()
                print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} won {colors.green}{coins}{colors.end} coins.')
            else:
                pass
        elif numb < numb2:
            await ctx.send(f'Incorrect. The number was **{numb2}**')
        elif numb == numb2:
            await ctx.send(f'You stupid! You could won 1 million coins if you choose jackpot!!!')
    if msg.content == 'jackpot':
        if numb == numb2:
            coins2 = randint(1000000, 5000000)
            await ctx.send(f'Congrats, your number was {numb2} and you earned {coins2} coins gg!')
            member_data = load_member_data(id)
            member_data.wallet += coins2
            save_member_data(id, member_data)
            if bool(log) == True:
                with open(server_actionlog, 'a') as f:
                    f.write(f'[{current_time}] {ctx.message.author.display_name} earned {coins}.\n')
                    f.close()
                print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} earned {colors.green}{coins2}{colors.end} coins.')
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
                with open(server_actionlog, 'a') as f:
                    f.write(f'[{current_time}] {ctx.message.author.display_name} earned {coins} coins\n')
                    f.close()
                print(f'[{current_time}] {ctx.message.author.display_name} earned {coins} coins')
            else:
                pass
        else:
            await ctx.send(f'Incorrect your number was {numb2}')
    else:
        await ctx.send(f'{msg.content} is not an option')

@client.command()
async def kill(ctx, user : User):
    global commandsIssued
    commandsIssued += 1
    if user == None:
        await ctx.send('Please tag someone to kill')
    elif user.id == ctx.message.author.id:
        await ctx.send('Ok you are dead, please tag someone else to kill')
    else:
        responses2 = [
            f"<@{user.id}> died from a dang baguette.",
            f"<@{ctx.message.author.id}> strikes <@{user.id}> with the killing curse... *Avada Kedavra!*",
            f"<@{user.id}> dies from dabbing too hard.",
            f"<@{ctx.message.author.id}> yeeted <@{user.id}> out of a window.",
            f"<@{user.id}> dropped his phone on the floor and broke it.",
            f"<@{user.id}> rage-quit life."
        ]
        await ctx.send(f'{choice(responses2)}')

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, *, member:discord.Member):
    global commandsIssued
    commandsIssued += 1
    server_actionlog = f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{ctx.guild.id}.txt'
    current_time = timefetch.timenow
    if member == ctx.message.author:
        await ctx.reply('I don\'t think you want to kick yourself.')
        return
    else:
        try:
            await member.kick()
            embedKick = Embed(title=f':white_check_mark: *{member} has been **kicked** from the server.*', color=color_success)
            await ctx.send(embed=embedKick)
            if bool(log) == True:
                with open(server_actionlog, 'a') as f:
                    f.write(f'[{current_time}] {ctx.message.author.display_name} kicked {member.display_name} from {ctx.message.guild.name}\n')
                    f.close()
                print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} kicked {colors.green}{member.display_name}{colors.end} from {colors.green}{ctx.message.guild.name}{colors.end}.')
            else:
                pass
        except:
            embedKick = Embed(description=f':x: I was unable to kick {member}', color=color_fail)
            await ctx.send(embed=embedKick)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, *, member : discord.Member):
    global commandsIssued
    commandsIssued += 1
    server_actionlog = f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{ctx.guild.id}.txt'
    current_time = timefetch.timenow
    if member == ctx.message.author:
        await ctx.reply('I don\'t think you want to ban yourself.')
        return
    else:
        try:
            await member.ban()
            embedBan = Embed(title=f':white_check_mark: *{member} has been **banned** from the server.*', color=color_success)
            await ctx.send(embed=embedBan)
            if bool(log) == True:
                with open(server_actionlog, 'a') as f:
                    f.write(f'[{current_time}] {ctx.message.author.display_name} banned {member.display_name}.\n')
                    f.close()
                print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} banned {colors.green}{member.display_name}{colors.end} from {colors.green}{ctx.message.guild.name}{colors.end}')
            else:
                pass
        except:
            embedBan = Embed(description=f':x: I was unable to ban {member}', color=color_fail)
            await ctx.send(embed=embedBan)

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member:discord.Member):
    global commandsIssued
    commandsIssued += 1
    server_actionlog = f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{ctx.guild.id}.txt'
    current_time = timefetch.timenow
    if member == ctx.message.author:
        await ctx.reply('You can\'t unban yourself.')
        return
    else:
        try:
            await member.unban()
            embedUnban = Embed(title=f':white_check_mark: *{member} has been **unbanned** from the server.*', color=color_success)
            await ctx.send(embed=embedUnban)
            if bool(log) == True:
                with open(server_actionlog, 'a') as f:
                    f.write(f'[{current_time}] {ctx.message.author.display_name} unbanned {member.display_name} in {ctx.message.guild.name}\n')
                    f.close()
                print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} unbanned {colors.green}{member.display_name}{colors.end} in {colors.green}{ctx.message.guild.name}{colors.end}')
            else:
                pass
        except:
            embedUnban = Embed(description=f':x: I was unable to unban {member}', color=color_fail)
            await ctx.send(embed=embedUnban)

@client.command(aliases=["lm"])
async def linuxmeme(ctx):
    global commandsIssued
    commandsIssued += 1
    memes_submissions = reddit.subreddit('linuxmemes').hot()
    post_to_pick = randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embed = Embed(title = submission.title, color=theme_color)
    embed.set_image(url=submission.url)
    embed.set_footer(text='I use Arch BTW.')
    await ctx.send(embed = embed)

@client.command(aliases=["nh"])
async def nothecker(ctx):
    global commandsIssued
    commandsIssued += 1
    nothecker_submissions = reddit.subreddit('nothecker').hot()
    post_to_pick = randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in nothecker_submissions if not x.stickied)
    embed = Embed(title = submission.title, color=theme_color)
    embed.set_image(url=submission.url)
    embed.set_footer(text=':eues:')
    await ctx.send(embed = embed)

@client.command(aliases=['pet'])
async def aww(ctx):
    global commandsIssued
    commandsIssued += 1
    aww_submissions = reddit.subreddit('aww').hot()
    post_to_pick = randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in aww_submissions if not x.stickied)
    embed = Embed(title = submission.title, color=theme_color)
    embed.set_image(url=submission.url)
    embed.set_footer(text='Meow/Woof!')
    await ctx.send(embed = embed)

@client.command(aliases=['sg'])
async def softwaregore(ctx):
    global commandsIssued
    commandsIssued += 1
    sg_submissions = reddit.subreddit('softwaregore').hot()
    post_to_pick = randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in sg_submissions if not x.stickied)
    embed = Embed(title = submission.title, color=theme_color)
    embed.set_image(url=submission.url)
    embed.set_footer(text='Softwaregore be like')
    await ctx.send(embed = embed)

@client.command(aliases=['meem'])
async def meme(ctx):
    global commandsIssued
    commandsIssued += 1
    memes_submissions = reddit.subreddit('memes').hot()
    post_to_pick = randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embed = Embed(title = submission.title, color=theme_color)
    embed.set_image(url=submission.url)
    embed.set_footer(text='Meems be like')
    await ctx.send(embed = embed)

@client.command(aliases=['stokr', 'stork', 'stroke'])
async def ihadastroke(ctx):
    global commandsIssued
    commandsIssued += 1
    memes_submissions = reddit.subreddit('ihadastroke').hot()
    post_to_pick = randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embed = Embed(title = submission.title, color=theme_color)
    embed.set_image(url=submission.url)
    embed.set_footer(text='Stokr... Stork... Stroke.')
    await ctx.send(embed = embed)

@client.command(aliases=['upvote'])
async def vote(ctx):
    global commandsIssued
    commandsIssued += 1
    e = Embed(title='Vote for isobot on DBL and top.gg', description=f'Discord Bot List: https://discordbotlist.com/bots/halloween-isobot \ntop.gg: https://top.gg/bot/896437848176230411/vote', color=theme_color)
    await ctx.send(embed=e)

@commands.cooldown(1, 1800, commands.BucketType.user)
async def work(ctx):
    global commandsIssued
    commandsIssued += 1
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    current_time = timefetch.timenow
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
async def uwu(ctx, user:User):
    global commandsIssued
    commandsIssued += 1
    await ctx.send(f'{ctx.message.author.mention} uwu\'ed {user.display_name}. *uwu*')

@client.command()
async def slap(ctx, user:User):
    global commandsIssued
    commandsIssued += 1
    responses3 = [
        "https://cdn.weeb.sh/images/Hkw1VkYP-.gif",
        "https://cdn.weeb.sh/images/HkA6mJFP-.gif",
        "https://cdn.weeb.sh/images/Sk9mfCtY-.gif",
        "https://cdn.weeb.sh/images/HJKiX1tPW.gif"
    ]
    e = Embed(title=f'{ctx.message.author.display_name} slaps {user.display_name}. Oof, that must hurt...', color=theme_color)
    e.set_image(url=f'{choice(responses3)}')
    await ctx.send(embed = e)

@client.command()
async def hug(ctx, user:User):
    global commandsIssued
    commandsIssued += 1
    responses3 = [
        "https://cdn.weeb.sh/images/Sk80wyhqz.gif",
        "https://cdn.weeb.sh/images/S1DyFuQD-.gif",
        "https://cdn.weeb.sh/images/HyllFdmwZ.gif",
        "https://cdn.weeb.sh/images/Hyec_OmDW.gif",
        "https://cdn.weeb.sh/images/Hk3ox0tYW.gif"
    ]
    if user == ctx.message.author:
        await ctx.send(f'{ctx.message.author.mention}, you can\'t hug yourself!')
    else:
        e = Embed(title=f'{ctx.message.author.display_name} hugs {user.display_name}. Aww!', color=theme_color)
        e.set_image(url=f'{choice(responses3)}')
        await ctx.send(embed = e)

@client.command(aliases=['nw'])
async def networth(ctx, user:User=None):
    global commandsIssued
    commandsIssued += 1
    if user == None:
        member_data = load_member_data(ctx.message.author.id)
        wallet = int(member_data.wallet)
        bank = int(member_data.bank)
        embed694201 = Embed(title=f'{user.display_name}\'s Net Worth', description=f'{wallet + bank} coins', color=theme_color)
        await ctx.send(embed=embed694201)
    else:
        member_data = load_member_data(user.id)
        wallet = int(member_data.wallet)
        bank = int(member_data.bank)
        embed694201 = Embed(title=f'{user.display_name}\'s Net Worth', description=f'{wallet + bank} coins', color=theme_color)
        await ctx.send(embed=embed694201)

@client.command()
async def stare(ctx, user : User):
    global commandsIssued
    commandsIssued += 1
    responses3 = [
        "https://cdn.weeb.sh/images/HJxqIyFvZ.gif",
        "https://cdn.weeb.sh/images/Sk9jLJKvZ.gif",
        "https://cdn.weeb.sh/images/HJ6v8yYP-.gif",
        "https://cdn.weeb.sh/images/HyT3UkFwb.gif",
        "https://cdn.weeb.sh/images/Sk5BOdQIG.gif"
    ]
    if user == ctx.message.author:
        await ctx.send(f'{ctx.message.author.mention} idk what kind of logic this is, how do you stare at yourself?')
    else:
        e = Embed(title=f'{ctx.message.author.display_name} stares into {user.display_name}\'s eyes...', color=theme_color)
        e.set_image(url=f'{choice(responses3)}')
        await ctx.send(embed = e)

@client.command()
async def floppa(ctx):
    global commandsIssued
    commandsIssued += 1
    responses_floppa = [
        "https://cdni.rbth.com/rbthmedia/images/2021.05/original/60b4cf1d85600a4427115b02.jpg",
        "https://i.kym-cdn.com/entries/icons/original/000/034/421/cover1.jpg",
        "https://static.wikia.nocookie.net/floppapedia-revamped/images/9/96/Floppa.jpg/revision/latest?cb=20210223180751",
        "https://pbs.twimg.com/profile_images/1417930987372257297/yk4xiTv5_400x400.jpg",
        "https://i.pinimg.com/236x/90/ff/1f/90ff1f3ec129b93c251730f838cc2d06.jpg"
    ]
    e = Embed(title='Floppa', color=theme_color)
    e.set_image(url=f'{choice(responses_floppa)}')
    await ctx.send(embed = e)


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def guess(ctx):
    global commandsIssued
    commandsIssued += 1
    current_time = timefetch.timenow
    if bool(currency) == False:
        await ctx.message.channel.send('Currency is disabled')
        return
    else:
        pass
    member_data = load_member_data(ctx.message.author.id)
    await ctx.message.channel.send('Guess a number from 1 to 10')
    x = randint(1, 10)
    def check(msg):
        return msg.author == ctx.message.author and msg.channel == ctx.message.channel and int(msg.content) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    msg = await client.wait_for("message", check=check)
    if int(msg.content) == x:
        coins = randint(1, 100)
        await ctx.message.channel.send(f"Correct, you earned {coins} coins")
        member_data.wallet += coins
        save_member_data(ctx.message.author.id, member_data)
        if bool(log) == True:
            print(f'[{current_time}]{colors.cyan}{ctx.message.author.display_name}{colors.end} has earned {colors.green}{x}{colors.end} coins')
        else:
            pass
    else:
        await ctx.message.channel.send(f"Nope. It was {x}")

@client.command(aliases=['sus'])
async def isSus(ctx, *, user : User):
    global commandsIssued
    commandsIssued += 1
    susvar = [
        True,
        False
    ]
    sus = choice(susvar)
    if bool(sus) == True:
        await ctx.send(f'{user.mention} is very sus')
    elif bool(sus) == False:
        await ctx.send(f'{user.mention} isn\'t sus')
    else:
        await ctx.reply('undefined')

@client.command(aliases=['pm'])
@commands.cooldown(1, 40, commands.BucketType.user)
async def postmeme(ctx):
    global commandsIssued
    commandsIssued += 1
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    member_data = load_member_data(ctx.message.author.id)
    current_time = timefetch.timenow
    await ctx.send(f'**{ctx.message.author.mention} What type of meme you want to post?**\n`f` Fresh meme\n`d` Dank meme\n`c` Copypasta\n`k` Kind\n*more coming soon*')

    def check(msg):
        return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content) in ['f', 'd', 'c', 'k']
    
    msg = await client.wait_for("message", check=check)

    x = randint(0, 200)
    if x == 0:
        await ctx.send(f'{ctx.message.author.mention}, you posted it on the internet, but it is now a DEAD meme. You gained 0 coins.')
    else:
        await ctx.send(f'You earned {x} coins')
        member_data.wallet += x
        save_member_data(ctx.message.author.id, member_data)
        if bool(log) == True:
            print(f'[{current_time}]{colors.cyan}{ctx.message.author.display_name}{colors.end} has earned {colors.green}{x}{colors.end} coins')
        else:
            pass

@client.command()
async def roll(ctx, number_of_dice:int, number_of_sides:int):
    global commandsIssued
    commandsIssued += 1
    dice = [
        str(choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.reply('Number rolled is, '.join(dice))

@client.command(aliases=['si'])
async def serverinfo(ctx):
    global commandsIssued
    commandsIssued += 1
    serverthumbnail = ctx.guild.icon_url
    guildDesc = ctx.guild.description
    guildOwner = client.get_user(ctx.guild.owner.id)
    emb = Embed(title=f'{ctx.guild}\'s Server Information', description=guildDesc, color=theme_color)
    emb.add_field(name='Owner', value=str(guildOwner))
    emb.add_field(name='Server ID', value=int(ctx.guild.id), inline=True)
    emb.add_field(name='Total Members', value=int(ctx.guild.member_count), inline=True)
    emb.set_thumbnail(url=serverthumbnail)
    await ctx.send(embed=emb)

@client.command()
async def stab(ctx, user : User):
    global commandsIssued
    commandsIssued += 1
    e = Embed(title=f':knife: {ctx.message.author} fstabbed {user}. Oof! :knife:', description='That must really fstabbing hurt...', color=theme_color)
    await ctx.send(embed = e)

@client.command()
async def null(ctx):
    global commandsIssued
    commandsIssued += 1
    await ctx.reply('You got **null** coins dood.')

@client.command(aliases=['gift'])
async def give(ctx, user : User, *, arg1):
    global commandsIssued
    commandsIssued += 1
    gd_data = load_guild_data(ctx.guild.id)
    if user.id == ctx.message.author.id:
        await ctx.reply('You can\'t give coins to yourself')
        return
    elif gd_data.gift == 0:
        await ctx.reply('This feature has been disabled in this server.')
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
async def add(ctx, user:User, *, arg1=None):
    global commandsIssued
    commandsIssued += 1
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

@client.command(aliases=['vs'])
async def viewsettings(ctx):
    global commandsIssued
    commandsIssued += 1
    gd_data = load_guild_data(ctx.guild.id)
    embed1232 = Embed(title=f'Settings for {ctx.guild.name} ({ctx.guild.id})', description=f'Swear filter: {gd_data.swearfilter}\nLeveling: {gd_data.levelingsystem}\nRobbing: {gd_data.rob}\nGifting: {gd_data.gift}\n\n*1 = enabled\n0 = disabled*', color=theme_color)
    await ctx.send(embed=embed1232)

@client.command(aliases=['sf'])
@commands.has_permissions(administrator=True)
async def setfeature(ctx, name, status):
    global commandsIssued
    commandsIssued += 1
    if name == 'swearfilter':
        if status == 'true':
            gd_data = load_guild_data(ctx.guild.id)
            if gd_data.swearfilter == 1:
                await ctx.reply('This feature is already enabled in this server.')
                return
            gd_data.swearfilter += 1
            save_config_data(ctx.guild.id, gd_data)
            await ctx.reply('Successfully **enabled** swear-filter in this server.')
        elif status == 'false':
            gd_data = load_guild_data(ctx.guild.id)
            if gd_data.swearfilter == 0:
                await ctx.reply('This feature is already disabled in this server.')
                return
            gd_data.swearfilter -= 1
            save_config_data(ctx.guild.id, gd_data)
            await ctx.reply('Successfully **disabled** swear-filter in this server.')
    elif name == 'rob':
        if status == 'true':
            gd_data = load_guild_data(ctx.guild.id)
            if gd_data.rob == 1:
                await ctx.reply('This feature is already enabled in this server.')
                return
            gd_data.rob += 1
            save_config_data(ctx.guild.id, gd_data)
            await ctx.reply('Successfully **enabled** robbing in this server.')
        elif status == 'false':
            gd_data = load_guild_data(ctx.guild.id)
            if gd_data.rob == 0:
                await ctx.reply('This feature is already disabled in this server.')
                return
            gd_data.rob -= 1
            save_config_data(ctx.guild.id, gd_data)
            await ctx.reply('Successfully **disabled** robbing in this server.')
    elif name == 'gift':
        if status == 'true':
            gd_data = load_guild_data(ctx.guild.id)
            if gd_data.gift == 1:
                await ctx.reply('This feature is already enabled in this server.')
                return
            gd_data.gift += 1
            save_config_data(ctx.guild.id, gd_data)
            await ctx.reply('Successfully **enabled** gifting in this server.')
        elif status == 'false':
            gd_data = load_guild_data(ctx.guild.id)
            if gd_data.gift == 0:
                await ctx.reply('This feature is already disabled in this server.')
                return
            gd_data.gift -= 1
            save_config_data(ctx.guild.id, gd_data)
            await ctx.reply('Successfully **disabled** gifting in this server.')
    elif name == 'leveling':
        if status == 'true':
            gd_data = load_guild_data(ctx.guild.id)
            if gd_data.levelingsystem == 1:
                await ctx.reply('This feature is already enabled in this server.')
                return
            gd_data.levelingsystem += 1
            save_config_data(ctx.guild.id, gd_data)
            await ctx.reply('Successfully **enabled** leveling in this server.')
        elif status == 'false':
            gd_data = load_guild_data(ctx.guild.id)
            if gd_data.levelingsystem == 0:
                await ctx.reply('This feature is already disabled in this server.')
                return
            gd_data.levelingsystem -= 1
            save_config_data(ctx.guild.id, gd_data)
            await ctx.reply('Successfully **disabled** leveling in this server.')
    else:
        await ctx.reply('Either this feature cannot be disabled, or this feature doesn\'t exist.')

@client.command()
@commands.cooldown(1, 1800, commands.BucketType.user)
async def work(ctx):
    global commandsIssued
    commandsIssued += 1
    server_actionlog = f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{ctx.guild.id}.txt'
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    current_time = timefetch.timenow
    member_data = load_member_data(ctx.message.author.id)
    coins = randint(1000, 25000)
    member_data.wallet += coins
    await ctx.send(f"You earned {coins} coins.")
    save_member_data(ctx.message.author.id, member_data)
    if bool(log) == True:
        with open(server_actionlog, 'a') as f:
                f.write(f'[{current_time}] {ctx.message.author.display_name} earned {coins} coins.\n')
                f.close()
        print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} earned {colors.green}{coins}{colors.end} coins')
    else:
        pass

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def beg(ctx):
    global commandsIssued
    commandsIssued += 1
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    current_time = timefetch.timenow
    member_data = load_member_data(ctx.message.author.id)
    success = [
        "failure",
        "completed"
    ]
    successRate = choice(success)
    if successRate == 'failure':
        await ctx.reply(f'No one was kind enough to give you some change, *sad*')
    elif successRate == 'completed':
        coins = randint(10, 500)
        member_data.wallet += coins
        await ctx.send(f'A kind person decided to give you {coins} coins to help you with your needs. What a kind individual!')

    save_member_data(ctx.message.author.id, member_data)
    if bool(log) == True:
        print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} earned {colors.green}{coins}{colors.end} coins from begging.')
    else:
        pass

@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
    global commandsIssued
    commandsIssued += 1
    if bool(currency) == False:
        await ctx.reply('Currency is disabled')
        return
    else:
        pass
    current_time = timefetch.timenow 
    member_data = load_member_data(ctx.message.author.id)
    member_data.wallet += 10000
    await ctx.send('You claimed 10,000 coins')
    save_member_data(ctx.message.author.id, member_data)
    if bool(log) == True:
        print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} claimed {colors.green}10000{colors.end} coins from daily command.')
    else:
        pass

@client.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def fish(message):
    global commandsIssued
    commandsIssued += 1
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
    item = choice(items)
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
@commands.cooldown(1, 10, commands.BucketType.user)
async def dig(message):
    global commandsIssued
    commandsIssued += 1
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
    item = choice(items)
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
        await message.channel.send(f'You found someone else\'s shovel while digging. Finders keepers! It has been placed in your inventory for later use..')
        member_data.shovel += 1
        save_member_data(message.author.id, member_data)
    elif item == 'treasure_chest':
        member_data = load_member_data(message.author.id)
        await message.channel.send(f'You found a treasure chest while digging. On opening it turns out that it is full of gold. You lucky ducky! You sold it and got a 5000 coin bounty.')
        member_data.wallet += 5000
        save_member_data(message.author.id, member_data)

@client.command(aliases=['dep'])
async def deposit(ctx, *, arg1):
    global commandsIssued
    commandsIssued += 1
    current_time = timefetch.timenow
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        member_data = load_member_data(ctx.message.author.id)
        if arg1 == 'all' or arg1 == 'max':
            if member_data.wallet == 0:
                await ctx.reply('You don\'t have any coins in your wallet!')
                return
            else:
                if member_data.wallet == 1:
                    await ctx.reply(f'You deposited {member_data.wallet} coin to your bank account.')
                else:
                    await ctx.reply(f'You deposited {member_data.wallet} coins to your bank account.')
                member_data.bank += int(member_data.wallet)
                member_data.wallet -= int(member_data.wallet)
                await ctx.send(f'Now you have `{member_data.wallet}` coins in your wallet and `{member_data.bank}` coins in your bank account.')
                if bool(log) == True:
                    print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} deposited {colors.green}{member_data.wallet}{colors.end} coin\\s to their bank account.')
                else:
                    pass
                save_member_data(ctx.message.author.id, member_data)
                return
        elif arg1.isdigit:
            if int(arg1) > member_data.wallet:
                await ctx.reply('You don\'t have that many coins in your wallet.')
                return
            elif int(arg1) < 0:
                await ctx.reply('Don\'t try to break me **dood**')
                return
            else:
                await ctx.send(f'You deposited {arg1} coins to your bank account.')
                member_data.wallet -= int(arg1)
                member_data.bank += int(arg1)
                await ctx.send(f'Now you have `{member_data.wallet}` coins in your wallet and `{member_data.bank}` coins in your bank account.')
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
    global commandsIssued
    commandsIssued += 1
    current_time = timefetch.timenow
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        member_data = load_member_data(ctx.message.author.id)
        if arg1 == 'all' or arg1 == 'max':
            if member_data.bank == 0:
                await ctx.send('You don\'t have any coins in your bank account!')
                return
            else:
                if member_data.bank == 1:
                    await ctx.reply(f'You withdrawn {member_data.bank} coin from your bank account.')
                else:
                    await ctx.reply(f'You withdrawn {member_data.bank} coins from your bank account.')    
                member_data.wallet += int(member_data.bank)
                member_data.bank -= int(member_data.bank)
                await ctx.send(f'Now you have `{member_data.wallet}` coins in your wallet and `{member_data.bank}` coins in your bank account.')
                if bool(log) == True:
                    print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} withdrew {colors.green}{member_data.bank}{colors.end} coin\\s from their bank account.')
                else:
                    pass
                save_member_data(ctx.message.author.id, member_data)
                return
        elif arg1.isdigit:
            if int(arg1) > member_data.bank:
                await ctx.reply('You don\'t have that many coins in your bank!')
                return
            elif int(arg1) < 0:
                await ctx.reply('Don\'t try to break me dood')
                return
            else:
                await ctx.reply(f'You withdrawn {arg1} coins from your bank account.')
                member_data.wallet += int(arg1)
                member_data.bank -= int(arg1)
                await ctx.send(f'Now you have `{member_data.wallet}` coins in your wallet and `{member_data.bank}` coins in your bank account.')
                if bool(log) == True:
                    print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} withdrew {colors.green}{arg1}{colors.end} coin\\s from their bank account.')
                else:
                    pass
                save_member_data(ctx.message.author.id, member_data)
                return
        else:
            raise BadArgument

@client.command(aliases=['steal'])
@commands.cooldown(1, 40, commands.BucketType.user)
async def rob(ctx, *, user : User):
    global commandsIssued
    commandsIssued += 1
    gd_data = load_guild_data(ctx.guild.id)
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    elif gd_data.rob == 0:
        await ctx.reply('This command has been disabled in this server.')
        return
    else:
        pass
    current_time = timefetch.timenow
    if ctx.message.author.id == user.id:
        await ctx.send('You cant rob yourself XD')
        return
    elif user.id == 738290097170153472:
        await ctx.send('You can\'t rob the bot developer LOL')
        return
    elif user.id == 705462972415213588:
        await ctx.send('You can\'t rob the ||other|| bot developer LOL')
        return
    else:
        rand3 = [
            "success",
            "failure"
        ]
        rand3X = choice(rand3)
        vic_data = load_member_data(user.id)
        if vic_data.wallet < 500:
            save_member_data(user.id, vic_data)
            await ctx.reply('This user has less than 500 coins. Not worth it.')
        elif vic_data.wallet >= 500:
            if rand3X == 'failure':
                await ctx.reply(f'You tried robbing {user.display_name}, but you failed in doing so. Better luck next time')
                return
            elif rand3X == 'success':
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
                await ctx.send(f'You stole {coins} coins from **{user.display_name}**, you sussy!')
            

@client.command()
async def whoppa(ctx):
    global commandsIssued
    commandsIssued += 1
    e = Embed(title='Whoppa')
    e.set_image(url='https://upload.wikimedia.org/wikipedia/commons/b/b8/WHOPPER_with_Cheese%2C_at_Burger_King_%282014.05.04%29.jpg')
    await ctx.send(embed = e)

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def hunt(message):
    global commandsIssued
    commandsIssued += 1
    if bool(currency) == False:
        await message.channel.send('Currency is disabled')
        return
    else:
        pass
    member_data = load_member_data(message.author.id)
    if member_data.rifle < 1:
        await message.reply(f'You can\'t go hunting in the woods without a rifle. It\'s too dangerous! To make your life easier, buy a rifle from the shop with `;buy rifle`.')
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
    item = choice(items)
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
    elif item == 'sniper':
        await message.channel.send('You went for hunting and found a rifle. Very interesting! This item has been added to your inventory for later use.')
        member_data = load_member_data(message.author.id)
        member_data.rifle += 1
        save_member_data(message.author.id, member_data)
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
    global commandsIssued
    commandsIssued += 1
    server_actionlog = f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{message.guild.id}.txt'
    if bool(currency) == False:
        await message.channel.send('Currency is disabled')
        return
    else:
        pass
    current_time = timefetch.timenow
    member_data = load_member_data(message.author.id)
    member_data.wallet += 50000
    await message.channel.send('You claimed 50,000 coins')
    save_member_data(message.author.id, member_data)
    if bool(log) == True:
        with open(server_actionlog, 'a') as f:
                f.write(f'[{current_time}] {message.author.display_name} claimed 50000 coins from weekly command.\n')
                f.close()
        print(f'[{current_time}] {colors.cyan}{message.author.display_name}{colors.end} claimed {colors.green}50000{colors.end} coins from weekly command.')
    else:
        pass

@client.command()
@commands.cooldown(1, 2592000, commands.BucketType.user)
async def monthly(message):
    global commandsIssued
    commandsIssued += 1
    server_actionlog = f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{message.guild.id}.txt'
    if bool(currency) == False:
        await message.channel.send('Currency is disabled')
        return
    else:
        pass
    current_time = timefetch.timenow
    member_data = load_member_data(message.author.id)
    member_data.wallet += 100000
    await message.channel.send('You claimed 100,000 coins')
    save_member_data(message.author.id, member_data)
    if bool(log) == True:
        with open(server_actionlog, 'a') as f:
            f.write(f'[{current_time}] {message.author.display_name} claimed 100000 coins from monthly command.\n')
            f.close()
        print(f'[{current_time}] {colors.cyan}{message.author.display_name}{colors.end} claimed {colors.green}100000{colors.end} coins from monthly command.')
    else:
        pass

@client.command()
async def yearly(ctx):
    global commandsIssued
    commandsIssued += 1
    await ctx.reply('What are you thinking lol')

@client.command()
async def dev_claim(message):
    global commandsIssued
    commandsIssued += 1
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
        await message.channel.send('Are you the bot developer? No, I don\'t think so.')

@client.command()
async def wipe_user(ctx, *, user : User):
    global commandsIssued
    commandsIssued += 1
    if ctx.message.author.id == 738290097170153472:
        server_actionlog = f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{ctx.guild.id}.txt'
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        member_data = load_member_data(user.id)
        member_data.wallet -= member_data.wallet
        member_data.bank -= member_data.bank
        await ctx.send(f"Wiped {user}'s account")
        save_member_data(user.id, member_data)
        if bool(log) == True:
            with open(server_actionlog, 'a') as f:
                f.write(f'[{current_time}] {ctx.message.author.display_name} wiped {user.display_name}\'s profile.\n')
                f.close()
            print(f'[{current_time}] {ctx.message.author.display_name} {colors.red}wiped{colors.end} {user.display_name}\'s profile.')
        else:
            pass
    else:
        await ctx.reply('I dont think you are my developer. Are you?')

@client.command(aliases=['claimcg', 'ccg'])
async def claimcatgirl(ctx):
    global commandsIssued
    commandsIssued += 1
    cgid = nekos.img('neko')
    embed1919 = Embed(title='Random catgirl', description=f'To claim, simply pin the message')
    embed1919.set_image(url=cgid)
    await ctx.send(embed=embed1919)

@client.command(aliases=['bal'])
async def balance(ctx, user : User=None):
    global commandsIssued
    commandsIssued += 1
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    if user == None:
        member_data = load_member_data(ctx.message.author.id)
        embed = Embed(title=f"{ctx.message.author.display_name}'s Balance", color=theme_color)
        embed.add_field(name="Wallet", value=str(member_data.wallet))
        embed.add_field(name="Bank", value=str(member_data.bank))
        embed.add_field(name='Net worth', value=int(member_data.wallet) + int(member_data.bank))
        embed.set_footer(text=f'Currency api made by {owner}')
        await ctx.send(embed=embed)
    else:
        member_data = load_member_data(user.id)
        embed = Embed(title=f"{user.display_name}'s Balance", color=theme_color)
        embed.add_field(name="Wallet", value=str(member_data.wallet))
        embed.add_field(name="Bank", value=str(member_data.bank))
        embed.add_field(name='Net worth', value=int(member_data.wallet) + int(member_data.bank))
        embed.set_footer(text=f'Currency api made {owner}')
        await ctx.send(embed=embed)

@client.command(aliases=['ui'])
async def userinfo(ctx, user:User = None):
    global commandsIssued
    commandsIssued += 1
    if user == None:
        is_bot = 'NA'
        if ctx.author.bot == True:
            is_bot = 'Bot'
        elif ctx.author.bot == False:
            is_bot = 'Normal user'
        userAvatar = ctx.message.author.avatar_url
        embed683 = Embed(title=f'User info for {ctx.message.author}', description=f'User Name: {ctx.message.author}\nDisplay Name: {ctx.message.author.display_name}\nUser ID: {ctx.message.author.id}\nAvatar URL: {userAvatar}\nAccount Created: {ctx.message.author.created_at}\nUser Type: {is_bot}\n', color=ctx.message.author.colour)
        embed683.set_thumbnail(url=userAvatar)
        embed683.set_footer(text=f'User info requested by {ctx.message.author}', icon_url=str(ctx.message.author.avatar_url))
        await ctx.send(embed=embed683)
    else:
        is_bot = 'NA'
        if user.bot == True:
            is_bot = 'Bot'
        elif user.bot == False:
            is_bot = 'Normal user'
        await ctx.trigger_typing()
        userAvatar = user.avatar_url
        embed683 = Embed(title=f'User info for {user}', description=f'Display Name: {user.display_name}\nDiscord Tag: {user}\nUser ID: {user.id}\nAvatar URL: {userAvatar}\nAccount Created: {user.created_at}\nUser Type: {is_bot}\n', color=user.colour)
        embed683.set_thumbnail(url=userAvatar)
        embed683.set_footer(text=f'User info requested by {ctx.message.author}', icon_url=str(ctx.message.author.avatar_url))
        await ctx.send(embed=embed683)

@client.command(aliases=['inv'])
async def inventory(ctx, userINV:User=None):
    global commandsIssued
    commandsIssued += 1
    if bool(currency) == False:
        await ctx.reply('Currency is disabled.')
        return
    else:
        pass
    if userINV == None:
        member_data = load_member_data(ctx.message.author.id)
        e = Embed(title=f'{ctx.message.author.display_name}\'s Inventory', description=f'**Utility**\nHunting rifle: {member_data.rifle}\nFishing pole: {member_data.fishingpole}\nShovel: {member_data.shovel}\n\n**Economy**\nBronze isocoin: {member_data.bronze}\nSilver isocoin: {member_data.silver}\nGold isocoin: {member_data.gold}\nPlatinum isocoin: {member_data.platinum}', color=theme_color)
        await ctx.send(embed=e)
    else:
        member_data = load_member_data(userINV.id)
        e = Embed(title=f'{userINV.display_name}\'s Inventory', description=f'**Utility**\nHunting rifle: {member_data.rifle}\nFishing pole: {member_data.fishingpole}\nShovel: {member_data.shovel}\n\n**Economy**\nBronze isocoin: {member_data.bronze}\nSilver isocoin: {member_data.silver}\nGold isocoin: {member_data.gold}\nPlatinum isocoin: {member_data.platinum}', color=theme_color)
        await ctx.send(embed=e)

@client.command()
async def shop(ctx):
    global commandsIssued
    commandsIssued += 1
    if bool(currency) == False:
        await ctx.reply('Currency is disabled.')
        return
    else:
        pass
    embShop = Embed(title='Shop for Items', description='Available items:\n\n**Hunting rifle**\nDescription: This is a tool used for hunting. Well, I guess not many people can hunt with their bare hands...\nPrice: 10000 coins\nHow to buy: `;buy rifle`\n\n**Fishing pole**\nDescription: This is a tool used for fishing. Fish without it and the fish will fall right back into the water.\nPrice: 5000 coins\nHow to buy: `;buy fishingpole`\n\n**Shovel**\nDescription: This is a tool used for digging. You\'re not a dog, are you?\nPrice: 3500 coins\nHow to buy: `;buy shovel`\n\n**Bronze isocoin**\nDescription: This isocoin is for showing off to your friends and also a collectable.\nPrice: 25000 coins\nHow to buy: `;buy bronze`\n\n**Silver isocoin**\nDescription: This isocoin is for showing off to your friends and also a collectable.\nPrice: 50000 coins\nHow to buy: `;buy silver`\n\n**Gold isocoin**\nDescription: This isocoin is for showing off to your friends and also a collectable.\nPrice: 100000 coins\nHow to buy: `;buy gold`\n\n**Platinum isocoin**\nDescription: This isocoin is for showing off to your friends and also a collectable. You better be rich to buy this :smirk:\nPrice: 1000000 coins\nHow to buy: `;buy platinum`\nTo buy an item, run `;buy [item_name]` command.', color=theme_color)
    await ctx.send(embed = embShop)

@client.command()
async def buy(ctx, *, arg1):
    global commandsIssued
    commandsIssued += 1
    if bool(currency) == False:
        await ctx.reply('Currency is disabled.')
        return
    elif bool(buy) == False:
        await ctx.reply('This command is disabled.')
        return
    else:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        member_data = load_member_data(ctx.message.author.id)
        if str(arg1) == 'bronze':
            if member_data.wallet < 25000:
                await ctx.reply('You don\'t have enough coins to buy this item!')
            else:
                member_data.wallet -= 25000
                member_data.bronze += 1
                save_member_data(ctx.message.author.id, member_data)
                await ctx.reply('You just bought 1 **Bronze isocoin** from the shop! :coin:')
                if bool(log) == True:
                    print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} bought {colors.green}1 Bronze isocoin{colors.end} from the shop.')
                else:
                    pass
        elif str(arg1) == 'silver':
            if member_data.wallet < 50000:
                await ctx.reply('You don\'t have enough coins to buy this item!')
            else:
                member_data.wallet -= 50000
                member_data.silver += 1
                save_member_data(ctx.message.author.id, member_data)
                await ctx.reply('You just bought 1 **Silver isocoin** from the shop! :coin:')
                if bool(log) == True:
                    print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} bought {colors.green}1 Silver isocoin{colors.end} from the shop.')
                else:
                    pass
        elif str(arg1) == 'gold':
            if member_data.wallet < 100000:
                await ctx.reply('You don\'t have enough coins to buy this item!')
            else:
                member_data.wallet -= 100000
                member_data.gold += 1
                save_member_data(ctx.message.author.id, member_data)
                await ctx.reply('You just bought 1 **Gold isocoin** from the shop! :coin:')
                if bool(log) == True:
                    print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} bought {colors.green}1 Gold isocoin{colors.end} from the shop.')
                else:
                    pass
        elif str(arg1) == 'rifle':
            if member_data.wallet < 10000:
                await ctx.reply('You don\'t have enough coins to buy this item!')
            else:
                member_data.wallet -= 10000
                member_data.rifle += 1
                save_member_data(ctx.message.author.id, member_data)
                await ctx.reply('You just bought 1 **Hunting rifle** from the shop!')
                if bool(log) == True:
                    print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} bought {colors.green}1 Hunting rifle{colors.end} from the shop.')
                else:
                    pass
        elif str(arg1) == 'platinum':
            if member_data.wallet < 1000000:
                await ctx.reply('You don\'t have enough coins to buy this item!')
            else:
                member_data.wallet -= 1000000
                member_data.rifle += 1
                save_member_data(ctx.message.author.id, member_data)
                await ctx.reply('You just bought 1 **Platinum isocoin** from the shop!')
                if bool(log) == True:
                    print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} bought {colors.green}1 Platinum isocoin{colors.end} from the shop.')
                else:
                    pass
        elif str(arg1) == 'shovel':
            if member_data.wallet < 3500:
                await ctx.reply('You don\'t have enough coins to buy this item!')
            else:
                member_data.wallet -= 3500
                member_data.shovel += 1
                save_member_data(ctx.message.author.id, member_data)
                await ctx.reply('You just bought 1 **Shovel** from the shop!')
                if bool(log) == True:
                    print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} bought {colors.green}1 Shovel{colors.end} from the shop.')
                else:
                    pass
        elif str(arg1) == 'fishingpole':
            if member_data.wallet < 5000:
                await ctx.reply('You don\'t have enough coins to buy this item!')
            else:
                member_data.wallet -= 5000
                member_data.fishingpole += 1
                save_member_data(ctx.message.author.id, member_data)
                await ctx.reply('You just bought 1 **Fishing pole** from the shop!')
                if bool(log) == True:
                    print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} bought {colors.green}1 Fishing pole{colors.end} from the shop.')
                else:
                    pass
        else:
            await ctx.reply(f'{arg1} isn\'t a shop item.')

@client.command()
async def sell(ctx, *, item_name = None):
    global commandsIssued
    commandsIssued += 1
    member_data = load_member_data(ctx.message.author.id)
    if item_name == None:
        await ctx.reply(f'{ctx.message.author.mention}, you have to choose the item you want to sell.')
    elif item_name == 'shovel':
        member_data.shovel -= 1
        member_data.wallet += 1250
        save_member_data(ctx.message.author.id, member_data)
        await ctx.reply(f'You sold 1 shovel in the market and earned **1250 coins**!')
    elif item_name == 'rifle':
        member_data.rifle -= 1
        member_data.wallet += 5000
        save_member_data(ctx.message.author.id, member_data)
        await ctx.reply(f'You sold 1 hunting rifle in the market and earned **5000 coins**!')
    elif item_name == 'fishingpole':
        member_data.shovel -= 1
        member_data.wallet += 2500
        save_member_data(ctx.message.author.id, member_data)
        await ctx.reply(f'You sold 1 fishing pole in the market and earned **2500 coins**!')
    else:
        await ctx.reply(f'The item \'{item_name}\' doesn\'t exist or you cannot sell it.')

@client.command()
async def tempadmin(ctx, user : User, arg1):
    global commandsIssued
    commandsIssued += 1
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

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, prefix):
    global commandsIssued
    commandsIssued += 1
    with open('C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    with open('C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send(f'Prefix successfully changed to `{prefix}`')
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

@slash.slash(name="fstab", description="fstab.goldfish")
async def fstab(ctx:SlashContext):
    await ctx.send('https://cdn.discordapp.com/attachments/878297190576062515/879845618636423259/IMG_20210825_005111.jpg')

@slash.slash(name='userinvites', description='Shows how many people a user has invited to the server', options=[create_option(name='user', description='The user who you want to see total invites from', option_type=6, required=False)])
async def invites(ctx:SlashContext, user:str = None):
    totalInvites = 0
    if user == None:
        for i in await ctx.guild.invites():
            if i.inviter == ctx.author:
                totalInvites += i.uses
        e = Embed(title=f'{ctx.author.display_name}\'s total invites', description=f"{totalInvites} invite{'' if totalInvites == 1 else 's'}", color=theme_color)
        await ctx.reply(embed=e)
    elif user.bot:
        await ctx.reply('This is a bot, not a user.')
        return
    else:
        for i in await ctx.guild.invites():
            if i.inviter == user:
                totalInvites += i.uses
        e = Embed(title=f'{user.display_name}\'s total invites', description=f"{totalInvites} invite{'' if totalInvites == 1 else 's'}", color=theme_color)
        await ctx.reply(embed=e)

@slash.slash(name="snipe", description="Shows the most recent deleted message")
async def snipe(ctx:SlashContext):
    channel = ctx.channel
    try:
        em = Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
    except:
        await ctx.send(f"There are no recently deleted messages in <#{channel.id}>")

@slash.slash(name="editsnipe", description="Shows the most recent edited message")
async def editsnipe(ctx:SlashContext):
    try:
        em = Embed(description=f'**Message before**: {editsnipe_messagebefore_content[ctx.channel.id]}\n**Message after**:{editsnipe_messageafter_content[ctx.channel.id]}')
        em.set_footer(text=f'This message was edited by {editsnipe_message_author[ctx.channel.id]}')
        await ctx.send(embed = em)
    except:
        await ctx.reply('No recent edited messages here :eyes:')

@slash.slash(name='help', description='Shows a list of commands that I can run (; prefix commands only)')
async def help(ctx:SlashContext):
    helpEmbed = Embed(title='**MY COMMAND LIST**', description='My Brackets are **;**\n\nEconomy:\nwork, beg, balance, deposit, withdraw, shop, buy, inventory, give, rob, hunt, fish, daily, weekly, monthly, postmeme\n\nBot Information:\nping, invites, avatar, userinfo, whoAmI, invite, uptime\n\nModeration:\nban, kick, warn, purge, lock, unlock, viewsettings, setfeature, nuke\n\nMisc:\n8ball, slap, kill, hug, stare, uwu, snipe, edit_snipe, meme, linuxmeme, nothecker, aww, softwaregore, ihadastroke, amogus, fstab, say\n\nTo get help on a specific command, type in `;help [command name]`.', color=theme_color)
    await ctx.send(embed = helpEmbed)

@slash.slash(name="balance", description="Shows the money amount of a user", options=[create_option(name="user", description="The user you want to see the balance of", option_type=6, required=False)])
async def balance(ctx, user:str=None):
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    if user == None:
        member_data = load_member_data(ctx.author.id)
        embed = Embed(title=f"{ctx.author.display_name}'s Balance", color=theme_color)
        embed.add_field(name="Wallet", value=str(member_data.wallet))
        embed.add_field(name="Bank", value=str(member_data.bank))
        embed.add_field(name='Net worth', value=int(member_data.wallet) + int(member_data.bank))
        embed.set_footer(text=f'Currency api made by {owner}')
        await ctx.send(embed=embed)
    else:
        member_data = load_member_data(user.id)
        embed = Embed(title=f"{user.display_name}'s Balance", color=theme_color)
        embed.add_field(name="Wallet", value=str(member_data.wallet))
        embed.add_field(name="Bank", value=str(member_data.bank))
        embed.add_field(name='Net worth', value=int(member_data.wallet) + int(member_data.bank))
        embed.set_footer(text=f'Currency api made {owner}')
        await ctx.send(embed=embed)

@slash.slash(name='uptime', description='Shows how long the bot has been running for')
async def uptime(ctx:SlashContext):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    await ctx.send(f'I have been running for {uptime}.')

@slash.slash(
    name="say",
    description="Makes the bot say anything",
    options=[
        create_option(
            name="text",
            description="What you want the bot to say",
            option_type=3,
            required=True
        )
    ]
)
async def say(ctx: SlashContext, text:str):
    await ctx.send(text)

@slash.slash(name='meme', description='Finds a random popular meme from reddit')
async def meme(ctx:SlashContext):
    memes_submissions = reddit.subreddit('memes').hot()
    post_to_pick = randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embed = Embed(title = submission.title, color=theme_color)
    embed.set_image(url=submission.url)
    embed.set_footer(text='Meems be like')
    await ctx.send(embed = embed)

@slash.slash(name='softwaregore', description='Shows excellent examples of software failing (r/softwaregore)')
async def softwaregore(ctx:SlashContext):
    sg_submissions = reddit.subreddit('softwaregore').hot()
    post_to_pick = randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in sg_submissions if not x.stickied)
    embed = Embed(title = submission.title, color=theme_color)
    embed.set_image(url=submission.url)
    embed.set_footer(text='Softwaregore be like')
    await ctx.send(embed = embed)

@slash.slash(name='ihadastroke', description='I hab a strkke')
async def ihadastroke(ctx:SlashContext):
    memes_submissions = reddit.subreddit('ihadastroke').hot()
    post_to_pick = randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embed = Embed(title = submission.title, color=theme_color)
    embed.set_image(url=submission.url)
    embed.set_footer(text='Stokr... Stork... Stroke.')
    await ctx.send(embed = embed)

@slash.slash(name='linuxmeme', description='sudo apt-get install memes')
async def linuxmeme(ctx:SlashContext):
    memes_submissions = reddit.subreddit('linuxmemes').hot()
    post_to_pick = randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embed = Embed(title = submission.title, color=theme_color)
    embed.set_image(url=submission.url)
    embed.set_footer(text='I use Arch BTW.')
    await ctx.send(embed = embed)

@slash.slash(name='aww', description='Shows cute images of dogs, cats, birds, and other adorable animals')
async def aww(ctx:SlashContext):
    aww_submissions = reddit.subreddit('aww').hot()
    post_to_pick = randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in aww_submissions if not x.stickied)
    embed = Embed(title = submission.title, color=theme_color)
    embed.set_image(url=submission.url)
    embed.set_footer(text='Meow/Woof!')
    await ctx.send(embed = embed)

@slash.slash(name='kill', description='Kills your enemies', options=[create_option(name='user', description='The user who you want to kill', option_type=6, required=False)])
async def kill(ctx:SlashContext, user:str = None):
    if user == None:
        await ctx.send('Please tag someone to kill')
    elif user.id == ctx.author.id:
        await ctx.send('Ok you are dead, please tag someone else to kill')
    else:
        responses2 = [
            f"<@{user.id}> died from a dang baguette.",
            f"<@{ctx.author.id}> strikes <@{user.id}> with the killing curse... *Avada Kedavra!*",
            f"<@{user.id}> dies from dabbing too hard.",
            f"<@{ctx.author.id}> yeeted <@{user.id}> out of a window.",
            f"<@{user.id}> dropped his phone on the floor and broke it.",
            f"<@{user.id}> rage-quit life."
        ]
        await ctx.send(f'{choice(responses2)}')

@slash.slash(name='eightball', description='Let the 8ball predict the future! (please don\'t always take the 8ball seriously)', options=[create_option(name='question', description='What you want to ask the 8ball', option_type=3, required=True)])
async def eightball(ctx:SlashContext, question):
    responses = [
            "no?????",
            "When you grow a braincell, yes",
            "You stupid, of course not",
            "lol no",
            "Absolutely!",
            "Bet on it",
            "As I see it, yes.",
            "Most likely.",
            "Yes.",
            "Idfk",
            "Try again",
            "Not today.",
            "I\'m not very sure, but I think the answer is no.",
            "I\'m not very sure, but I think the answer is yes!",
            "brain.exe stopped responding.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Its a secret :>"
    ]
    ballEmbed= Embed(title=f':8ball: {question}', description=f'{choice(responses)}')
    await ctx.send(embed=ballEmbed)

@slash.slash(name='avatar', description='Fetches your avatar or a user\'s avatar', options=[create_option(name='user', description='Choose the user you want to pull an avatar from', option_type=6, required=False)])
async def avatar(ctx:SlashContext, user:str = None):
    if user == None:
        userAvatar = ctx.author.avatar_url
        embed182 = Embed(title=f'{ctx.author}\'s avatar')
        embed182.set_image(url=userAvatar)
        await ctx.send(embed = embed182)
    else:
        userAvatar = user.avatar_url
        embed182 = Embed(title=f'{user}\'s avatar')
        embed182.set_image(url=userAvatar)
        await ctx.send(embed = embed182)

@slash.slash(name='fact', description='Gives a random fact')
async def fact(ctx:SlashContext):
    rand_fact = nekos.fact()
    await ctx.send(f'**A random fact**\n> {rand_fact}')

@slash.slash(name='level', description='Shows your level, or the level of another user', options=[create_option(name='user', description='Displays the user\'s level', option_type=6, required=False)])
async def rank(ctx:SlashContext, user:str = None):
    if user == None:
        member_data = load_member_data(ctx.author.id)
        e = Embed(title=f"{ctx.author.display_name}'s XP")
        if member_data.level == 0:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/25'))
        elif member_data.level == 1:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/50'))
        elif member_data.level == 2:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/100'))
        elif member_data.level == 3:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/500'))
        elif member_data.level == 4:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/750'))
        elif member_data.level == 5:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1000'))
        elif member_data.level == 6:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1200'))
        elif member_data.level == 7:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1400'))
        elif member_data.level == 8:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1600'))
        elif member_data.level == 9:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1800'))
        elif member_data.level == 10:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2000'))
        elif member_data.level == 11:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2200'))
        elif member_data.level == 12:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2400'))
        elif member_data.level == 13:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2600'))
        elif member_data.level == 14:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2800'))
        elif member_data.level == 15:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3000'))
        elif member_data.level == 16:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3200'))
        elif member_data.level == 17:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3400'))
        elif member_data.level == 18:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3600'))
        elif member_data.level == 19:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3800'))
        elif member_data.level == 20:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/4000'))
        e.set_footer(text='To level up, keep on chatting!')
        await ctx.send(embed=e)
    else:
        member_data = load_member_data(user.id)
        e = Embed(title=f"{user.display_name}'s XP")
        if member_data.level == 0:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/25'))
        elif member_data.level == 1:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/50'))
        elif member_data.level == 2:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/100'))
        elif member_data.level == 3:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/500'))
        elif member_data.level == 4:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/750'))
        elif member_data.level == 5:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1000'))
        elif member_data.level == 6:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1200'))
        elif member_data.level == 7:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1400'))
        elif member_data.level == 8:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1600'))
        elif member_data.level == 9:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1800'))
        elif member_data.level == 10:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2000'))
        elif member_data.level == 11:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2200'))
        elif member_data.level == 12:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2400'))
        elif member_data.level == 13:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2600'))
        elif member_data.level == 14:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2800'))
        elif member_data.level == 15:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3000'))
        elif member_data.level == 16:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3200'))
        elif member_data.level == 17:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3400'))
        elif member_data.level == 18:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3600'))
        elif member_data.level == 19:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3800'))
        elif member_data.level >= 20:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/4000'))
        e.set_footer(text='To level up, keep on chatting!')
        await ctx.send(embed=e)

@slash.slash(name='kick', description='Kicks a member from the server', options=[create_option(name='member', description='The person you want to kick', option_type=6, required=True)])
async def kick(ctx:SlashContext, member:str):
    server_actionlog = f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{ctx.guild.id}.txt'
    current_time = timefetch.timenow
    if not ctx.author.guild_permissions.kick_members:
        await ctx.reply('You don\'t have permission to use this command.')
        return
    if member == ctx.author:
        await ctx.reply('I don\'t think you want to do that.')
        return
    else:
        try:
            await member.kick()
            embedKick = Embed(title=f':white_check_mark: *{member} has been **kicked** from the server.*', color=color_success)
            await ctx.send(embed=embedKick)
            if bool(log) == True:
                with open(server_actionlog, 'a') as f:
                    f.write(f'[{current_time}] {ctx.author.display_name} kicked {member.display_name} from {ctx.guild.name}\n')
                    f.close()
                print(f'[{current_time}] {colors.cyan}{ctx.author.display_name}{colors.end} kicked {colors.green}{member.display_name}{colors.end} from {colors.green}{ctx.guild.name}{colors.end}.')
            else:
                pass
        except:
            embedKick = Embed(description=f':x: I was unable to kick {member}', color=color_fail)
            await ctx.send(embed=embedKick)

@slash.slash(name='ban', description='Bans a member from the server', options=[create_option(name='member', description='The person you want to ban', option_type=6, required=True)])
async def ban(ctx:SlashContext, member:str):
    server_actionlog = f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{ctx.guild.id}.txt'
    current_time = timefetch.timenow
    if not ctx.author.guild_permissions.ban_members:
        await ctx.reply('You don\'t have permission to use this command.')
        return
    if member == ctx.author:
        await ctx.reply('I don\'t think you want to ban **yourself.**')
        return
    else:
        try:
            await member.ban()
            embedBan = Embed(title=f':white_check_mark: *{member} has been **banned** from the server.*', color=color_success)
            await ctx.send(embed=embedBan)
            if bool(log) == True:
                with open(server_actionlog, 'a') as f:
                    f.write(f'[{current_time}] {ctx.author.display_name} banned {member.display_name} from {ctx.guild.name}\n')
                    f.close()
                print(f'[{current_time}] {colors.cyan}{ctx.author.display_name}{colors.end} banned {colors.green}{member.display_name}{colors.end} from {colors.green}{ctx.guild.name}{colors.end}')
            else:
                pass
        except:
            embedBan = Embed(description=f':x: I was unable to ban {member}', color=color_fail) 

@slash.slash(name='purge', description='Deletes a specific amount of messages from the chat', options=[create_option(name='amount', description='The number of messages you want to purge (Maximum: 550)', option_type=4, required=True)])
async def purge(ctx:SlashContext, amount:int):
    server_actionlog = f'C:\\Users\\dbhat\\OneDrive\\Desktop\\botcode\\botLog\\actionlogs\\{ctx.guild.id}.txt'
    if not ctx.author.guild_permissions.manage_messages:
        await ctx.reply('You don\'t have permission to use this command.')
        return
    if amount > 550:
        await ctx.reply('You have gone over the purge limit of `550` messages. Please try to purge less messages next time.')
        pass
    elif amount <= 0:
        await ctx.reply('You can\'t reverse purge messages.')
        pass
    else:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        await ctx.channel.purge(limit=amount)
        embedSuccessPurge = Embed(title=':white_check_mark: Purge Successful', description=f'Purged {amount} messages from #{ctx.channel.name}.', color=color_success)
        await ctx.send(embed = embedSuccessPurge)
        if bool(log) == True:
                with open(server_actionlog, 'a') as f:
                    f.write(f'[{current_time}] {ctx.author.display_name} purged {amount} from #{ctx.channel.name}.\n')
                    f.close()
                print(f'[{current_time}] {colors.cyan}{ctx.author.display_name}{colors.end} purged {colors.green}{amount}{colors.end} messages from {colors.green}#{ctx.channel.name}{colors.end}.')
        else:
            pass

@slash.slash(name="sus", description="Tells if a user is sus", options=[create_option(name="user", description="is sus user", option_type=6, required=True)])
async def sus(ctx: SlashContext, user:str):
    susbool = [
        True,
        False
    ]
    isSus = choice(susbool)
    if isSus == True:
        await ctx.send(f'{user.mention} is very sus')
    else:
        await ctx.send(f'{user.mention} isn\'t sus')

@slash.slash(name="ping", description="Shows bot ping")
async def ping(ctx:SlashContext):
    await ctx.send(f'Pong! My ping is {round(client.latency * 1000)}ms')

@slash.slash(name="invite", description="Sends an invite link for isobot")
async def invite(ctx:SlashContext):
    inviteLink = 'https://discord.com/oauth2/authorize?client_id=896437848176230411&permissions=8&scope=bot%20applications.commands'
    await ctx.reply(f'Invite isobot to your server with this link >> {inviteLink}')

@slash.slash(name="null", description="null")
async def null(ctx:SlashContext):
    await ctx.reply("You got __null__ coins **dood**")

client.run(cm.bottoken)
