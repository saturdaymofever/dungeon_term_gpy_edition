from character import Character

#Création de la classe Player
class Player(Character):
    pw_coef = 1.2
    def attack(self, target):
        target.pv -= self.pw * self.pw_coef