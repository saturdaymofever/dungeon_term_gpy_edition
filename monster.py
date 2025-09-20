import random, constant
from character import Character


#Création de la classe Monster
class Monster(Character):
    pass

    def __init__(self, pv, pw):
           super().__init__(pv, pw)
           self.defname()
    def defname(self):
        with open ("ressources/list/"+constant.lang+"/monster.txt") as monsterlist:      
            names = monsterlist.read().splitlines()
        self.name = random.choice(names)