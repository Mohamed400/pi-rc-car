import pygame
import time

pygame.init()
pygame.joystick.init()

print("Joysticks found:", pygame.joystick.get_count())

if pygame.joystick.get_count() == 0:
    print("No controller detected.")
    exit()

js = pygame.joystick.Joystick(0)
js.init()

print("Connected:", js.get_name())

while True:
    pygame.event.pump()

    print(
        f"LX={js.get_axis(0):+.2f} "
        f"LY={js.get_axis(1):+.2f}",
        end="\r"
    )

    time.sleep(0.05)
