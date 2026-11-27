from dataclasses import dataclass
from core.entity import Entity
from typing import *
from core.item import Item




class Character(Entity):
    def __init__(self, name: str, hp: int, max_hp: int, defense: int, attack: int, equipement: List['Item']):
        super().__init__(name, hp, max_hp, defense, attack)
        self.equipement = equipement
    
    def __str__(self):
        return f"{self.name} (HP: {self.hp}/{self.max_hp}, Attack: {self.get_attack()}, Defense: {self.get_defense()})"

    def equip_item(self, item : 'Item') -> bool:
        if len(self.equipement) >= 3:
            return False

        if not self.is_slot_available(item.item_type):
            return False

        self.equipement.append(item)
        return True

    def unequip_item(self, item : 'Item') -> None:
        if item in self.equipement:
            self.equipement.remove(item)
    def is_slot_available(self, slot_name: str) -> bool:
        for i in self.equipement:
            if i.item_type == slot_name:
                return False
        return True
    def get_equipement(self, slot_name : str) -> List['Item']:
        for item in self.equipement:
            if item.item_type == slot_name:
                return item

        return None
    def project_damage(self, target) -> int:
        return min(max(self.get_attack() - target.get_defense(), 1),target.hp)
    def play_turn(self, target: 'Entity') -> int:

        return self.attack_target(target)
    def get_attack(self) -> int:
        attack = self.attack
        for item in self.equipement:
            attack += item.stats.get("attack", 0)
        return attack
    def get_defense(self) -> int:
        defense = self.defense
        for item in self.equipement:
            defense += item.stats.get("defense", 0)
        return defense  
    

