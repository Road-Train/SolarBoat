import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
OCEAN = (79, 66, 181)

# Player attributes
PLAYER_SIZE = 100
PLAYER_SPEED = 5

# Target attributes
TARGET_SIZE = 50

# Font for displaying score
font = pygame.font.Font(None, 36)

def load_image(file, width, height):
    """Load and scale an image."""
    image = pygame.image.load(file)
    return pygame.transform.scale(image, (width, height))

class Player:
    def __init__(self, image):
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.score = 0
        self.angle = 0

    def move(self, x, y):
        self.rect.x += x * PLAYER_SPEED
        self.rect.y += y * PLAYER_SPEED
        self.rect.x = max(0, min(SCREEN_WIDTH - PLAYER_SIZE, self.rect.x))
        self.rect.y = max(0, min(SCREEN_HEIGHT - PLAYER_SIZE, self.rect.y))

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

class Target:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.randomize_position()

    def randomize_position(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - TARGET_SIZE)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - TARGET_SIZE)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

def display_message(screen, message, font, color, position):
    """Display a message on the screen."""
    text = font.render(message, True, color)
    screen.blit(text, position)

def show_intro(screen, font):
    """Show the introduction screen."""
    screen.fill(OCEAN)
    instructions = [
        "Check Control Movements On The Boat",
        "Use the left thumbstick to move the player.",
        "Use the right thumbstick to also move the player.",
        "Press 'Circle' to show quit confirmation.",
        "Press 'Cross' to confirm quit.",
        "Press any button to start."
    ]
    y_offset = 100
    for instruction in instructions:
        display_message(screen, instruction, font, WHITE, (50, y_offset))
        y_offset += 50
    pygame.display.flip()
    wait_for_start()

def wait_for_start():
    """Wait for the player to press any button to start."""
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.KEYDOWN:
                waiting = False
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

def run():
    pygame.joystick.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("How To Control Boat With Controller")
    
    player_image = load_image("solarboat-demo.png", PLAYER_SIZE, PLAYER_SIZE)
    target_image = load_image("finish.png", TARGET_SIZE, TARGET_SIZE)
    
    player = Player(player_image)
    target = Target(target_image)
    joystick = None
    last_print_time = 0
    print_delay = 0.5
    total_distance = 0
    start_time = time.time()
    elapsed_time = 0
    movement_message = ""

    pygame.joystick.init()
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
    else:
        print("No joystick connected.")
        pygame.quit()
        return

    show_intro(screen, font)

    running = True
    while running:
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if confirm_quit(screen, font, joystick):
                    running = False
            elif event.type == pygame.JOYBUTTONDOWN:
                if joystick.get_button(1):  # Circle button
                    if confirm_quit(screen, font, joystick):
                        running = False

        if joystick:
            # Combine left and right thumbsticks for movement
            x_axis = joystick.get_axis(0) + joystick.get_axis(2)
            y_axis = joystick.get_axis(1) + joystick.get_axis(3)
            player.move(x_axis, y_axis)

            if current_time - last_print_time > print_delay:
                if abs(x_axis) > 0.01 or abs(y_axis) > 0.01:
                    movement_distance = (x_axis**2 + y_axis**2) ** 0.5
                    total_distance += movement_distance
                    #print(f"Movement: X={x_axis:.2f}, Y={y_axis:.2f}")
                    movement_message = (f"Movement: X={x_axis:.2f}, Y={y_axis:.2f}")
                    last_print_time = current_time
                    elapsed_time = time.time() - current_time

        if player.rect.colliderect(target.rect):
            player.score += 1
            target.randomize_position()
            
        # Convert elapsed time to hours, minutes, and seconds
        hours = int(elapsed_time / 3600)
        minutes = int((elapsed_time % 3600) / 60)
        seconds = int(elapsed_time % 60)
        time_string = f"{hours:02}:{minutes:02}:{seconds:02}" # Format the elapsed time as a string
                
        screen.fill(OCEAN)
        player.draw(screen)
        target.draw(screen)
        display_message(screen, f"Score: {player.score}", font, WHITE, (10, 10))
        display_message(screen, f"Time: {time_string}", font, WHITE, (10, 90)) # Display the elapsed time
        display_message(screen, f"{movement_message}", font, WHITE, (10, 130)) # Display the movements 
        display_message(screen, f"Total Distance: {total_distance/1000:.4f} km", font, WHITE, (10, 50))

        pygame.display.flip()

    pygame.quit()

def confirm_quit(screen, font, joystick):
    """Show quit confirmation and return True if the player confirms, False otherwise."""
    screen.fill(OCEAN)
    display_message(screen, "Do you really want to quit?", font, WHITE, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
    display_message(screen, "Yes OR No", font, WHITE, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if joystick.get_button(0):  # Cross button
                    return True
                if joystick.get_button(1):  # Circle button
                    return False
            elif event.type == pygame.QUIT:
                pygame.quit()
                exit()

if __name__ == "__main__":
    run()
