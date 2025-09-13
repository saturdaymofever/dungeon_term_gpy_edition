import random 
class Player():
    pv = 10
    pw = None
    coord = None

    def __init__(self, pv=10, pw=2):
        self.pv = pv
        self.pw = pw
        self.move()
    
    def move():
        coord = (random.randint(1,gamezone(0)), random.randint(1,gamezone(1)))

