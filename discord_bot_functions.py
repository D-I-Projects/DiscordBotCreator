"""
    Normal Use:
    import discord_bot_fujnctions as dbf
    dbf.start_bot("Bot TOKEN", [["command_type", "command name", "Response-Message (With variables)", "command-description"], ["Way more commands"]])
"""

from discord.ext import commands
from discord import app_commands, Intents
import discord
from datetime import datetime, date
import logging
import os

logging.basicConfig(filename='Discord-Bot.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='.', intents=Intents().all())

    async def on_ready(self):
        logging.info("Logged in as " + self.user.name)
        synced = await self.tree.sync()
        if len(synced) == 1:
            logging.info("Slash CMDs Synced " + str(len(synced)) + " Command")
        else:
            logging.info("Slash CMDs Synced " + str(len(synced)) + " Commands")

class ResponseCommand:
    def __init__(self, command_name, response_text, client, description="..."):
        @client.tree.command(name=command_name, description=description)
        async def my_command(interaction: discord.Interaction):
            await interaction.response.send_message(response_text)

class BotVariables:
    def __init__(self):
        pass

    def timeVar(self):
        return datetime.now().strftime("%H:%M")

    def dateVar(self):
        return date.today()

def make_logs():   
    if not os. path. exists():
        os.mkdir("./logs")
        logging.info("Created log folder")

def start_client(token, adding_command_list):
    client = Client()
    add_command(adding_command_list, client)
    client.run(token)

def replace_BotVars(command):
    replace_rules = [["{timeVar}", str(BotVars.timeVar())], ["{dateVar}", str(BotVars.dateVar())]]
    for rules in replace_rules:
        command = command.replace(rules[0], rules[1])
    return command
    

def add_command(command_list, client):
    for command in command_list:
        command_name, response_text, description = command[1], replace_BotVars(command[2]), command[3]
        ResponseCommand(command_name, response_text, client, description)

def start_bot(TOKEN, adding_command_list):
    logging.error('Started basic logging system')
    make_logs()
    start_client(TOKEN, adding_command_list)

BotVars = BotVariables()

if __name__ == "__main__":  
    TOKEN = ""
    adding_command_list = [["response_command", "hi", "Hi!", "Say you hi"], ["response_command", "time", "Current date is {dateVar}, {timeVar}", "Say you hello"]]
    start_client(TOKEN, adding_command_list)
