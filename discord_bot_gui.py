import tkinter as tk
import sys
import threading as thread
import customtkinter as ctk
import discord_bot_functions as dbf

root = ctk.CTk()
root.geometry("1280x720")

main_fm = ctk.CTkFrame(master=root)
main_fm.pack(pady=10, padx=10, fill="both", expand=True)

class ConsoleRedirector:
    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert(tk.END, text)
        self.widget.see(tk.END)

    def flush(self):
        pass

def run_script():
    TOKEN = "YOUR_DISCORD_BOT_TOKEN"
    adding_command_list = [
        ["response_command", "hi", "Hi!", "Sag Hi!"],
        ["response_command", "time", "Aktuelles Datum ist {dateVar}, {timeVar}", "Sag das aktuelle Datum und die Uhrzeit"]
    ]
    dbf.start_bot(TOKEN, adding_command_list)

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

def main_page():
    main_page_fm = ctk.CTkFrame(main_fm)
    main_page_fm.pack(pady=10, padx=10, fill="both", expand=True)

    label = ctk.CTkLabel(main_page_fm, text="DiscordBotCreator", font=("Open Sans", 26))
    label.pack(pady=10, padx=10, side=tk.TOP)

    run_and_stop_button.configure(state=tk.NORMAL)
    
    console_text = ctk.CTkTextbox(main_page_fm, wrap=tk.WORD, width=500, height=500)
    console_text.pack(anchor="center", pady=10, padx=10, side=tk.BOTTOM)
    console_text.configure(scrollbar_button_color="", scrollbar_button_hover_color="")

    def update_output():
        sys.stdout = ConsoleRedirector(console_text)
        sys.stderr = ConsoleRedirector(console_text)

    update_output()

def configure_page():
    configure_page_fm = ctk.CTkFrame(main_fm)
    configure_page_fm.pack(pady=10, padx=10, fill="both", expand=True)
    
    def back():
        switch(main_page)
        
    run_and_stop_button.configure(state=tk.DISABLED)
    
    global back_button
    back_button = ctk.CTkButton(barframe, text="Back", fg_color="red3", hover_color="red4", command=back)
    back_button.pack(padx=10, pady=10, side=tk.RIGHT)
    
barframe = ctk.CTkFrame(root, width=1280, height=20)
barframe.pack(padx=10, pady=10, side=tk.BOTTOM)

run_and_stop_button = ctk.CTkButton(barframe, text="Run Bot", command=thread_run_script)
run_and_stop_button.pack(pady=10, padx=10, side=tk.LEFT)

configure_button = ctk.CTkButton(barframe, text="Configure", command=lambda: switch(configure_page))
configure_button.pack(pady=10, padx=10, side=tk.LEFT)

switch(main_page)
root.mainloop()
