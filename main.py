import pygame, sys, random, os
pygame.font.init()

# Blits
BALL = pygame.image.load(os.path.join("assets", "ball.png"))
PADDLE = pygame.image.load(os.path.join("assets", "paddle.png"))
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg.png")), (640, 480))

# Variables
screenWidth = 640
screenHeight = 480
white = (255, 255, 255)

playerVel = 0
playerTwoVel = 0
playerScore = 0
time = 0

ballSpeedX = 5 * random.choice((1, -1))
ballSpeedY = 5 * random.choice((1, -1))
ballSpeedX2 = 6 * random.choice((1, -1))
ballSpeedY2 = 6 * random.choice((1, -1))
ballSpeedX3 = 7 * random.choice((1, -1))
ballSpeedY3 = 7 * random.choice((1, -1))

# Functions

def playerAnimation():
    player.y += playerVel
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screenHeight:
        player.bottom = screenHeight

    player2.y += playerTwoVel
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screenHeight:
        player2.bottom = screenHeight

def ballAnimation():
    global ballSpeedX, ballSpeedY, ballSpeedX2, ballSpeedY2, ballSpeedX3, ballSpeedY3, playerScore
    ball.x += ballSpeedX
    ball.y += ballSpeedY
    
    if ball.top <= 0 or ball.bottom >= screenHeight:
        ballSpeedY *= -1
    if ball.left <= 0:
        ballSpeedX *= -1
    if ball.right >= screenWidth:
        ballSpeedX *= -1
        playerScore += 1
    if ball.colliderect(player):
        gameRestart()

    ball2.x += ballSpeedX2
    ball2.y += ballSpeedY2
    
    if ball2.top <= 0 or ball2.bottom >= screenHeight:
        ballSpeedY2 *= -1
    if ball2.left <= 0:
        ballSpeedX2 *= -1
    if ball2.right >= screenWidth:
        ballSpeedX2 *= -1
        playerScore += 1
    if ball2.colliderect(player):
        gameRestart()

    ball3.x += ballSpeedX3
    ball3.y += ballSpeedY3
    
    if ball3.top <= 0 or ball3.bottom >= screenHeight:
        ballSpeedY3 *= -1
    if ball3.left <= 0:
        ballSpeedX3 *= -1
    if ball3.right >= screenWidth:
        ballSpeedX3 *= -1
        playerScore += 1
    if ball3.colliderect(player):
        gameRestart()

    if secondPlayer == True:
        if ball.colliderect(player):
                gameRestart()
        if ball2.colliderect(player):
                gameRestart()
        if ball3.colliderect(player):
                gameRestart()
        if ball.colliderect(player2):
                gameRestart()
        if ball2.colliderect(player2):
                gameRestart()
        if ball3.colliderect(player2):
                gameRestart()

def gameRestart():
    global ballSpeedX, ballSpeedY, ballSpeedX2, ballSpeedY2, ballSpeedX3, ballSpeedY3, playerScore, time
    ball.center = (screenWidth / 2, screenHeight / 2)
    ballSpeedY *= random.choice((1, -1))
    ballSpeedX *= random.choice((1, -1))
    ball2.center = (screenWidth / 2, screenHeight / 2)
    ballSpeedY2 *= random.choice((1, -1))
    ballSpeedX2 *= random.choice((1, -1))
    ball3.center = (screenWidth / 2, screenHeight / 2)
    ballSpeedY3 *= random.choice((1, -1))
    ballSpeedX3 *= random.choice((1, -1))
    playerScore = 0
    time = 0
    
# Main Setup
pygame.init()
clock = pygame.time.Clock()

# Window Setup
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pong Avoid")

# Rects
player = pygame.Rect(screenWidth - 20, screenHeight / 2 - 35, 10, 70)
player2 = pygame.Rect(screenWidth - 620, screenHeight / 2 - 35, 10, 70)
ball = pygame.Rect( screenWidth / 2 - 7.5, screenHeight / 2 - 7.5, 15, 15)
ball2 = pygame.Rect(screenWidth / 2 - 7.5, screenHeight / 2 - 7.5, 15, 15)
ball3 = pygame.Rect(screenWidth / 2 - 7.5, screenHeight / 2 - 7.5, 15, 15)

# Main Loop
secondPlayer = False
run = True
mainFont = pygame.font.SysFont("Arial", 40)
while run:

    # Function Calling
    playerAnimation()
    ballAnimation()
    
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerVel += 3.5
            if event.key == pygame.K_UP:
                playerVel -= 3.5
            if event.key == pygame.K_TAB:
                secondPlayer = True
            if event.key == pygame.K_s and secondPlayer == True:
                playerTwoVel += 3.5
            if event.key == pygame.K_w and secondPlayer == True:
                playerTwoVel -= 3.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerVel -= 3.5
            if event.key == pygame.K_UP:
                playerVel += 3.5
            if event.key == pygame.K_s and secondPlayer == True:
                playerTwoVel -= 3.5
            if event.key == pygame.K_w and secondPlayer == True:
                playerTwoVel += 3.5
            

    if secondPlayer == True:
        time += 1

    # Visuals
    playerScoreLabel = mainFont.render(f"{playerScore}", 1, (255,255,255))
    timeLabel = mainFont.render(f"{time}", 1, (255,255,255))

    window.fill((0,0,0))
    window.blit(BG, (0,0))
    window.blit(PADDLE, player)
    window.blit(BALL, ball)
    window.blit(BALL, ball2)
    window.blit(BALL, ball3)

    if secondPlayer == False:
        window.blit(playerScoreLabel, (20, 20))

    if secondPlayer == True:
        window.blit(PADDLE, player2)
        window.blit(timeLabel, (20, 20))
    
    pygame.display.update()

    # Display Handling
    clock.tick(60)
            
# If Main Loop Is Killed
pygame.quit()
