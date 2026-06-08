import pygame
import time

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No controller found")
    quit()

js = pygame.joystick.Joystick(0)
js.init()

print("Controller:", js.get_name())
print("Axes:", js.get_numaxes())
print("Buttons:", js.get_numbuttons())

while True:
    pygame.event.pump()

    print("\n--------------------")

    for i in range(js.get_numaxes()):
        print(f"Axis {i}: {js.get_axis(i):+.3f}")

    for i in range(js.get_numbuttons()):
        if js.get_button(i):
            print(f"Button {i}: PRESSED")

    time.sleep(0.2)

