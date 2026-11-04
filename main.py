from game import *
from rich.console import Console
from rich.panel import Panel
from InquirerPy import inquirer


while True:
    choix = main_menu()
    start_choice(choix, heroes)


