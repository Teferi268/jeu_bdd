from dataclasses import dataclass
from typing import *



@dataclass
class Entity:
    name: str
    hp: int
    max_hp: int
    defense: int
    attack: int

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, damage: int) -> int:
        acutual_damage = max(damage - self.defense, 1)
        self.hp = max(self.hp - acutual_damage, 0)
        return acutual_damage


@dataclass
class Character(Entity):
    equipement: List['Item']

@dataclass
class Enemy(Entity):
    dropable: List['Item']

@dataclass
class Item:
    name: str
    item_type: str
    rarity: str
    effect: Dict[str, int]
    consumable: bool
