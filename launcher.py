from discord.ext import commands
from discord import app_commands, Intents
import discord
import datetime
import os
from log_settings import logsettings
import botvariables
import threading
import re

logger = logsettings.log_settings()

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

def start_client(token, adding_command_list):
    client = Client()
    add_command(adding_command_list, client)
    client.run(token)

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
                # Dynamically get the function from botvariables module and call it
                function = getattr(botvariables, name)
                result = function()
                command = command.replace(placeholder, str(result))
            except AttributeError:
                logger.error(f"Function {name} not found in botvariables module.")
            except Exception as e:
                logger.error(f"Error calling function {name}: {e}")

    return command

def add_command(command_list, client):
    for command in command_list:
        command_name, response_text, description = command[1], command[2], command[3]
        ResponseCommand(command_name, response_text, client, description)

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

def read_token():
    with open("TOKEN.txt") as txt_token:
        # Please write your TOKEN in "TOKEN.txt"
        TOKEN = txt_token.read().strip()
    return TOKEN

def start_bot(adding_command_list):
    TOKEN = read_token()
    start_client(TOKEN, adding_command_list)

#LÖSCH DAS HIER NICHT MICH BISST DU DUMM ODER SO? LASS ES STEHEN (AN DEVIN)
#Examples in Example_Use.txt
if __name__ == "__main__":
    add_variables([["sys", "test", "'hallo'"]])
    delete_variable("test")
    start_bot([["response_command", "hi", "Hi!", "Say you hi"], ["response_command", "time", "Current date is {date_var()}, {time_var()}", "Say the current date and time"]])

