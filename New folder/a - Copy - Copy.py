'''import pygame

pygame.init()
pygame.joystick.init()

# Get the number of available game controllers
num_joysticks = pygame.joystick.get_count()

if num_joysticks > 0:
    # Initialize the first game controller
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    # Print the name of the game controller
    print(f"Using game controller: {joystick.get_name()}")

while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} pressed")
        elif event.type == pygame.JOYBUTTONUP:
            print(f"Button {event.button} released")
        elif event.type == pygame.JOYAXISMOTION:
            print(f"Axis {event.axis} moved to {event.value}")
'''
