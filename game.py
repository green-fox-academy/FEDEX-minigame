import os
import pygame
import random


pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
SIZE = [700, 700]
random_fruits = []
x = random.randrange(0, 600)
y = random.randrange(0, 600)
basket_x = 300
basket_randomx = random.randrange(0, 600)
basket_randomy = random.randrange(0, 600)

speed = 1
score = 0

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Mini Game")
background = pygame.image.load(os.path.join("assets", "screen_tree.jpg"))
background = pygame.transform.scale(background, SIZE)

clock = pygame.time.Clock()
fruits = [pygame.image.load(os.path.join("assets", 'orange.png')), pygame.image.load(os.path.join("assets", 'banana.png')), pygame.image.load(os.path.join("assets", 'melon.png')), pygame.image.load(os.path.join("assets", 'apple.png'))]
life = pygame.image.load(os.path.join("assets", "heart.png"))
basket_left = pygame.image.load(os.path.join("assets", "basket_left.png"))
basket_right = pygame.image.load(os.path.join("assets", "basket_right.png"))
basket = basket_left
basket_size = 238
life_x = 0
life_count = 3

# start_clock = clock.get_time()/1000
# seconds = (pygame.time.get_ticks() - start_clock)/1000 #calculate how many seconds


class Fruits():
    def __init__(self, picture):
        self.picture = picture
        self.x = random.randrange(0, 600)
        self.y = -50

    def increment_y(self, number):
        self.y += number
        
    def display(self, screen):
        screen.blit(self.picture, (self.x, self.y))

    def is_it_in_the_basket(self, x, basket_size):
        # fruits x should be between x and x+basket_size
        if self.y == basket_randomy and self.x == basket_randomx:
            return True
        

one_fruit = Fruits(random.choice(fruits))
all_fruits = [one_fruit]
start_ticks=pygame.time.get_ticks()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  
    screen.fill(WHITE)
    screen.blit(background, (0,0))
    actual_ticks = pygame.time.get_ticks()
    seconds=(actual_ticks-start_ticks)/1000 #calculate how many seconds
    
    for i in range(life_count):
        screen.blit(life, (life_x + i * 32, 0))
    
    if seconds > 1:
        all_fruits.append(Fruits(random.choice(fruits)))
        speed += 1
        start_ticks = actual_ticks
        
    #randomly add new fruits to the list during the game
    # for i in range(random_number):
    for fruit in all_fruits:
        fruit.display(screen)
        fruit.increment_y(speed)
    # if fruit felt down - check is it in basket - remove it
        if fruit.y > 550:
            if fruit.is_it_in_the_basket(basket_x, basket_size):
                #increment points
                score += 1
            else:
                life_count -1
            #remove fruit

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and basket_x > -30:
            basket_x -= 10
            basket = basket_left
        if event.key == pygame.K_RIGHT and basket_x < 600:
            basket_x += 10
            basket = basket_right
    
    screen.blit(basket, (basket_x,500))

    pygame.display.flip()
    pygame.display.update()
    clock.tick(120)

    
pygame.quit()
quit()
