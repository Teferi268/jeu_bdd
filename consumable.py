from dataclasses import dataclass
from entity import Entity
from item import Item

class Consumable(Item):

    def use(self, target: 'Entity') -> None:
        if "hp" in self.stats:
            target.heal(self.stats["hp"])

        if "attack" in self.stats:
            target.attack += self.stats["attack"]

        if "defense" in self.stats:
            target.defense += self.stats["defense"]