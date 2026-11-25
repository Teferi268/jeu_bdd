from dataclasses import dataclass
from typing import *
from item import Item
from character import Character
from enemy import Enemy
from entity import Entity
from db_init import MongoClient
from vague import vague



class Game:
    def __init__(self, player: Character):
        self.player = player
        self.mongoclient = MongoClient()
        self.vague = vague(1, [])

    def SaveGame(self):
        self.mongoclient.save_game(self.player, self.vague)
    def LoadGame(self):
        self.player, self.vague = self.mongoclient.load_game()
    def LaunchGame(self):
        while self.player.is_alive() and self.vague.PlayVague():
            for monster in self.vague.monsters:
                if monster.is_alive():
                    damage = self.player.play_turn(monster)
                    monster.hp -= damage
                    if monster.is_alive():
                        damage = monster.Playturn(self.player)
                        self.player.hp -= damage
        if not self.player.is_alive():
            print("Perdu")
        else:
            print("Vous avez gagné la vague ", self.vague.vague_actuelle)
    def ShowLeaderboard(self):
        leaderboard = self.mongoclient.get_leaderboard()
        for entry in leaderboard:
            print(f"{entry['name']}: {entry['score']}")
    def ExitGame(self):
        self.SaveGame()
        print("Game saved. Exiting...")
        
    



