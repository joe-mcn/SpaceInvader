import pygame
import random

# Start Pygame
pygame.init()

# create screen
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
# Background
background = pygame.image.load("space.jpg")
# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

# Player Specs
playerPic = pygame.image.load("player.png")
playerX = screenWidth / 2
playerY = screenHeight - 100
playerX_change = 0
playerY_change = 0

# Enemy
enemyPic = pygame.image.load("ufo.png")
enemyX = random.randint(0, screenWidth)
enemyY = random.randint(0, 150)
enemyX_change = 0.1
enemyY_change = 40

# Bullet
bullet_Pic = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = .5
bullet_state = "ready"


def player(x, y):
    screen.blit(playerPic, (x, y))


def enemy(x, y):
    screen.blit(enemyPic, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_Pic, (x + 16, y + 10))


# Game Loop
running = True
while running:
    # RGB of Screen
    screen.fill((150, 100, 180))
    # Background
    screen.blit(background, (0, 0))

    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            running = False
        # Check for keystroke left or right
        if action.type == pygame.KEYDOWN:
            if action.key == pygame.K_LEFT:
                playerX_change = -0.4
            if action.key == pygame.K_RIGHT:
                playerX_change = 0.4
            # if action.key == pygame.K_UP:
            #     playerY_change = -0.2
            # if action.key == pygame.K_DOWN:
            #     playerY_change = 0.2
            if action.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)
        if action.type == pygame.KEYUP:
            if action.key == pygame.K_LEFT or action.key == pygame.K_RIGHT:
                playerX_change = 0
            # if action.key == pygame.K_UP or action.key == pygame.K_DOWN:
            #     playerY_change = 0

    # Calling Player Class
    playerX += playerX_change
    playerY += playerY_change

    # If player hits boundary
    if playerX <= 0:
        playerX = 0
    elif playerX >= screenWidth - 64:
        playerX = screenWidth - 64
    # if playerY <= 0:
    #     playerY = 0
    # elif playerY >= screenHeight - 64:
    #     playerY = screenHeight - 64

    # Enemy Movement
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.1
        enemyY += enemyY_change

    elif enemyX >= screenWidth - 64:
        enemyX_change = - .1
        enemyY += enemyY_change

    # Bullet Movement
    if bullet_state is "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
