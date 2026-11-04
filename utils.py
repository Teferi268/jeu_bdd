import os
def clear_console():
	os.system('cls' if os.name == 'nt' else 'clear')
def lobby_message():
    largeur = 36

    print("\n+" + "-" * largeur + "+")
    print("|" + "BIENVENUE SUR LE JEU".center(largeur) + "|")
    print("+" + "-" * largeur + "+")


def choice_heroe_message(pseudo):
    largeur = 36

    print("\n+" + "-" * largeur + "+")
    print("|" + f"BIENVENUE {pseudo}".center(largeur) + "|")
    print("+" + "-" * largeur + "+")
    print("|" + "Vous allez devoir choisir".center(largeur) + "|")
    print("|" + "3 heros parmi cette liste".center(largeur) + "|")
    print("+" + "-" * largeur + "+")


def choice_menu():
    largeur = 36
    choix = [
        "[1] Nouvelle partie",
        "[2] Voir les scores",
        "[3] Quitter"
    ]

    print("\n+" + "-" * largeur + "+")

    for option in choix:
        print("|" + option.center(largeur) + "|")

    print("+" + "-" * largeur + "+")

    return input("...")
def affichage_spawn_monster(monster):
	print(f"Vous allez affronter un {monster["nom"]}")

def affichage_end_message(round):
	print(f"Vous avez atteint le round {round}")
def affichage_stat_team(team):
	for heroe in team:
		if heroe['PV'] < 1:
			print(f"Le {heroe['nom']} est mort")
		else:
			print(f"Le {heroe['nom']} n'a plus que {round(heroe['PV'])} point de vie.")

def choose_number(message,min, max):
	#Verifie si le nombre est bien un nombre et se situe entre le mln et le max
	choix = input(message)
	if choix.isdigit() == False or int(choix) < min or int(choix) > max:
		choose_number(message,min, max)
	return int(choix)



def message_error_username():
	print("Pseudo incorrecte : lettre uniquement, 12 caractères max.")

def is_username_valide(username):
	#Permet de verifier si le pseudo est bien une chaine de caractère et est plus petit que 12 caractères
	if username.isalpha() == False or len(username) > 12:
		message_error_username()
		return False
	return True








def charger_heroes_db(collection_heroes):
	#Permet de mettre tout les heroes de la BDD dans un tableau heroes
	heroes = []
	for doc in collection_heroes.find({}, {"_id": 0}):
		if "nom" in doc:
			heroes.append({doc["nom"]: {"ATK": doc["ATK"], "DEF": doc["DEF"], "PV": doc["PV"]}})
		else:
			for key, value in doc.items():
				if isinstance(value, dict) and "ATK" in value and "DEF" in value and "PV" in value:
					#Verifie que c'est bien un dictionaire avant d'ajouter l'heros
					heroes.append({key: value})
					break
	return heroes


def charger_monstres_db(collection_monsters):
	#Permet de mettre tout les monstres de la BDD dans un tableau monstres
	monstres = []
	for doc in collection_monsters.find({}, {"_id": 0}):
		if "nom" in doc:
			monstres.append(
				{doc["nom"]: {"ATK": doc["ATK"], "DEF": doc["DEF"], "PV": doc["PV"]}}
			)
		else:
			for key, value in doc.items():
				if isinstance(value, dict) and "ATK" in value and "DEF" in value and "PV" in value:
					#Verifie que c'est bien un dictionaire avant d'ajouter le monstre
					monstres.append({key: value})
					break
	return monstres