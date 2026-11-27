from typing import *
from core.enemy import Enemy
from db.db_init import *
from random import choice
from core.player import Player
from ui.affichage import Affichage
from ui.vues import (
    OPTIONS_TOUR,
    VueChoixCible,
    VueInfoTour,
    VueInventaire,
    VueSelectionCibleObjet,
    VueTourJoueur,
)
from core.consumable import Consumable
from core.equipable import equipable


class vague:
    def __init__(self, vague_actuelle: int, monsters: List['Enemy']):
        self.vague_actuelle = vague_actuelle
        self.monsters = monsters


    def creates_dropable(self, monster_data):
        items_par_nom = {item.name: item for item in ItemList}
        taux_par_rarete = {
            rarity["name"]: rarity["drop_rate"]
            for rarity in RarityList
        }

        dropables = []

        for nom in monster_data["dropable"]:
            item_data = items_par_nom[nom]
            item_class = Consumable if item_data.consumable else equipable

            dropables.append(item_class(
                name=item_data.name,
                description="",
                droprate=taux_par_rarete[item_data.rarity],
                rarity=item_data.rarity,
                item_type=item_data.item_type,
                stats=item_data.effect,
            ))

        return dropables

                        
    def pick_enemies(self, vague_actuelle: int):
        #on choisit un montre parmi la liste de monstres dispo pour la vague actuelle selon la database
        self.vague_actuelle = vague_actuelle
        self.monsters = []

        difficulty = self.get_difficulty()
        numero = (vague_actuelle - 1) % 30 + 1

        for vague_data in VagueList:
            if vague_data["start_number"] <= numero <= vague_data["end_number"]:
                monster_data = choice(vague_data["monsters"])
                break
        
        monster = Enemy(
            name=monster_data["name"],
            hp=int(monster_data["hp"] * difficulty["health_multiplier"]),
            max_hp=int(monster_data["hp"] * difficulty["health_multiplier"]),
            defense=int(monster_data["defense"] * difficulty["defense_multiplier"]),
            attack=int(monster_data["attack"] * difficulty["attack_multiplier"]),
            dropable=self.creates_dropable(monster_data)
        )

        self.monsters.append(monster)

        return self.monsters

    def tour_attaque(self, player: Player, character):
        alive_monsters = [monster for monster in self.monsters if monster.is_alive()]
        if not alive_monsters:
            return

        index_cible = Affichage.display_vue(
            VueChoixCible(player.team, character, alive_monsters),
            len(alive_monsters),
        )
        if index_cible is None:  # Échap
            return

        target = alive_monsters[index_cible]
        damage = character.play_turn(target)
        if not target.is_alive():
            loot = target.drop_loot()
            for item in loot:
                player.add_item(item)
        event = f"{character.name} attaque {target.name} et inflige {damage} dégâts."
        VueInfoTour(player.team, event, self.monsters)
    def tour_utiliser_objet(self, player: Player, character):

        index_objet = Affichage.display_vue(
            VueInventaire(player.inventory, player.team),
            len(player.inventory),
        )
        if index_objet is None:  # Échap
            return

        item = player.inventory[index_objet]
        target_index = Affichage.display_vue(
            VueSelectionCibleObjet(item, player.team),
            len(player.team),
        )
        if target_index is None:  # Échap
            return

        target = player.team[target_index]
        success = player.use_item(item, target)
        if success:
            event = f"{character.name} utilise {item.name} sur {target.name}."
        else:
            event = f"{character.name} n'a pas pu utiliser {item.name} sur {target.name}."

        VueInfoTour(player.team, event, self.monsters)
    def tour_joueur(self, player: Player):
        for character in player.get_alive_characters():
            alive_monsters = [monster for monster in self.monsters if monster.is_alive()]
            if not alive_monsters:
                break
            action = Affichage.display_vue(
            VueTourJoueur(player.team, character, alive_monsters),
            len(OPTIONS_TOUR),
            )
            if action is None:  # Échap
                return

            if action == 0:  # Attaquer
                self.tour_attaque(player, character)

            elif action == 1:  # Utiliser un objet  
                self.tour_utiliser_objet(player, character)

            elif action == 2:  # Passer le tour
                event = f"{character.name} passe son tour."
                VueInfoTour(player.team, event, self.monsters)

    def tour_monstres(self, player: Player):
        for monster in self.monsters:
            if monster.is_alive():
                if not player.is_team_alive():
                    break
                target = choice(player.get_alive_characters())
                damage = monster.play_turn(target)
                event = f"{monster.name} attaque {target.name} et inflige {damage} dégâts."
                VueInfoTour(player.team, event, self.monsters)
    def play_vague(self, player : Player):

        while player.is_team_alive():
            alive_monsters = [monster for monster in self.monsters if monster.is_alive()]
            if not alive_monsters:
                return True
            self.tour_joueur(player)
            self.tour_monstres(player)
        return False



    def get_difficulty(self) -> dict:
        lap = (self.vague_actuelle - 1) // 10 + 1

        for difficulty in DifficultyList:
            if difficulty["lap"] == lap:
                return difficulty

        return DifficultyList[-1]
            