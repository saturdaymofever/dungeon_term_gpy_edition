import player, monster

player1 = player.Player()
player1.move()

monster1 = monster.Monster()
monster1.move()

print(player1.pv, player1.coord)
print(monster1.pv, monster1.coord)