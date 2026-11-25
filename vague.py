from dataclasses import dataclass
from typing import *
from item import Item
from character import Character
from enemy import Enemy



class vague:
    def __init__(self, vague_actuelle: int, monsters: List['Enemy']):
        self.vague_actuelle = vague_actuelle
        self.monsters = monsters

    def PickEnemies(self, vague, monsters: List['Enemy']):
        self.vague_actuelle = vague
        self.monsters = monsters

    def PlayVague(self):
        for monster in self.monsters:
            if monster.hp > 0:
                return True
        return False
    def GetDifficulty(self) -> int:
        difficulty = 0
        for monster in self.monsters:
            difficulty += monster.hp + monster.attack + monster.defense
        return difficulty