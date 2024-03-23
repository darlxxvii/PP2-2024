"""Draw circle - a red ball of size 50 x 50 (radius = 25) on white background. When user presses Up, 
Down, Left, Right arrow keys on keyboard, the ball should move by 20 pixels in the direction of pressed 
key. The ball should not leave the screen, i.e. user input that leads the ball to leave of the screen
should be ignored"""
import pygame 

pygame.init()

res= width, height=500,500
screen= pygame.display.set_mode(res)
white=(255,255,255)

def ball(x,y):
    pygame.draw.circle(screen,(255,0,0),(x,y),25)

x, y=0, 0 #initial points of the ball
v = 20 #velocity
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                x+=v
            elif event.key==pygame.K_LEFT:
                x-=v
            if event.key==pygame.K_UP:
                y-=v
            elif event.key==pygame.K_DOWN:
                y+=v
        
    if x < 25:
        x = 25
    elif x > width - 25:
        x = width - 25
    if y < 25:
        y = 25
    elif y > height - 25:
        y = height - 25

    
    screen.fill(white)
    ball(x,y)
    pygame.display.update()
pygame.quit()
    