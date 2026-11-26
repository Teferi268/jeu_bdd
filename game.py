from dataclasses import dataclass
from item import Item
from character import Character
from db_init import MongoClient
from vague import vague



class Game:
    def __init__(self, player: Character):
        self.player = player
        self.mongoclient = MongoClient()
        self.vague = vague(1, [])

    def save_game(self):
        self.mongoclient.save_game(self.player, self.vague)
    def load_game(self):
        self.player, self.vague = self.mongoclient.load_game()
    def launch_game(self):
        while self.player.team.is_alive():
            self.vague.play_vague()
    def show_leaderboard(self):
        leaderboard = self.mongoclient.get_leaderboard()
        for entry in leaderboard:
            print(f"{entry['name']}: {entry['score']}")
    def exit_game(self):
        self.save_game()
        print("Game saved. Exiting...")
        
    



