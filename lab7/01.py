import pygame
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 1200, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

seconds = pygame.image.load("left_hand.png")
minutes = pygame.image.load("right_hand.png")

background = pygame.image.load("mainclock.png")
background = pygame.transform.scale(background, (1200, 900))  

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    now = datetime.now()
    minute_time = now.minute 
    second_time = now.second

    minute_angle = -minute_time * 6 
    second_angle = -second_time * 6 

    rotated_minutes = pygame.transform.rotate(minutes, minute_angle)
    rotated_seconds = pygame.transform.rotate(seconds, second_angle)

    screen.blit(background, (0, -70))
    screen.blit(rotated_minutes, (600 - rotated_minutes.get_width()//2, 380 - rotated_minutes.get_height()//2))  
    screen.blit(rotated_seconds, (600 - rotated_seconds.get_width()//2-3, 380 - rotated_seconds.get_height()//2)) 
    pygame.display.flip()
