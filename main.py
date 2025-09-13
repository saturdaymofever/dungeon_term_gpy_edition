import sys, pygame
pygame.init()
pygame.font.init()
size = width, height = 1920,1080

black = 0, 0, 0

my_font = pygame.font.SysFont('Comic Sans MS', 100)
text_surface = my_font.render('Dungeon Term "PyGame Edition"', False, (255, 255, 255))
screen = pygame.display.set_mode(size)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.fill(black)
    screen.blit(text_surface, (0,0))
    pygame.display.flip()