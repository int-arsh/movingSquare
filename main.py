import pygame
import sys
import asyncio

# Initialize Pygame
pygame.init()

# Set up the game window
window_size = (400, 400)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Simple Pygame Example")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

async def main():
    # Square properties
    square_size = 50
    square_x = 175  # Initial x position of the square
    square_y = 175  # Initial y position of the square
    speed_x = 5
    speed_y = 5

    # Game loop
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move the square
        square_x += speed_x
        square_y += speed_y

        # Bounce the square off the edges
        if square_x <= 0 or square_x >= window_size[0] - square_size:
            speed_x = -speed_x
        if square_y <= 0 or square_y >= window_size[1] - square_size:
            speed_y = -speed_y

        # Fill the screen with white
        screen.fill(WHITE)

        # Draw the square
        pygame.draw.rect(screen, BLUE, (square_x, square_y, square_size, square_size))

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(60)

        # Yield control to allow other tasks to run
        await asyncio.sleep(0)

    pygame.quit()
    sys.exit()

# Run the async main function
asyncio.run(main())
