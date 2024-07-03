from discord.ext import commands
from discord import app_commands, Intents
import discord
import datetime
import os
from log_settings import logsettings
import botvariables
import threading
import re
from bot_token import token

#Load .env
token.load_token()
logger = logsettings.log_settings()

#Client and command types classes
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
            await interaction.response.send_message(replace_bot_vars(response_text))

"""class TextFieldCommand:
    def __init__(self, command_name, response_text, client, description="", text_fields):
        @app_commands.command(name=command_name, description=description)
        async def my_command(interaction: discord.Interaction, hex_code: str):
        
            await interaction.response.send_message(f"The RGB value for `{hex_code}` is `{rgb}`")"""

#Command adding function
def add_command(command_list, client):
    for command in command_list:
        command_name, response_text, description = command[1], command[2], command[3]
        ResponseCommand(command_name, response_text, client, description)

#Functions for Bot-Variables
def add_variables(variables):
    with open("botvariables.py", "a") as txt:
        for lists in variables:
            variable = (f"import {lists[0]}\n" if lists[0] else "") + f"def {lists[1]}(): return {lists[2]}\n" #f"import {lists[0]}\ndef {lists[1]}(): return {lists[2]}\n"
            txt.write(variable)

def delete_variable(function_name):
    with open("botvariables.py", "r") as file:
        lines = file.readlines()
    
    new_lines = []
    inside_function = False

    for line in lines:
        if re.match(rf"def {function_name}\s*\(", line):
            inside_function = True
            continue

        if inside_function and re.match(r"def \w+\s*\(", line):
            inside_function = False

        if inside_function:
            continue

        new_lines.append(line)

    with open("botvariables.py", "w") as file:
        file.writelines(new_lines)

def replace_bot_vars(command):
    def extract_function_names():
        with open("botvariables.py", 'r') as file:
            content = file.read()

        function_names = re.findall(r'def\s+(\w+)\s*\(', content)
        return function_names

    function_names = extract_function_names()
    for name in function_names:
        placeholder = f"{{{name}()}}"
        if placeholder in command:
            try:
                function = getattr(botvariables, name)
                result = function()
                command = command.replace(placeholder, str(result))
            except AttributeError:
                logger.error(f"Function {name} not found in botvariables module.")
            except Exception as e:
                logger.error(f"Error calling function {name}: {e}")

    return command

#Start Functions
def start_client(token, adding_command_list):
    client = Client()
    add_command(adding_command_list, client)
    client.run(token)

def start_bot(adding_command_list):
    TOKEN = token.read_token() #read token
    start_client(TOKEN, adding_command_list)

if __name__ == "__main__":
    start_bot([["response_command", "hi", "Hi!", "Say you hi"], ["response_command", "time", "Current date is {date_var()}, {time_var()}", "Say the current date and time"]])
