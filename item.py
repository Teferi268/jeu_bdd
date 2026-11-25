from dataclasses import dataclass
from entity import Entity
from typing import *



class Item:
    name: str
    description: str
    droprate: int
    rarity: str
    item_type: str
    stats: Dict[str, int]