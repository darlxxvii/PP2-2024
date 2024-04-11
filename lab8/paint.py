import pygame

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((500, 500))

# Set the initial color
color = (0, 0, 0)

# Run until the user asks to quit
running = True
drawing = False
mode = "draw"  # Can be "draw", "rectangle", "circle", or "eraser"

while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mode == "draw":
                drawing = True
                pygame.draw.circle(screen, color, event.pos, 2)
            elif mode == "rectangle":
                start_pos = event.pos
            elif mode == "circle":
                center_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if mode == "rectangle":
                end_pos = event.pos
                pygame.draw.rect(screen, color, (start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])))
            elif mode == "circle":
                radius = int(((center_pos[0] - event.pos[0]) ** 2 + (center_pos[1] - event.pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, color, center_pos, radius)
            drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing and mode == "draw":
                pygame.draw.circle(screen, color, event.pos, 5)
            elif mode == "eraser":
                pygame.draw.circle(screen, (0, 0, 0), event.pos, 10)

        # Change modes based on key presses
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rectangle"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_d:
                mode = "draw"
            elif event.key == pygame.K_1:
                color = (255, 0, 0)  # Red
            elif event.key == pygame.K_2:
                color = (0, 255, 0)  # Green
            elif event.key == pygame.K_3:
                color = (0, 0, 255)  # Blue

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
'''
Press r to switch to rectangle drawing mode.
Press c to switch to circle drawing mode. 
Press e to switch to eraser mode.
Press d to switch back to drawing mode.
Press 1, 2, or 3 to change the color to red, green, or blue.
'''