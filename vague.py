from dataclasses import dataclass
from typing import *
from enemy import Enemy
from db_init import *
from random import choice
from player import Player


class vague:
    def __init__(self, vague_actuelle: int, monsters: List['Enemy']):
        self.vague_actuelle = vague_actuelle
        self.monsters = monsters

    def pick_enemies(self, vague_actuelle: int):
        self.monsters = range(int(vague_actuelle * self.get_difficulty()))

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

                print(f"{target.name} attaque {character.name} et inflige {damage} points de dégâts.")
                print(f"{character.name} a maintenant {character.hp} points de vie.")

        print("Game over")
        return False





    def get_difficulty(self) -> int:
        #obtenir le "lap" de difficulté de db_init.py
        return database["difficulty"].find_one({"lap": self.vague_actuelle})