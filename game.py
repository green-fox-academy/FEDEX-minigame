import os
import pygame
import random

pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
SIZE = [600, 600]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Mini Game")
background = pygame.image.load(os.path.join("assets", "screen_tree.jpg"))
background = pygame.transform.scale(background, SIZE)

clock = pygame.time.Clock()

# pygame.mouse.set_visible(False)
# pygame.event.set_grab(True)

done = False
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    screen.fill(WHITE)
    screen.blit(background, (0,0))
    pygame.display.update()


pygame.quit()
quit()
