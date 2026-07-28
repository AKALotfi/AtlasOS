# Description des commandes
descriptions = {
    "help": "Displays all available commands",
    "clear": "Clears the terminal",
    "about": "Shows information about AtlasOS",
    "calc": "Opens the calculator",
    "notes": "Manage notes",
    "exit": "Exit AtlasOS"
}

def help_command():
    print("=" * 35)
    print("     == Available Commands ==")
    print("=" * 35)

    for command, description in descriptions.items():
        print(f"{command:<10} - {description}")

    print("=" * 35)