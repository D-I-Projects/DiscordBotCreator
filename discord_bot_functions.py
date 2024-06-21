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


class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='.', intents=Intents().all())

    async def on_ready(self):
        print("Logged in as " + self.user.name)
        synced = await self.tree.sync()
        if len(synced) == 1:
            print("Slash CMDs Synced " + str(len(synced)) + " Command")
        else:
            print("Slash CMDs Synced " + str(len(synced)) + " Commands")


class ResponseCommand:
    def __init__(self, command_name, response_text, client, description="..."):
        @client.tree.command(name=command_name, description=description)
        async def command(interaction: discord.Interaction):
            await interaction.response.send_message(response_text)

class ArgumentCommand:
    def __init__(self, command_name, response_text, client, description="..."):
        @app_commands.command(name=command_name, description=description)
        async def command(interaction: discord.Interaction, file_name: str, content: str):
            await interaction.response.send_message(response_text)


        client.tree.add_command(command)



class BotVariables:
    def __init__(self):
        pass

    def timeVar(self):
        return datetime.now().strftime("%H:%M")

    def dateVar(self):
        return date.today()


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
        if command_list[0] == "response_command":
            command_name, response_text, description = command[1], replace_BotVars(command[2]), command[3]
            ResponseCommand(command_name, response_text, client, description)
        elif command_list[0] == "argument_command":
            command_name, response_text, description, = command[1], replace_BotVars(command[2]), command[3]
            ArgumentCommand(command_name, response_text, client, description)
            


def start_bot(TOKEN, adding_command_list):
    start_client(TOKEN, adding_command_list)


BotVars = BotVariables()

if __name__ == "__main__":
    TOKEN = ""
    adding_command_list = [["argument_command", "hi", "Hi!", "Say you hi"]]
    start_client(TOKEN, adding_command_list)
