from dataclasses import dataclass
from typing import *
from item import Item
from character import Character
from entity import Entity

class Player(Entity):
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score
        self.team: List['Character'] = []
        self.inventory: List['Item'] = []

    def create_team(self,characters: List['Character']):
        self.team = characters

    def pick_character(self, character:' Character'):
        self.team.append(character)
    def is_team_alive(self) -> bool:
        for character in self.team:
            if character.hp > 0:
                return True
        return False
    def check_inventory(self) -> List['Item']:
        return self.inventory
    
    def use_item(self, item: 'Item'):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return None