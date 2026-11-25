from dataclasses import dataclass
from typing import *
from item import Item
from character import Character

class Player:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score
        self.team: List['Character'] = []
        self.invotory: List['Item'] = []

    def CreateTeam(self,characters: List['Character']):
        self.team = characters

    def PickCharacter(self, character:' Character'):
        self.team.append(character)
    def IsTeamAlive(self) -> bool:
        for character in self.team:
            if character.hp > 0:
                return True
        return False
    def CheckInventory(self) -> List['Item']:
        return self.invotory
    
    def UseItem(self, item: 'Item'):
        if item in self.invotory:
            self.invotory.remove(item)
            return item
        else:
            return None