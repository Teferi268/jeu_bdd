from typing import *



class Item:
    def __init__(self, name: str, description: str,
            droprate: float, rarity: str,
            item_type: str, stats: Dict[str, int]):
    

        self.name = name
        self.description = description
        self.droprate = droprate
        self.rarity = rarity
        self.item_type = item_type
        self.stats = stats

    def __str__(self) -> str:
        return self.name