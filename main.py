import sys, pygame, constant

version = str(constant.version)
pygame.init()
pygame.font.init()
pygame.display.set_caption("Dungeon Term Pygame Edition - Version: " + version )

size = width, height = 1920,1080
screen = pygame.display.set_mode(size)
hero_img = pygame.image.load("ressources/img/hero.png").convert_alpha()
monster_img = pygame.image.load("ressources/img/monster.png").convert_alpha()
hero_img = pygame.transform.scale(hero_img, (256, 256))
monster_img = pygame.transform.scale(monster_img, (512, 512))
monster_img = pygame.transform.flip(monster_img, True, False)

my_font = pygame.font.SysFont('Comic Sans MS', 100)
text_surface = my_font.render('Dungeon Term "PyGame Edition"', False, (255, 255, 255))


text_rect = text_surface.get_rect(center=(width // 2, height // 2))
black = 0, 0, 0
# Calcul positions bas écran
hero_x = width - hero_img.get_width()
hero_y = height - hero_img.get_height()
monster_x = 0
monster_y = height - monster_img.get_height()


screen = pygame.display.set_mode(size)

run = True
menu = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    screen.fill(black)
    screen.blit(text_surface, text_rect)
    screen.blit(hero_img,(hero_x,hero_y))
    screen.blit(monster_img,(0,monster_y))
    pygame.display.flip()