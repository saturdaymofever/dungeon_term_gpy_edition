import random, constant

#Création de la classe Player
class Player():
    pv = None
    pw = None
    coord = None
    def __init__(self, pv=10, pw=2):
        self.pv = pv
        self.pw = pw
        self.move()
    
    def move(self):
        self.coord = (random.randint(1,constant.mapV), random.randint(1,constant.mapH))

