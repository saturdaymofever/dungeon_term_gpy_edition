import random, constant, player


#Création de la classe Monster
class Monster():
    pv = None
    pw = None
    coord = None
    name = None
    
    def __init__(self, pv=8, pw=1):
        self.pv = pv
        self.pw = pw
        self.defname()
        self.move()
    
    def move(self):
        self.coord = (random.randint(1,constant.mapV), random.randint(1,constant.mapH))
    def attack(self, player):
        player.pv -= self.pw
    def defname(self):
        with open ("ressources/list/FR/monster.txt") as monsterlist:      
            names = monsterlist.read().splitlines()
        self.name = random.choice(names)