import os
import pymongo
from model import *
# Dictionnaire des personnages et leurs statistiques
CharacterList = [CharacterDB.__dict__() for CharacterDB in [
	CharacterDB(name="Guerrier", hp=100, defense=10, attack=15),
	CharacterDB(name="Mage", hp=80, defense=5, attack=20),
	CharacterDB(name="Archer", hp=90, defense=7, attack=18),
	CharacterDB(name="Voleur", hp=85, defense=8, attack=22),
	CharacterDB(name="Paladin", hp=110, defense=12, attack=14),
	CharacterDB(name="Sorcier", hp=70, defense=3, attack=25),
	CharacterDB(name="Chevalier", hp=120, defense=15, attack=17),
	CharacterDB(name="Moine", hp=95, defense=9, attack=19),
	CharacterDB(name="Berserker", hp=105, defense=6, attack=23),
	CharacterDB(name="Chasseur", hp=100, defense=11, attack=16),
	CharacterDB(name="Druide", hp=90, defense=8, attack=18),
	CharacterDB(name="Nécromancien", hp=75, defense=4, attack=24),
	CharacterDB(name="Barde", hp=85, defense=6, attack=15),
	CharacterDB(name="Samouraï", hp=100, defense=10, attack=21),
	CharacterDB(name="Templier", hp=115, defense=14, attack=16)
]]


print("CharacterList initialized.")
print(CharacterList)
ItemList = [
	Item(name="Potion de soin", item_type="consommable",
	     rarity="commune", effect={"hp": 50}, consumable=True),
	Item(name="Épée en fer rouillée", item_type="arme", rarity="commune",
	     effect={"attack": 5}, consumable=False),
	Item(name="Bouclier en bois", item_type="armure",
	     rarity="commune", effect={"defense": 3}, consumable=False),
	Item(name="Anneau magique", item_type="accessoire", rarity="rare",
	     effect={"attack": 10, "defense": 5}, consumable=False),
	Item(name="Bouclier en acier", item_type="armure", rarity="rare",
	     effect={"defense": 10}, consumable=False),
	Item(name="Arc long", item_type="arme", rarity="rare",
	     effect={"attack": 12}, consumable=False),
	Item(name="Dague empoisonnée", item_type="arme", rarity="épique",
	     effect={"attack": 20}, consumable=False),
	Item(name="Bouclier en mithril", item_type="armure", rarity="épique",
	     effect={"defense": 20}, consumable=False),
	Item(name="Excalibur", item_type="arme", rarity="légendaire",
	     effect={"attack": 150, "defense": -50}, consumable=False),
	Item(name="Cape d'invisibilité", item_type="armure", rarity="épique",
	     effect={"defense": 20}, consumable=False),
	Item(name="Bottes de vitesse", item_type="armure", rarity="rare",
	     effect={"defense": 5, "attack": 5}, consumable=False),
	Item(name="Lame Vorpaline", item_type="arme", rarity="légendaire",
	     effect={"attack": 200, "defense": -500}, consumable=False),
	Item(name="Grande potion de soin", item_type="consommable",
	     rarity="rare", effect={"hp": 150}, consumable=True),
	Item(name="Élixir de force", item_type="consommable",
	     rarity="rare", effect={"attack": 10}, consumable=True),
	Item(name="Hache de guerre", item_type="arme", rarity="rare",
	     effect={"attack": 15}, consumable=False),
	Item(name="Casque en fer", item_type="armure", rarity="commune",
	     effect={"defense": 4}, consumable=False),
	Item(name="Amulette du dragon", item_type="accessoire", rarity="épique",
	     effect={"attack": 15, "defense": 15}, consumable=False),
	Item(name="Bâton de l'archimage", item_type="arme", rarity="légendaire",
	     effect={"attack": 120, "hp": 50}, consumable=False)
]
ItemListDict = [Item.__dict__() for Item in ItemList]


RarityList = [Rarity.__dict__() for Rarity in [
	Rarity(name="commune", drop_rate=0.7),
	Rarity(name="rare", drop_rate=0.25),
	Rarity(name="épique", drop_rate=0.04),
	Rarity(name="légendaire", drop_rate=0.01)
]]

ScoresList = [ScoreDB.__dict__() for ScoreDB in [
	ScoreDB(player_name="Player1", score=100),
	ScoreDB(player_name="Player2", score=200),
	ScoreDB(player_name="Player3", score=150)
]]

EnemyList = [
	MonsterDB(name="Goblin", hp=50, defense=5, attack=10,
	          dropable=[ItemList[0], ItemList[1]]),
	MonsterDB(name="Orc", hp=120, defense=8, attack=20,
	          dropable=[ItemList[1], ItemList[2]]),
	MonsterDB(name="Dragon", hp=300, defense=20,
	          attack=35, dropable=[ItemList[2], ItemList[8], ItemList[11]]),
	MonsterDB(name="Zombie", hp=70, defense=6, attack=12,
	          dropable=[ItemList[0], ItemList[2]]),
	MonsterDB(name="Troll", hp=200, defense=15,
	          attack=25, dropable=[ItemList[1], ItemList[4]]),
	MonsterDB(name="Spectre", hp=100, defense=10,
	          attack=18, dropable=[ItemList[3], ItemList[9]]),
	MonsterDB(name="Golem", hp=250, defense=25,
	          attack=30, dropable=[ItemList[4], ItemList[7]]),
	MonsterDB(name="Vampire", hp=150, defense=12,
	          attack=22, dropable=[ItemList[5], ItemList[6]]),
	MonsterDB(name="Loup-Garou", hp=180, defense=18,
	          attack=28, dropable=[ItemList[6], ItemList[10]]),
	MonsterDB(name="Squelette", hp=90, defense=7,
	          attack=15, dropable=[ItemList[0], ItemList[1]]),
	MonsterDB(name="Araignée géante", hp=80, defense=6,
	          attack=14, dropable=[ItemList[0], ItemList[15]]),
	MonsterDB(name="Minotaure", hp=220, defense=16,
	          attack=27, dropable=[ItemList[14], ItemList[12]]),
	MonsterDB(name="Liche", hp=200, defense=14,
	          attack=32, dropable=[ItemList[13], ItemList[17]]),
	MonsterDB(name="Hydre", hp=280, defense=19,
	          attack=33, dropable=[ItemList[16], ItemList[8]]),
	MonsterDB(name="Gargouille", hp=160, defense=22,
	          attack=20, dropable=[ItemList[4], ItemList[15]])
]
EnemyListDict = [MonsterDB.__dict__() for MonsterDB in EnemyList]


VagueList = [VagueDB.__dict__() for VagueDB in [
	VagueDB(start_number=1, end_number=5, monsters=[EnemyList[0], EnemyList[1]]),
	VagueDB(start_number=6, end_number=10, monsters=[EnemyList[3], EnemyList[9]]),
	VagueDB(start_number=11, end_number=15,
	        monsters=[EnemyList[4], EnemyList[5]]),
	VagueDB(start_number=16, end_number=20,
	        monsters=[EnemyList[6], EnemyList[7]]),
	VagueDB(start_number=21, end_number=25, monsters=[EnemyList[8]]),
	VagueDB(start_number=26, end_number=30, monsters=[EnemyList[2]]),
]]


DifficultyList = [difficulty.__dict__() for difficulty in [
	Difficulty(lap=1, health_multiplier=1.0, attack_multiplier=1.0,
	           defense_multiplier=1.0, item_multiplier=1.0),
	Difficulty(lap=2, health_multiplier=1.2, attack_multiplier=1.1,
	           defense_multiplier=1.1, item_multiplier=1.0),
	Difficulty(lap=3, health_multiplier=1.5, attack_multiplier=1.3,
	           defense_multiplier=1.2, item_multiplier=1.0),
	Difficulty(lap=4, health_multiplier=1.8, attack_multiplier=1.5,
	           defense_multiplier=1.35, item_multiplier=1.1),
	Difficulty(lap=5, health_multiplier=2.2, attack_multiplier=1.8,
	           defense_multiplier=1.5, item_multiplier=1.2),
	Difficulty(lap=6, health_multiplier=2.7, attack_multiplier=2.1,
	           defense_multiplier=1.7, item_multiplier=1.3),
	Difficulty(lap=7, health_multiplier=3.3, attack_multiplier=2.5,
	           defense_multiplier=1.9, item_multiplier=1.4),
	Difficulty(lap=8, health_multiplier=4.0, attack_multiplier=3.0,
	           defense_multiplier=2.2, item_multiplier=1.5),
	Difficulty(lap=9, health_multiplier=5.0, attack_multiplier=3.6,
	           defense_multiplier=2.5, item_multiplier=1.6),
	Difficulty(lap=10, health_multiplier=6.0, attack_multiplier=4.2,
	           defense_multiplier=2.8, item_multiplier=1.8)
]]
print("Initializing database...")
client: pymongo.MongoClient = pymongo.MongoClient(os.getenv("MONGO_URL"))
print("Connected to MongoDB.")
print("Selecting database...")
database = client["game_db"]
print("Database selected.")


print("Selecting collections...")
Characters = database["characters"]
Monsters = database["monsters"]
Scores = database["scores"]
difficulty = database["difficulty"]
Vagues = database["vagues"]
Items = database["items"]
rarities = database["rarities"]
Saves = database["saves"]

SavesList = [save.__dict__() for save in [
	SaveDB(
		player_name="Player1",
		score=100,
		equipe=[
			CharacterSaveDB(name="Guerrier", hp=100, equipement=[
			                ItemList[1], ItemList[2]]),
			CharacterSaveDB(name="Mage", hp=80, equipement=[ItemList[3]]),
			CharacterSaveDB(name="Archer", hp=90, equipement=[ItemList[5]])
		],
		monsters=[
			MonsterSaveDB(name="Goblin", hp=50),
			MonsterSaveDB(name="Orc", hp=120)
		],
		inventaire=[ItemList[0], ItemList[0]]
	),
	SaveDB(
		player_name="Player2",
		score=200,
		equipe=[
			CharacterSaveDB(name="Paladin", hp=110, equipement=[ItemList[4]]),
			CharacterSaveDB(name="Sorcier", hp=60, equipement=[ItemList[16]]),
			CharacterSaveDB(name="Voleur", hp=85, equipement=[ItemList[6]])
		],
		monsters=[
			MonsterSaveDB(name="Troll", hp=150),
			MonsterSaveDB(name="Spectre", hp=100)
		],
		inventaire=[ItemList[12], ItemList[13]]
	),
	SaveDB(
		player_name="Player3",
		score=150,
		equipe=[
			CharacterSaveDB(name="Chevalier", hp=120, equipement=[
			                ItemList[7], ItemList[15]]),
			CharacterSaveDB(name="Druide", hp=90, equipement=[ItemList[10]])
		],
		monsters=[
			MonsterSaveDB(name="Zombie", hp=70),
			MonsterSaveDB(name="Squelette", hp=45)
		],
		inventaire=[ItemList[0]]
	)
]]


print("Dropping existing collections...")


Characters.drop()
Monsters.drop()
Scores.drop()
difficulty.drop()
Vagues.drop()
Items.drop()
rarities.drop()
Saves.drop()

print("Inserting documents...")
Characters.insert_many(CharacterList)
Monsters.insert_many(EnemyListDict)
Scores.insert_many(ScoresList)
difficulty.insert_many(DifficultyList)
Vagues.insert_many(VagueList)
Items.insert_many(ItemListDict)
rarities.insert_many(RarityList)
Saves.insert_many(SavesList)

print("Database populated:")
for name in database.list_collection_names():
	print(f"  {name}: {database[name].count_documents({})} documents")
