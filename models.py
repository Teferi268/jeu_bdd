class Heroe:
    #Class pour les heroes
    def __init__(self, nom, atk, defense, pv):
        self.nom = nom
        self.atk = atk
        self.defense = defense
        self.pv = pv


class Monster(Heroe):
    #Reprend les même attribue que la class Heroe
    pass 