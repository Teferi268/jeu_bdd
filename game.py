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
from random import *


def ask_pseudo():
    #Permet de demander le pseudo et de le verifier 
    username = input("Veuillez chosir votre pseudo pour cette partie...")
    if not is_username_valide(username):
        return ask_pseudo()
    return username

def show_heroe_list(heroes):
    #affiche la liste depuis un dictionaire
    for heroe in heroes:
        print(f"{heroe}\n")

def choose_heroe(heroes):
    #Gère le choix des personage 
    choice = 0
    team = []
    counter = 1 #Permet l'affichage dinamyque dans la demande de l'équipe
    while len(team) < 3:
        #Pour s'arreter à 3 heroe dans l'équipe 
        choice = choose_number(f"Veuillez taper le numero de votre heroe numero {counter} : ",1,len(heroes))
        team.append(heroes[choice])
        counter += 1
    return team
def show_team(team):
    #Permet d'afficher l'équipe de joueur
    print("Votre équipe est composée de :")
    for hero in team:
        print(f"- {hero}")

def final_choice_team():
    choix = int(input("1- Valider l'équipe 2- Changer d'équipe"))
    if choix == 2:
        return False
    elif choix == 1:  
        return True
def main_menu():
    #Variable essentiel 
    set_up_db() 
    #-Message de bienvenue + règles 
    lobby_message()
    #Menu du debut
    return choice_menu()
    
   
def game_start(pseudo, heroes):
    valid_team = False
    choice_heroe_message(pseudo)
    while valid_team == False:
        show_heroe_list(heroes)
        team = choose_heroe(heroes)
        show_team(team)
        valid_team = final_choice_team()
        start_battle(valid_team)


def start_battle(team):
    monster = choose_monster()
    battle(team, monster)

def choose_monster(monster):
    monster = choice(monster)

def battle(team, monster):
    attack_monster(monster,team)
    attack_team(team, monster)

def attack_monster(monster,team):
    atk_monster = get_monster_atk(monster)
    take_damage_team(team,atk_monster)

def attack_team(team,monster):
    atk_team = get_team_atk(team)
    take_damage_monster(monster,atk_team)

def get_team_atk(team):
    team = is_alive_team(team)
    total_dmg = 0
    for heroe in team:
        total_dmg += heroe["ATK"]
    return total_dmg
def get_monster_atk(monster):
    return monster[0]["ATK"]
def take_damage_team(team, damage):
    team = is_alive_team(team)
    for hero in team:
        hero["PV"] - damage // is_alive_team(team) 
def is_alive_team(team):
    team_alive = []
    for heroe in team:
        if heroe["PV"] > 0:
            team_alive.append(heroe)
    return team_alive
def take_damage_monster(monster, damage):
    monster["PV"] - damage
    

def start_choice(choix, heroes):
    if int(choix) == 1:
        #-Demander les inputs -Pseudo
        username = ask_pseudo()
        game_start(username, heroes)
    elif int(choix) == 2:
        show_score()
    elif int(choix) == 3:    
        pass


