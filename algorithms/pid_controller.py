from pygame.locals import *


class PIDController:

    def __init__(self, kp: float, ki: float, kd: float):
        self.u = 0.0
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral = 0.0
        self.derivative = 0.0
        self.last_error = 0.0

    def update(self, target_for_new_pipe: bool, error: float) -> None:
        if target_for_new_pipe:
            self.reset()

        self.integral += error
        self.derivative = error - self.last_error
        self.last_error = error

        self.u = self.kp * error + self.ki * self.integral + self.kd * self.derivative

    def reset(self) -> None:
        self.u = 0.0
        self.integral = 0
        self.derivative = 0
        self.last_error = 0

    def flap(self) -> bool:
        return self.u > 1.0
