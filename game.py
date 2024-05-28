import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player attributes
PLAYER_SIZE = 50
PLAYER_COLOR = GREEN
PLAYER_SPEED = 5

# Target attributes
TARGET_SIZE = 30
TARGET_COLOR = RED

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Controller Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Font for displaying score
font = pygame.font.Font(None, 36)

# Player class
class Player:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE)
        self.score = 0

    def move(self, x, y):
        self.rect.x += x * PLAYER_SPEED
        self.rect.y += y * PLAYER_SPEED
        # Prevent the player from moving out of the screen
        self.rect.x = max(0, min(SCREEN_WIDTH - PLAYER_SIZE, self.rect.x))
        self.rect.y = max(0, min(SCREEN_HEIGHT - PLAYER_SIZE, self.rect.y))

    def draw(self, surface):
        pygame.draw.rect(surface, PLAYER_COLOR, self.rect)

# Target class
class Target:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - TARGET_SIZE),
                                random.randint(0, SCREEN_HEIGHT - TARGET_SIZE),
                                TARGET_SIZE, TARGET_SIZE)

    def draw(self, surface):
        pygame.draw.ellipse(surface, TARGET_COLOR, self.rect)

# Main function
def main():
    player = Player()
    target = Target()
    joystick = None

    # Initialize joystick
    pygame.joystick.init()
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
    else:
        print("No joystick connected.")
        pygame.quit()
        return

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if joystick:
            x_axis = joystick.get_axis(0)
            y_axis = joystick.get_axis(1)
            player.move(x_axis, y_axis)

        # Check for collision with the target
        if player.rect.colliderect(target.rect):
            player.score += 1
            target = Target()

        # Draw everything
        screen.fill(WHITE)
        player.draw(screen)
        target.draw(screen)

        # Display score
        score_text = font.render(f"Score: {player.score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()