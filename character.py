import constant, random


class Character():
    pv = None
    pw = None
    coord = None
    name = None
    
    def __init__(self, pv=8, pw=1):
        self.pv = pv
        self.pw = pw
        self.move()
    
    def move(self):
        self.coord = (random.randint(1,constant.mapV), random.randint(1,constant.mapH))
    def attack(self, target):
        target.pv -= self.pw
