import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
options = webdriver.EdgeOptions()
options.add_argument("--headless=new")
driver = webdriver.Edge(options=options)

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_message(message):
    if message.author == bot.user:
         return
    await bot.process_commands(message)

@bot.event
async def on_ready():
    print(f'Logou como {bot.user}')

@bot.command()
async def frame(ctx, arg1, arg2):
    driver.get(f"https://www.streetfighter.com/6/character/{arg1}/frame")
    moves_name = driver.find_elements(By.CLASS_NAME, "frame_arts__CNftl")
    moves_startup = driver.find_elements(By.CLASS_NAME, "frame_startup_frame__IeKL6")
    moves_active = driver.find_elements(By.CLASS_NAME, "frame_active_frame__1pLtR")
    moves_recovery = driver.find_elements(By.CLASS_NAME, "frame_recovery_frame__WLqFt")
    move_list = {move.get_attribute("innerText"): {"Startup": startup.get_attribute("innerText"), "Active": active.get_attribute("innerText"), "Recovery": recovery.get_attribute("innerText")}
             for move in moves_name
             for startup in moves_startup
             if moves_name.index(move)+1 == moves_startup.index(startup)
             for active in moves_active
             if moves_name.index(move)+1 == moves_active.index(active)
             for recovery in moves_recovery
             if moves_name.index(move)+1 == moves_recovery.index(recovery)}
    await ctx.channel.send(f'{arg1.upper()} {arg2}:')
    for data,key in move_list[arg2].items():
        await ctx.channel.send(f"{data}: {key}")

bot.run(DISCORD_TOKEN)