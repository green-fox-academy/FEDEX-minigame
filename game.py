import os
import pygame
import random
from fruits import Fruits


pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
SIZE = [700, 700]


screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Mini Game")
background = pygame.image.load(os.path.join("assets", "screen_tree.jpg"))
background = pygame.transform.scale(background, SIZE)

clock = pygame.time.Clock()
fruits = [pygame.image.load(os.path.join("assets", 'orange.png')), pygame.image.load(os.path.join("assets", 'banana.png')), pygame.image.load(os.path.join("assets", 'melon.png')), pygame.image.load(os.path.join("assets", 'apple.png'))]
one_fruit = random.choice(fruits)
for i in range(100):
    x = random.randrange(0, 700)
    y = random.randrange(0, 700)
# pygame.mouse.set_visible(False)
# pygame.event.set_grab(True)
done = False
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    screen.fill(WHITE)
    screen.blit(background, (0,0))
    screen.blit(one_fruit, (20,20))
    pygame.display.update()

pygame.quit()
quit()
