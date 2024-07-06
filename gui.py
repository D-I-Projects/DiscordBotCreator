import tkinter as tk
import threading as thread
from tkinter import messagebox
import customtkinter as ctk
from cc import cc
import launcher as dbf
from CTkMenuBar import *
import sys
from bot_token import token
from log_settings import logsettings
import tkinter as tk

logger = logsettings.log_settings()

root = ctk.CTk()
root.geometry("1280x720")
root.title("DiscordBotCreator")
root.resizable(width=False, height=False)

menu = CTkTitleMenu(root)

help_title_btn = menu.add_cascade("Help")
help_dropdown = CustomDropdownMenu(widget=help_title_btn)
help_dropdown.add_option(option="Discord", command=lambda: cc.open_discord())
help_dropdown.add_option(option="Support", command=lambda: cc.open_contact())

program_title_btn = menu.add_cascade("Program")
dropdown1 = CustomDropdownMenu(widget=program_title_btn)
dropdown1.add_option(option="Wiki", command=lambda: cc.open_wiki())
dropdown1.add_option(option="Check for update", command=lambda: cc.check_version())
dropdown1.add_separator()
exit_dropdown_btn = dropdown1.add_option("Exit", command=lambda: cc.exit())

main_fm = ctk.CTkFrame(master=root)
main_fm.pack(pady=10, padx=10, fill="both", expand=True)

def on_closing():
    cc.exit()
        
class ConsoleRedirector:
    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert(tk.END, text)
        self.widget.see(tk.END)

    def flush(self):
        pass

bot_running = False

def run_script():
    global bot_running
    TOKEN = "No"
    adding_command_list = [
        ["response_command", "hello", "Hi!", "Greet the bot!"],
        ["response_command", "time", "Aktuelles Datum ist {dateVar}, {timeVar}", "Sag das aktuelle Datum und die Uhrzeit"]
    ]
    dbf.start_bot(TOKEN, adding_command_list)
    bot_running = True
    update_button_state()

def stop_bot():
    global bot_running
    dbf.stop_bot()
    bot_running = False
    update_button_state()

def update_button_state():
    if bot_running:
        run_and_stop_button.configure(text="Stop Bot", fg_color="red3", hover_color="red4", command=stop_bot)
    else:
        run_and_stop_button.configure(text="Run Bot", fg_color="", hover_color="", command=thread_run_script)

def thread_run_script():
    script_thread = thread.Thread(target=run_script)
    script_thread.start()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

back_button = None

def switch(page_func):
    global back_button
    for fm in main_fm.winfo_children():
        fm.destroy()
    if back_button:
        back_button.destroy()
    page_func()

def console_page():
    logger.info("Opened console_page.")
    console_page_fm = ctk.CTkFrame(main_fm)
    console_page_fm.pack(pady=10, padx=10, fill="both", expand=True)

    label = ctk.CTkLabel(console_page_fm, text="DiscordBotCreator", font=("Open Sans", 33))
    label.pack(pady=12, padx=10, side=tk.TOP)

    run_and_stop_button.configure(state=tk.NORMAL)
    
    console_text = ctk.CTkTextbox(console_page_fm, wrap=tk.WORD, width=500, height=500)
    console_text.pack(anchor="center", pady=10, padx=10, side=tk.BOTTOM)
    console_text.configure(scrollbar_button_color="", scrollbar_button_hover_color="")

    def update_output():
        sys.stdout = ConsoleRedirector(console_text)
        sys.stderr = ConsoleRedirector(console_text)

    update_output()

def create_function_frame(parent, button_text, button_command, description_text, indicator_needed=False, fg_color=None):
    function_frame = ctk.CTkFrame(parent, fg_color=fg_color)
    function_frame.pack(fill=tk.X, padx=10, pady=10)

    button = ctk.CTkButton(function_frame, text=button_text, command=button_command)
    button.grid(row=0, column=0, sticky="w")

    description = ctk.CTkLabel(function_frame, text=description_text, font=("Open Sans", 15))
    description.grid(row=0, column=2, sticky="e")

    return function_frame, button

def settings_page():
    logger.info("Opened settings_page.")
    settings_page_fm = ctk.CTkScrollableFrame(main_fm)
    settings_page_fm.pack(pady=10, padx=10, fill="both", expand=True)
    
    def configure_option1(): #Example
        print("Configure option 1")
    
    general_label = ctk.CTkLabel(settings_page_fm, text="General", font=("Open Sans", 33))
    general_label.pack(padx = 10, pady = 10)
    
    function_frame, button = create_function_frame(
        settings_page_fm,
        "Check for update",
        configure_option1,
        "  Check for new updates."
    )
    
    function_frame, button = create_function_frame(
        settings_page_fm,
        "Open directory",
        configure_option1,
        "  Open directory for saved files."
    )
    
    token_label = ctk.CTkLabel(settings_page_fm, text="Token", font=("Open Sans", 33))
    token_label.pack(pady = 10, padx = 10)
    
    function_frame, button = create_function_frame(
        settings_page_fm,
        "Set token",
        configure_option1,
        "  Set your discord bot token.",
    )
    
    function_frame, button = create_function_frame(
        settings_page_fm,
        "Change token",
        configure_option1,
        "  Change your discord bot token.",
    )
    
    function_frame, button = create_function_frame(
        settings_page_fm,
        "Delete token",
        configure_option1,
        "  Delete your discord bot token.",
    )
    
    theme_label = ctk.CTkLabel(settings_page_fm, text="Theme", font=("Open Sans", 33))
    theme_label.pack(pady = 10, padx = 10)
    
    function_frame, button = create_function_frame(
        settings_page_fm,
        "Dark Mode",
        configure_option1,
        "  Set theme to Dark Mode",
    )
    
    function_frame, button = create_function_frame(
        settings_page_fm,
        "Light Mode",
        configure_option1,
        "  Set theme to Light Mode",
    )
    
    function_frame, button = create_function_frame(
        settings_page_fm,
        "System Mode",
        configure_option1,
        "  Set theme to default system design",
    )
    
    def back():
        switch(console_page)
    
    run_and_stop_button.configure(state=tk.DISABLED)
    
    global back_button
    back_button = ctk.CTkButton(barframe, text="Back", fg_color="red3", hover_color="red4", command=back)
    back_button.pack(padx=10, pady=10, side=tk.RIGHT)

    
barframe = ctk.CTkFrame(root, width=1280, height=20)
barframe.pack(padx=10, pady=10, side=tk.BOTTOM)

run_and_stop_button = ctk.CTkButton(barframe, text="Run Bot", command=thread_run_script)
run_and_stop_button.pack(pady=10, padx=10, side=tk.LEFT)

configure_button = ctk.CTkButton(barframe, text="Settings", command=lambda: switch(settings_page))
configure_button.pack(pady=10, padx=10, side=tk.LEFT)

switch(console_page)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
