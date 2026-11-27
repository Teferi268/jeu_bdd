from core.game import Game
from core.player import Player
from core.character import Character

player = Player("Test", 0)

player.create_team([
    Character("Guerrier", 100, 100, 10, 15, []),
    Character("Mage", 80, 80, 5, 20, []),
    Character("Archer", 90, 90, 7, 18, [])
])

game = Game(player)

print("--- EQUIPE ---")

for character in player.team:
    print(character)

print("--- LANCEMENT DU JEU ---")

game.launch_game()

print("--- FIN DU JEU ---")
print("Score :", player.score)