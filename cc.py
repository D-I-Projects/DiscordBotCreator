import os
import webbrowser
import requests
from tkinter import messagebox
from log_settings import logsettings
from packaging import version

logger = logsettings.log_settings()
current_version = "none"

repo_url = "https://api.github.com/repos/D-I-Projects/DiscordBotManager/tags"

class cc:
    def exit():
        os._exit(0)
    
    def open_wiki():
        webbrowser.open_new_tab("https://github.com/D-I-Projects/DiscordBotManager/wiki")
    
    def open_discord():
        webbrowser.open_new_tab("https://discord.gg/GpGKz7V6GW")
        
    def open_contact():
        webbrowser.open_new_tab("https://github.com/D-I-Projects/.github/blob/main/CONTACT.md")
    
    def check_version():
        response = requests.get(repo_url)
        if response.status_code == 200:
            tags = response.json()
            if tags:
                latest_tag = tags[0]['name']
                if version.parse(latest_tag) > version.parse(current_version):
                    logger.info(f"New version available : {latest_tag} / https://github.com/D-I-Projects/DiscordBotManager/releases/tag/{current_version}.")
                    messagebox.showinfo("DiscordBotManager", f"New version available: {latest_tag}. Current version : {current_version}.")
                else:
                    logger.info("DiscordBotCreator is up to date.")
                    messagebox.showinfo("DiscordBotManager", f"Destor is up to date. Current version : {current_version}.")
            else:
                logger.info("No tags found.")
                messagebox.showinfo("DiscordBotManager", "No tags found.")
        else:
            logger.error(f"Error : {response.status_code}")
            messagebox.showinfo("DiscordBotManager", f"Error : {response.status_code}.")
        
    def auto_check():
        try:
            response = requests.get(repo_url)
            if response.status_code == 200:
                tags = response.json()
                if tags:
                    latest_tag = tags[0]['name']
                    if version.parse(latest_tag) > version.parse(current_version):    
                        logger.info(f"New version available : {latest_tag} / https://github.com/D-I-Projects/DiscordBotManager/releases/tag/{current_version}")
                    else:
                        logger.info("No updates found!")
        except:
            pass
