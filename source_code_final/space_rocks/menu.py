import pygame

pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Game Menu')

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the text for the options
start_text = font.render('Start Game', True, (255, 255, 255))
quit_text = font.render('Quit Game', True, (255, 255, 255))

# Get the text dimensions
start_text_width, start_text_height = font.size('Start Game')
quit_text_width, quit_text_height = font.size('Quit Game')

# Position the text in the center of the screen
start_text_x = (window_width - start_text_width) // 2
start_text_y = (window_height - start_text_height) // 2 - 50
quit_text_x = (window_width - quit_text_width) // 2
quit_text_y = (window_height - quit_text_height) // 2 + 50

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked on the "Start Game" button
            if start_text_rect.collidepoint(event.pos):
                # Start the game
                running = False
            # Check if the user clicked on the "Quit Game" button
            elif quit_text_rect.collidepoint(event.pos):
                # Quit the game
                pygame.quit()

    # Draw the text on the screen
    start_text_rect = window.blit(start_text, (start_text_x, start_text_y))
    quit_text_rect = window.blit(quit_text, (quit_text_x, quit_text_y))

    # Update the screen
    pygame.display.flip()

pygame.quit()