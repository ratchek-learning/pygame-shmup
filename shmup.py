# Pygame template - skeleton for a new pygame project
import pygame
import random
import os

WIDTH = 360
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
folder = os.path.abspath(os.path.dirname(__file__))
images_folder = os.path.join(folder, "resources/img/")
player_image = pygame.image.load(os.path.join(images_folder, "playerShip1_blue.png")).convert_alpha()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image =player_image
        self.rect = self.image.get_rect()
        self.rect.center =  (WIDTH/2, HEIGHT/2)
        
    def update(self):
        self.rect.x +=1
        self.rect.y +=1

player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(GREEN)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
