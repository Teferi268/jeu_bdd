from dataclasses import dataclass
from typing import Dict, List

@dataclass
class CharacterDB:
    name:str
    hp: int
    defense: int
    attack : int 
    inventaire: List['Item'] 

@dataclass
class MonsterDB:
    name:str
    hp: int
    defense: int
    attack : int
    dropable : List['Item']


@dataclass
class ScoreDB:
    player_name: str
    score: int


@dataclass
class CharacterSaveDB:
    name:str
    hp: int
    equipe: List["Item"]

@dataclass
class MonstersSaveDB:
    name:str
    hp: int

@dataclass
class SaveDB:
    player_name: str
    score: int
    characters: List[CharacterSaveDB]
    monsters: List[MonstersSaveDB]
    inventaire: List["Item"] 

@dataclass
class Item:
    name: str
    item_type: str
    rarity: str
    effect : Dict[str, int]
    consumable: bool

@dataclass
class Vague:
    start_number: int
    end_number: int
    monsters: List[MonsterDB]

@dataclass
class Difficulty:
    lap : int
    health_multiplier: float
    attack_multiplier: float
    defense_multiplier: float
    item_mutiplier: float



@dataclass
class Rarity:
    name: str
    drop_rate: float

