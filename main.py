from auth.login import login

from commands.help import help_command
from commands.exit import exit_command
from commands.clear import clear_command
from commands.about import about_command
from commands.date import date_command
from commands.time import time_command
from commands.calc import calc_command
from commands.notes import notes_command

from database.setup import create_tables

def display_banner():
    print("=" * 33)
    print("      == AtlasOS v1.0 ==")
    print("=" * 33)
    print()

commands = {
    "help": help_command,
    "exit": exit_command,
    "clear": clear_command,
    "about": about_command,
    "date": date_command,
    "time": time_command,
    "calc": calc_command,
    "notes": notes_command
}

def shell():
    while True:
        command = input("AtlasOS > ").lower()

        if command in commands:
            commands[command]()
        else:
            print("Unknown command. Type 'help' to see the available commands.\n")

def main():

    create_tables()
    
    display_banner()

    if login():
        shell()

if __name__ == "__main__":
    main()