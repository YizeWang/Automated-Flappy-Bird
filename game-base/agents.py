import pygame
import random
import time
from constants import *
from pygame.locals import *


class Bird(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        images = [BLUEBIRD_DOWNFLAP_MAP, BLUEBIRD_MIDFLAP_MAP, BLUEBIRD_UPFLAP_MAP]
        self.images = [pygame.image.load(image).convert_alpha() for image in images]

        self.y_speed = 0

        self.image = self.images[0]
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = BIRD_X_POS
        self.rect[1] = BIRD_INIT_Y_POS

    def update(self, frame: int):
        self.image = self.images[frame % len(self.images)]
        self.y_speed += Y_GRAVITY
        self.rect[1] += self.y_speed

    def flap(self):
        self.y_speed = -FLAP_Y_SPEED


class Pipe(pygame.sprite.Sprite):

    def __init__(self, inverted: bool, x_pos: int, y_size: int):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(PIPE_MAP).convert_alpha()
        self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, PIPE_HEIGHT))

        self.rect = self.image.get_rect()
        self.rect[0] = x_pos

        if inverted:
            self.image = pygame.transform.flip(self.image, flip_x=False, flip_y=True)
            self.rect[1] = y_size - self.rect[3]
        else:
            self.rect[1] = SCREEN_HEIGHT - y_size

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect[0] -= X_SPEED


def get_random_pipes(xpos: int) -> list[Pipe]:
    bottom_pipe_height = random.randint(PIPE_MIN_HEIGHT, PIPE_MAX_HEIGHT)
    top_pipe_height = SCREEN_HEIGHT - bottom_pipe_height - PIPE_GAP
    bottom_pipe = Pipe(inverted=False, x_pos=xpos, y_size=bottom_pipe_height)
    top_pipe = Pipe(inverted=True, x_pos=xpos, y_size=top_pipe_height)
    return [bottom_pipe, top_pipe]


class Ground(pygame.sprite.Sprite):

    def __init__(self, xpos: int):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(GROUND_MAP).convert_alpha()
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = SCREEN_HEIGHT - GROUND_HEIGHT

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect[0] -= X_SPEED


def is_off_screen(sprite) -> bool:
    return (sprite.rect[0] + sprite.rect[2] < 0)
