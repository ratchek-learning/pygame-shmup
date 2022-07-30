# Pygame template - skeleton for a new pygame project
import pygame
import random
import os

WIDTH = 400 
HEIGHT = 600
FPS = 60

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
mobs = pygame.sprite.Group()
folder = os.path.abspath(os.path.dirname(__file__))
images_folder = os.path.join(folder, "resources/img/")
player_image = pygame.image.load(os.path.join(images_folder, "playerShip1_blue.png")).convert_alpha()

class Mob (pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.width = width
        self.height = height
        color = random.choice([WHITE,BLACK,RED,BLUE])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.spawn_at_top()
    def spawn_at_top(self):
        self.rect.left = random.randrange(WIDTH-self.width)
        self.rect.bottom = random.randrange(-100, -10)
        self.speedy = random.randrange(1,8)
        self.speedx = random.randrange(-3,3)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top >= HEIGHT or self.rect.right < 0 or self.rect.right>WIDTH:
            self.spawn_at_top()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image =player_image
        self.rect = self.image.get_rect()
        self.rect.center =  (WIDTH/2, HEIGHT-60)
        self.speedx = 0
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx -= 8
        if keystate[pygame.K_RIGHT]:
            self.speedx += 8
        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

player = Player()
all_sprites.add(player)
for x in range(10):
    mob = Mob(30,40)
    all_sprites.add(mob)
    mobs.add(mob)
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
