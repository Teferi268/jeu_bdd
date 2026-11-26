from dataclasses import dataclass
from entity import Entity
from typing import *
from item import Item




class Character(Entity):
    def __init__(self, name: str, hp: int, max_hp: int, defense: int, attack: int, equipement: List['Item']):
        super().__init__(name, hp, max_hp, defense, attack)
        self.equipement = equipement

    def equip_item(self, item : 'Item') -> None:
        self.equipement.append(item)

    def unequip_item(self, item : 'Item') -> None:
        if item in self.equipement:
            self.equipement.remove(item)
    def is_slot_available(self) -> bool:
        if len(self.equipement) < 3:
            return True
        else:
            return False
    def get_equipement(self) -> List['Item']:
        return self.equipement
    def project_damage(self, target) -> int:
        projected_damage = max(self.attack - target.defense, 1)
        return projected_damage
    def play_turn(self, target: 'Entity') -> int:
        return self.project_damage(target)
    

