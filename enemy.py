from dataclasses import dataclass
from entity import Entity
from typing import *
from item import Item



class Enemy(Entity):
    def __init__(self, name: str, hp: int, max_hp: int, defense: int, attack: int, dropable: List['Item']):
        super().__init__(name, hp, max_hp, defense, attack)
        self.dropable = dropable

    def get_dropable(self) -> List['Item']:
        return self.dropable
    def play_turn(self, target: 'Entity') -> int:
        return self.attack(target)