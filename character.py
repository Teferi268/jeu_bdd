from dataclasses import dataclass
from entity import Entity
from typing import *
from item import Item




class Character(Entity):
    def __init__(self, name: str, hp: int, max_hp: int, defense: int, attack: int, equipement: List['Item']):
        super().__init__(name, hp, max_hp, defense, attack)
        self.equipement = equipement

    def equipitem(self, item : 'Item') -> None:
        self.equipement.append(item)

    def unequipitem(self, item : 'Item') -> None:
        if item in self.equipement:
            self.equipement.remove(item)
    def isSlotAvailable(self, item : 'Item') -> bool:
        if len(self.equipement) < 3:
            return True
        else:
            return False
    def getEquipement(self) -> List['Item']:
        return self.equipement
    def projectDamage(self, target) -> int:
        projected_damage = max(self.attack - target.defense, 1)
        return projected_damage
    def play_turn(self, target: 'Entity') -> int:
        return self.projectDamage(target)
    

