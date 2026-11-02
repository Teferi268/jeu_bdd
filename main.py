import os
from pymongo import MongoClient
from db_init import set_up_db
from utils import lobby_message


def ask_pseudo():
    username = input("Veuillez chosir votre pseudo pour cette partie...")
    if username.isalpha() == False or len(username) > 12:
        print("Pseudo incorrecte : lettre uniquement, 12 caractères max.")
        return ask_pseudo()
    return username
def main_menu():
    set_up_db()
    lobby_message()
    pseudo = ask_pseudo()
