from dataclasses import dataclass
from typing import *
from item import Item




class Entity:
    def __init__(self, name: str, hp: int, max_hp: int, defense: int, attack: int):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.defense = defense
        self.attack = attack

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, damage: int) -> int:
        acutual_damage = max(damage - self.defense, 1)
        self.hp = max(self.hp - acutual_damage, 0)
        return acutual_damage

    def heal(self, amount: int) -> int:
        actual_heal = min(amount, self.max_hp - self.hp)
        self.hp += actual_heal
        return actual_heal

    def attack(self,target : 'Entity') -> int:
        domage_deal = target.take_damage(self.attack)
        return domage_deal
    
    def play_turn(self, target: 'Entity') -> int:
        return self.attack(target)
        
    