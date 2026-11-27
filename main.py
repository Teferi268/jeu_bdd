from core.character import Character
from core.game import Game
from core.player import Player
from db.db_init import CharacterList
from ui.affichage import Affichage
from ui.vues import (
    OPTIONS_ECRAN_TITRE,
    OPTIONS_GAME_OVER,
    VueEcranTitre,
    VueGameOver,
    VueSelectionEquipe,
)


def main():
    while True:
        choix = Affichage.display_vue(VueEcranTitre(), len(OPTIONS_ECRAN_TITRE))
        if choix == 0:  # Nouvelle partie
            player_name = Affichage.demander_input("Entrez le nom du joueur : ")
            player = Player(player_name, 0)
            personnages = [
                Character(
                    name=p["name"],
                    hp=p["hp"],
                    max_hp=p["hp"],
                    defense=p["defense"],
                    attack=p["attack"],
                    equipement=[],
                )
                for p in CharacterList
            ]

            player.choisir_equipe(personnages)
            game = Game(player)
            game.launch_game()
            Affichage.display_vue(VueGameOver(), len(OPTIONS_GAME_OVER))
        elif choix == 1:  # Charger une partie
            game = Game(None)
            game.load_game()
        elif choix == 2:  # Leaderboard
            game = Game(None)
            game.show_leaderboard()
        elif choix == 3:  # Quitter
            Affichage.display_vue(VueGameOver(), len(OPTIONS_GAME_OVER))
            break


if __name__ == "__main__":
    main()
