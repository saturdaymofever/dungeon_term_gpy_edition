import random, constant, player

monstres = [
        "Loup affamé",
        "Ours brun",
        "Sanglier enragé",
        "Serpent venimeux",
        "Araignée géante",
        "Corbeau aux yeux rouges",
        "Esprit de la forêt",
        "Goule rampante",
        "Gobelin rôdeur",
        "Troll des bois",
        "Dryade corrompue",
        "Ent sombre",
        "Spectre brumeux",
    ]

#Création de la classe Monster
class Monster():
    pv = None
    pw = None
    coord = None
    name = None
    
    def __init__(self, pv=8, pw=1):
        self.pv = pv
        self.pw = pw
        self.name = random.choice(monstres)
        self.move()
    
    def move(self):
        self.coord = (random.randint(1,constant.mapV), random.randint(1,constant.mapH))
    def attack(self, player):
        player.pv -= self.pw