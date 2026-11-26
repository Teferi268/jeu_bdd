from dataclasses import dataclass
from typing import *
from enemy import Enemy
from db_init import *
from random import random


class vague:
    def __init__(self, vague_actuelle: int, monsters: List['Enemy']):
        self.vague_actuelle = vague_actuelle
        self.monsters = monsters

    def pick_enemies(self, vague_actuelle: int):
        self.monsters = range(int(vague_actuelle * self.get_difficulty()))

    def play_vague(self):
        for monster in self.monsters:
            if monster.is_alive():
                damage = self.player.play_turn(monster)
                monster.hp -= damage
                if monster.is_alive():
                    damage = monster.play_turn(self.player)
                    self.player.hp -= damage
                if not self.player.is_alive():
                    print("Perdu")
                else:
                    print("Vous avez gagné la vague ", self.vague_actuelle)

    def get_difficulty(self) -> int:
        #obtenir le "lap" de difficulté de db_init.py
        return database["difficulty"].find_one({"lap": self.vague_actuelle})