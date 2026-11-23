import os
import pymongo
from models import *
from dataclasses import asdict

# Dictionnaire des personnages et leurs statistiques
CharacterList = [
    CharacterDB(name="Guerrier", hp=100, defense=10, attack=15, inventaire=[]),
    CharacterDB(name="Mage", hp=80, defense=5, attack=20, inventaire=[]),
    CharacterDB(name="Archer", hp=90, defense=7, attack=18, inventaire=[]),
    CharacterDB(name="Voleur", hp=85, defense=8, attack=22, inventaire=[]),
    CharacterDB(name="Paladin", hp=110, defense=12, attack=14, inventaire=[]),
    CharacterDB(name="Sorcier", hp=70, defense=3, attack=25, inventaire=[]),
    CharacterDB(name="Chevalier", hp=120, defense=15, attack=17, inventaire=[]),
    CharacterDB(name="Moine", hp=95, defense=9, attack=19, inventaire=[]),
    CharacterDB(name="Berserker", hp=105, defense=6, attack=23, inventaire=[]),
    CharacterDB(name="Chasseur", hp=100, defense=11, attack=16, inventaire=[])
]

CharacterListDict = [asdict(character) for character in CharacterList]

EnemyList = [
    MonsterDB(name="Goblin", hp=50, defense=5, attack=10, dropable=[]),
    MonsterDB(name="Orc", hp=120, defense=8, attack=20, dropable=[]),
    MonsterDB(name="Dragon", hp=300, defense=20, attack=35, dropable=[]),
    MonsterDB(name="Zombie", hp=70, defense=6, attack=12, dropable=[]),
    MonsterDB(name="Troll", hp=200, defense=8, attack=25, dropable=[]),
    MonsterDB(name="Spectre", hp=100, defense=10, attack=18, dropable=[]),
    MonsterDB(name="Golem", hp=250, defense=25, attack=30, dropable=[]),
    MonsterDB(name="Vampire", hp=150, defense=12, attack=22, dropable=[]),
    MonsterDB(name="Loup-Garou", hp=180, defense=18, attack=28, dropable=[]),
    MonsterDB(name="Squelette", hp=90, defense=7, attack=15, dropable=[])
]

EnemyListDict = [asdict(enemy) for enemy in EnemyList]

RarityList = [
    Rarity(name="Commun", drop_rate=0.5),
    Rarity(name="Peu Commun", drop_rate=0.3),
    Rarity(name="Rare", drop_rate=0.15),
    Rarity(name="Épique", drop_rate=0.04),
    Rarity(name="Légendaire", drop_rate=0.01),
]

RarityListDict = [asdict(rarity) for rarity in RarityList]

ItemList = [
    Item(name="Potion de soin", item_type="consommable", rarity="Commun", effect={"hp": 50}, consumable=True),
    Item(name="Épée en fer", item_type="arme", rarity="Peu Commun", effect={"attack": 10}, consumable=False),
    Item(name="Bouclier en bois", item_type="bouclier", rarity="Commun", effect={"defense": 5}, consumable=False),
    Item(name="Armure en cuir", item_type="armure", rarity="Peu Commun", effect={"defense": 8}, consumable=False),
    Item(name="Baguette magique", item_type="arme", rarity="Rare", effect={"attack": 15}, consumable=False),
    Item(name="Anneau de force", item_type="accessoire", rarity="Épique", effect={"attack": 20}, consumable=False),
    Item(name="Amulette de protection", item_type="accessoire", rarity="Épique", effect={"defense": 15}, consumable=False),
    Item(name="Épée légendaire", item_type="arme", rarity="Légendaire", effect={"attack": 30}, consumable=False),
    Item(name="Lance patate", item_type="arme", rarity="Légendaire", effect={"attack": 50}, consumable=False),
]

ItemListDict = [asdict(item) for item in ItemList]

scoreList = [
    ScoreDB(player_name="Alice", score=1500),
    ScoreDB(player_name="Bob", score=1200),
    ScoreDB(player_name="Charlie", score=1800),
    ScoreDB(player_name="David", score=900),
    ScoreDB(player_name="Eve", score=2000),
]

ScoreListDict = [asdict(score) for score in scoreList]

VagueList = [
    Vague(start_number=1, end_number=5, monsters=[EnemyList[0], EnemyList[1]]),
    Vague(start_number=6, end_number=10, monsters=[EnemyList[2], EnemyList[3]]),
    Vague(start_number=11, end_number=15, monsters=[EnemyList[4], EnemyList[5]]),
    Vague(start_number=16, end_number=20, monsters=[EnemyList[6], EnemyList[7]]),
    Vague(start_number=21, end_number=25, monsters=[EnemyList[8], EnemyList[9]]),
]

VagueListDict = [asdict(vague) for vague in VagueList]

DifficultyList = [
    Difficulty(lap=1, health_multiplier=1.0, attack_multiplier=1.0, defense_multiplier=1.0, item_mutiplier=1.0),
    Difficulty(lap=2, health_multiplier=1.2, attack_multiplier=1.2, defense_multiplier=1.2, item_mutiplier=1.1),
    Difficulty(lap=3, health_multiplier=1.5, attack_multiplier=1.5, defense_multiplier=1.5, item_mutiplier=1.2),
    Difficulty(lap=4, health_multiplier=2.0, attack_multiplier=2.0, defense_multiplier=2.0, item_mutiplier=1.3),
    Difficulty(lap=5, health_multiplier=3.0, attack_multiplier=3.0, defense_multiplier=3.0, item_mutiplier=1.5),
]

DifficultyListDict = [asdict(difficulty) for difficulty in DifficultyList]


client = pymongo.MongoClient("mongodb://localhost:27017")
database = client["game_db"]

Characters = database["characters"]
Monsters = database["monsters"]
Scores = database["scores"]
difficulties = database["difficulties"]
Items = database["items"]
rarities = database["rarities"]
vagues = database["vagues"]

Characters.drop()
Monsters.drop()
Scores.drop()
difficulties.drop()
Items.drop()
rarities.drop()
vagues.drop()

Characters.insert_many(CharacterListDict)
Monsters.insert_many(EnemyListDict)
Scores.insert_many(ScoreListDict)
difficulties.insert_many(DifficultyListDict)
Items.insert_many(ItemListDict)
rarities.insert_many(RarityListDict)
vagues.insert_many(VagueListDict)