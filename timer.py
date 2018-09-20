import sys
import pygame
pygame.init()

RES = (640, 480)
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

display = pygame.display.set_mode(RES, pygame.FULLSCREEN)
clock = pygame.time.Clock()

bg_img = pygame.Surface(RES)
bg_img.fill(WHITE)
for y in (229, 290):
    for x in range(40, RES[0], 40):
        bg_img.set_at((x, y), BLUE)

def motion_test():

    rect = pygame.rect.Rect((0, 240), (40, 40))

    while True:

        display.blit(bg_img, (0, 0))
        
        for e in pygame.event.get():
            if (e.type == pygame.QUIT or
                e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
        
        rect.x += 1
        if rect.x >= RES[0]:
            rect.x = 0
        
        pygame.draw.rect(display, BLUE, rect)
        
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    motion_test()
