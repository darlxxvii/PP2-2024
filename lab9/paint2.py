import pygame
import sys
import math

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Set the initial color
color = (0, 0, 0)

# Run until the user asks to quit
running = True
drawing = False
mode = "draw"  # Can be "draw", "rectangle", "circle", "square", "right_triangle", "equilateral_triangle", "rhombus", or "eraser"

while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mode == "draw":
                drawing = True
                pygame.draw.circle(screen, color, event.pos, 5)
            elif mode in ["rectangle", "square", "right_triangle", "equilateral_triangle", "rhombus"]:
                start_pos = event.pos
            elif mode == "circle":
                center_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if mode == "rectangle":
                end_pos = event.pos
                pygame.draw.rect(screen, color, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])))
            elif mode == "square":
                end_pos = event.pos
                side_length = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                pygame.draw.rect(screen, color, pygame.Rect(start_pos, (side_length, side_length)))
            elif mode == "right_triangle":
                end_pos = event.pos
                pygame.draw.polygon(screen, color, [start_pos, (start_pos[0], end_pos[1]), end_pos])
            elif mode == "equilateral_triangle":
                end_pos = event.pos
                height = abs(end_pos[1] - start_pos[1])
                pygame.draw.polygon(screen, color, [start_pos, (start_pos[0] + height * math.sqrt(3) / 2, start_pos[1]), (start_pos[0] + height * math.sqrt(3) / 4, end_pos[1])])
            elif mode == "rhombus":
                end_pos = event.pos
                dx = abs(end_pos[0] - start_pos[0])
                dy = abs(end_pos[1] - start_pos[1])
                pygame.draw.polygon(screen, color, [start_pos, (start_pos[0] + dx / 2, start_pos[1] - dy), (start_pos[0] + dx, start_pos[1]), (start_pos[0] + dx / 2, start_pos[1] + dy)])
            elif mode == "circle":
                radius = int(((center_pos[0] - event.pos[0]) ** 2 + (center_pos[1] - event.pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, color, center_pos, radius)
            drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing and mode == "draw":
                pygame.draw.circle(screen, color, event.pos, 5)
            elif mode == "eraser":
                pygame.draw.circle(screen, (255, 255, 255), event.pos, 10)

        # Change modes based on key presses
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rectangle"
            elif event.key == pygame.K_s:
                mode = "square"
            elif event.key == pygame.K_t:
                mode = "right_triangle"
            elif event.key == pygame.K_q:
                mode = "equilateral_triangle"
            elif event.key == pygame.K_h:
                mode = "rhombus"
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

    pygame.display.flip()

pygame.quit()
