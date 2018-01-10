import pygame
import random

pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
SIZE = [600, 600]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Mini Game")

snow_list = []
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snow_list.append([x, y])

clock = pygame.time.Clock()

done = False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    screen.fill(WHITE)

pygame.quit()
quit()
