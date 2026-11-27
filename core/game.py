from core.vague import vague
from core.player import Player
from db.db_init import *
from pymongo import MongoClient


class Game:
    def __init__(self, player: Player):
        self.player = player
        self.mongo_client = MongoClient()
        self.vague = vague(1, [])

    def save_game(self):
        save_data = SaveDB(
        player_name=self.player.name,
        score=self.player.score,
        equipe=[
            CharacterSaveDB(
                name=character.name,
                hp=character.hp,
                equipement=character.equipement
            )
            for character in self.player.team
        ],
        monsters=[
            MonsterSaveDB(
                name=monster.name,
                hp=monster.hp
            )
            for monster in self.vague.monsters
        ],
        inventaire=self.player.inventory
        )

        self.mongo_client["game_db"]["saves"].update_one(
            {"player_name": self.player.name},
            {"$set": save_data.__dict__()},
            upsert=True
        )

        print("Sauvegarde effectuee avec succes")

        return save_data

    def load_game(self, player_name: str):
        return self.mongo_client["game_db"]["saves"].find_one({"player_name": player_name})


    def launch_game(self):
        while self.player.is_team_alive():
            self.vague.pick_enemies(self.vague.vague_actuelle)
            victoire = self.vague.play_vague(self.player)
            if not victoire:
                break
            self.player.score += 1
            self.vague.vague_actuelle += 1
        print(f"score final de {self.player.name} : {self.player.score}")

    def show_leaderboard(self):
        scores = (
            self.mongo_client["game_db"]["scores"]
            .find()
            .sort("score", -1)
            .limit(10)
        )
        print("Classement des meilleurs scores :")
        for i, player in enumerate(scores, start=1):
            print(f"{i}. {player['player_name']} - Score: {player['score']}")


    def exit_game(self):
        self.save_game()
        print("La partie a été sauvegardée avec succès.")
        exit()



