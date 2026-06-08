import pygame


class PS4Controller:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()

        if pygame.joystick.get_count() == 0:
            raise RuntimeError("No controller detected")

        self.joy = pygame.joystick.Joystick(0)
        self.joy.init()

        print(f"Connected: {self.joy.get_name()}")

    def update(self):
        pygame.event.pump()

    def steering(self):
        return self.joy.get_axis(0)

    def throttle(self):
        r2 = self.joy.get_axis(5)
        l2 = self.joy.get_axis(2)

        forward = (r2 + 1) / 2
        reverse = (l2 + 1) / 2

        return forward - reverse


if __name__ == "__main__":
    import time

    controller = PS4Controller()

    while True:
        controller.update()

        print(
            f"Steering={controller.steering():+.2f}  "
            f"Throttle={controller.throttle():+.2f}"
        )

        time.sleep(0.1)
