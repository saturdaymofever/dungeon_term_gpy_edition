import sys, pygame, constant

version = str(constant.version)
pygame.init()
pygame.font.init()
pygame.display.set_caption("Dungeon Term Pygame Edition - Version: " + version )
my_font = pygame.font.SysFont('Comic Sans MS', 100)
text_surface = my_font.render('Dungeon Term "PyGame Edition"', False, (255, 255, 255))
size = width, height = 1920,1080
text_rect = text_surface.get_rect(center=(width // 2, height // 2))
black = 0, 0, 0



screen = pygame.display.set_mode(size)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.fill(black)
    screen.blit(text_surface, text_rect)
    pygame.display.flip()