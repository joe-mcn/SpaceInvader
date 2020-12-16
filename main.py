import pygame
import random
import math

# Start Pygame
pygame.init()

# create screen
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
# Background
# background = pygame.image.load("space.jpg")
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
enemyPic = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyPic.append(pygame.image.load("ufo.png"))
    enemyX.append(random.randint(0, screenWidth - 65))
    enemyY.append(random.randint(0, 150))
    enemyX_change.append(0.1)
    enemyY_change.append(40)

# Bullet
bullet_Pic = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = .5
bullet_state = "ready"
# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10
# Game over
over_font = pygame.font.Font('freesansbold.ttf', 55)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 255, 0))
    screen.blit(score, (x, y))


def game_over():
    over_text = over_font.render("GAME OVER Score was " + str(score_value), True, (0, 255, 0))
    screen.blit(over_text, (50, 250))


def player(x, y):
    screen.blit(playerPic, (x, y))


def enemy(x, y, i):
    screen.blit(enemyPic[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_Pic, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:
    # RGB of Screen
    screen.fill((150, 100, 180))
    # Background
    # screen.blit(background, (0, 0))

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
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if action.type == pygame.KEYUP:
            if action.key == pygame.K_LEFT or action.key == pygame.K_RIGHT:
                playerX_change = 0
            # if action.key == pygame.K_UP or action.key == pygame.K_DOWN:
            #     playerY_change = 0

    # Calling Player Class
    playerX += playerX_change
    # playerY += playerY_change

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
    for i in range(num_of_enemies):
        # Game over
        if enemyY[i] > 350:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = .5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= screenWidth - 64:
            enemyX_change[i] = -.5
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, screenWidth - 65)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
