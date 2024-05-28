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
        'left_trigger': 0.0,
        'right_trigger': 0.0
    }

    # Button names for Xbox controller
    XBOX_button_names = {
        0: 'A',
        1: 'B',
        2: 'X',
        3: 'Y',
        4: 'Left Bumper',
        5: 'Right Bumper',
        6: 'XBOX Double Screen',
        7: 'XBOX Menu',
        8: 'Left Joystick',
        9: 'Right Joystick',
        10: 'XBOX',
        11: 'Update'
    }

    # Button names for PS5 controller
    PS5_button_names = {
        0: 'Triangle',
        1: 'Circle',
        2: 'Square',
        3: 'Cross',
        4: 'Left Thumbstick button',
        5: 'PS5',
        6: 'Right Thumbstick button',
        7: 'XBOX Menu',
        8: 'Left Stick',
        9: 'L1',
        10: 'R1',
        11: 'Up',
        12: 'Down',
        13: 'Left',
        14: 'Right',
        15: 'D-Pad'
    }

    @staticmethod
    def initialize_joystick():
        """Initialize the joystick subsystem and return the first joystick if available."""
        pygame.joystick.init()  # Reinitialize the joystick subsystem
        joystick_count = pygame.joystick.get_count()
        if joystick_count == 0:
            return None
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        return joystick

    def process_joystick_events(self):
        """Process joystick events and print button presses and axis movements."""
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                # Handle button press
                print(f"{self.PS5_button_names.get(event.button, 'Unknown')} pressed")
            elif event.type == pygame.JOYAXISMOTION:
                # Handle axis movement
                axis_value = event.value
                axis_name = self.get_axis_name(event.axis)
                if axis_name and abs(axis_value - self.last_values[axis_name]) > self.DEAD_ZONE:
                    self.last_values[axis_name] = axis_value
                    axis_human = self.get_human_axis(axis_name)
                    print(f"Axis {axis_human} value: {axis_value:.2f}")
            elif event.type == pygame.JOYHATMOTION:
                # Handle D-Pad movement
                print(f"D-Pad: {event.value}")

    @staticmethod
    def get_axis_name(axis_index):
        """Map axis index to axis name."""
        return {
            0: 'left_x',
            1: 'left_y',
            2: 'right_x',
            3: 'right_y',
            4: 'left_trigger',
            5: 'right_trigger'
        }.get(axis_index, None)
        
    @staticmethod
    def get_human_axis(axis_index):
        """Map axis index to axis name."""
        return {
            'left_x':'Left Joystick Horizontal',
            'left_y': 'Left Joystick Vertical',
            'right_x': 'Right Joystick Horizontal',
            'right_y': 'Right Joystick Vertical',
            'left_trigger': 'Left Sharp Turn',
            'right_trigger': 'Right Sharp Turn'
        }.get(axis_index, None)

def main():
    pygame.init()
    input_reader = InputReader()
    while True:
        joystick = InputReader.initialize_joystick()
        if joystick:
            print(f"Joystick name: {joystick.get_name()}")
            while pygame.joystick.get_count() > 0:
                input_reader.process_joystick_events()
                time.sleep(0.01)  # Adjust sleep time as needed to balance responsiveness and CPU usage
                pygame.joystick.init()  # Reinitialize to check for disconnects
        else:
            print("No joystick connected.")
            pygame.quit()
            pygame.init()
        time.sleep(3)  # Check for joystick reconnection every 3 seconds if none are connected


if __name__ == "__main__":
    main()