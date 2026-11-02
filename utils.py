def lobby_message():
    print("Bienvenue dans le jeu")
    print("Le jeu ce déroule tour par tout et fais affronter votre équipe contre des monstres")

def choice_heroe_message(pseudo):
    print(f"Bienvenue {pseudo}")
    print("Vous allez devoir choisir 3 heros parmis cette liste")


def charger_heroes_db(collection_heroes):
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