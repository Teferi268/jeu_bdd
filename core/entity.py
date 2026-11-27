from dataclasses import dataclass
from typing import *
from core.item import Item




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
        actual_damage = min(
            max(damage - self.get_defense(), 1),
            self.hp
            )
        self.hp -= actual_damage
        return actual_damage

    def heal(self, amount: int) -> int:
        actual_heal = min(amount, self.max_hp - self.hp)
        self.hp += actual_heal
        return actual_heal

    def attack_target(self,target : 'Entity') -> int:
        return target.take_damage(self.get_attack())
    
    def play_turn(self, target: 'Entity') -> int:
        return self.attack_target(target)

    def get_attack(self) -> int:
        return self.attack
    def get_defense(self) -> int:
        return self.defense
        
    