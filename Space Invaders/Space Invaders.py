import pygame
import random
import math
from pygame import mixer
mixer.init()
pygame.init()
screen = pygame.display.set_mode((800 ,600))

# Background
background = pygame.image.load("C:/Users/BIJUMINI/Desktop/Pygamers/Space Invaders/Blue.jpg")
# Background sound
mixer.music.load("C:/Users/BIJUMINI/Desktop/Pygamers/Space Invaders/Joel.wav")
mixer.music.play(-1)

# Icon and Logo
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("C:/Users/BIJUMINI/Desktop/Pygamers/Space Invaders/spaceship.png")
pygame.display.set_icon(icon)

# Player and Enemy 
playerImg = pygame.image.load('C:/Users/BIJUMINI/Desktop/Pygamers/Space Invaders/space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

oppImg = []
oppX = []
oppY = []
oppX_change =[]
oppY_change = []
number_of_enemies = 6
for i in range(number_of_enemies):
                oppImg.append(pygame.image.load('C:/Users/BIJUMINI/Desktop/Pygamers/Space Invaders/ghost1.png'))
                oppX.append(random.randint(0, 736))
                oppY.append(75)
                oppX_change.append(7)
                oppY_change.append(3)

# Bullet state
bulletImg = pygame.image.load('C:/Users/BIJUMINI/Desktop/Pygamers/Space Invaders/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
levelgame = 0
score = 0

    
game_over = pygame.font.Font("freesansbold.ttf", 64)


def game_over():
    game_over = font.render("GAME OVER", True, (255, 255, 255))
    game_over = screen.blit(game_over, (400, 300))

def change_level():
    global levelgame
    global score
    global number_of_enemies
    if score_value%20 == 0:
        if score_value != score:
            levelgame+=1
            score = score_value
            

                
def show_score(x, y):
    score = font.render('Score:' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def level_show (x,y):
        level_show = level_title.render("Level:"+str(levelgame),True,(255,255,255))
        screen.blit(level_show,(x,y))

def player(x, y):
    screen.blit(playerImg, (x, y))


def Opp(x, y, i):
    screen.blit(oppImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(oppX, oppY, bulletX, bulletY):
    distance = math.sqrt(math.pow(oppX - bulletX, 2) + math.pow(oppY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_UP:
                playerY_change = -0.2
            if event.key == pygame.K_DOWN:
                playerY_change= 0.2
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('C:/Users/BIJUMINI/Desktop/Pygamers/Space Invaders/laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
    # Player Movement
    playerX += playerX_change
    playerY += playerY_change
    # Boundary
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    if playerY > 536:
        playerY = 536


    # Enemy Boundary and Movement
    for i in range(number_of_enemies):
        if oppY[i] > 300:
            running = False
            for j in range(number_of_enemies):
                oppY[j] = 2000
                game_over()
                break

        oppX[i] += oppX_change[i]
        if oppX[i] <= 0:
            oppY_change[i] = 40
            oppX_change[i] = 2
            oppY[i] += oppY_change[i]
        elif oppX[i] >= 736:
            oppY_change[i] = 40
            oppX_change[i] = -2
            oppY[i] += oppY_change[i]

        Opp(oppX[i], oppY[i], i)

        # Collision
        collision = isCollision(oppX[i], oppY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('C:/Users/BIJUMINI/Desktop/Pygamers/Space Invaders/explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 2
        
        
            oppX[i] = random.randint(0, 736)
            oppY[i] = 75

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY_change = 10
        bulletY -= bulletY_change
    #Level
    textX1 = 660
    textY1 = 10
   
    level_title = pygame.font.Font("freesansbold.ttf",32)

    player(playerX, playerY)
    show_score(textX, textY)
    level_show(textX1,textY1)
    change_level()
    pygame.display.update()  


