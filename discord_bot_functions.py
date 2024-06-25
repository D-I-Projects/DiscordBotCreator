#def start_bot():
#    TOKEN = "YOUR_DISCORD_BOT_TOKEN"
#    adding_command_list = [
#        ["response_command", "hi", "Hi!", "Say you hi"],
#        ["response_command", "time", "Current date is {dateVar}, {timeVar}", "Say the current date and time"]
#    ]
#    dbf.start_bot(TOKEN, adding_command_list)

from discord.ext import commands
from discord import app_commands, Intents
import discord
import datetime
import os
import logging

def log_settings():
    log_dir = os.path.join("Logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_filename = os.path.join(log_dir, f"Destor_{current_datetime}.log")

    logger = logging.getLogger("Destor")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

logger = log_settings()

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='.', intents=Intents().all())

    async def on_ready(self):
        logger.info("Logged in as " + self.user.name)
        synced = await self.tree.sync()
        logger.info(f"Slash CMDs Synced {len(synced)} Command{'s' if len(synced) != 1 else ''}")

class ResponseCommand:
    def __init__(self, command_name, response_text, client, description="..."):
        @client.tree.command(name=command_name, description=description)
        async def my_command(interaction: discord.Interaction):
            await interaction.response.send_message(response_text)

class BotVariables:
    @staticmethod
    def time_var():
        return datetime.datetime.now().strftime("%H:%M")

    @staticmethod
    def date_var():
        return datetime.date.today().strftime("%Y-%m-%d")

def start_client(token, adding_command_list):
    client = Client()
    add_command(adding_command_list, client)
    client.run(token)

def replace_bot_vars(command):
    replace_rules = [["{timeVar}", BotVariables.time_var()], ["{dateVar}", BotVariables.date_var()]]
    for old, new in replace_rules:
        command = command.replace(old, new)
    return command

def add_command(command_list, client):
    for command in command_list:
        command_name, response_text, description = command[1], replace_bot_vars(command[2]), command[3]
        ResponseCommand(command_name, response_text, client, description)

def start_bot(TOKEN, adding_command_list):
    start_client(TOKEN, adding_command_list)
#Comment for the Commit Streak! (It's day 4 of doing this. xD)
