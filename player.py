import random, constant, monster
from character import Character

#Création de la classe Player
class Player(Character):

    def attack(self, target):
        target.pv -= self.pw * 2