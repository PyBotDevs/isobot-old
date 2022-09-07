### Modules ###
import os
import time
import pickle
import os.path
import discord
import datetime
import praw
from ossapi import *
import nekos
import host
from host import keep_alive
import nacl
import ffmpeg
import json
import asyncio
import aiohttp
import timefetch
import requests
import psutil
import libs.api.auth
import libs.api.admins
import helpdb.helpdb as helpdb
from translate import Translator
from random import randint, choice
from discord import Embed, User
from discord.ext import commands, tasks
from discord.ext.commands import *
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow
### Modules end ###

### Startup/variables ###
ids = list(libs.api.admins.ids)
class emojis:
    economy = '<:isoecon:956175023977168926>'
    edit = '<:isoedit:956175024035885116>'
    info = '<:isoinfo:956175023721316383>'
    moderation = '<:isomod:956175023947784222>'
    music = '<:isomusic:956175023968751696>'
    reddit = '<:isoreddit:956176599693262888>'
    stream = '<:isostream:956175023817768963>'
with open('isobot/defaultswear.json', 'r') as f:
  imp = json.load(f)
  global bad
  bad = list(imp.keys())
whitelist = [
    'document',
    'cucumber',
    'sussex',
    'dickson',
    'class'
]
links = [
    'http://',
    'https://',
    'www.',
    'ww2.'
]
log = True
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
intents = discord.Intents.all()
errHandlerVer = 'v3.0.1'
botVer = '2022.501.0'
currencyVer = 'v2.7.4'
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
owner = 'notsniped#4573'
homedir = os.path.expanduser("~")
def get_prefix(client, message):
    with open('isobot/prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]
client = commands.Bot(command_prefix=(get_prefix), intents=intents)
slash = SlashCommand(client, sync_commands=True)
global startTime
startTime = time.time()
client.remove_command('help')
client.remove_command('membercount')
reddit = praw.Reddit(client_id='_pazwWZHi9JldA', client_secret='1tq1HM7UMEGIro6LlwtlmQYJ1jB4vQ', user_agent='idk', check_for_async=False)
api = OssapiV2(13110, 'UDGR1XA2e406y163lRzzJgs4tQCvu94ehbkXU8w2')
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
count = 0
theme_color = 0x8124af
color_success = 0x77b255
color_fail = 0xc92424
loggerHandler_path = 'isobot/botLog/log.txt'
errorHandler_path = "isobot/botLog/errors.txt"
mainDB_path = 'isobot/database.pickle'
configDB_path = 'isobot/config.pickle'
error_display = '<:Isobot_Error:914807604511924224>'
warning_display = '<:Isobot_Warning:914807514837708852>'
### Functions and classes ###
def convert(time):
  pos = ["s","m","h","d"]
  time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d": 3600*24}
  unit = time[-1]
  if unit not in pos:
    return -1
  try:
    val = int(time[:-1])
  except:
    return -2
  return val * time_dict[unit]

def convert_value(value):
  pos = ["k","m","b"]
  num_dict = {"k" : 1000, "m" : 1000000, "b" : 1000000000, "t": 1000000000000}
  unit = value[-1]
  if unit not in pos:
    raise SystemError("The unit you entered was invalid.")
  #try:
  val = int(value[:-1])
  #except:
  #  return -2
  return val * num_dict[unit]

if os.name == 'posix':
    data_filename = mainDB_path
    config_filename = configDB_path
else:
    data_filename = "/sdcard/Download/database.pickle"
    config_filename = '/sdcard/Download/config.pickle'

def randEmbedColor():
    return discord.Colour.random()

class Data:
    def __init__(self, wallet, bank, rifle, bronze, silver, gold, platinum, shovel, fishingpole, normalbox, probox, devbox, cbomb):
        self.wallet = wallet
        self.bank = bank
        self.rifle = rifle
        self.bronze = bronze
        self.silver = silver
        self.gold = gold
        self.platinum = platinum
        self.shovel = shovel
        self.fishingpole = fishingpole
        self.normalbox = normalbox
        self.probox = probox
        self.devbox = devbox
        self.cbomb = cbomb

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
  
## BADGES ##
with open('isobot/db/badges/prestige.json', 'r') as f:
    global prestige_conf
    prestige_conf = json.load(f)
## BOXES ##
with open('isobot/db/boxes/normalbox.json', 'r') as f:
    global normalbox
    normalbox = json.load(f)
with open('isobot/db/boxes/probox.json', 'r') as f:
    global probox
    probox = json.load(f)
with open('isobot/db/boxes/devbox.json', 'r') as f:
    global devbox
    devbox = json.load(f)
## CONFIGURATION ##
with open('isobot/db/config/levelup.json', 'r') as f:
    global levelupchannel
    levelupchannel = json.load(f)
with open('isobot/db/config/welcomer.json', 'r') as f:
    global welcomemsg
    welcomemsg = json.load(f)
with open('isobot/db/config/goodbye.json', 'r') as f:
    global goodbyemsg
    goodbyemsg = json.load(f)
with open('isobot/db/config/linkblocker.json', 'r') as f:
    global linkblocker
    linkblocker = json.load(f)
with open('isobot/db/config/passive.json', 'r') as f:
    global passivemode
    passivemode = json.load(f)
with open('isobot/db/globalwelcomer.json', 'r') as f:
    global welcomer
    welcomer = json.load(f)

with open(f'isobot/db/levels.json', 'r') as f:
    global levels
    levels = json.load(f)
with open(f'isobot/db/xp.json', 'r') as f:
    global exp
    exp = json.load(f)
with open(f'isobot/db/warnings.json', 'r') as f:
    global warnings
    warnings = json.load(f)
with open(f'isobot/db/serverbackups.json', 'r') as f:
    global serverbackups
    serverbackups = json.load(f)
with open(f'isobot/db/autoroles.json', 'r') as f:
    global autoroles
    autoroles = json.load(f)

def savejson():
    ## BADGES ##
    with open(f'isobot/db/badges/prestige.json', 'w+') as f:
        json.dump(prestige_conf, f, indent=4)
    ## BOXES ##
    with open(f'isobot/db/boxes/normalbox.json', 'w+') as f:
        json.dump(normalbox, f, indent=4)
    with open(f'isobot/db/boxes/probox.json', 'w+') as f:
        json.dump(probox, f, indent=4)
    with open(f'isobot/db/boxes/devbox.json', 'w+') as f:
        json.dump(devbox, f, indent=4)
    ## CONFIGURATION ##
    with open(f'isobot/db/config/levelup.json', 'w+') as f:
        json.dump(levelupchannel, f, indent=4)
    with open(f'isobot/db/config/welcomer.json', 'w+') as f:
        json.dump(welcomemsg, f, indent=4)
    with open(f'isobot/db/config/goodbye.json', 'w+') as f:
        json.dump(goodbyemsg, f, indent=4)
    with open(f'isobot/db/config/linkblocker.json', 'w+') as f:
        json.dump(linkblocker, f, indent=4)
    with open(f'isobot/db/config/passive.json', 'w+') as f:
        json.dump(passivemode, f, indent=4)
    with open(f'isobot/db/globalwelcomer.json', 'w+') as f:
        json.dump(welcomer, f, indent=4)
  
    with open(f'isobot/db/levels.json', 'w+') as f:
        json.dump(levels, f, indent=4)
    with open(f'isobot/db/xp.json', 'w+') as f:
        json.dump(exp, f, indent=4)
    with open(f'isobot/db/warnings.json', 'w+') as f:
        json.dump(warnings, f, indent=4)
    with open(f'isobot/db/serverbackups.json', 'w+') as f:
        json.dump(serverbackups, f, indent=4)
    with open(f'isobot/db/autoroles.json', 'w+') as f:
        json.dump(autoroles, f, indent=4)

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
        return Data(5000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]

def load_guild_data(guild_ID):
    data = load_config_data()

    if guild_ID not in data:
        return GData(0, 1, 1, 1)

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
    return timefetch.timenow

def returnhelp(cmdhelp:str, cmdDisplay, cooldownTime, availability:str):
    helpSubCmdEmbed = Embed(title=f'Help for **{cmdhelp} command**', description=f'Command name: {cmdhelp}\nUsage: `{cmdDisplay}`\nCooldown: {cooldownTime} seconds\nAvailability: {availability}\n\n*Anything in `[]` is compulsary and anything in `<>` is optional.*', color=theme_color)
    return helpSubCmdEmbed

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
        client.load_extension("cogs.eval")
        print(f'Cogs loaded: {colors.green}SUCCESS{colors.end}')
    except Exception as e:
        print(f'Cogs loaded: {colors.red}FAIL: {colors.end} Reason: {e}')
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
        print('==================')
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
        botpath = "isobot/main.py"
        botsize = os.path.getsize(botpath)
        print(f'Bot file size: {botsize}b')
        print('------------------')
    except FileNotFoundError:
        if os.name == 'posix':
            try:
                print('Bot file size: ' + os.path.getsize('/main.py'))
                print('------------------')
            except FileNotFoundError:
                print('Bot file size: ' + os.path.getsize(str(os.getcwd() + '/main.py')))
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
            print(f'[{current_time}] Ignoring exception at {colors.cyan}CommandNotFound{colors.end}. Details: This command does not exist. {colors.red}The user was not notified of this error. This error was logged at \'F:\\bot\\logs\\errors.txt\'{colors.end}')
        else:
            pass
    if isinstance(error, CommandOnCooldown):
        await ctx.send(f':stopwatch: Not now! Please try after **{str(datetime.timedelta(seconds=int(round(error.retry_after))))}**')
        if os.name == 'nt':
            print(f'[{current_time}] Ignoring exception at {colors.cyan}CommandOnCooldown{colors.end}. Details: This command is currently on cooldown. {colors.red}This error was logged at \'F:\\bot\\logs\\errors.txt\'{colors.end}')
        else:
            pass
    if isinstance(error, MissingRequiredArgument):
        await ctx.send(':warning: Missing required argument(s)', delete_after=8)
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at MissingRequiredArgument. Details: The command can\'t be executed because required arguments are missing.\n')
                f.close()
            print(f'[{current_time}] Ignoring exception at {colors.cyan}MissingRequiredArgument{colors.end}. Details: The command can\'t be executed because required arguments are missing. {colors.red}This error was logged at \'F:\\bot\\logs\\errors.txt\'{colors.end}')
        else:
            pass
    if isinstance(error, MissingPermissions):
        await ctx.send(':x: You dont have permissions to use this command.', delete_after=8)
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at MissingPermissions. Details: The user doesn\'t have the required permissions.\n')
                f.close()
            print(f'[{current_time}] Ignoring exception at {colors.cyan}MissingPermissions{colors.end}. Details: The user doesn\'t have the required permissions. {colors.red}This error was logged at \'F:\\bot\\logs\\errors.txt\'{colors.end}')
        else:
            pass
    if isinstance(error, BadArgument):
        await ctx.send(':x: Invalid argument.', delete_after=8)
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at BadArgument.\n')
                f.close()
            print(f'[{current_time}] Ignoring exception at {colors.cyan}BadArgument{colors.end}. {colors.red}This error was logged at \'F:\\bot\\logs\\errors.txt\'{colors.end}')
        else:
            pass
    if isinstance(error, BotMissingPermissions):
        await ctx.send(':x: I don\'t have the required permissions to use this.')
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at BotMissingPermissions.\n Details: The bot doesn\'t have the required permissions.\n')
                f.close()
            print(f'[{current_time}] Ignoring exception at {colors.cyan}BotMissingPremissions{colors.end}. Details: The bot doesn\'t have the required permissions. {colors.red}This error was logged at \'F:\\bot\\logs\\errors.txt\'{colors.end}')
        else:
            pass
    if isinstance(error, BadBoolArgument):
        await ctx.send(':x: Invalid true/false argument.', delete_after=8)
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at BadBoolArgument.\n')
                f.close()
            print(f'[{current_time}] Ignoring exception at {colors.cyan}BadBoolArgument{colors.end}. {colors.red}This error was logged at \'F:\\bot\\logs\\errors.txt\'{colors.end}')
        else:
            pass
# Error handler end #

snipe_message_author = {}
snipe_message_content = {}
editsnipe_message_author = {}
editsnipe_messagebefore_content = {}
editsnipe_messageafter_content = {}
slashCommandsIssued = 0
prefixCommandsIssued = 0

@client.event
async def on_message_delete(message):
    if not message.author.bot:
        channel = message.channel
        snipe_message_author[message.channel.id] = message.author
        snipe_message_content[message.channel.id] = message.content
        if bool(log) == True:
            if message.guild.id == 880409977074888714:
                c = client.get_channel(897387063576506379)
                em = Embed(title=f"Message deleted by {snipe_message_author[channel.id]}", description = f'**Message content**```{snipe_message_content[channel.id]}```', color=discord.Color.red())
                em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]} in #{channel.name}")
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
    gd_data = load_guild_data(message_after.guild.id)
    if not message_after.author.bot:
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
            if guild == 880409977074888714:
                c = client.get_channel(897387063576506379)
                em = Embed(title=f'Message edited by {message_before.author}', description = f"**Message before**```{message_before.content}```\n**Message after**```{message_after.content}```", color=discord.Color.orange())
                em.set_footer(text = f"This message was edited in #{channel}")
                await c.send(embed = em)
            else:
                pass
        else:
            pass
    else:
        pass
    
@client.event
async def on_member_kick(guild, member):
    guild = member.guild.name
    if bool(log) == True:
        if guild == 880409977074888714:
            c = client.get_channel(897387063576506379)
            em = Embed(title=f'Member kicked in {guild.name}', description = f"**User:**```{member}```", color=discord.Color.red())
            await c.send(embed = em)
        else:
            pass
    else:
        pass
@client.event
async def on_member_ban(guild, member):
    if bool(log) == True:
        if guild == 880409977074888714:
            c = client.get_channel(897387063576506379)
            em = Embed(title=f'Member banned in {guild.name}', description = f"**User:**```{member}```", color=discord.Color.red())
            await c.send(embed = em)
        else:
            pass
    else:
        pass
@client.event
async def on_member_unban(guild, member):
    if bool(log) == True:
        if guild == 880409977074888714:
            c = client.get_channel(897387063576506379)
            em = Embed(title=f'Member unbanned in {guild.name}', description = f"**User:**```{member}```", color=discord.Color.orange())
            await c.send(embed = em)
        else:
            pass
    else:
        pass
@client.event
async def on_invite_create(invite):
    guild = invite.guild
    if bool(log) == True:
        if guild.id == 880409977074888714:
            c = client.get_channel(897387063576506379)
            em = Embed(title=f'A new server invite for {guild.name} was created', description = f"**Invite link:**```{invite}```", color=discord.Color.green())
            await c.send(embed = em)
        else:
            pass
    else:
        pass
@client.event
async def on_invite_delete(invite):
    guild = invite.guild
    if bool(log) == True:
        if guild.id == 880409977074888714:
            c = client.get_channel(897387063576506379)
            em = Embed(title=f'A server invite for {guild.name} was revoked', description = f"**Revoked invite link:**```{invite}```", color=discord.Color.red())
            await c.send(embed = em)
        else:
            pass
    else:
        pass

@client.event
async def on_member_join(member):
    current_time = timefetch.timenow
    if welcomemsg[str(member.guild.id)] == 0:
        pass
    else:
        try:
            await member.send(f'{welcomemsg[str(member.guild.id)]}\n\n*Sent from: {member.guild.name}*')
        except:
            print(f'[{current_time}]: [Main/WARN]: Ignoring exception at {colors.cyan}BadRequest{colors.end}. {colors.red}Error code: 400, Details: Cannot send DM messages to this user{colors.end}')
    if welcomer[str(member.guild.id)] == 0:
        pass
    else:
        channel = client.get_channel(welcomer[str(member.guild.id)])
        await channel.send(f'{member.mention} has joined {member.guild}!')
    if autoroles[str(member.guild.id)] == 0:
      pass
    else:
      await member.add_roles(autoroles[str(member.guild.id)], reason="Server autorole")

@client.event
async def on_member_remove(member):
    current_time = timefetch.timenow
    if goodbyemsg[str(member.guild.id)] == 0:
        pass
    else:
        try:
            await member.send(f'{goodbyemsg[str(member.guild.id)]}\n\n*Sent from: {member.guild.name}*')
        except:
            print(f'[{current_time}]: [Main/WARN]: Ignoring exception at {colors.cyan}BadRequest{colors.end}. {colors.red}Error code: 400, Details: Cannot send DM messages to this user{colors.end}')

@client.event
async def on_guild_join(guild):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"chats (;help) | {str(len(client.guilds))} servers!"), status=discord.Status.online)
    with open("isobot/prefixes.json", 'r') as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = ';'
    with open("isobot/prefixes.json", 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"chats (;help) | {str(len(client.guilds))} servers!"), status=discord.Status.online)
    with open("isobot/prefixes.json", 'r') as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))
    with open("isobot/prefixes.json", 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_role_create(role):
    guild = role.guild.id
    if bool(log):
        if guild == 880409977074888714:
            c = client.get_channel(897387063576506379)
            em = Embed(title=f'New role created in {role.guild.name}', description = f"**Role name:**```{role.name}```", color=discord.Color.green())
            await c.send(embed = em)
        else:
            pass
    else:
        pass

@client.event
async def on_guild_role_delete(role):
    guild = role.guild.id
    if bool(log):
        if guild == 880409977074888714:
            c = client.get_channel(897387063576506379)
            em = Embed(title=f'Existing role deleted in {role.guild.name}', description = f"**Role name:**```{role.name}```", color=discord.Color.red())
            await c.send(embed = em)
        else:
            pass
    else:
        pass

@client.event
async def on_message(message):
    prefixes = {}
    gd_data = load_guild_data(message.guild.id)
    with open("isobot/prefixes.json", 'r') as f:
      prefixes = json.load(f)
    if str(message.guild.id) in prefixes:
      pass
    else:
      prefixes[str(message.guild.id)] = ";"
      with open("isobot/prefixes.json", 'w') as f:
        json.dump(prefixes, f, indent=4)
    ## BOXES DATA ##
    if str(message.author.id) in normalbox:
        pass
    else:
        normalbox[str(message.author.id)] = 1
    if str(message.author.id) in probox:
        pass
    else:
        probox[str(message.author.id)] = 0
    if str(message.author.id) in devbox:
        pass
    else:
        devbox[str(message.author.id)] = 0
    ## BADGES DATA ##
    if str(message.author.id) in prestige_conf:
        pass
    else:
        prestige_conf[str(message.author.id)] = 0
    ## CONFIGURATION DATA ##
    if str(message.guild.id) in levelupchannel:
        pass
    else:
        levelupchannel[str(message.guild.id)] = 0
    if str(message.guild.id) in welcomemsg:
        pass
    else:
        welcomemsg[str(message.guild.id)] = 0
    if str(message.guild.id) in goodbyemsg:
        pass
    else:
        goodbyemsg[str(message.guild.id)] = 0
    if str(message.guild.id) in linkblocker:
        pass
    else:
        linkblocker[str(message.guild.id)] = 0
    if str(message.author.id) in passivemode:
        pass
    else:
        passivemode[str(message.author.id)] = 0
    if str(message.guild.id) in welcomer:
        pass
    else:
        welcomer[str(message.guild.id)] = 0
    if str(message.guild.id) in autoroles:
        pass
    else:
        autoroles[str(message.guild.id)] = 0
    ## LEVELING SYSTEM ##
    if str(message.guild.id) in levels:
        pass
    else:
        levels[str(message.guild.id)] = {}
    if str(message.author.id) in levels[str(message.guild.id)]:
        pass
    else:
        levels[str(message.guild.id)][str(message.author.id)] = 0
    if str(message.guild.id) in exp:
        pass
    else:
        exp[str(message.guild.id)] = {}
    if str(message.author.id) in exp[str(message.guild.id)]:
        pass
    else:
        exp[str(message.guild.id)][str(message.author.id)] = 0
    ## WARNING SYSTEM ##
    if str(message.guild.id) in warnings:
        pass
    else:
        warnings[str(message.guild.id)] = {}
    if str(message.author.id) in warnings[str(message.guild.id)]:
        pass
    else:
        warnings[str(message.guild.id)][str(message.author.id)] = []
    savejson()

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
                    print(f'{colors.red}[Main/WARN]: Failed to delete message.{colors.end} Description: Message content 404ed.')
                await message.channel.send(f'{message.author.mention} watch your language.', delete_after=5)
            else:
                pass
        if linkblocker[str(message.guild.id)] == 0:
            pass
        else:
            if any(x in message.content.lower() for x in links):
                try:
                    await message.delete()
                except discord.errors.NotFound:
                    print(f'{colors.red}[Main/WARN]: Failed to delete message.{colors.end} Description: Message content 404ed.')
                await message.channel.send(f'{message.author.mention} no links allowed.', delete_after=5)
            else:
                pass
    else:
        pass

    if not message.author.bot:
        if gd_data.levelingsystem == 0:
            pass
        else:
            exp[str(message.guild.id)][str(message.author.id)] += randint(1, 5)
            channelid = None
            if levelupchannel[str(message.guild.id)] == 0:
                channelid = message.channel
            else:
                channelid = client.get_channel(levelupchannel[str(message.guild.id)])
            xpreq = 0
            for level in range(int(levels[str(message.guild.id)][str(message.author.id)])):
                xpreq += 50
                if xpreq >= 5000:
                    break
            if exp[str(message.guild.id)][str(message.author.id)] >= xpreq:
                exp[str(message.guild.id)][str(message.author.id)] = 0
                levels[str(message.guild.id)][str(message.author.id)] += 1
                await channelid.send(f"{message.author.mention}, you are now level **{levels[str(message.guild.id)][str(message.author.id)]}**!")
            savejson()
    else:
        pass
    await client.process_commands(message)

### Events end ###

### Commands ###

@client.command()
async def add_xp(ctx, user:User, *, arg1):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if ctx.author.id not in ids:
        return
    else:
        if arg1.isdigit:
            exp[str(ctx.guild.id)][str(user.id)] += int(arg1)
            savejson()
            await ctx.reply(f'Added `{arg1}` XP to {user.display_name}\'s account.')
        else:
            await ctx.reply(f'**{arg1}** is not a number.')

@client.command()
async def edit_snipe(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    try:
        em = Embed(description=f'**Message before**: {editsnipe_messagebefore_content[ctx.channel.id]}\n**Message after**:{editsnipe_messageafter_content[ctx.channel.id]}', color=theme_color)
        em.set_footer(text=f'This message was edited by {editsnipe_message_author[ctx.channel.id]}')
        await ctx.send(embed = em)
    except:
        await ctx.reply('No recent edited messages here :eyes:')

@client.command(aliases=['set_lvl', 'change_lvl'])
@commands.has_permissions(administrator=True)
async def set_level(ctx, user:User, *, arg1):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if arg1.isdigit:
        if arg1 < 1:
            await ctx.reply(':warning: You can\'t set a member\'s level less than `1`.')
            return
        else:
            pass
        levels[str(ctx.guild.id)][str(user.id)] = int(arg1)
        await ctx.reply(f'Added `{arg1}` level(s) to {user.display_name}\'s account.')
        savejson()
    else:
        await ctx.reply(f'{arg1} is not a number rolling_eyes:')

@client.command()
async def unload(ctx, pkg):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if ctx.author.id not in ids:
        return
    else:
        try:
            client.unload_extension(f'cogs.{pkg}')
            await ctx.send(f':white_check_mark: Package \'{pkg}\' unloaded.')
        except:
            await ctx.reply(f'**Error:** \'{pkg}\' is an unknown package.')

@client.command()
async def load(ctx, pkg):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if ctx.author.id not in ids:
        return
    else:
        try:
            client.load_extension(f'cogs.{pkg}')
            await ctx.send(f':white_check_mark: Package \'{pkg}\' loaded.')
        except:
            await ctx.reply(f'**Error:** \'{pkg}\' is an unknown package.')

@client.command()
async def reload(ctx, pkg):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if ctx.author.id not in ids:
        return
    else:
        try:
            client.unload_extension(f'cogs.{pkg}')
            time.sleep(0.2)
            client.load_extension(f'cogs.{pkg}')
            await ctx.send(f':white_check_mark: Package \'{pkg}\' reloaded.')
        except:
            await ctx.reply(f'**Error:** \'{pkg}\' is an unknown package.')

@client.command()
async def commandsissued(ctx):
    await ctx.send(f'**{prefixCommandsIssued + slashCommandsIssued}** total commands were issued during this session. They include:\n   **{prefixCommandsIssued}** normal commands\n   **{slashCommandsIssued}** slash commands')

@client.command()
async def invite(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    inviteLink = 'https://discord.com/oauth2/authorize?client_id=896437848176230411&permissions=8&scope=bot%20applications.commands'
    await ctx.reply(f'Invite isobot to your server with this link >> {inviteLink}')

@client.command()
async def say(ctx, *, text):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    await ctx.message.delete()
    if '@everyone' in ctx.message.content:
        return
    else:
        pass
    if ctx.author.id in ids:
      pass
    else:
      text.append(f' - _{ctx.author.display_name}_')
    await ctx.send(text)

@client.command()
async def uptime(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    await ctx.send(f'I have been running for {uptime}.')

@client.command()
async def snipe(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    channel = ctx.channel
    try:
        if any(x in snipe_message_content[channel.id].lower() for x in bad):
            em = Embed(name = f"Last deleted message in #{channel.name}", description = f'||{snipe_message_content[channel.id]}||', color=0xcf1515)
            em.set_footer(text = f"WARNING! This message contains profane text.\nThis message was sent by {snipe_message_author[channel.id]}")
            await ctx.send(embed = em)
        else:
            em = Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id], color=theme_color)
            em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
            await ctx.send(embed = em)
    except:
        await ctx.send(f"There are no recently deleted messages in <#{channel.id}>")

@client.command(aliases=['pong'])
async def ping(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
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
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    botcpu = psutil.cpu_percent(4)
    serverCount = str(len(client.guilds))
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    ping = int(round(client.latency * 1000))
    emb39 = Embed(title='Session Info', description='Information gets reset after the bot restarts', color=theme_color)
    emb39.add_field(name='Uptime', value=uptime)
    emb39.add_field(name='Ping (Current)', value=f'{ping}ms')
    emb39.add_field(name='Commands Issued', value=prefixCommandsIssued + slashCommandsIssued)
    emb39.add_field(name='Prefix Commands Issued', value=prefixCommandsIssued)
    emb39.add_field(name='Slash Commands Issued', value=slashCommandsIssued)
    emb39.add_field(name='Server Count', value=f'{serverCount} servers')
    emb39.add_field(name='Bot CPU Usage', value=f'{botcpu}%')
    await ctx.send(embed=emb39)

@client.command()
async def add_item(ctx, user:discord.User, *, itemname):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if ctx.author.id not in ids:
        await ctx.reply('I\'m 101%% sure this command doesn\'t exist :eyes:')
        return
    else:
        pass
    member_data = load_member_data(user.id)
    if itemname == 'coinbomb':
        member_data.cbomb += 1
        save_member_data(user.id, member_data)
        await ctx.send(f'Added 1 {itemname} to {user.display_name}\'s inventory')
    elif itemname == 'devbox':
        devbox[str(user.id)] += 1
        savejson()
        await ctx.send(f'Added 1 {itemname} to {user.display_name}\'s inventory')
    elif itemname == 'normalbox':
        normalbox[str(user.id)] += 1
        savejson()
        await ctx.send(f'Added 1 {itemname} to {user.display_name}\'s inventory')
    elif itemname == 'probox':
        probox[str(user.id)] += 1
        savejson()
        await ctx.send(f'Added 1 {itemname} to {user.display_name}\'s inventory')
    elif itemname == 'rifle':
        member_data.rifle += 1
        save_member_data(user.id, member_data)
        await ctx.send(f'Added 1 {itemname} to {user.display_name}\'s inventory')
    elif itemname == 'shovel':
        member_data.shovel += 1
        save_member_data(user.id, member_data)
        await ctx.send(f'Added 1 {itemname} to {user.display_name}\'s inventory')
    elif itemname == 'fishingpole':
        member_data.fishingpole += 1
        save_member_data(user.id, member_data)
        await ctx.send(f'Added 1 {itemname} to {user.display_name}\'s inventory')
    else:
        raise(BadArgument)

@client.command()
async def help(ctx, cmdhelp=None):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if cmdhelp == None:
      p0 = Embed(title='**MY COMMAND LIST**', description=f'My main prefix is **;**\n\n')
      p0.add_field(name='Categories', value=f'{emojis.economy} Economy:\n{emojis.music} Music\n{emojis.info} Bot Information\n{emojis.moderation} Moderation\n:sparkles: Misc\n{emojis.reddit} Reddit Commands\n{emojis.edit} Server Setup Utility')
      p0.set_footer(text='You are viewing page 1')
      p1 = Embed(title=f'{emojis.economy} Economy Commands', description='```work, beg, balance, deposit, withdraw, shop, buy, inventory, /give, rob, bankrob, hunt, fish, daily, weekly, monthly, postmeme, scout, highlow, rockpaperscissor```')
      p1.set_footer(text='You are viewing page 2 | To get help on a specific command, type in `;help [command name]')
      p2 = Embed(title=f'{emojis.music} Music Commands', description='```join, play, skip, stop, volume, current, pause, queue, shuffle, remove, loop```')
      p2.set_footer(text='You are viewing page 3 | To get help on a specific command, type in `;help [command name]')
      p3 = Embed(title=f'{emojis.info} Bot Information', description='```session, ping, invites, avatar, userinfo, /usercount, invite, uptime```')
      p3.set_footer(text='You are viewing page 4 | To get help on a specific command, type in `;help [command name]')
      p4 = Embed(title=f'{emojis.moderation} Moderation Commands', description='```ban, kick, mute, unmute, warn, warnings, clearwarns, set_level, purge, lock, unlock, nuke```')
      p4.set_footer(text='You are viewing page 5 | To get help on a specific command, type in `;help [command name]')
      p5 = Embed(title=f':sparkles: Misc', description='```poll, pollresults, giveaway, reroll, /8ball, /vote, slap, kill, hug, stare, uwu, snipe, edit_snipe, osu, amogus, fstab, say, cat```')
      p5.set_footer(text='You are viewing page 6 | To get help on a specific command, type in `;help [command name]')
      p6 = Embed(title=f'{emojis.reddit} Reddit Commands', description='```meme, linuxmeme, nothecker, aww, softwaregore, ihadastroke```')
      p6.set_footer(text='You are viewing page 7 | To get help on a specific command, type in `;help [command name]')
      p7 = Embed(title=f'{emojis.edit} Server Setup Utility', description='```viewsettings, setfeature, changeprefix, /autorole, setlevelupchannel, /welcomemsg, /goodbyemsg, /autowelcome, linkblocker```')
      p7.set_footer(text='You are viewing page 8 | To get help on a specific command, type in `;help [command name]')
      pages = [p0, p1, p2, p3, p4, p5, p6, p7]
      message = await ctx.send(embed = p0)
      await message.add_reaction('⏮️')
      await message.add_reaction('◀')
      await message.add_reaction('▶')
      await message.add_reaction('⏭')
      def check(reaction, user):
        return user == ctx.author
      i = 0
      reaction = None
      while True:
        if str(reaction) == '◀':
            if i > 0:
                i -= 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '▶':
            if i < 7:
                i += 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '⏭':
          i = 7
          await message.edit(embed = pages[i])
        elif str(reaction) == '⏮️':
          i = 0
          await message.edit(embed = pages[i])
        try:
            reaction, user = await client.wait_for('reaction_add', timeout = 30.0, check = check)
            await message.remove_reaction(reaction, user)
        except:
            break
      await message.clear_reactions()
    elif cmdhelp == 'work': await ctx.send(embed=returnhelp(cmdhelp, helpdb.work1, 1800, "everyone"))
    elif cmdhelp == 'beg': await ctx.send(embed=returnhelp(cmdhelp, helpdb.beg1, 30, "everyone"))
    elif cmdhelp == 'balance': await ctx.send(embed=returnhelp(cmdhelp, helpdb.bal1, 0, "everyone"))
    elif cmdhelp == 'deposit': await ctx.send(embed=returnhelp(cmdhelp, helpdb.dep1, 0, "everyone"))
    elif cmdhelp == 'withdraw': await ctx.send(embed=returnhelp(cmdhelp, helpdb.with1, 0, "everyone"))
    elif cmdhelp == 'sell': await ctx.send(embed=returnhelp(cmdhelp, helpdb.sell1, 0, "everyone"))
    elif cmdhelp == 'give': await ctx.send(embed=returnhelp(cmdhelp, helpdb.give1, 0, "everyone"))
    elif cmdhelp == 'rob': await ctx.send(embed=returnhelp(cmdhelp, helpdb.amogus1, 40, "everyone"))
    elif cmdhelp == 'hunt': await ctx.send(embed=returnhelp(cmdhelp, helpdb.hunt1, 30, "everyone"))
    elif cmdhelp == 'fish': await ctx.send(embed=returnhelp(cmdhelp, helpdb.fish1, 15, "everyone"))
    elif cmdhelp == 'poll': await ctx.send(embed=returnhelp(cmdhelp, '`;poll [question] [option 1] [option 2] <opt3> <opt4> <opt5> <opt6> <opt7> <opt8> <opt9> <opt10>`', 0, "everyone"))
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
    elif cmdhelp == 'postmeme': await ctx.send(embed=returnhelp(cmdhelp, helpdb.postmeme1, 35, "everyone"))
    elif cmdhelp == 'dig': await ctx.send(embed=returnhelp(cmdhelp, helpdb.dig1, 10, "everyone"))
    elif cmdhelp == 'kick': await ctx.send(embed=returnhelp(cmdhelp, helpdb.kick1, 5, "moderators with **kick members** permission"))
    elif cmdhelp == 'ban': await ctx.send(embed=returnhelp(cmdhelp, helpdb.ban1, 5, "moderators with **ban members** permission"))
    elif cmdhelp == 'say': await ctx.send(embed=returnhelp(cmdhelp, helpdb.say1, 0, "everyone"))
    elif cmdhelp == 'nuke': await ctx.send(embed=returnhelp(cmdhelp, helpdb.nuke1, 0, "moderators with **manage channels** permission"))
    elif cmdhelp == 'purge': await ctx.send(embed=returnhelp(cmdhelp, helpdb.purge1, 2, "moderators with **manage messages** permission"))
    elif cmdhelp == 'lock': await ctx.send(embed=returnhelp(cmdhelp, helpdb.lock1, 0, "moderators with **manage channels** permission"))
    elif cmdhelp == 'unlock': await ctx.send(embed=returnhelp(cmdhelp, helpdb.unlock1, 0, "moderators with **manage channels** permission"))
    elif cmdhelp == 'ping': await ctx.send(embed=returnhelp(cmdhelp, helpdb.ping1, 0, "everyone"))
    elif cmdhelp == 'invites': await ctx.send(embed=returnhelp(cmdhelp, helpdb.invites1, 0, "everyone"))
    elif cmdhelp == 'uptime': await ctx.send(embed=returnhelp(cmdhelp, helpdb.uptime1, 0, "everyone"))
    elif cmdhelp == 'invite': await ctx.send(embed=returnhelp(cmdhelp, helpdb.invite1, 0, "everyone"))
    elif cmdhelp == 'slap': await ctx.send(embed=returnhelp(cmdhelp, helpdb.slap1, 0, "everyone"))
    elif cmdhelp == 'pollresults': await ctx.send(embed=returnhelp(cmdhelp, '`;pollresults [poll id]`', 0, "everyone"))
    elif cmdhelp == 'hug': await ctx.send(embed=returnhelp(cmdhelp, helpdb.hug1, 0, "everyone"))
    elif cmdhelp == 'stare1': await ctx.send(embed=returnhelp(cmdhelp, helpdb.stare1, 0, "everyone"))
    elif cmdhelp == 'kill': await ctx.send(embed=returnhelp(cmdhelp, helpdb.kill1, 0, "everyone"))
    elif cmdhelp == 'uwu': await ctx.send(embed=returnhelp(cmdhelp, helpdb.uwu1, 0, "everyone"))
    elif cmdhelp == 'snipe': await ctx.send(embed=returnhelp(cmdhelp, helpdb.snipe1, 0, "everyone"))
    elif cmdhelp == 'edit_snipe': await ctx.send(embed=returnhelp(cmdhelp, helpdb.edit_snipe1, 0, "everyone"))
    elif cmdhelp == 'meme': await ctx.send(embed=returnhelp(cmdhelp, helpdb.meme1, 0, "everyone"))
    elif cmdhelp == 'nothecker': await ctx.send(embed=returnhelp(cmdhelp, helpdb.nothecker1, 0, "everyone"))
    elif cmdhelp == 'ihadastroke': await ctx.send(embed=returnhelp(cmdhelp, helpdb.ihadastroke1, 0, "everyone"))
    elif cmdhelp == 'aww': await ctx.send(embed=returnhelp(cmdhelp, helpdb.aww1, 0, "everyone"))
    elif cmdhelp == 'softwaregore': await ctx.send(embed=returnhelp(cmdhelp, helpdb.softwaregore1, 0, "everyone"))
    elif cmdhelp == 'linuxmeme': await ctx.send(embed=returnhelp(cmdhelp, helpdb.linuxmeme1, 0, "everyone"))
    elif cmdhelp == 'sus': await ctx.send(embed=returnhelp(cmdhelp, helpdb.sus1, 0, "everyone"))
    elif cmdhelp == '8ball': await ctx.send(embed=returnhelp(cmdhelp, helpdb._8ball1, 0, "everyone"))
    elif cmdhelp == 'amogus': await ctx.send(embed=returnhelp(cmdhelp, helpdb.amogus1, 0, "everyone"))
    elif cmdhelp == 'fstab': await ctx.send(embed=returnhelp(cmdhelp, helpdb.fstab1, 0, "everyone"))
    elif cmdhelp == 'bankrob': await ctx.send(embed=returnhelp(cmdhelp, ';bankrob [Member]', 210, "everyone"))
    elif cmdhelp == 'autowelcome': await ctx.send(embed=returnhelp(cmdhelp, '`/autowelcome <Channel>` (Slash Command)', 0, "administrators"))
    elif cmdhelp == 'warn': await ctx.send(embed=returnhelp(cmdhelp, helpdb.warn1, 0, "moderators with **Manage Messages Permissions**"))
    elif cmdhelp == 'clearwarns': await ctx.send(embed=returnhelp(cmdhelp, ';clearwarns [Member]', 0, "moderators with **Manage Messages Permissions**"))
    elif cmdhelp == 'warnings': await ctx.send(embed=returnhelp(cmdhelp, ';warnings [Member]', 0, "moderators with **Manage Messages Permissions**"))
    elif cmdhelp == 'avatar': await ctx.send(embed=returnhelp(cmdhelp, helpdb.avatar1, 0, "everyone"))
    elif cmdhelp == 'changeprefix': await ctx.send(embed=returnhelp(cmdhelp, helpdb.changeprefix1, 0, "Server administrators"))
    elif cmdhelp == 'setlevelupchannel': await ctx.send(embed=returnhelp(cmdhelp, helpdb.levelups1, 0, "Server administrators"))
    elif cmdhelp == 'inventory': await ctx.send(embed=returnhelp(cmdhelp, helpdb.inventory1, 0, "everyone"))
    elif cmdhelp == 'buy': await ctx.send(embed=returnhelp(cmdhelp, helpdb.buy1, 0, "everyone"))
    elif cmdhelp == 'shop': await ctx.send(embed=returnhelp(cmdhelp, helpdb.shop1, 0, "everyone"))
    elif cmdhelp == 'catgirl': await ctx.send(embed=returnhelp(cmdhelp, helpdb.cg1, 0, "everyone"))
    elif cmdhelp == 'viewsettings': await ctx.send(embed=returnhelp(cmdhelp, helpdb.vs1, 0, "everyone"))
    elif cmdhelp == 'setfeature': await ctx.send(embed=returnhelp(cmdhelp, helpdb.sf1, 0, "everyone"))
    elif cmdhelp == 'scout': await ctx.send(embed=returnhelp(cmdhelp, helpdb.scout1, 25, "everyone"))
    elif cmdhelp == 'networth': await ctx.send(embed=returnhelp(cmdhelp, helpdb.nw1, 0, "everyone"))
    elif cmdhelp == 'roll': await ctx.send(embed=returnhelp(cmdhelp, helpdb.roll1, 0, "everyone"))
    elif cmdhelp == 'set_level': await ctx.send(embed=returnhelp(cmdhelp, helpdb.setlevel1, 0, "Server administrators"))
    elif cmdhelp == 'serverinfo': await ctx.send(embed=returnhelp(cmdhelp, helpdb.si1, 0, "everyone"))
    elif cmdhelp == 'play': await ctx.send(embed=returnhelp(cmdhelp, helpdb.play1, 0, "everyone"))
    elif cmdhelp == 'pause': await ctx.send(embed=returnhelp(cmdhelp, helpdb.pause1, 0, "everyone"))
    elif cmdhelp == 'skip': await ctx.send(embed=returnhelp(cmdhelp, helpdb.skip, 0, "everyone"))
    elif cmdhelp == 'stop': await ctx.send(embed=returnhelp(cmdhelp, helpdb.stop1, 0, "everyone"))
    elif cmdhelp == 'osu': await ctx.send(embed=returnhelp(cmdhelp, ';osu [osu! user]', 0, "everyone"))
    elif cmdhelp == 'loop': await ctx.send(embed=returnhelp(cmdhelp, helpdb.loop, 0, "everyone"))
    elif cmdhelp == 'use': await ctx.send(embed=returnhelp(cmdhelp, helpdb.use1, 4, "everyone"))
    elif cmdhelp == 'welcomemsg': await ctx.send(embed=returnhelp(cmdhelp, '`/welcomemsg <Message>` (Slash Command)', 0, "Server Administrators"))
    elif cmdhelp == 'goodbyemsg': await ctx.send(embed=returnhelp(cmdhelp, '`/goodbyemsg <Message>` (Slash Command)', 0, "Server Administrators"))
    elif cmdhelp == 'autorole': await ctx.send(embed=returnhelp(cmdhelp, '`/autorole <Role>` (Slash Command)', 0, "Server Administrators"))
    elif cmdhelp == 'linkblocker': await ctx.send(embed=returnhelp(cmdhelp, helpdb.linkblock1, 0, "Server Administrators"))
    elif cmdhelp == 'giveaway': await ctx.send(embed=returnhelp(cmdhelp, ';giveaway', 0, "Moderators"))
    elif cmdhelp == 'reroll': await ctx.send(embed=returnhelp(cmdhelp, ';reroll [channel] [message ID]', 0, "Moderators"))
    elif cmdhelp == 'help': await ctx.reply('You want help for help? *I wonder how you got this far then*')
    else: await ctx.reply(f'I can\'t find a command called {cmdhelp}.')

@client.command(aliases=['av'])
async def avatar(ctx, username:User=None):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if username == None:
        userAvatar = ctx.author.avatar_url
        embed182 = Embed(title=f'{ctx.author}\'s avatar')
        embed182.set_image(url=userAvatar)
        await ctx.send(embed = embed182)
    else:
        userAvatar = username.avatar_url
        embed182 = Embed(title=f'{username}\'s avatar')
        embed182.set_image(url=userAvatar)
        await ctx.send(embed = embed182)

@client.command()
async def cat(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    async with aiohttp.ClientSession() as session:
        async with session.get('http://aws.random.cat/meow') as r:
            if r.status == 200:
                js = await r.json()
                await ctx.send(js['file'])

@client.command()
@commands.has_permissions(manage_channels=True)
async def nuke(ctx, channel: discord.TextChannel = None):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if channel == None: 
        await ctx.send("You did not mention a channel!")
        return
    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)
    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="The channel has been Nuked!")
        await nuke_channel.delete()
        await new_channel.send("This channel has been nuked!")
        await ctx.send("Nuked the Channel sucessfully!")
    else:
        await ctx.reply(f"No channel named {channel.name} was found!")

@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel = None):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
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
            print(f'[{current_time}] {colors.cyan}{ctx.author.display_name}{colors.end} locked {colors.green}{lock_channel}{colors.end}.')
        else:
            pass
    else:
        await ctx.reply(f'No channel named {channel.name} was found.')

@client.command()
@commands.has_permissions(manage_messages=True)
@commands.cooldown(1, 2, commands.BucketType.user)
async def purge(ctx, amount:int, user:User=None):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
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
            print(f'[{current_time}] {colors.cyan}{ctx.author.display_name}{colors.end} purged {colors.green}{amount}{colors.end} messages from {colors.green}#{ctx.channel.name}{colors.end}.')
        else:
            pass

@client.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, user:discord.Member, *, warn_reason:str):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    try:
        warnings[str(ctx.guild.id)][str(user.id)].append(warn_reason)
        savejson()
        embed67 = Embed(title=f'You were warned in {ctx.guild}.', description=f'*Reason: {warn_reason}*', color=theme_color)
        await user.send(embed = embed67)
        embed70 = Embed(title=f':white_check_mark: {user} has been warned', description=f'**Reason:** {warn_reason}')
        await ctx.channel.send(embed = embed70)
    except:
        warnings[str(ctx.guild.id)][str(user.id)].append(warn_reason)
        savejson()
        embed71 = Embed(title=f':x: Hold up!', description=f'I was unable to DM {user}, however the warning has been logged for them.', color=color_fail)
        await ctx.send(embed = embed71)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clearwarns(ctx, user:discord.Member):
  global prefixCommandsIssued
  prefixCommandsIssued += 1
  warnings[str(ctx.guild.id)][str(user.id)] = []
  savejson()
  embed70 = Embed(title=f':white_check_mark: All warnings cleared for {user}.', color=color_success)
  await ctx.send(embed = embed70)

@client.command(aliases=['warnings'])
@commands.has_permissions(manage_messages=True)
async def showwarns(ctx, user:User):
  outputstr = ""
  for x in warnings[str(ctx.guild.id)][str(user.id)]:
    outputstr = outputstr + str(x) + '\n'
  if warnings[str(ctx.guild.id)][str(user.id)] == []:
    outputstr = '*Nothing here*'
  e = Embed(title=f'Warnings for {user}', description=outputstr, color=theme_color)
  await ctx.send(embed=e)

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel = None):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
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
            print(f'[{current_time}] {colors.cyan}{ctx.author.display_name}{colors.end} unlocked {colors.green}{unlock_channel}{colors.end}.')
        else:
            pass
    else:
        await ctx.reply(f'No channel named {channel.name} was found.')

@client.command()
@commands.cooldown(1, 25, commands.BucketType.user)
async def scout(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
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
    member_data = load_member_data(ctx.author.id)
    found = randint(100, 2000)
    member_data.wallet += found
    save_member_data(ctx.author.id, member_data)

@client.command()
async def invites(ctx, *, user : User=None):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
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

@client.command()
async def forcecache(ctx, *, user:User):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if ctx.author.id not in ids:
        return
    else:
        pass
    await ctx.reply(f'Caching database for {user}...')
    print('[Main/INFO]: Caching data for {user} start')
    ## BOXES DATA ##
    print('[JSON/PROCESS]: Creating values for \'normalbox\'...')
    if str(user.id) in normalbox:
        pass
    else:
        normalbox[str(user.id)] = 1
        savejson()
        print('[JSON/PROCESS]: Creating values for \'probox\'...')
    if str(user.id) in probox:
        pass
    else:
        probox[str(user.id)] = 0
        savejson()
    print('[JSON/PROCESS]: Creating values for \'devbox\'...')
    if str(user.id) in devbox:
        pass
    else:
        devbox[str(user.id)] = 0
        savejson()
    ## BADGES DATA ##
    print('[JSON/PROCESS]: Creating values for \'prestige_conf\'...')
    if str(user.id) in prestige_conf:
        pass
    else:
        prestige_conf[str(user.id)] = 0
        savejson()
    ## CONFIGURATION DATA ##
    print('[JSON/PROCESS]: Creating values for \'passivemode\'...')
    if str(user.id) in passivemode:
        pass
    else:
        passivemode[str(user.id)] = 0
        savejson()
    ## LEVELING SYSTEM ##
    print('[JSON/PROCESS]: Creating values for \'levels\'...')
    if str(user.id) in levels[str(ctx.guild.id)]:
        pass
    else:
        levels[str(ctx.guild.id)][str(user.id)] = 0
        savejson()
    print('[JSON/PROCESS]: Creating values for \'exp\'...')
    if str(user.id) in exp[str(ctx.guild.id)]:
        pass
    else:
        exp[str(ctx.guild.id)][str(user.id)] = 0
        savejson()
    print('[Main/INFO]: Done!')
    await ctx.reply('Done!')

@client.command()
async def shutdown(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if ctx.author.id == 738290097170153472:
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
        await ctx.send(f'I\'m 101% that this command doesn\'t exist :eyes:')

@client.command(aliases=['hl'])
@commands.cooldown(1, 40, commands.BucketType.user)
async def highlow(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    numb = randint(1, 100)
    numb2 = randint(1, 100)
    id = ctx.author.id
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
        else:
            await ctx.send(f'Incorrect the number was {numb2}')
    if msg.content == 'high':
        if numb < numb2:
            await ctx.send(f'Congrats, your number was {numb2} and you earned {coins} coins')
            member_data = load_member_data(id)
            member_data.wallet += coins
            save_member_data(id, member_data)
        else:
            await ctx.send(f'Incorrect your number was {numb2}')
            return
    else:
        await ctx.send(f'{msg.content} is not an option')

@client.command(aliases=['cred', 'credits'])
async def credit(ctx):
    e = Embed(title='Isobot\'s Credits', description='Some awesome people who helped contribute to isobot...\n\n<@!738290097170153472>: Owner, learnt Python from Arch bot\'s code, JavaScript dood, cool\n<@!705462972415213588>: Largest contributor, uses **Arch btw**, owner of Arch bot (original of isobot), master-debloater, pog, **fixed ;rank command**, ||anti-nexus gang||\n<@!706697300872921088>: 2nd largest contributor, 101% not a bot, fstab.ti, bug-squasher, likes Arch Linux but is a Windows user, owner of iso6.9 (based on isobot)', color=theme_color)
    await ctx.send(embed=e)

@client.command()
async def kill(ctx, user : User):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
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

@client.command()
@commands.has_permissions(kick_members=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def kick(ctx, member:discord.Member, *, reason:str = None):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if member == ctx.author:
      await ctx.reply('I don\'t think you want to kick yourself.')
      return
    else:
      if reason == None:
        reason = 'Not provided'
      try:
        await member.kick(reason = reason)
        embedKick = Embed(title=f':white_check_mark: *{member} has been **kicked** from the server.*', color=color_success)
        await ctx.send(embed=embedKick)
      except:
        embedKick = Embed(description=f':x: I was unable to kick {member}', color=color_fail)
        await ctx.send(embed=embedKick)

@client.command()
@commands.has_permissions(ban_members=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def ban(ctx, member:discord.Member, *, reason:str = None):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if member == ctx.author:
      await ctx.reply('I don\'t think you want to ban yourself.')
      return
    else:
      if reason == None:
        reason = 'Not provided'
      try:
        await member.ban(reason = reason)
        embedBan = Embed(title=f':white_check_mark: *{member} has been **banned** from the server.*', color=color_success)
        await ctx.send(embed=embedBan)
      except:
        embedBan = Embed(description=f':x: I was unable to ban {member}', color=color_fail)
        await ctx.send(embed=embedBan)

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member:discord.Member):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if member == ctx.author:
        await ctx.reply('You can\'t unban yourself.')
        return
    else:
        try:
            await member.unban()
            embedUnban = Embed(title=f':white_check_mark: *{member} has been **unbanned** from the server.*', color=color_success)
            await ctx.send(embed=embedUnban)
        except:
            embedUnban = Embed(description=f':x: I was unable to unban {member}', color=color_fail)
            await ctx.send(embed=embedUnban)

@client.command(aliases=["lm"])
async def linuxmeme(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    memes_submissions = reddit.subreddit('linuxmemes').hot()
    post_to_pick = randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embed = Embed(title = submission.title, color=randEmbedColor())
    embed.set_image(url=submission.url)
    embed.set_footer(text='I use Arch BTW.')
    await ctx.send(embed = embed)

@client.command(aliases=["nh"])
async def nothecker(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    nothecker_submissions = reddit.subreddit('nothecker').hot()
    post_to_pick = randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in nothecker_submissions if not x.stickied)
    embed = Embed(title = submission.title, color=randEmbedColor())
    embed.set_image(url=submission.url)
    embed.set_footer(text=':eues:')
    await ctx.send(embed = embed)

@client.command(aliases=['pet'])
async def aww(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    aww_submissions = reddit.subreddit('aww').hot()
    post_to_pick = randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in aww_submissions if not x.stickied)
    embed = Embed(title = submission.title, color=randEmbedColor())
    embed.set_image(url=submission.url)
    embed.set_footer(text='Meow/Woof!')
    await ctx.send(embed = embed)

@client.command(aliases=['sg'])
async def softwaregore(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    sg_submissions = reddit.subreddit('softwaregore').hot()
    post_to_pick = randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in sg_submissions if not x.stickied)
    embed = Embed(title = submission.title, color=randEmbedColor())
    embed.set_image(url=submission.url)
    embed.set_footer(text='Softwaregore be like')
    await ctx.send(embed = embed)

@client.command(aliases=['meem'])
async def meme(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    memes_submissions = reddit.subreddit('memes').hot()
    post_to_pick = randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embed = Embed(title = submission.title, color=randEmbedColor())
    embed.set_image(url=submission.url)
    embed.set_footer(text='Meems be like')
    await ctx.send(embed = embed)

@client.command(aliases=['stokr', 'stork', 'stroke'])
async def ihadastroke(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    memes_submissions = reddit.subreddit('ihadastroke').hot()
    post_to_pick = randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embed = Embed(title = submission.title, color=randEmbedColor())
    embed.set_image(url=submission.url)
    embed.set_footer(text='Stokr... Stork... Stroke.')
    await ctx.send(embed = embed)

@client.command()
@commands.cooldown(1, 1800, commands.BucketType.user)
async def work(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if not bool(currency):
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    member_data = load_member_data(ctx.author.id)
    coins = randint(1000, 25000)
    member_data.wallet += coins
    save_member_data(ctx.author.id, member_data)
    await ctx.send(f"You worked for a 30-minute shift and earned {coins} coins.")

@client.command()
async def uwu(ctx, user:User):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    await ctx.send(f'{ctx.author.mention} uwu\'ed {user.display_name}. *uwu*')

@client.command(aliases=['open'])
@commands.cooldown(1, 4, commands.BucketType.user)
async def use(ctx, *, itemname):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    member_data = load_member_data(ctx.author.id)
    if itemname == 'coinbomb':
        if member_data.cbomb < 1:
            await ctx.reply('You don\'t have any coin bombs in your inventory!')
            return
        else:
            pass
        await ctx.send('Opening 1 **coin bomb**...')
        await asyncio.sleep(3)
        member_data.cbomb -= 1
        randCoins = randint(1000, 6500)
        await ctx.send(f'The coin bomb exploded, and it let out {randCoins} coins!')
        member_data.wallet += randCoins
        save_member_data(ctx.author.id, member_data)

    elif itemname == 'devbox':
        if devbox[str(ctx.author.id)] < 1:
            await ctx.reply('You don\'t have any developer boxes in your inventory! Maybe... try asking my developer?')
            return
        else:
            pass
        await ctx.send('Opening 1 **developer box**...')
        await asyncio.sleep(3)
        devbox[str(ctx.author.id)] -= 1
        randCoins = randint(25000, 100000)
        await ctx.send(f'You opened 1 developer box and you found {randCoins} coins!')
        member_data.wallet += randCoins
        save_member_data(ctx.author.id, member_data)
        savejson()

    elif itemname == 'normalbox':
        if normalbox[str(ctx.author.id)] < 1:
            await ctx.reply('You don\'t have any normal boxes in your inventory!')
            return
        else:
            pass
        await ctx.send('Opening 1 **normal box**...')
        await asyncio.sleep(3)
        normalbox[str(ctx.author.id)] -= 1
        randCoins = randint(1000, 10000)
        await ctx.send(f'You opened 1 normal box and you found:\n   **{randCoins}** coins.\n   **2** coin bombs.')
        member_data.wallet += randCoins
        member_data.cbomb += 2
        save_member_data(ctx.author.id, member_data)
        savejson()

    elif itemname == 'probox':
        if probox[str(ctx.author.id)] < 1:
            await ctx.reply('You don\'t have any pro boxes in your inventory! If you get lucky, you might find one.')
            return
        else:
            pass
        await ctx.send('Opening 1 **pro box**...')
        await asyncio.sleep(3)
        probox[str(ctx.author.id)] -= 1
        randCoins = randint(10000, 55000)
        items = ['rifle', 'shovel', 'fishingpole']
        randitem = choice(items)
        await ctx.send(f'You opened 1 pro box and you found:\n   {randCoins} coins\n   **4** coin bombs\n   **1** {randitem}')
        member_data.wallet += randCoins
        member_data.cbomb += 4
        if randitem == 'rifle': member_data.rifle += 1
        elif randitem == 'shovel': member_data.shovel += 1
        elif randitem == 'fishingpole': member_data.fishingpole += 1
        member_data.rifle += 1
        save_member_data(ctx.author.id, member_data)
        savejson()
    else:
        raise(BadArgument)

@client.command()
async def slap(ctx, user:User):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    responses3 = [
        "https://cdn.weeb.sh/images/Hkw1VkYP-.gif",
        "https://cdn.weeb.sh/images/HkA6mJFP-.gif",
        "https://cdn.weeb.sh/images/Sk9mfCtY-.gif",
        "https://cdn.weeb.sh/images/HJKiX1tPW.gif"
    ]
    e = Embed(title=f'{ctx.author.display_name} slaps {user.display_name}. Oof, that must hurt...', color=theme_color)
    e.set_image(url=f'{choice(responses3)}')
    await ctx.send(embed = e)

@client.command()
async def roles(ctx):
  outputstr = ""
  for x in ctx.guild.roles:
    if x == '@everyone':
      pass
    else:
      outputstr = outputstr + f'<@&{x.id}>' + '\n'
  e = Embed(title=f'Roles in {ctx.guild}', description=outputstr, color=theme_color)
  await ctx.send(embed=e)

@client.command()
async def hug(ctx, user:User):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    responses3 = [
        "https://cdn.weeb.sh/images/Sk80wyhqz.gif",
        "https://cdn.weeb.sh/images/S1DyFuQD-.gif",
        "https://cdn.weeb.sh/images/HyllFdmwZ.gif",
        "https://cdn.weeb.sh/images/Hyec_OmDW.gif",
        "https://cdn.weeb.sh/images/Hk3ox0tYW.gif"
    ]
    if user == ctx.author:
        await ctx.send(f'{ctx.author.mention}, you can\'t hug yourself!')
    else:
        e = Embed(title=f'{ctx.author.display_name} hugs {user.display_name}. Aww!', color=theme_color)
        e.set_image(url=f'{choice(responses3)}')
        await ctx.send(embed = e)

@client.command(aliases=['nw'])
async def networth(ctx, user:User=None):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if user == None:
        member_data = load_member_data(ctx.author.id)
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
async def automod_set(ctx, item:str, value:int):
  gd_data = load_guild_data(ctx.guild.id)
  if item == 'swearfilter':
    if value == 0:
      gd_data.swearfilter = 0
      await ctx.reply('Swear filter disabled.')
    elif value == 1:
      gd_data.swearfilter = 1
      await ctx.reply('Swear filter enabled.')
    else:
      await ctx.reply(':warning: That\'s not a valid range! Range can be `0 - 1`.')
    save_config_data(ctx.guild.id, gd_data)
  elif item == 'linkdelete':
    if value == 0:
      linkblocker[str(ctx.guild.id)] = 0
      await ctx.reply('Link blocker disabled.')
    elif value == 1:
      linkblocker[str(ctx.guild.id)] = 1
      await ctx.reply('Link blocker enabled.')
    else:
      await ctx.reply(':warning: That\'s not a valid range! Range can be `0 - 1`.')
    savejson()
  else:
    await ctx.reply(':x: That\'s not a valid automod setting.')

@client.command(aliases=['profile'])
async def _profile(ctx, user:User=None):
    if user == None:
        member_data = load_member_data(ctx.author.id)
        e = Embed(title=f'{ctx.author.display_name}\'s Profile Stats', description=f'**Prestige {prestige_conf[str(ctx.author.id)]}**', color=theme_color)
        e.add_field(name='Net Worth', value=f'{member_data.wallet + member_data.bank} coins', inline=True)
        e.add_field(name=f'Wallet', value=f'{member_data.wallet} coins', inline=True)
        e.add_field(name=f'Bank', value=f'{member_data.bank} coins', inline=True)
    else:
        member_data = load_member_data(user.id)
        e = Embed(title=f'{user.display_name}\'s Profile Stats', description=f'**Prestige {prestige_conf[str(user.id)]}**', color=theme_color)
        e.add_field(name=f'Net Worth', value=f'{member_data.wallet + member_data.bank} coins', inline=True)
        e.add_field(name=f'Wallet', value=f'{member_data.wallet} coins', inline=True)
        e.add_field(name=f'Bank', value=f'{member_data.bank} coins', inline=True)
    await ctx.send(embed=e)

@client.command()
async def stare(ctx, user : User):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    responses3 = [
        "https://cdn.weeb.sh/images/HJxqIyFvZ.gif",
        "https://cdn.weeb.sh/images/Sk9jLJKvZ.gif",
        "https://cdn.weeb.sh/images/HJ6v8yYP-.gif",
        "https://cdn.weeb.sh/images/HyT3UkFwb.gif",
        "https://cdn.weeb.sh/images/Sk5BOdQIG.gif"
    ]
    if user == ctx.author:
        await ctx.send(f'{ctx.author.mention} idk what kind of logic this is, how do you stare at yourself?')
    else:
        e = Embed(title=f'{ctx.author.display_name} stares into {user.display_name}\'s eyes...', color=theme_color)
        e.set_image(url=f'{choice(responses3)}')
        await ctx.send(embed = e)

@client.command()
async def floppa(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
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
@commands.cooldown(1, 120000, commands.BucketType.user)
async def prestige(ctx):
    member_data = load_member_data(ctx.author.id)
    if member_data.wallet < 100000:
        await ctx.reply('You need `100000` coins or more in your wallet!')
        return
    else:
        pass
    await ctx.reply('Prestiging means you lose all of your coins, and your entire inventory is wiped. **This action is irreversable.** Are you sure you want to continue?')
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.message.channel and str(msg.content) in ['yes', 'no']
    msg = await client.wait_for("message", check=check)
    if str(msg.content.lower()) == 'yes':
        member_data.wallet = 10000
        member_data.bank = 0
        member_data.rifle = 0
        member_data.fishingpole = 0
        member_data.shovel = 0
        normalbox[str(ctx.author.id)] = 0
        probox[str(ctx.author.id)] = 1
        devbox[str(ctx.author.id)] = 0
        member_data.cbomb = 0

        prestige_conf[str(ctx.author.id)] += 1

        save_member_data(ctx.author.id, member_data)
        savejson()
        await ctx.reply(f'**Congratulations!** You are now **Prestige {prestige_conf[str(ctx.author.id)]}**!')
    else:
        await msg.reply('Ok, looks like we aren\'t prestiging after all.')

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def guess(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    current_time = timefetch.timenow
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    member_data = load_member_data(ctx.author.id)
    await ctx.send('Guess a number from 1 to 10')
    x = randint(1, 10)
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.message.channel and int(msg.content) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    msg = await client.wait_for("message", check=check)
    if int(msg.content) == x:
        coins = randint(100, 500)
        await ctx.send(f"Correct, you earned {coins} coins")
        member_data.wallet += coins
        save_member_data(ctx.author.id, member_data)
        if bool(log) == True:
            print(f'[{current_time}]{colors.cyan}{ctx.author.display_name}{colors.end} has earned {colors.green}{x}{colors.end} coins')
        else:
            pass
    else:
        await ctx.send(f"Nope. It was {x}")

@client.command(aliases=['sus'])
async def isSus(ctx, *, user : User):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
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
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    member_data = load_member_data(ctx.author.id)
    current_time = timefetch.timenow
    await ctx.send(f'**{ctx.author.mention} What type of meme you want to post?**\n`f` Fresh meme\n`r` Reposted\n`i` Intellectual\n`d` Dank meme\n`l` Linux meme\n`c` Copypasta\n`k` Kind')
    def check(msg):
        return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content) in ['f', 'r', 'i' 'd', 'l', 'c', 'k']
    msg = await client.wait_for("message", check=check)
    x = randint(0, 200)
    if x == 0:
        await ctx.send(f'{ctx.author.mention}, you posted it on the internet, but it is now a DEAD meme. You gained 0 coins.')
    else:
        await ctx.send(f'You earned {x} coins')
        member_data.wallet += x
        save_member_data(ctx.author.id, member_data)
        if bool(log) == True:
            print(f'[{current_time}]{colors.cyan}{ctx.author.display_name}{colors.end} has earned {colors.green}{x}{colors.end} coins')
        else:
            pass

@client.command()
async def osu(ctx, *, user:str):
  try:
    compact_user = api.search(query=user).users.data[0]
    e = Embed(title=f'osu! stats for {user}', color=0xff66aa)
    e.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Osu%21_Logo_2016.svg/2048px-Osu%21_Logo_2016.svg.png')
    e.add_field(name='Rank (Global)', value=f'#{compact_user.expand().statistics.global_rank}')
    e.add_field(name='Rank (Country)', value=f'#{compact_user.expand().statistics.country_rank}')
    e.add_field(name='Ranked Score', value=f'{compact_user.expand().statistics.ranked_score}')
    e.add_field(name='Level', value=f'Level {compact_user.expand().statistics.level.current} ({compact_user.expand().statistics.level.progress}% progress)')
    e.add_field(name='pp', value=round(compact_user.expand().statistics.pp))
    e.add_field(name='Max Combo', value=f'{compact_user.expand().statistics.maximum_combo}x')
    e.add_field(name='Total Hits', value=f'{compact_user.expand().statistics.total_hits}')
    e.add_field(name='Play Count', value=compact_user.expand().statistics.play_count)
    e.add_field(name='Accuracy', value=f'{round(compact_user.expand().statistics.hit_accuracy, 2)}%')
    e.add_field(name='Replays Watched by Others', value=f'{compact_user.expand().statistics.replays_watched_by_others}')
    await ctx.send(embed=e)
  except: await ctx.send(f':warning: {user} was not found in osu!.')

@client.command()
async def osubeatmap(ctx, *, query:int):
  try:
    beatmap = api.beatmap(beatmap_id=query)
    e = Embed(title=f'osu! beatmap info for {beatmap.expand()._beatmapset.title} ({beatmap.expand()._beatmapset.title_unicode})', color=0xff66aa)
    e.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Osu%21_Logo_2016.svg/2048px-Osu%21_Logo_2016.svg.png')
    #.beatmap.data[0]
    e.add_field(name='Artist', value=f'{beatmap.expand()._beatmapset.artist} ({beatmap.expand()._beatmapset.artist_unicode})')
    e.add_field(name='Mapper', value=beatmap.expand()._beatmapset.creator)
    e.add_field(name='Difficulty', value=f'{beatmap.expand().difficulty_rating} stars')
    e.add_field(name='BPM', value=beatmap.expand().bpm)
    e.add_field(name='Circles', value=beatmap.expand().count_circles)
    e.add_field(name='Sliders', value=beatmap.expand().count_sliders)
    e.add_field(name='HP Drain', value=beatmap.expand().drain)
    await ctx.send(embed=e)
  except Exception as f:
    await ctx.reply(f)

@client.command()
async def roll(ctx, number_of_dice:int, number_of_sides:int):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    dice = [
        str(choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.reply('Number rolled is, '.join(dice))

@client.command()
async def backup(ctx):
    e = Embed(title='Backing up your server...', description='Please be patient while we backup.', color=discord.Color.blue())
    e.add_field(name='Items being backed up', value='Members\nChannels (excluding permissions and categories)')
    e.set_footer(text='This will overwrite any existing backups.')
    await ctx.reply(embed=e)
    try:
        serverbackups[str(ctx.guild.id)] = {}
        serverbackups[str(ctx.guild.id)][str('members')] = []
        for i in ctx.guild.members:
            serverbackups[str(ctx.guild.id)][str('members')].append(i.id)
        serverbackups[str(ctx.guild.id)][str('channels')] = []
        for i in ctx.guild.channels:
            serverbackups[str(ctx.guild.id)][str('channels')].append(i.name)
        serverbackups[str(ctx.guild.id)][str('roles')] = []
        for i in ctx.guild.roles:
            serverbackups[str(ctx.guild.id)][str('roles')].append(i.name)
        savejson()
        await ctx.send(':white_check_mark: Backup complete!')
    except Exception as catch:
        await ctx.send(f':x: An error occured when backing up! ```Exception: {catch}```')


@client.command(aliases=['si'])
async def serverinfo(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
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
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    e = Embed(title=f':knife: {ctx.author} fstabbed {user}. Oof! :knife:', description='That must really fstabbing hurt...', color=theme_color)
    await ctx.send(embed = e)

@client.command()
async def null(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    await ctx.reply('You got **null** coins dood.')

@client.command()
async def add(ctx, user:User, *, arg1=None):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if ctx.author.id not in ids:
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
                print(f'[{current_time}]{colors.cyan}{ctx.author.display_name}{colors.end} added {colors.green}{hexv}{colors.end} coins to {colors.cyan}{user.display_name}\'s{colors.end} account')
            except ValueError:
                await ctx.send(f'Invalid hex value')
        elif arg1.startswith('0b') or arg1.startswith('-0b'):
            try:
                binv = int(f'{arg1}', 2)
                member_data = load_member_data(user.id)
                member_data.wallet += int(binv)
                save_member_data(user.id, member_data)
                await ctx.send(f'Added {binv} coins to {user.display_name}\'s account')
                print(f'[{current_time}]{colors.cyan}{ctx.author.display_name}{colors.end} added {colors.green}{binv}{colors.end} coins to {colors.cyan}{user.display_name}\'s{colors.end} account')
            except ValueError:
                await ctx.send('Invalid binary value')
        elif arg1.isdigit:
            member_data = load_member_data(user.id)
            member_data.wallet += int(arg1)
            save_member_data(user.id, member_data)
            await ctx.send(f'Added {arg1} coins to {user.display_name}\'s account')
            if bool(log) == True:
                print(f"[{current_time}]{colors.cyan}{ctx.author.display_name}{colors.end} added {colors.green}{arg1}{colors.end} coins to {colors.cyan}{user.display_name}{colors.end}\'s account")
            else:
                pass
        elif arg1 == None:
            await ctx.reply('Usage: `;add <user> binary\\hex\\decimal`')
            return
        else:
            await ctx.send('Invalid value.')

@client.command(aliases=['vs', 'configuration', 'config'])
async def viewsettings(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    gd_data = load_guild_data(ctx.guild.id)
    embed1232 = Embed(title=f'Settings for {ctx.guild.name} (ID: {ctx.guild.id})', color=theme_color)
    embed1232.add_field(name='Swear filter', value=gd_data.swearfilter, inline=True)
    embed1232.add_field(name='Link blocker', value=linkblocker[str(ctx.guild.id)], inline=True)
    embed1232.add_field(name='Leveling', value=gd_data.levelingsystem, inline=True)
    embed1232.add_field(name='Welcome message', value=str(welcomemsg[str(ctx.guild.id)]), inline=True)
    embed1232.add_field(name='Goodbye message', value=str(goodbyemsg[str(ctx.guild.id)]), inline=True)
    embed1232.add_field(name='Robbing', value=gd_data.rob, inline=True)
    embed1232.add_field(name='Gifting', value=gd_data.gift, inline=True)
    embed1232.set_footer(icon_url=ctx.guild.icon_url, text='1 = enabled\n0 = disabled')
    await ctx.send(embed=embed1232)

@client.command(aliases=['sf', 'setconfiguration', 'setconfig'])
@commands.has_permissions(administrator=True)
async def setfeature(ctx, name, status):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
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
async def status(ctx):
  e = Embed(title='We have moved on.', description='Due to UptimeRobot blacklisting our hosting platform, we are forced to move away from it. However to get uptime status, we will find another solution ASAP.', color=theme_color)
  await ctx.reply(embed=e)

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def beg(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    current_time = timefetch.timenow
    member_data = load_member_data(ctx.author.id)
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

    save_member_data(ctx.author.id, member_data)
    if bool(log) == True:
        print(f'[{current_time}] {colors.cyan}{ctx.author.display_name}{colors.end} earned {colors.green}{coins}{colors.end} coins from begging.')
    else:
        pass

@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if bool(currency) == False:
        await ctx.reply('Currency is disabled')
        return
    else:
        pass
    current_time = timefetch.timenow 
    member_data = load_member_data(ctx.author.id)
    member_data.wallet += 10000
    await ctx.send('You claimed 10,000 coins')
    save_member_data(ctx.author.id, member_data)
    if bool(log) == True:
        print(f'[{current_time}] {colors.cyan}{ctx.author.display_name}{colors.end} claimed {colors.green}10000{colors.end} coins from daily command.')
    else:
        pass

@client.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def fish(message):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if bool(currency) == False:
        await message.channel.send('Currency is disabled')
        return
    else:
        pass
    member_data = load_member_data(message.author.id)
    if member_data.fishingpole < 1:
        await message.reply(f'How will you be able to catch fish without a fishing rod? First buy a fishing pole from the shop with `;buy fishingpole`.')
        return
    else:
        pass
    items = [
        "nothing",
        "fish",
        "rare fish",
        "goldfish",
        "mythic fish",
        "exotic fish"
    ]
    item = choice(items)
    if item == 'nothing':
        await message.channel.send('Looks like the fish were weary of your rod... you caught nothing.')
    elif item == 'fish':
        await message.channel.send(f'You caught a **fish** and sold it for 100 coins')
        member_data.wallet += 100
        save_member_data(message.author.id, member_data)
    elif item == 'rare fish':
        await message.channel.send(f'You caught a **rare fish** and sold it for 300 coins')
        member_data.wallet += 300
        save_member_data(message.author.id, member_data)
    elif item == 'goldfish':
        await message.channel.send(f'You caught a **goldfish** and sold it for 420 coins')
        member_data.wallet += 420
        save_member_data(message.author.id, member_data)
    elif item == 'mythic fish':
        await message.channel.send(f'You caught a **mythic** fish and sold it for 1000 coins')
        member_data.wallet += 1000
        save_member_data(message.author.id, member_data)
    elif item == 'exotic fish':
        await message.channel.send(f'You caught an **exotic** fish and sold it for 10000 coins. GG!')
        member_data.wallet += 1000
        save_member_data(message.author.id, member_data)

@client.command()
@commands.has_permissions(kick_members=True)
async def giveaway(ctx):
  await ctx.send("Let's start with this giveaway!")
  questions = ["Which channel should it be hosted in?", "What should be the duration of the giveaway? (s|m|h|d)", "What is the prize of the giveaway?"]
  answers = []
  #def check(m):
  #  return m.author == ctx.author and m.channel == ctx.channel
  def check(msg):
    return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)
  for i in questions:
    await ctx.send(i)
    try:
      msg = await client.wait_for('message', timeout=15.0, check=check)
    except asyncio.TimeoutError:
      await ctx.send('You didn\'t answer in time, please be quicker next time!')
      return
    else: 
      answers.append(msg.content)
  try:
    c_id = int(answers[0][2:-1])
  except:
    await ctx.send(f"You didn't mention a channel properly. Do it like this {ctx.channel.mention} next time.")
    return
  channel = client.get_channel(c_id)
  time = convert(answers[1])
  if time == -1:
    await ctx.send("You didn't answer with a proper unit. Use (s|m|h|d) next time!")
    return
  elif time == -2:
    await ctx.send("The time just be an integer. Please enter an integer next time.")
    return
  prize = answers[2]
  await ctx.send(f"Ok, the giveaway will be in {channel.mention} and will last {answers[1]}")
  embed = discord.Embed(title = ":tada: A Giveaway Started!", description = f"{prize}", color = discord.Color.random())
  embed.add_field(name = "Hosted by:", value = ctx.author.mention)
  embed.set_footer(text = f"Ends {answers[1]} from now")
  my_msg = await channel.send(embed = embed)
  await my_msg.add_reaction("🎉")
  await asyncio.sleep(time)
  new_msg = await channel.fetch_message(my_msg.id)
  users = await new_msg.reactions[0].users().flatten()
  users.pop(users.index(client.user))
  winner = choice(users)
  await channel.send(f"Congratulations! {winner.mention} won the prize: {prize}!")

@client.command()
@commands.has_permissions(kick_members=True)
async def reroll(ctx, channel:discord.TextChannel, id_:int):
  try:
    new_msg = await channel.fetch_message(id_)
  except:
    await ctx.send("I couldn't find a giveaway attached to this ID, make sure you have entered the correct giveaway message ID.")
  users = await new_msg.reactions[0].users().flatten()
  users.pop(users.index(client.user))
  winner = choice(users)
  await channel.send(f"The new winner is {winner.mention} for the giveaway rerolled!")

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def dig(message):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    member_data = load_member_data(message.author.id)
    if bool(currency) == False:
        await message.channel.send('Currency is disabled')
        return
    else:
        pass
    if member_data.shovel < 1:
        await message.reply(f'You can\'t dig the ground with your bare hands. You need a shovel for that! Use `;buy shovel` to get one.')
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
        await message.channel.send('After some time of digging, you found absolutely nothing an decided to give up')
    if item == 'fell':
        await message.channel.send('You fell into the hole and died of fall damage. You lost 300 coins.')
        member_data.wallet -= 300
        save_member_data(message.author.id, member_data)
    elif item == 'rock':
        await message.channel.send(f'You found a rock. You sold it and earned 100 coins.')
        member_data.wallet += 100
        save_member_data(message.author.id, member_data)
    elif item == 'python':
        await message.channel.send(f'You found a pet python. You sold it and earned 500 coins.')
        member_data.wallet += 500
        save_member_data(message.author.id, member_data)
    elif item == 'shovel':
        await message.channel.send(f'You found someone else\'s shovel while digging. Finders keepers! It has been placed in your inventory for later use..')
        member_data.shovel += 1
        save_member_data(message.author.id, member_data)
    elif item == 'treasure_chest':
        await message.channel.send(f'You found a treasure chest while digging. On opening it turns out that it is full of gold. You lucky ducky! You sold it and got a 5000 coin bounty.')
        member_data.wallet += 5000
        save_member_data(message.author.id, member_data)

@client.command(aliases=['dep'])
async def deposit(ctx, *, arg1):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        member_data = load_member_data(ctx.author.id)
        if arg1 == 'all' or arg1 == 'max':
            if member_data.wallet == 0:
                await ctx.reply('You don\'t have any coins in your wallet!')
                return
            elif (member_data.wallet + member_data.bank) > 100000000000:
                amt = member_data.bank
                todeposit = 100000000000 - amt #This gets the amount of coin-space available in the bank account#
                member_data.bank += int(todeposit)
                member_data.wallet -= int(todeposit)
                save_member_data(ctx.author.id, member_data)
                await ctx.reply(f'You deposited {todeposit} coins into your bank account. You have now reached your bank account limit of `100,000,000,000` coins.')
                return
            elif member_data.bank == 100000000000:
                await ctx.reply('You have reached your bank account limit of `100,000,000,000` coins!')
                return
            else:
                if member_data.wallet == 1:
                    await ctx.reply(f'You deposited {member_data.wallet} coin to your bank account.')
                else:
                    await ctx.reply(f'You deposited {member_data.wallet} coins to your bank account.')
                member_data.bank += int(member_data.wallet)
                member_data.wallet -= int(member_data.wallet)
                save_member_data(ctx.author.id, member_data)
                return
        elif arg1.isdigit:
            num = 0
            try: num = convert_value(arg1)
            except: num = arg1
            if int(num) > member_data.wallet:
                await ctx.reply('You don\'t have that many coins in your wallet.')
                return
            elif int(num) < 0:
                await ctx.reply('Don\'t try to break me **dood**')
                return
            elif (int(num) + member_data.bank) > 100000000000:
                await ctx.reply('That\'s past your bank account\'s maximum limit of `100,000,000,000` coins!')
                return
            else:
                await ctx.send(f'You deposited {num} coins to your bank account.')
                member_data.wallet -= int(num)
                member_data.bank += int(num)
                save_member_data(ctx.author.id, member_data)
                return
        else:
            raise BadArgument

@client.command(aliases=['with'])
async def withdraw(ctx, *, arg1):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    current_time = timefetch.timenow
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        member_data = load_member_data(ctx.author.id)
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
                if bool(log) == True:
                    print(f'[{current_time}] {colors.cyan}{ctx.author.display_name}{colors.end} withdrew {colors.green}{member_data.bank}{colors.end} coin\\s from their bank account.')
                else:
                    pass
                save_member_data(ctx.author.id, member_data)
                return
        elif arg1.isdigit:
            num = 0
            try: num = convert_value(arg1)
            except: num = arg1
            if int(num) > member_data.bank:
                await ctx.reply('You don\'t have that many coins in your bank!')
                return
            elif int(num) < 0:
                await ctx.reply('Don\'t try to break me dood')
                return
            else:
                await ctx.reply(f'You withdrawn {num} coins from your bank account.')
                member_data.wallet += int(num)
                member_data.bank -= int(num)
                save_member_data(ctx.author.id, member_data)
                return
        else:
            raise BadArgument

@client.command()
@commands.cooldown(1, 210, commands.BucketType.user)
async def bankrob(ctx, user:User):
    try:
        data = load_member_data(ctx.author.id)
        target_data = load_member_data(user.id)
        if ctx.author.id == user.id:
            await ctx.reply('You can\'t raid your own bank!')
            return
        elif data.wallet < 10000:
            await ctx.reply('You need at least 10k in your wallet to raid a bank.')
            return
        elif passivemode[str(ctx.author.id)] == 1:
            await ctx.send('Don\'t think of raiding someone\'s bank when you\'re already in passive.')
            return
        elif passivemode[str(user.id)] == 1:
            await ctx.send('Looks like the person who you are trying to rob from, is in passive.')
            return
        else:
            successrate = randint(1, 100)
            if (int(successrate) <= 30):
                payout:int = randint(10000, int(target_data.bank))
                target_data.bank -= payout
                save_member_data(user.id, target_data)
                data.wallet += payout
                save_member_data(ctx.author.id, data)
                await ctx.send(embed=Embed(name='Bank raid payout', description=f':money_with_wings: {ctx.author.display_name} raided {user.display_name}\'s bank and fetched {payout} coins!'))
            else:
                await ctx.reply(f'{ctx.author.mention}, you successfully FAILED to rob {user.display_name}\'s bank account...')
    except Exception as e:
        await ctx.send(e)

@client.command(aliases=['createpoll'])
async def poll(ctx, question, *options: str):
    if len(options) <= 1:
        await ctx.send('You need more than one option to make a poll!')
        return
    if len(options) > 10:
        await ctx.send('You cannot make a poll for more than 10 things!')
        return

    if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
        reactions = ['✅', '❌']
    else:
        reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

    description = []
    for x, option in enumerate(options):
        description += '\n {} {}'.format(reactions[x], option)
    embed = discord.Embed(title=question, description=''.join(description), color=discord.Color.random())
    react_message = await ctx.send(embed=embed)
    for reaction in reactions[:len(options)]:
        await react_message.add_reaction(reaction)
    embed.set_footer(text=f'Poll ID: {react_message.id}')
    await react_message.edit(embed=embed)

@client.command(aliases=['showpoll'])
async def pollresults(ctx, id):
    poll_message = await ctx.get_message(id)
    if not poll_message.embeds:
        return
    embed = poll_message.embeds[0]
    if poll_message.author.id != 896437848176230411:
        return
    if not embed['footer']['text'].startswith('Poll ID:'):
        await ctx.reply('I could not find a poll attached to that ID.')
        return
    unformatted_options = [x.strip() for x in embed['description'].split('\n')]
    opt_dict = {x[:2]: x[3:] for x in unformatted_options} if unformatted_options[0][0] == '1' \
        else {x[:1]: x[2:] for x in unformatted_options}
    # check if we're using numbers for the poll, or x/checkmark, parse accordingly
    voters = [ctx.message.server.me.id]  # add the bot's ID to the list of voters to exclude it's votes

    tally = {x: 0 for x in opt_dict.keys()}
    for reaction in poll_message.reactions:
        if reaction.emoji in opt_dict.keys():
            reactors = await ctx.get_reaction_users(reaction)
            for reactor in reactors:
                if reactor.id not in voters:
                    tally[reaction.emoji] += 1
                    voters.append(reactor.id)

    output = 'Results of the poll for "{}":\n'.format(embed['title']) + \
             '\n'.join(['{}: {}'.format(opt_dict[key], tally[key]) for key in tally.keys()])
    await ctx.send(output)

@client.command(aliases=['steal'])
@commands.cooldown(1, 40, commands.BucketType.user)
async def rob(ctx, *, user : User):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    gd_data = load_guild_data(ctx.guild.id)
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    elif gd_data.rob == 0:
        await ctx.reply('This command has been disabled in this server.')
        return
    elif passivemode[str(ctx.author.id)] == 1:
        await ctx.send('Hey, you\'re in passive. Disable that to rob!')
        return
    elif passivemode[str(user.id)] == 1:
        await ctx.send('The person you\'re trying to rob is currently in passive LOL')
        return
    else:
        pass
    current_time = timefetch.timenow
    if ctx.author.id == user.id:
        await ctx.send('Imagine robbing yourself')
        return
    elif user.id == 738290097170153472:
        await ctx.send('You can\'t rob the bot developer LOL')
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
                vic_data.wallet -= coins
                save_member_data(user.id, vic_data)
                member_data = load_member_data(ctx.author.id)
                member_data.wallet += coins
                save_member_data(ctx.author.id, member_data)
                await ctx.send(f'You stole {coins} coins from **{user.display_name}**, sussy baka')

@slash.slash(name='membercount', description='Shows the number of users in the server')
async def membercount(ctx):
    e = Embed(title=f'Member count in {ctx.guild}', description=f'{ctx.guild.member_count} members', color=theme_color)
    e.set_footer(text='Bots are included')
    await ctx.reply(embed=e)

@client.command(aliases=['silence', 'shutup'])
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member:discord.Member, *, reason:str=None):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if member.id == ctx.author.id:
        await ctx.reply('You can\'t mute yourself.')
        return
    else:
        pass
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title=f":white_check_mark: {member.display_name} was muted.", description=f"Reason: *{reason}*", colour=theme_color)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f"{member.mention}, you have been muted from: {guild.name}.\nReason: *{reason}*")

@client.command(aliases=['unsilence', 'unshutup'])
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member:discord.Member):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if member.id == ctx.author.id:
        await ctx.reply('You can\'t unmute yourself.')
        return
    else:
        pass
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(mutedRole)
    await member.send(f"{member.mention}, you have been unmuted from {ctx.guild.name}.")
    embed = discord.Embed(title=f":white_check_mark: Unmuted {member.display_name}", colour=theme_color)
    await ctx.send(embed=embed)

@client.command()
async def whoppa(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    e = Embed(title='Whoppa')
    e.set_image(url='https://upload.wikimedia.org/wikipedia/commons/b/b8/WHOPPER_with_Cheese%2C_at_Burger_King_%282014.05.04%29.jpg')
    await ctx.send(embed = e)

@client.command()
@commands.has_permissions(administrator = True)
async def setlevelupchannel(ctx, channelid:discord.TextChannel):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    levelupchannel[str(ctx.guild.id)] = channelid.id
    savejson()
    await ctx.send(f':white_check_mark: New level-ups will now redirect to <#{channelid.id}>')

@client.command(aliases=['rps'])
@commands.cooldown(1, 30, commands.BucketType.user)
async def rockpaperscissor(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    actions = [
        'rock',
        'paper',
        'scissor'
    ]
    actionselect = choice(actions)
    def check(msg):
        return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)
    embed1001 = Embed(title='Rock Paper Scissor', description='Choose \'rock\', \'paper\' or \'scissor\'!', color=theme_color)
    await ctx.send(embed = embed1001)
    memberdata = load_member_data(ctx.author.id)
    msg = await client.wait_for("message", check=check)
    randcoins = randint(100, 800)
    if msg.content == 'rock':
        if actionselect == 'rock':
            await ctx.send('Ayo, that\'s a tie!')
        elif actionselect == 'paper':
            await ctx.send('You chose: **rock**\nI chose: **paper**\n\nI defeated you! You earned nothing.')
        elif actionselect == 'scissor':
            await ctx.send(f'You chose: **rock**\nI chose: **scissor**\n\nOk you won. You earned {randcoins}.')
            memberdata.wallet += randcoins
            save_member_data(ctx.author.id, memberdata)
    elif msg.content == 'paper':
        if actionselect == 'rock':
            await ctx.send(f'You chose: **paper**\nI chose: **rock**\n\nOk you won. You earned {randcoins}.')
            memberdata.wallet += randcoins
            save_member_data(ctx.author.id, memberdata)
        elif actionselect == 'paper':
            await ctx.send('Ayo, that\'s a tie!')
        elif actionselect == 'scissor':
            await ctx.send('You chose: **paper**\nI chose: **scissor**\n\nI defeated you! You earned nothing.')
    elif msg.content == 'scissor':
        if actionselect == 'rock':
            await ctx.send('You chose: **scissor**\nI chose: **rock**\n\nI defeated you! You earned nothing.')
        elif actionselect == 'paper':
            await ctx.send(f'You chose: **scissor**\nI chose: **paper**\n\nOk you won. You earned {randcoins}.')
            memberdata.wallet += randcoins
            save_member_data(ctx.author.id, memberdata)
        elif actionselect == 'scissor':
            await ctx.send('Ayo, that\'s a tie!')
    else:
        raise(BadArgument)

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def hunt(message):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
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
        "died",
        "box"
    ]
    item = choice(items)
    if item == 'nothing':
        await message.channel.send('You went into the woods for hunting, but you found nothing. Better luck next time!')
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
    elif item == 'box':
        await message.channel.send('You went for hunting, but instead found a normal box! See what\'s inside it by typing `;open normalbox`!')
        member_data = load_member_data(message.author.id)
        member_data.normalbox += 1
        save_member_data(message.author.id, member_data)

@client.command()
@commands.cooldown(1, 604800, commands.BucketType.user)
async def weekly(message):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    server_actionlog = '/botLog/actionlogs/{message.guild.id}.txt'
    if bool(currency) == False:
        await message.channel.send('Currency is disabled')
        return
    else:
        pass
    current_time = timefetch.timenow
    member_data = load_member_data(message.author.id)
    member_data.wallet += 50000
    await message.reply('You claimed 50,000 coins')
    save_member_data(message.author.id, member_data)

@client.command()
@commands.cooldown(1, 2592000, commands.BucketType.user)
async def monthly(message):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    server_actionlog = '/botLog/actionlogs/{message.guild.id}.txt'
    if bool(currency) == False:
        await message.reply('Currency is disabled')
        return
    else:
        pass
    current_time = timefetch.timenow
    member_data = load_member_data(message.author.id)
    member_data.wallet += 100000
    await message.channel.send('You claimed 100,000 coins')
    save_member_data(message.author.id, member_data)

@client.command()
async def yearly(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    await ctx.reply('What are you thinking lol')

@client.command()
async def dev_claim(message):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
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
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if ctx.author.id == 738290097170153472:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        member_data = load_member_data(user.id)
        member_data.wallet -= member_data.wallet
        member_data.bank -= member_data.bank
        await ctx.send(f"Wiped {user}'s account")
        save_member_data(user.id, member_data)
        if bool(log) == True:
            print(f'[{current_time}] {ctx.author.display_name} {colors.red}wiped{colors.end} {user.display_name}\'s profile.')
        else:
            pass
    else:
        await ctx.reply('I dont think you are my developer. Are you?')

@client.command(aliases=['cg'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def catgirl(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    cgid = ''
    try:
      cgid = nekos.img('neko')
    except:
      await ctx.reply('Unable to find a catgirl. Is nekos.life down?')
      return
    embed1919 = Embed(title='Catgirl')
    embed1919.set_image(url=cgid)
    msge = await ctx.send(embed=embed1919)
    await msge.add_reaction('🔄')
    def check(reaction, user):
        return user == ctx.author
    reaction = None
    while True:
        if str(reaction) == '🔄':
            cgid = nekos.img('neko')
            embed1919.set_image(url=cgid)
            await msge.edit(embed = embed1919)
        try:
            reaction, user = await client.wait_for('reaction_add', timeout = 30.0, check = check)
            await msge.remove_reaction(reaction, user)
        except:
            break
    await msge.clear_reactions()

@client.command(aliases=['bal'])
async def balance(ctx, user : User=None):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    if user == None:
        member_data = load_member_data(ctx.author.id)
        embed = Embed(title=f"{ctx.author.display_name}'s Balance", color=theme_color)
        embed.add_field(name="Wallet", value=str(member_data.wallet))
        embed.add_field(name="Bank", value=f'{str(member_data.bank)}/100,000,000,000')
        embed.add_field(name='Net worth', value=int(member_data.wallet) + int(member_data.bank))
        embed.set_footer(text=f'Currency api made by {owner}')
        await ctx.send(embed=embed)
    else:
        member_data = load_member_data(user.id)
        embed = Embed(title=f"{user.display_name}'s Balance", color=theme_color)
        embed.add_field(name="Wallet", value=str(member_data.wallet))
        embed.add_field(name="Bank", value=f'{str(member_data.bank)}/100,000,000,000')
        embed.add_field(name='Net worth', value=int(member_data.wallet) + int(member_data.bank))
        embed.set_footer(text=f'Currency api made {owner}')
        await ctx.send(embed=embed)

@client.command(aliases=['ui'])
async def userinfo(ctx, user:User = None):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if user == None:
        is_bot = 'NA'
        if ctx.author.bot == True:
            is_bot = 'Bot'
        elif ctx.author.bot == False:
            is_bot = 'Normal user'
        await ctx.trigger_typing()
        created = f'{ctx.author.created_at.strftime("%H:%M:%S")} on {ctx.author.created_at.strftime("%d/%m/%Y")}'
        userAvatar = ctx.author.avatar_url
        embed683 = Embed(title=f'User info for {ctx.author}', description=f'User Name: {ctx.author}\nDisplay Name: {ctx.author.display_name}\nUser ID: {ctx.author.id}\nAvatar URL: {userAvatar}\nAccount Created: {created}\nUser Type: {is_bot}\n', color=ctx.author.colour)
        embed683.set_thumbnail(url=userAvatar)
        embed683.set_footer(text=f'User info requested by {ctx.author}', icon_url=str(ctx.author.avatar_url))
        await ctx.send(embed=embed683)
    else:
        is_bot = 'NA'
        if user.bot == True:
            is_bot = 'Bot'
        elif user.bot == False:
            is_bot = 'Normal user'
        await ctx.trigger_typing()
        created = f'{user.created_at.strftime("%H:%M:%S")} on {user.created_at.strftime("%d/%m/%Y")}'
        userAvatar = user.avatar_url
        embed683 = Embed(title=f'User info for {user}', description=f'Display Name: {user.display_name}\nDiscord Tag: {user}\nUser ID: {user.id}\nAvatar URL: {userAvatar}\nAccount Created: {created}\nUser Type: {is_bot}\n', color=user.colour)
        embed683.set_thumbnail(url=userAvatar)
        embed683.set_footer(text=f'User info requested by {ctx.author}', icon_url=str(ctx.author.avatar_url))
        await ctx.send(embed=embed683)

@client.command(aliases=['inv'])
async def inventory(ctx, userINV:User=None):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if bool(currency) == False:
        await ctx.reply('Currency is disabled.')
        return
    else:
        pass
    if userINV == None:
        member_data = load_member_data(ctx.author.id)
        mid = str(ctx.author.id)
        e = Embed(title=f'{ctx.author.display_name}\'s Inventory', description=f'**Utility**\nHunting rifle `ID: rifle`: {member_data.rifle}\nFishing pole `ID: fishingpole`: {member_data.fishingpole}\nShovel `ID: shovel`: {member_data.shovel}\n\n**Boxes**\nNormal Box `ID: normalbox`: {normalbox[mid]}\nPro Box `ID: probox`: {probox[mid]}\nDeveloper Box `ID: devbox`: {devbox[mid]}\n\n**Economy**\nCoin Bomb `ID: coinbomb`: {member_data.cbomb}\n\n**Badges:**\nPrestige `ID: prestige`: {prestige_conf[mid]}', color=theme_color)
        await ctx.send(embed=e)
    else:
        mid = str(userINV.id)
        member_data = load_member_data(userINV.id)
        e = Embed(title=f'{userINV.display_name}\'s Inventory', description=f'**Utility**\nHunting rifle: {member_data.rifle}\nFishing pole: {member_data.fishingpole}\nShovel: {member_data.shovel}\n\n**Boxes**\nNormal Box: {normalbox[mid]}\nPro Box: {probox[mid]}\nDeveloper Box: {devbox[mid]}\n\n**Economy**\nCoin Bomb: {member_data.cbomb}\n\n**Badges**\nPrestige `ID: prestige`: {prestige_conf[mid]}', color=theme_color)
        await ctx.send(embed=e)

@client.command()
async def shop(ctx):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if bool(currency) == False:
        await ctx.reply('Currency is disabled.')
        return
    else:
        pass
    page1 = Embed(title='Utility Tools Shop', description='Available items:\n\n**Hunting rifle**\nDescription: This is a tool used for hunting. Well, I guess not many people can hunt with their bare hands...\nPrice: 10000 coins\nHow to buy: `;buy rifle`\n\n**Fishing pole**\nDescription: This is a tool used for fishing. Fish without it and the fish will fall right back into the water.\nPrice: 5000 coins\nHow to buy: `;buy fishingpole`\n\n**Shovel**\nDescription: This is a tool used for digging. You\'re not a dog, are you?\nPrice: 3500 coins\nHow to buy: `;buy shovel`', color=theme_color)
    page2 = Embed(title='Economy Items Shop', description='Available items:\n\n**Coin Bomb**\nDescription: A bomb full of coins which you can explode to claim!\nPrice: 1500 coins\nHow to buy: `;buy coinbomb`', color=theme_color)
    page3 = Embed(title='Boxes Shop', description='Available Items:\n\n**Normal Box**\nDescription: A common box you can buy from the shop (here), or which you can encounter while hunting.\nPrice: 10000 coins\nHow to buy: `;buy normalbox`\n\n**Pro Box**\nDescription: A rare box you can only buy from the shop, and contains some cool stuff!\nPrice: 35000 coins\nHow to buy: `;buy probox`', color=theme_color)
    page4 = Embed(title='Badges Shop', description='**Coming Soon!**', color=theme_color)
    page1.set_footer(text='To buy an item, run \';buy [item_name]\' command.')
    page2.set_footer(text='To buy an item, run \';buy [item_name]\' command.')
    page3.set_footer(text='To buy an item, run \';buy [item_name]\' command.')
    page4.set_footer(text='To buy an item, run \';buy [item_name]\' command.')
    pages = [
        page1,
        page2,
        page3,
        page4
    ]
    message = await ctx.send(embed = page1)
    await message.add_reaction('◀')
    await message.add_reaction('▶')
    def check(reaction, user):
        return user == ctx.author
    i = 0
    reaction = None
    while True:
        if str(reaction) == '◀':
            if i > 0:
                i -= 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '▶':
            if i < 3:
                i += 1
                await message.edit(embed = pages[i])
        try:
            reaction, user = await client.wait_for('reaction_add', timeout = 30.0, check = check)
            await message.remove_reaction(reaction, user)
        except:
            break
    await message.clear_reactions()

@client.command(aliases=['purchase'])
async def buy(ctx, *, arg1):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if bool(currency) == False:
        await ctx.reply('Currency is disabled.')
        return
    elif bool(buy) == False:
        await ctx.reply('This command is disabled.')
        return
    else:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        member_data = load_member_data(ctx.author.id)
        if str(arg1) == 'rifle':
            if member_data.wallet < 10000:
                await ctx.reply('You don\'t have enough coins to buy this item!')
            else:
                member_data.wallet -= 10000
                member_data.rifle += 1
                save_member_data(ctx.author.id, member_data)
                await ctx.reply('You just bought 1 **Hunting rifle** from the shop!')
                if bool(log) == True:
                    print(f'[{current_time}]: [Shop/INFO]: {colors.cyan}{ctx.author.display_name}{colors.end} bought {colors.green}1 Hunting rifle{colors.end} from the shop.')
                else:
                    pass
        elif str(arg1) == 'shovel':
            if member_data.wallet < 3500:
                await ctx.reply('You don\'t have enough coins to buy this item!')
            else:
                member_data.wallet -= 3500
                member_data.shovel += 1
                save_member_data(ctx.author.id, member_data)
                await ctx.reply('You just bought 1 **Shovel** from the shop!')
                if bool(log) == True:
                    print(f'[{current_time}]: [Shop/INFO]: {colors.cyan}{ctx.author.display_name}{colors.end} bought {colors.green}1 Shovel{colors.end} from the shop.')
                else:
                    pass
        elif str(arg1) == 'fishingpole':
            if member_data.wallet < 5000:
                await ctx.reply('You don\'t have enough coins to buy this item!')
            else:
                member_data.wallet -= 5000
                member_data.fishingpole += 1
                save_member_data(ctx.author.id, member_data)
                await ctx.reply('You just bought 1 **Fishing pole** from the shop!')
                if bool(log) == True:
                    print(f'[{current_time}]: [Shop/INFO]: {colors.cyan}{ctx.author.display_name}{colors.end} bought {colors.green}1 Fishing pole{colors.end} from the shop.')
                else:
                    pass
        elif str(arg1) == 'coinbomb':
            if member_data.wallet < 1500:
                await ctx.reply('You don\'t have enough coins to buy this item!')
            else:
                member_data.wallet -= 1500
                member_data.cbomb += 1
                save_member_data(ctx.author.id, member_data)
                await ctx.reply('You just bought 1 **Coin Bomb** from the shop!')
                if bool(log) == True:
                    print(f'[{current_time}]: [Shop/INFO]: {colors.cyan}{ctx.author.display_name}{colors.end} bought {colors.green}1 Coin Bomb{colors.end} from the shop.')
                else:
                    pass
        elif str(arg1) == 'normalbox':
            if member_data.wallet < 10000:
                await ctx.reply('You don\'t have enough coins to buy this item!')
            else:
                member_data.wallet -= 10000
                normalbox[str(ctx.author.id)] += 1
                savejson()
                save_member_data(ctx.author.id, member_data)
                await ctx.reply('You just bought 1 **Normal box** from the shop!')
                if bool(log) == True:
                    print(f'[{current_time}]: [Shop/INFO]: {colors.cyan}{ctx.author.display_name}{colors.end} bought {colors.green}1 Normal box{colors.end} from the shop.')
                else:
                    pass
        elif str(arg1) == 'probox':
            if member_data.wallet < 35000:
              await ctx.reply('You don\'t have enough coins to buy this item!')
            else:
              member_data.wallet -= 35000
              probox[str(ctx.author.id)] += 1
              savejson()
              save_member_data(ctx.author.id, member_data)
              await ctx.reply('You just bought 1 **Pro box** from the shop!')
              if bool(log) == True:
                print(f'[{current_time}]: [Shop/INFO]: {colors.cyan}{ctx.author.display_name}{colors.end} bought {colors.green}1 Pro box{colors.end} from the shop.')
              else:
                pass
        else:
          await ctx.message.add_reaction('❌')
          await ctx.reply(f'wtf is {arg1}?')

@client.command()
async def sell(ctx, *, item_name = None):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    member_data = load_member_data(ctx.author.id)
    if item_name == None:
        await ctx.reply(f'{ctx.author.mention}, you have to choose the item you want to sell.')
    elif item_name == 'shovel':
        member_data.shovel -= 1
        member_data.wallet += 1250
        save_member_data(ctx.author.id, member_data)
        await ctx.reply(f'You sold 1 shovel in the market and earned **1250 coins**!')
    elif item_name == 'rifle':
        member_data.rifle -= 1
        member_data.wallet += 5000
        save_member_data(ctx.author.id, member_data)
        await ctx.reply(f'You sold 1 hunting rifle in the market and earned **5000 coins**!')
    elif item_name == 'fishingpole':
        member_data.shovel -= 1
        member_data.wallet += 2500
        save_member_data(ctx.author.id, member_data)
        await ctx.reply(f'You sold 1 fishing pole in the market and earned **2500 coins**!')
    else:
        await ctx.reply(f'The item \'{item_name}\' doesn\'t exist or you cannot sell it.')

@client.command()
async def tempadmin(ctx, user : User, arg1):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    if ctx.author.id == 738290097170153472:
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

@client.command(aliases=['translate'])
async def translator(ctx, language:str, *, inputstr:str):
    translator = Translator(to_lang=language)
    translation = translator.translate(inputstr)
    e = Embed(title=f'Translation of {inputstr}', description=str(translation), color=theme_color)
    e.set_footer(text=f'Translated to {language}')
    await ctx.reply(embed=e)

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, prefix):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    with open('isobot/prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    with open('isobot/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send(f'Prefix successfully changed to `{prefix}`')

@client.command(aliases=['linkblocker'])
@commands.has_permissions(administrator=True)
async def linkblock(ctx, status):
    if status.lower() == 'true':
        linkblocker[str(ctx.guild.id)] = 1
        await ctx.reply(':white_check_mark: Link blocker enabled.')
    elif status.lower() == 'false':
        linkblocker[str(ctx.guild.id)] = 0
        await ctx.reply(':white_check_mark: Link blocker disabled.')
    else:
        raise(BadArgument)
    savejson()

@client.command()
async def passive(ctx, arg1):
    if arg1.lower() == 'true':
        if passivemode[str(ctx.author.id)] == 1:
            await ctx.reply('You do you think you can enable something that\'s already enabled?')
            return
        else:
            passivemode[str(ctx.author.id)] = 1
            await ctx.reply('You\'re now in passive mode.')
    elif arg1.lower() == 'false':
        if passivemode[str(ctx.author.id)] == 0:
            await ctx.reply('You do you think you can disable something that\'s already disabled?')
            return
        else:
            passivemode[str(ctx.author.id)] = 0
            await ctx.reply('You\'re now out of passive mode. Be careful!')

@client.command()
async def reddit(ctx, subreddit):
  global prefixCommandsIssued
  prefixCommandsIssued += 1
  try:
    submissions = reddit.subreddit(str(subreddit)).hot()
    post_to_pick = randint(1, 100)
    for i in range(0, post_to_pick):
      submission = next(x for x in submissions if not x.stickied)
    embed = Embed(title = submission.title, color=randEmbedColor())
    embed.set_image(url=submission.url)
    embed.set_footer(text='Powered by PRAW (reddit)')
    await ctx.send(embed = embed)
  except Exception as e:
    await ctx.reply(f'Error: {e}.')

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

@slash.slash(name='userinvites', description='Shows how many people a user has invited to the server', options=[create_option(name='user', description='The user who you want to see total invites from', option_type=6, required=False)])
async def invites(ctx:SlashContext, user:str = None):
    global slashCommandsIssued
    slashCommandsIssued += 1
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
    global slashCommandsIssued
    slashCommandsIssued += 1
    channel = ctx.channel
    try:
        em = Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
    except:
        await ctx.send(f"There are no recently deleted messages in <#{channel.id}>")

@slash.slash(name="editsnipe", description="Shows the most recent edited message")
async def editsnipe(ctx:SlashContext):
    global slashCommandsIssued
    slashCommandsIssued += 1
    try:
        em = Embed(description=f'**Message before**: {editsnipe_messagebefore_content[ctx.channel.id]}\n**Message after**:{editsnipe_messageafter_content[ctx.channel.id]}')
        em.set_footer(text=f'This message was edited by {editsnipe_message_author[ctx.channel.id]}')
        await ctx.send(embed = em)
    except:
        await ctx.reply('No recent edited messages here :eyes:')

@slash.slash(name='help', description='Shows a list of commands that I can run (; prefix commands only)')
async def help(ctx:SlashContext):
    global slashCommandsIssued
    slashCommandsIssued += 1
    await ctx.send(embed=discord.Embed(title='**MY COMMAND LIST**', description=f'My main prefix is **;**\n\n**:moneybag: Economy:**\n```work, beg, balance, deposit, withdraw, shop, buy, inventory, give, rob, hunt, fish, daily, weekly, monthly, postmeme, scout, highlow, rockpaperscissor```\n**:musical_note: Music:**\n```join, play, skip, stop, volume, current, pause, queue, shuffle, remove, loop```\n**:information_source: Bot Information:**\n```session, ping, invites, avatar, userinfo, invite, uptime```\n**:shield: Moderation:**\n```ban, kick, mute, unmute, warn, set_level, purge, lock, unlock, nuke```\n**:sparkles: Misc:**\n```poll, pollresults, giveaway, reroll, 8ball, slap, kill, hug, stare, uwu, snipe, edit_snipe, amogus, fstab, say, cat```\n**:scroll: Reddit Commands:**\n```meme, linuxmeme, nothecker, aww, softwaregore, ihadastroke```\n**:wrench: Server Setup Utility:**\n```viewsettings, setfeature, changeprefix, setlevelupchannel, setwelcomemsg, setgoodbyemsg, linkblocker```\nTo get help on a specific command, type in `;help [command name]`.', color=theme_color))

@slash.slash(name="balance", description="Shows the money amount of a user", options=[create_option(name="user", description="The user you want to see the balance of", option_type=6, required=False)])
async def balance(ctx, user:str=None):
    global slashCommandsIssued
    slashCommandsIssued += 1
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
    global slashCommandsIssued
    slashCommandsIssued += 1
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    await ctx.send(f'I have been running for {uptime}.')

@slash.slash(name="say", description="Makes the bot say anything", options=[create_option(name="text", description="What you want the bot to say", option_type=3, required=True)])
async def say(ctx:SlashContext, text:str):
    global slashCommandsIssued
    slashCommandsIssued += 1
    await ctx.send(text)

@slash.slash(name='changeprefix', description='Changes the prefix the bot responds to in this server', options=[create_option(name='prefix', description='The new preifx', option_type=3, required=True)])
async def changeprefix(ctx:SlashContext, prefix:str):
    global slashCommandsIssued
    slashCommandsIssued += 1
    if not ctx.author.guild_permissions.administrator:
        raise(MissingPermissions)
    else:
        pass
    with open('isobot/prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    with open('isobot/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send(f'Prefix successfully changed to `{prefix}`')

@slash.slash(name='welcomemessage', description='DMs a person a custom message when they join the server', options=[create_option(name='message', description='The custom message you want to set', option_type=3, required=False)])
async def setwelcomemessage(ctx:SlashContext, msgname:str = None):
    global slashCommandsIssued
    slashCommandsIssued += 1
    if not ctx.author.guild_permissions.administrator:
      raise(MissingPermissions)
    if msgname == None:
      welcomemsg[str(ctx.guild.id)] = 0
      await ctx.reply(':white_check_mark: Welcome message reset.')
    else:
      welcomemsg[str(ctx.guild.id)] = msgname
      await ctx.reply(':white_check_mark: Welcome message successfully set.')
    savejson()

@slash.slash(name='goodbyemessage', description='DMs a person a custom message when they leave the server', options=[create_option(name='message', description='The custom message you want to set', option_type=3, required=False)])
async def setgoodbyemessage(ctx:SlashContext, msgname:str = None):
    global slashCommandsIssued
    slashCommandsIssued += 1
    if not ctx.author.guild_permissions.administrator:
      raise(MissingPermissions)
    if msgname == None:
      goodbyemsg[str(ctx.guild.id)] = 0
      await ctx.reply(':white_check_mark: Goodbye message reset.')
    else:
      goodbyemsg[str(ctx.guild.id)] = msgname
      await ctx.reply(':white_check_mark: Goodbye message successfully set.')
    savejson()

@slash.slash(name='autowelcome', description='Sends a welcome message each time a member joins', options=[create_option(name='channel', description='The channel where you want the bot to send welcome messages', option_type=7, required=False)])
async def autowelcome(ctx:SlashContext, channel = None):
  global slashCommandsIssued
  slashCommandsIssued += 1
  if not ctx.author.guild_permissions.administrator:
    raise(MissingPermissions)
  if channel == None:
    welcomer[str(ctx.guild.id)] = 0
    await ctx.send(':white_check_mark: Auto-welcome has been disabled.')
  else:
    welcomer[str(ctx.guild.id)] = channel.id
    await ctx.send(f':white_check_mark: Auto-welcome set to <#{channel.id}>.')
             
@slash.slash(name='meme', description='Finds a random popular meme from reddit')
async def meme(ctx:SlashContext):
    global slashCommandsIssued
    slashCommandsIssued += 1
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
    global slashCommandsIssued
    slashCommandsIssued += 1
    msg1 = await ctx.send('Processing command...')
    sg_submissions = reddit.subreddit('softwaregore').hot()
    post_to_pick = randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in sg_submissions if not x.stickied)
    embed = Embed(title = submission.title, color=theme_color)
    embed.set_image(url=submission.url)
    embed.set_footer(text='Softwaregore be like')
    await msg1.edit(embed = embed)

@slash.slash(name='ihadastroke', description='I hab a strkke')
async def ihadastroke(ctx:SlashContext):
    global slashCommandsIssued
    slashCommandsIssued += 1
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
    global slashCommandsIssued
    slashCommandsIssued += 1
    memes_submissions = reddit.subreddit('linuxmemes').hot()
    post_to_pick = randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embed = Embed(title = submission.title, color=theme_color)
    embed.set_image(url=submission.url)
    embed.set_footer(text='I use Arch BTW')
    await ctx.send(embed = embed)

@slash.slash(name='aww', description='Shows cute images of dogs, cats, birds, and other adorable animals')
async def aww(ctx:SlashContext):
    global slashCommandsIssued
    slashCommandsIssued += 1
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
    global slashCommandsIssued
    slashCommandsIssued += 1
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

@slash.slash(name='reddit', description='Fetches a post from any subreddit.', options=[create_option(name='subreddit', description='The subreddit you want to view', option_type=3, required=True)])
async def reddit(ctx:SlashContext, subreddit):
  global slashCommandsIssued
  slashCommandsIssued += 1
  try:
    aww_submissions = reddit.subreddit(subreddit).hot()
    post_to_pick = randint(1, 100)
    for i in range(0, post_to_pick):
      submission = next(x for x in aww_submissions if not x.stickied)
    embed = Embed(title = submission.title, description=submission.selftext, color=theme_color)
    embed.set_image(url=submission.url)
    embed.set_footer(text=f'Brought to you by {subreddit} (Reddit)')
    await ctx.send(embed = embed)
  except:
    await ctx.reply('That\'s not a valid subreddit.')
                                                                                   
@slash.slash(name='8ball', description='Let the 8ball predict an outcome! (don\'t always take it seriously, it\'s probably wrong anyway)', options=[create_option(name='question', description='What you want to ask the 8ball', option_type=3, required=True)])
async def eightball(ctx:SlashContext, question):
    global slashCommandsIssued
    slashCommandsIssued += 1
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
        "You must be stupid or something, the answer is obviously no",
        "Hell to the yes!",
        "Frick yeah!",
        "Im an 8ball, not a 'dealwithurcrap' ball.",
        "What do you think? The answer is obviously yes",
        "What do you think? The answer is obviously no",
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
    global slashCommandsIssued
    slashCommandsIssued += 1
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
    global slashCommandsIssued
    slashCommandsIssued += 1
    rand_fact = nekos.fact()
    await ctx.send(f'**A random fact**\n> {rand_fact}')

@slash.slash(name='level', description='Shows your level, or the level of another user', options=[create_option(name='user', description='Displays the user\'s level', option_type=6, required=False)])
async def rank(ctx:SlashContext, user:str = None):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    gd_data = load_guild_data(ctx.guild.id)
    if gd_data.levelingsystem == 0:
        await ctx.reply(':warning: Leveling is disabled in this server')
        return
    else:
        pass
    if user == None:
        xpreq = 0
        for level in range(int(levels[str(ctx.guild.id)][str(ctx.author.id)])):
            xpreq += 50
            if xpreq >= 5000:
                break
        e = Embed(title=f"{ctx.author.display_name}'s XP")
        e.add_field(name='Level', value=str(levels[str(ctx.guild.id)][str(ctx.author.id)]))
        e.add_field(name='XP', value=str(f'{exp[str(ctx.guild.id)][str(ctx.author.id)]}/{xpreq}'))
        e.set_footer(text='To level up, keep on chatting!')
        await ctx.send(embed=e)
    else:
        xpreq = 0
        for level in range(levels[str(ctx.guild.id)][str(user.id)]):
            xpreq += 50
            if xpreq >= 5000:
                break
        e = Embed(title=f"{user.display_name}'s XP")
        e.add_field(name='Level', value=str(levels[str(ctx.guild.id)][str(user.id)]))
        e.add_field(name='XP', value=str(f'{exp[str(ctx.guild.id)][str(user.id)]}/{xpreq}'))
        e.set_footer(text='To level up, keep on chatting!')
        await ctx.send(embed=e)

@slash.slash(name='kick', description='Kicks a member from the server', options=[create_option(name='member', description='The person you want to kick', option_type=6, required=True)])
async def kick(ctx:SlashContext, member:str):
    global slashCommandsIssued
    slashCommandsIssued += 1
    current_time = timefetch.timenow
    if not ctx.author.guild_permissions.kick_members:
        raise(MissingPermissions)
    if member == ctx.author:
        await ctx.reply(':warning: I don\'t think you want to do that.')
        return
    else:
        try:
            await member.kick()
            embedKick = Embed(title=f':white_check_mark: *{member} has been **kicked** from the server.*', color=color_success)
            await ctx.send(embed=embedKick)
            if bool(log) == True:
                print(f'[{current_time}] {colors.cyan}{ctx.author.display_name}{colors.end} kicked {colors.green}{member.display_name}{colors.end} from {colors.green}{ctx.guild.name}{colors.end}.')
            else:
                pass
        except:
            embedKick = Embed(description=f':x: I was unable to kick {member}', color=color_fail)
            await ctx.send(embed=embedKick)

@slash.slash(name='ban', description='Bans a member from the server', options=[create_option(name='member', description='The person you want to ban', option_type=6, required=True)])
async def ban(ctx:SlashContext, member:str):
    global slashCommandsIssued
    slashCommandsIssued += 1
    current_time = timefetch.timenow
    if not ctx.author.guild_permissions.ban_members:
        raise(MissingPermissions)
    if member == ctx.author:
        await ctx.reply(':warning: I don\'t think you want to do that.')
        return
    else:
        try:
            await member.ban()
            embedBan = Embed(title=f':white_check_mark: *{member} has been **banned** from the server.*', color=color_success)
            await ctx.send(embed=embedBan)
            if bool(log) == True:
                print(f'[{current_time}] {colors.cyan}{ctx.author.display_name}{colors.end} banned {colors.green}{member.display_name}{colors.end} from {colors.green}{ctx.guild.name}{colors.end}')
            else:
                pass
        except:
            embedBan = Embed(description=f':x: I was unable to ban {member}', color=color_fail) 

@slash.slash(name='purge', description='Deletes a specific amount of messages from the chat', options=[create_option(name='amount', description='The number of messages you want to purge (Maximum: 550)', option_type=4, required=True)])
async def purge(ctx:SlashContext, amount:int):
    global slashCommandsIssued
    slashCommandsIssued += 1
    if not ctx.author.guild_permissions.manage_messages:
        raise(MissingPermissions)
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
        await ctx.send(embed = embedSuccessPurge, hidden=True)
        if bool(log) == True:
                print(f'[{current_time}] {colors.cyan}{ctx.author.display_name}{colors.end} purged {colors.green}{amount}{colors.end} messages from {colors.green}#{ctx.channel.name}{colors.end}.')
        else:
            pass

@slash.slash(name='automod', description='Shows the current configuration for automod')
async def automod(ctx):
  gd_data = load_guild_data(ctx.guild.id)
  e = Embed(title=f'Automod settings for {ctx.guild}', color=theme_color)
  e.add_field(name='Delete banned words (swearfilter)', value=gd_data.swearfilter)
  e.add_field(name='Delete all links (linkdelete)', value=linkblocker[str(ctx.guild.id)])
  e.add_field(name='Delete Discord invites (invitedelete)', value='*Coming soon*')
  e.set_footer(text='Use ";automod_set" to change automod settings.')
  await ctx.send(embed=e)

@slash.slash(name="sus", description="Tells if a user is sus", options=[create_option(name="user", description="is sus user", option_type=6, required=True)])
async def sus(ctx: SlashContext, user:str):
    global slashCommandsIssued
    slashCommandsIssued += 1
    susbool = [
        True,
        False
    ]
    isSus = choice(susbool)
    if isSus == True:
        await ctx.send(f'{user.mention} is very sus')
    else:
        await ctx.send(f'{user.mention} isn\'t sus')

@slash.slash(name="translate", description="Translate English text to any other language", options=[create_option(name='language', description='The language you want to translate into', option_type=3, required=True), create_option(name='text', description='The text you want to translate', option_type=3, required=True)])
async def translator(ctx:SlashContext, language:str, text:str):
    translator = Translator(to_lang=language)
    translation = translator.translate(text)
    e = Embed(title=f'Translation of {text}', description=str(translation), color=theme_color)
    e.set_footer(text=f'Translated to {language}')
    await ctx.reply(embed=e)

@slash.slash(name="ping", description="Shows bot ping")
async def ping(ctx:SlashContext):
    global slashCommandsIssued
    slashCommandsIssued += 1
    await ctx.send(f'Pong! My ping is {round(client.latency * 1000)}ms')

@slash.slash(name="invite", description="Sends an invite link for isobot")
async def invite(ctx:SlashContext):
    global slashCommandsIssued
    slashCommandsIssued += 1
    inviteLink = 'https://discord.com/oauth2/authorize?client_id=896437848176230411&permissions=8&scope=bot%20applications.commands'
    await ctx.reply(f'Invite isobot to your server with this link >> {inviteLink}')

@slash.slash(name="null", description="null")
async def null(ctx:SlashContext):
    global slashCommandsIssued
    slashCommandsIssued += 1
    await ctx.reply("You got __null__ coins **dood**")

@slash.slash(name='mute', description='Mutes a user in the server', options=[create_option(name='member', description='The member you want to mute', option_type=6, required=True), create_option(name='reason', description='The reason why you want to mute the user, if any', option_type=3, required=False)])
async def mute(ctx:SlashContext, member:discord.Member, *, reason=None):
    global slashCommandsIssued
    slashCommandsIssued += 1
    if not ctx.author.guild_permissions.manage_messages:
        raise(MissingPermissions)
    if member.id == ctx.author.id:
        await ctx.reply(':x: You can\'t mute yourself.', hidden=True)
        return
    else:
        pass
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title=f":white_check_mark: {member.display_name} was muted.", description=f"Reason: *{reason}*", colour=theme_color)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f"{member.mention}, you have been muted from: {guild.name}.\nReason: *{reason}*")

@slash.slash(name='unmute', description='Unmutes a user in the server', options=[create_option(name='member', description='The member you want to unmute', option_type=6, required=True)])
async def unmute(ctx:SlashContext, member:discord.Member):
    global slashCommandsIssued
    slashCommandsIssued += 1
    if not ctx.author.guild_permissions.manage_messages:
        return(MissingPermissions)
    if member.id == ctx.author.id:
        await ctx.reply(':x: You can\'t unmute yourself.', hidden=True)
        return
    else:
        pass
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(mutedRole)
    await member.send(f"{member.mention}, you have been unmuted from {ctx.guild.name}.")
    embed = discord.Embed(title=f":white_check_mark: Unmuted {member.display_name}", colour=theme_color)
    await ctx.send(embed=embed)

@slash.slash(
    name='usercount', 
    description='Shows the total number of users in the server.'
)
async def _membercount(ctx:SlashContext):
    e = Embed(title=f'Member count in {ctx.guild}', description=f'{ctx.guild.member_count} members', color=theme_color)
    e.set_footer(text='Bots are included')
    await ctx.reply(embed=e)

@slash.slash(
    name='give', 
    description='Lets you give coins to someone.', 
    options=[
        create_option(name='user', description='Who you want to give the cash to', option_type=6, required=True),
        create_option(name='amount', description='How many coins do you want to give?', option_type=4, required=True)
    ]
)
async def give(ctx:SlashContext, user, *, amount):
    global prefixCommandsIssued
    prefixCommandsIssued += 1
    gd_data = load_guild_data(ctx.guild.id)
    if user.id == ctx.author.id:
        await ctx.reply('You can\'t give coins to yourself')
        return
    elif gd_data.gift == 0:
        await ctx.reply('This feature has been disabled in this server.')
        return
    else:
        if amount.isdigit:
            member_data = load_member_data(ctx.author.id)
            if member_data.wallet < int(amount):
                await ctx.reply('You don\'t have that many coins in your wallet')
                return
            elif int(amount) < 0:
                await ctx.reply('Don\'t try to break me **dood**')
            elif int(amount) == 0:
                await ctx.reply('You can\'t gift 0 coins')
            else:
                member_data.wallet -= int(amount)
                save_member_data(ctx.author.id, member_data)
                user_data = load_member_data(user.id)
                user_data.wallet += int(amount)
                save_member_data(user.id, user_data)
                await ctx.reply(f'You gave {amount} coins to {user.display_name}')
        else:
            await ctx.reply(f'{amount} is not a digit **dood**')

@slash.slash(name='passive', description='Turns passive mode on or off', options=[create_option(name='value', description='Turn it on or off', option_type=3, required=True)])
async def passive(ctx:SlashContext, value):
    if value == 'true':
        if passivemode[str(ctx.author.id)] == 1:
            await ctx.reply('You do you think you can enable something that\'s already enabled?')
            return
        else:
            passivemode[str(ctx.author.id)] = 1
            await ctx.reply('You\'re now in passive mode.')
    elif value == 'false':
        if passivemode[str(ctx.author.id)] == 0:
            await ctx.reply('You do you think you can disable something that\'s already disabled?')
            return
        else:
            passivemode[str(ctx.author.id)] = 0
            await ctx.reply('You\'re now out of passive mode. Be careful!')

@slash.slash(name='vote', description='Vote for the bot on multiple sites!')
async def vote(ctx:SlashContext):
    global slashCommandsIssued
    slashCommandsIssued += 1
    e = Embed(title='Vote for isobot on DBL and top.gg', description=f'Discord Bot List: https://discordbotlist.com/bots/halloween-isobot \ntop.gg: https://top.gg/bot/896437848176230411/vote', color=theme_color)
    await ctx.send(embed=e)

@slash.slash(
  name='autorole',
  description='Gives new members the mentioned role',
  options=[
    create_option(name='role', description='What role do you want to give? (leave empty to disable)', option_type=8, required=False)
  ]
)
async def autorole(ctx:SlashContext, role:discord.Role):
  if not ctx.author.guild_permissions.administrator:
    await ctx.send(':x: You need administrator permissions to do this.', hidden=True)
    return
  if role == None:
    autoroles[str(ctx.guild.id)] = 0
    savejson()
    await ctx.send(":white_check_mark: Autoroles successfully disabled.")
  else:
    r_id = role.id
    autoroles[str(ctx.guild.id)] = r_id
    savejson()
    await ctx.send(f":white_check_mark: Now all new users will get the \"{role.name}\" role.")

#Execution
keep_alive()
client.run(libs.api.auth.token)
