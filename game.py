"""
Décomposition :

-Lancement du jeu 
    -Message de bienvenue + règles 
    -Demander les inputs
        -Pseudo
        -Verifier si le pseudo valide
            -Chaine caractère
            -Entre 1 et 12 caractères
    -Choix des heroes
        -Présentation des differents heroes
            -Présentation sous la forme (    1 -> Nom_du_heroe - DGT:40 - PV:100 - DEF:10   )
        -Choix des heroes via l'input de chiffre
            -Verifier que les inputs corresponde bien à des heroes
            -Attribuer les heroes dans l'equipe du joueur
                -Ajout dans la bdd
            -Montrer l'équipe au joueur
            -Demander si il veut en changer
    -Lancement des manches
        BOUCLE
        -Choix du monstre aleatoire parmis la collection
        -Message pour montrer quel monstre on affronte
        -Affrontement de l'equipe et du montre
            -Choix random pour savoir qui commance
            -Attaque des heroes sur le monstre (dgt cumulé de tout les heroes)
            -Monstre subit les degats
                -Calcul avec la defense du monstre
                -Verification pour savoir si il est mort
                    -Si oui
                        -Incrémentation du nombre de vague
                        -prochaine manche
                    -Si non
                        -on continue
            -Monstre attaque les heroes (total des degat du montre divisé par le nombre de heroes en vie)
                -Calcul avec la defense du heroe
                -Verification pour savoir si des heroes sont morts
                    -Si oui
                        -Message de mort pour le heroes en question
                        -Supression du heroes de l'équipe
                    -Si non 
                        -on continue
        BOUCLE
    -Message de fin avec le nombre de vague vaincu + contre quel montre on est mort
-Fin du jeu"""

import os
from pymongo import MongoClient
from db_init import *
from utils import *


def ask_pseudo():
    #Permet de demander le pseudo et de le verifier 
    username = input("Veuillez chosir votre pseudo pour cette partie...")
    if username.isalpha() == False or len(username) > 12:
        print("Pseudo incorrecte : lettre uniquement, 12 caractères max.")
        return ask_pseudo()
    return username

def show_heroe_list(heroes):
    #affiche la liste depuis un dictionaire
    for heroe in heroes:
        print(f"{heroe}\n")

def choose_heroe(heroes):
    #Gère le choix des personage 
    choix = 0
    team = []
    while len(team) < 3:
        #Pour s'arreter à 3 heroe dans l'équipe 
        choix = choose_number("Veuillez taper à la suite les nombre a vos 3 heroes...",1,len(heroes))
        team.append(heroes[choix])
        

    return team
def show_team(team):
    print("Votre équipe est composée de :")
    for hero in team:
        print(f"- {hero}")
def main_menu():
    heroes = charger_heroes_db(collection_heroes)
    monsters = charger_monstres_db(collection_monster)
    set_up_db()
    lobby_message()
    pseudo = ask_pseudo()
    choice_heroe_message(pseudo)
    show_heroe_list(heroes)
    team = choose_heroe(heroes)
    show_team(team)