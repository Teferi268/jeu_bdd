"""Démo manuelle des vues : python -m ui.demo ou python ui/demo.py.

Les données sont écrites en dur, MongoDB n'est pas nécessaire.
"""
import sys
from pathlib import Path

if not __package__:
	sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from ui.affichage import Affichage
from core.character import Character
from core.consumable import Consumable
from core.enemy import Enemy
from core.equipable import equipable
from db.model import CharacterSaveDB, MonsterSaveDB, SaveDB, ScoreDB
from ui.vues import (
	VueChargerSauvegarde,
	VueChoixCible,
	VueEcranTitre,
	VueGameOver,
	VueInfoTour,
	VueInventaire,
	VueLeaderboard,
	VueQuitter,
	VueSelectionCibleObjet,
	VueSelectionEquipe,
	VueTourJoueur,
)

# ===== Objets =====
potion = Consumable(
	name="Potion de soin", description="Restaure 50 PV",
	droprate=0.7, rarity="commune", item_type="consommable", stats={"hp": 50})
elixir = Consumable(
	name="Élixir de force", description="Augmente l'attaque de 10",
	droprate=0.25, rarity="rare", item_type="consommable", stats={"attack": 10})
epee = equipable(
	name="Épée en fer rouillée", description="Une vieille épée",
	droprate=0.7, rarity="commune", item_type="arme", stats={"attack": 5})
bouclier = equipable(
	name="Bouclier en bois", description="Mieux que rien",
	droprate=0.7, rarity="commune", item_type="armure", stats={"defense": 3})
anneau = equipable(
	name="Anneau magique", description="Il brille dans le noir",
	droprate=0.25, rarity="rare", item_type="accessoire", stats={"attack": 10, "defense": 5})
excalibur = equipable(
	name="Excalibur", description="L'épée des rois",
	droprate=0.01, rarity="légendaire", item_type="arme", stats={"attack": 150, "defense": -50})

inventaire = [potion, elixir, anneau, excalibur]

# ===== Équipe : un perso équipé, un blessé, un KO =====
guerrier = Character(name="Guerrier", hp=100, max_hp=100, attack=15, defense=10,
                     equipement=[epee, bouclier])
mage = Character(name="Mage", hp=35, max_hp=80, attack=20, defense=5, equipement=[])
archer = Character(name="Archer", hp=0, max_hp=90, attack=18, defense=7, equipement=[])
team = [guerrier, mage, archer]

personnages_disponibles = [
	Character(name="Voleur", hp=85, max_hp=85, attack=22, defense=8, equipement=[]),
	Character(name="Paladin", hp=110, max_hp=110, attack=14, defense=12, equipement=[]),
	Character(name="Sorcier", hp=70, max_hp=70, attack=25, defense=3, equipement=[]),
	Character(name="Nécromancien", hp=75, max_hp=75, attack=24, defense=4, equipement=[]),
]

# ===== Ennemis =====
goblin = Enemy(name="Goblin", hp=50, max_hp=50, attack=10, defense=5,
               dropable=[potion, epee])
orc = Enemy(name="Orc", hp=120, max_hp=120, attack=20, defense=8,
            dropable=[epee, bouclier])
golem = Enemy(name="Golem", hp=250, max_hp=250, attack=30, defense=25,
              dropable=[anneau])
ennemis = [goblin, orc, golem]

# ===== Scores et sauvegardes =====
scores = [
	ScoreDB(player_name="Player2", score=200),
	ScoreDB(player_name="Player3", score=150),
	ScoreDB(player_name="Player1", score=100),
]

sauvegardes = [
	SaveDB(
		player_name="Player1",
		score=100,
		equipe=[
			CharacterSaveDB(name="Guerrier", hp=100, equipement=[epee, bouclier]),
			CharacterSaveDB(name="Mage", hp=80, equipement=[anneau]),
		],
		monsters=[MonsterSaveDB(name="Goblin", hp=50),
                    MonsterSaveDB(name="Orc", hp=120)],
		inventaire=[potion, potion],
	),
	SaveDB(
		player_name="Player2",
		score=200,
		equipe=[CharacterSaveDB(name="Paladin", hp=110, equipement=[])],
		monsters=[MonsterSaveDB(name="Golem", hp=150)],
		inventaire=[],
	),
]

evenement = (
	f"{guerrier.name} inflige {guerrier.project_damage(goblin)} dégâts à {goblin.name}\n"
	f"{orc.name} attaque {mage.name}"
)

# (nom affiché, vue, nombre de choix possibles dans la vue)
DEMOS = [
	("VueEcranTitre", VueEcranTitre(), 4),
	("VueSelectionEquipe", VueSelectionEquipe(team, personnages_disponibles),
	 len(personnages_disponibles)),
	("VueTourJoueur", VueTourJoueur(team, guerrier, ennemis), 3),
	("VueChoixCible", VueChoixCible(team, guerrier, ennemis), len(ennemis)),
	("VueInfoTour", VueInfoTour(team, evenement, ennemis), 1),
	("VueInventaire", VueInventaire(inventaire, team), len(inventaire)),
	("VueInventaire (vide)", VueInventaire([], team), 1),
	("VueSelectionCibleObjet", VueSelectionCibleObjet(potion, team), len(team)),
	("VueGameOver", VueGameOver(), 2),
	("VueLeaderboard", VueLeaderboard(scores), 1),
	("VueLeaderboard (vide)", VueLeaderboard([]), 1),
	("VueChargerSauvegarde", VueChargerSauvegarde(sauvegardes), len(sauvegardes)),
	("VueChargerSauvegarde (vide)", VueChargerSauvegarde([]), 1),
	("VueQuitter", VueQuitter(), 1),
]


def main():
	noms = [nom for nom, _, _ in DEMOS] + ["Quitter la démo"]

	def menu(index: int):
		return Affichage.create_select_box(
			titre="Démo des vues",
			items=noms,
			index=index,
			box_color="cyan",
			text_color="white",
			hover_color="yellow"
		)

	Affichage.console.print(
		"[dim]↑/↓ naviguer • ⏎ ouvrir une vue, puis ⏎ pour revenir au menu • Ctrl+C quitter[/dim]")
	try:
		Affichage.demander_input("Appuyez sur Entrée pour commencer la démo...")
		while True:
			choix = Affichage.display_vue(menu, len(noms))
			if choix is None or choix == len(DEMOS):
				print("Esc ou Ctrl+C détecté, sortie de la démo.")
				break
			nom, vue, max_index = DEMOS[choix]
			resultat = Affichage.display_vue(vue, max_index)
			Affichage.console.print(f"{nom} → index retourné : {resultat}")
	except KeyboardInterrupt:
		print("Ctrl+C détecté, sortie de la démo.")
		pass


if __name__ == "__main__":
	main()
