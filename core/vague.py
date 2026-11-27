from typing import *
from core.enemy import Enemy
from db.db_init import *
from random import choice
from core.player import Player


class vague:
    def __init__(self, vague_actuelle: int, monsters: List['Enemy']):
        self.vague_actuelle = vague_actuelle
        self.monsters = monsters

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
            dropable=[]
        )

        self.monsters.append(monster)

        return self.monsters

    def play_vague(self, player : Player):

        while player.is_team_alive():
            alive_monsters = [monster for monster in self.monsters if monster.is_alive()]
            if not alive_monsters:
                print("Vous avez gagné la vague ", self.vague_actuelle)
                return True
            for character in player.get_alive_characters():
                alive_monsters = [monster for monster in self.monsters if monster.is_alive()]
                if not alive_monsters:
                    break
                target = choice(alive_monsters)
                damage = character.play_turn(target)
                print(f"{character.name} attaque {target.name} et inflige {damage} points de dégâts.")
                print(f"{target.name} a maintenant {target.hp} points de vie.")
                print()

            for monster in self.monsters:
                if monster.is_alive():
                    if not player.is_team_alive():
                        break

                    target = choice(player.get_alive_characters())
                    damage = monster.play_turn(target)

                    print(f"{monster.name} attaque {target.name} et inflige {damage} points de dégâts.")
                    print(f"{target.name} a maintenant {target.hp} points de vie.")

        print("Game over")
        return False



    def get_difficulty(self) -> dict:
        lap = (self.vague_actuelle - 1) // 10 + 1

        for difficulty in DifficultyList:
            if difficulty["lap"] == lap:
                return difficulty

        return DifficultyList[-1]
            