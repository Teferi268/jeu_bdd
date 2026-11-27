from dataclasses import dataclass
from typing import *
from core.item import Item



class vue:
    def vue_inventaire(self, inventaire: List[Item], team: List[Character]):
        pass

    def vue_tour_joueur(self, team: List[Character], personnage: Character, ennemies: List[Enemy]):
        pass

    def vue_choix_cible(self, team: List[Character], personnage: Character, ennemies: List[Enemy]):
        pass

    def vue_info_tour(self, team: List[Character], event: str, ennemies: List[Enemy]):
        pass

    def vue_selection_equipe(self, team: List[Character], listSelection: List[Character]):
        pass

    def vue_ecran_titre(self):
        pass

    def vue_leaderboard(self, scores):
        pass

    def vue_game_over(self):
        pass

    def vue_charger_sauvegarde(self):
        pass

    def vue_quitter(self):
        pass
