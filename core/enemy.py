from dataclasses import dataclass
from core.entity import Entity
from typing import *
from core.item import Item
from random import random



class Enemy(Entity):
    def __init__(self, name: str, hp: int, max_hp: int, defense: int, attack: int, dropable: List['Item']):
        super().__init__(name, hp, max_hp, defense, attack)
        self.dropable = dropable

    def get_dropable(self) -> List['Item']:
        return self.dropable
    def play_turn(self, target: 'Entity') -> int:
        return self.attack_target(target)
    def drop_loot(self) -> List['Item']:
        loot = []
        for item in self.dropable:
            if random() <= item.droprate:
                loot.append(item)
        return loot