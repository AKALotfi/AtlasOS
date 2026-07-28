import os

def clear_command():
    os.system("cls" if os.name == "nt" else "clear")