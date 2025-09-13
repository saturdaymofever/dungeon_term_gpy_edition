import random, constant

#Création de la classe Monster
class Monster():
    pv = None
    pw = None
    coord = None
    def __init__(self, pv=8, pw=1):
        self.pv = pv
        self.pw = pw
        self.move()
    
    def move(self):
        self.coord = (random.randint(1,constant.mapV), random.randint(1,constant.mapH))