import pygame

# Initialize the pygame
pygame.init()
# Create the screen
screen = pygame.display.set_mode((900, 500))
# Title and icon
pygame.display.set_caption("Deep Search: The End (Final Edition)")
icon = pygame.image.load('golo1.png')
# Player
character = pygame.image.load('ch1.png')
PlayerX = 300
PlayerY = 200


def player(x, y):
    screen.blit(character, (x, y))


# Icon
pygame.display.set_icon(icon)
# Game Loop
running = True
while running:
       # Background
    screen.fill((5, 14, 98))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # Background
    screen.fill((5, 14, 98))

    player()
    pygame.display.update()

