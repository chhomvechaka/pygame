import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Click and Drag")

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Variables for tracking the position and state of the mouse
mouse_pos = (0, 0)
is_dragging = False

# Main game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse movement event
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()

        # Mouse button press event
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                is_dragging = True

        # Mouse button release event
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                is_dragging = False

 

    # Draw onto the screen
    screen.fill((255, 255, 255))  # Fill the screen with white

    # Draw a rectangle at the current mouse position
    if is_dragging:
        pygame.draw.rect(
            screen, RED, (mouse_pos[0] - 25, mouse_pos[1] - 25, 50, 50))
    else:
        pygame.draw.rect(
            screen, BLUE, (mouse_pos[0] - 25, mouse_pos[1] - 25, 50, 50))

    # Draw text based on the mouse state
    if is_dragging:
        text = "Dragging"
        color = GREEN
    else:
        text = "Not Dragging"
        color = RED
        
    font = pygame.font.Font(None, 24)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (10, 10))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
