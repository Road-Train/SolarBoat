import pygame
import time

# Initialize threshold and last sent values
DEAD_ZONE = 0.01
last_values = {
    'left_x': 0.0,
    'left_y': 0.0,
    'right_x': 0.0,
    'right_y': 0.0
}

def initialize_joystick():
    pygame.joystick.init()  # Reinitialize the joystick subsystem
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        return None
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    return joystick

def process_joystick_events(joystick):
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} pressed")
        elif event.type == pygame.JOYBUTTONUP:
            print(f"Button {event.button} released")
        elif event.type == pygame.JOYAXISMOTION:
            axis_value = event.value
            axis_index = event.axis
            
            if axis_index == 0:
                axis_name = 'left_x'
            elif axis_index == 1:
                axis_name = 'left_y'
            elif axis_index == 2:
                axis_name = 'right_x'
            elif axis_index == 3:
                axis_name = 'right_y'
            else:
                continue
            
            if abs(axis_value - last_values[axis_name]) > DEAD_ZONE:
                last_values[axis_name] = axis_value
                print(f"Axis {axis_name} value: {axis_value:.2f}")
        elif event.type == pygame.JOYHATMOTION:
            print(f"Hat {event.hat} value: {event.value}")

def main():
    pygame.init()
    while True:
        joystick = initialize_joystick()
        if joystick:
            print(f"Joystick name: {joystick.get_name()}")
            while pygame.joystick.get_count() > 0:
                process_joystick_events(joystick)
                time.sleep(0.01)  # Adjust sleep time as needed to balance responsiveness and CPU usage
                pygame.joystick.init()  # Reinitialize to check for disconnects
        else:
            print("No joystick connected.")
            pygame.quit()
            pygame.init()
        time.sleep(3)  # Check for joystick reconnection every second if none are connected

if __name__ == "__main__":
    main()
