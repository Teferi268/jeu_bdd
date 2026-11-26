from dataclasses import dataclass
from typing import *
from item import Item
from character import Character
from enemy import Enemy
from db_init import *



class vague:
    def __init__(self, vague_actuelle: int, monsters: List['Enemy']):
        self.vague_actuelle = vague_actuelle
        self.monsters = monsters

    def pick_enemies(self, vague, monsters: List['Enemy']):
        self.vague_actuelle = vague
        self.monsters = monsters

    def play_vague(self):
        while self.player.is_alive():
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

    def get_difficulty(self, difficulty: int) -> int:
        #obtenir le lap de difficulté de db_init.py
        Diffulty_lap = 
        