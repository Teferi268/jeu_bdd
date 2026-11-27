from typing import *
from item import Item
from character import Character
from consumable import Consumable
from equipable import equipable


class Player():
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score
        self.team: List['Character'] = []
        self.inventory: List['Item'] = []

    def create_team(self,characters: List['Character']):
        self.team = []
        for character in characters:
            self.pick_character(character)
            if len(self.team) == 3:
                break
        return self.team

    def pick_character(self, character:' Character') -> bool:
        if len(self.team) >= 3:
            return False
        for member in self.team:
            if member.name == character.name:
                return False
        self.team.append(character)
        return True
    def is_team_alive(self) -> bool:
        for character in self.team:
            if character.hp > 0:
                return True
        return False

    def get_alive_characters(self) -> List['Character']:
        return [character for character in self.team if character.is_alive()]
    def check_inventory(self) -> List['Item']:
        return self.inventory
    
    def use_item(self, item: 'Item', target: 'Character') -> bool:
        if item not in self.inventory:
            return False

        if target not in    self.team:
            return False

        if isinstance(item, Consumable):
            item.use(target)

        elif isinstance(item, equipable):
            if not target.equip_item(item):
                return False

        else:
            return False

        self.inventory.remove(item)
        return True
            

    def add_item(self, item: 'Item'):
        self.inventory.append(item)