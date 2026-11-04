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
import time
from rich.console import Console
from rich.panel import Panel
from InquirerPy import inquirer


def ask_pseudo():
    #Permet de demander le pseudo et de le verifier 
    username = input("Veuillez chosir votre pseudo pour cette partie...")
    if not is_username_valide(username):
        return ask_pseudo()
    return username

def show_heroe_list(heroes):
    #affiche la liste depuis un dictionaire
    liste_choix = []

    for hero in heroes:
        option = { "name": f"{hero['nom']} | ATK: {hero['ATK']} | DEF: {hero['DEF']} | PV: {hero['PV']}","value": hero}

        liste_choix.append(option)

    choix = inquirer.select(
        message="Sélectionnez un héros :",
        choices=liste_choix,
        pointer="▶"
    ).execute()
    return choix


def choose_heroe(heroes):
    #Gère le choix des personage 
    team = []
    team_dispo = heroes.copy()
    while len(team) < 3:
        #Pour s'arreter à 3 heroe dans l'équipe 
        hero = show_heroe_list(team_dispo)
        team.append(hero.copy())
        team_dispo.remove(hero)

    return team

def show_team(team):
    #Permet d'afficher l'équipe de joueur
    print("Votre équipe est composée de :")
    compteur = 1
    for heroe in team:
        print(f"{compteur}-{heroe['nom']} ATK:{heroe['ATK']} DEF:{heroe['DEF']} PV:{heroe['PV']} \n")
        compteur += 1

def final_choice_team():
    #Permet la gestion de la finalisation du choix de l'équipe
    choix = choix = inquirer.select(
                message="",
                choices=["[1] Valider","[2] Changer" ],
                pointer="▶", 
                ).execute()
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
    choix = choice_menu()
    clear_console()

    if choix.startswith("[1]"):
        return 1
    elif choix.startswith("[2]"):
        return 2
    elif choix.startswith("[3]"):
        return 3
    
   
def game_start(pseudo, heroes):
    #Lance le choix du joueur qui est de faire une nouvelle partie
    valid_team = False
    choice_heroe_message(pseudo)
    while valid_team == False:
        team = choose_heroe(heroes)
        show_team(team)
        valid_team = final_choice_team()
    return start_battle(team)


def start_battle(team):
    #Round du combat
    round_count = 0
    while True:
        #Lancement de la boucle de jeu
        clear_console()
        monster = choose_monster(monsters)
        if team_alive(get_alive_team(team)):
            #Le monstre attaque
            attack_monster(monster,team)
            affichage_stat_team(team)
            #L'équipe attaque
            attack_team(team, monster)
            round_count += 1
            time.sleep(1)
        else :
            #Toute l'équipe est morte
            return round_count
    affichage_end_message(round_count)

def choose_monster(monster):
    #Permet de choisir un monstre aleatoire
    monster = choice(monster).copy()
    affichage_spawn_monster(monster)
    return monster
def team_alive(team):
    #verifie si l'équipe est en vie
    if not team:
        return False
    return True
    

def attack_monster(monster,team):
    #Fais en sorte que le monstre attaque les heroes de l'équipe
    atk_monster = get_monster_atk(monster)
    take_damage_team(team,atk_monster)
    return print(f"Le monstre inflige {monster['ATK']} points de degats à chaque enenemie")

def attack_team(team,monster):
    #Fais en sorte que l'équipe attaque le monstre
    atk_team = get_team_atk(team)
    take_damage_monster(monster,atk_team)
    return print(*(f"Le {h['nom']} attaque le monstre en infligeant {h['ATK']}" for h in team), sep="\n")

def get_team_atk(team):
    #Permet de recuperrer le nombre total d'atk de l'équipe en vie
    team = get_alive_team(team)
    total_dmg = 0
    for heroe in team:
        total_dmg += heroe["ATK"]
    return total_dmg

def get_monster_atk(monster):
    #Permet de recuperrer l'atk du monstre
    return monster["ATK"]

def take_damage_team(team, damage):
    #Fais en sorte que l'équipe prenne les degats du monstre
    team = get_alive_team(team)
    for hero in team:
        hero["PV"] -= damage / len(get_alive_team(team)) 

def get_alive_team(team):
    #Permet de mettre tout les heroes de l'équipe dans une nouvelle liste de heroes qui seront ceux en vie
    team_alive = []
    for heroe in team:
        if heroe["PV"] > 0:
            team_alive.append(heroe)
    return team_alive
def take_damage_monster(monster, damage):
    #Fais en sorte que le monstre prenne les degats des heroes 
    monster["PV"] -= damage
    

def start_choice(choix, heroes):
    #Permet la gestion du choix de l'utilisateur au debut
    if int(choix) == 1:
        #-Demander les inputs -Pseudo
        username = ask_pseudo()
        score = game_start(username, heroes)
        save_score(username, score)
    elif int(choix) == 2:
        list_scores = load_score()
        show_score(list_scores)
    elif int(choix) == 3:    
        return exit()





#Partie pour gerer le score

def save_score(username, score):
    print("sauvegarde reussi")
    collection_scores.insert_one({"username" : username , "score" : score})
    return load_score()
def load_score():
    return list(collection_scores.find({}, {"_id": 0}).sort("score", -1))
def show_score(scores):
    rang = 1
    print("\n=== SCORES ===")
    if is_score_empty(scores):
        return print("Aucun score enregistré")
    for score in scores:
        print(f"{rang}. {score['username']} - {score['score']} vagues")
        rang += 1
def is_score_empty(scores):
    if len(scores) == 0:
        return True
    return False