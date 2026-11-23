import pymongo

# Dictionnaire des personnages et leurs statistiques
CharacterList = [
    {"name" : "Guerrier", "hp" : 100, "defense" : 10, "attack" : 15 },
    {"name": "Mage", "hp" : 80, "defense": 5, "attack" : 20 },
    {"name" : "Archer", "hp" : 90, "defense": 7, "attack" : 18},
    {"name" : "Voleur", "hp" : 85, "defense": 8, "attack" : 22},
    {"name" : "Paladin", "hp" : 110, "defense": 12, "attack" : 14},
    {"name" : "Sorcier", "hp" : 70, "defense": 3, "attack" : 25},
    {"name" : "Chevalier", "hp" : 120,"defense": 15, "attack" : 17},
    {"name" : "Moine", "hp" : 95, "defense": 9, "attack" : 19 },
    {"name" : "Berserker", "hp" : 105, "defense": 6, "attack" : 23},
    {"name" : "Chasseur", "hp" : 100, "defense": 11, "attack" : 16}
]

EnemyList = [
    {"name" : "Goblin", "hp" : 50, "defense" : 5, "attack" : 10},
    {"name" : "Orc", "hp" : 120, "defense": 8, "attack" : 20 },
    {"name" : "Dragon", "hp" : 300, "defense": 20, "attack" : 35 },
    {"name" : "Zombie", "hp" : 70, "defense": 6, "attack" : 12 },
    {"name" : "Troll", "hp" : 200, "defense": 15, "attack" : 25},
    {"name" : "Spectre",  "hp" : 100, "defense": 10, "attack" : 18},
    {"name" : "Golem", "hp" : 250, "defense": 25, "attack" : 30 },
    {"name" : "Vampire", "hp" : 150, "defense": 12, "attack" : 22 },
    {"name" : "Loup-Garou", "hp" : 180, "defense": 18, "attack" : 28 },
    {"name" : "Squelette", "hp" : 90, "defense": 7, "attack" : 15 }
]

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["game_db"]

Characters = database["characters"]
Monsters = database["monsters"]
Scores = database["scores"]

Characters.drop()
Monsters.drop()

Characters.insert_many(CharacterList)
Monsters.insert_many(EnemyList)