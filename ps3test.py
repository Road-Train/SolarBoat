import pygame
import sys
import time
from pygame.locals import *

pygame.init()
pygame.joystick.init()

# Set up the display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World')

# Set the interval for the loop
interval = 0.01

# Get joystick details
joystick_count = pygame.joystick.get_count()
print("Joystick count:", joystick_count)
print("--------------")

if joystick_count == 0:
    print("No joysticks found. Please connect a joystick and try again.")
    pygame.quit()
    sys.exit()

# Initialize the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()
print("Initialised Joystick : %s" % joystick.get_name())

#numaxes = joystick.get_numaxes()
#print("Number of axes:", numaxes)
#print("--------------")

#numbuttons = joystick.get_numbuttons()
#print("Number of buttons:", numbuttons)
#print("--------------")

loopQuit = False
while not loopQuit:
    # Test controller buttons
    #outstr = ""
    #for i in range(numbuttons):
    #    button = joystick.get_button(i)
    #    outstr += str(i) + ":" + str(button) + "|"
    #print(outstr)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            loopQuit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loopQuit = True

    # Other event tests (commented out)
    if event.type == pygame.JOYBUTTONDOWN:
        print("Joy button down")
    if event.type == pygame.JOYBUTTONUP:
        print("Joy button up")
    if event.type == pygame.JOYBALLMOTION:
        print("Joy ball motion")
    if event.type == pygame.JOYAXISMOTION:
        print("Joy axis motion")

    pygame.display.update()
    time.sleep(interval)

pygame.quit()
sys.exit()