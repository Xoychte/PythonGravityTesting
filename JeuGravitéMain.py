import pygame
from pygame.locals import*
from random import randint
from JeuGravitéForces import *
from math import*

FPS = 60
(windowWidth, windowHeight) = (1500, 1200)

GREY=(30,30,30)
WHITE=(255,255,255)
RED=(255,0,0)
ballRadius = 20
ballX = 20
ballY = ballRadius
g = 9.81
m = 1

hitGround = False
bouncing = False
i = 1

totalForcesX = 0
totalForcesY = 0

speedX = 20
speedY = 0

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((windowWidth, windowHeight), RESIZABLE)
window.fill(WHITE)
font_obj = pygame.font.Font('freesansbold.ttf', 12)

continuer = True

while continuer == True:
    clock.tick(FPS)
    window.fill(GREY)
    mouseX, mouseY =  pygame.mouse.get_pos()
    
    for event in pygame.event.get() :
        if event.type == QUIT:
            continuer = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            print("reset")
            ballX = randint(ballRadius, windowWidth - ballRadius)
            ballY = 20
            hitGround = False
            
    if hitGround == False:
        totalForcesY += pesanteur(m, g)
        print("falling")
    
    if ballY + speedY > windowHeight-ballRadius and hitGround == False:
        print(speedY)
        ballY = windowHeight-ballRadius
        bounce = speedY*7
        speedY = 0
        totalForcesY = 0
        bouncing = True

    
    if bouncing == True and hitGround == False:       
        print(i)
        totalForcesY -= bounce/i
        i+=0.5
        if bounce/i < 4:
            bouncing = False
            print("stopped bouncing")
            i = 1

    if ballY == windowHeight - ballRadius and abs(totalForcesY) < 1 and hitGround == False:
        hitGround = True
        print("hit ground")
        
    if hitGround == True:
        totalForcesY = 0
    
    speedY += totalForcesY * (1/m) * (1/60)
    totalForcesY = 0
    
    #temp
    if ballX < ballRadius or ballX > windowWidth - ballRadius:
        speedX = -speedX
    
    ballX += speedX
    ballY += speedY
    
    pygame.draw.circle(window, RED, (ballX, ballY), ballRadius)
    pygame.display.flip()
    

pygame.quit()