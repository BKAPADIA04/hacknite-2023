import pygame

pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load resources
font = pygame.font.Font(None, 32)
loading_text = font.render("Loading...", True, WHITE)
loading_text_rect = loading_text.get_rect(center=(screen_width/2, screen_height/2))

rocket_image = pygame.image.load("Group 12.png").convert_alpha()
rocket_rect = rocket_image.get_rect(center=(screen_width/2, screen_height/2))

# Display the loading screen
run = True
while run:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update the rocket position
    rocket_rect.y -= 2
    if rocket_rect.top < 0:
        rocket_rect.bottom = screen_height

    # Draw the loading screen
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (100, 550, 600, 20))
    pygame.draw.rect(screen, RED, (100, 550, 600-rocket_rect.y, 20))
    screen.blit(loading_text, loading_text_rect)
    screen.blit(rocket_image, rocket_rect)
    if rocket_rect.y<= 30:
        run = False

    # Update the display
    pygame.display.flip()
    pygame.time.wait(10)
