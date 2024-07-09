
import pygame
import time


class InputReader:
    # Initialize threshold and last sent values
    DEAD_ZONE = 0.01
    last_values = {
        'left_x': 0.0,
        'left_y': 0.0,
        'right_x': 0.0,
        'right_y': 0.0,
        'left_trigger':0.0,
        'right_trigger':0.0
    }
    button_names = {
        0:'A',
        1:'B',
        2:'X',
        3:'Y',
        4:'Left Bumper',
        5:'Right Bumper',
        6:'Double Screen',
        7:'Menu',
        8:'Left Joystick',
        9:'Right Joystick',
        10:'XBOX',
        11:'Upload'
    }
    def initialize_joystick():
        pygame.joystick.init()  # Reinitialize the joystick subsystem
        joystick_count = pygame.joystick.get_count()
        if joystick_count == 0:
            return None
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        return joystick

    def process_joystick_events(self):
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                print(f"{self.button_names[event.button]} pressed")

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
                elif axis_index == 4:
                    axis_name = 'left_trigger'
                elif axis_index == 5:
                    axis_name = 'right_trigger'
                else:
                    continue
                
                if abs(axis_value - self.last_values[axis_name]) > self.DEAD_ZONE:
                    self.last_values[axis_name] = axis_value
                    print(f"Axis {axis_name} value: {axis_value:.2f}")
            elif event.type == pygame.JOYHATMOTION:
                print(f"D-Pad: {event.value}")

def main():
    pygame.init()
    while True:
        joystick = InputReader.initialize_joystick()
        if joystick:
            print(f"Joystick name: {joystick.get_name()}")
            while pygame.joystick.get_count() > 0:
                InputReader.process_joystick_events(InputReader)
                time.sleep(0.01)  # Adjust sleep time as needed to balance responsiveness and CPU usage
                pygame.joystick.init()  # Reinitialize to check for disconnects
        else:
            print("No joystick connected.")
            pygame.quit()
            pygame.init()
        time.sleep(3)   # Check for joystick reconnection every second if none are connected

if __name__ == "__main__":
    main()
