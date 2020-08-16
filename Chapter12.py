import sys
import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Pygame Window")
    
    bg_color = (0, 0, 255)
        
    while True:
        
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        pygame.display.flip()
        
        screen.fill(bg_color)
        pygame.display.flip()

run_game()