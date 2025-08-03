from agents import *
from pygame.locals import *
from constants import *
import time
import pygame


def update_and_draw_groups(screen: pygame.Surface, groups: list[pygame.sprite.Group]):
    for group in groups:
        group.update()
        group.draw(screen)


def init_bird_group() -> pygame.sprite.Group:
    bird_group = pygame.sprite.Group()
    bird_group.add(Bird())
    return bird_group


def init_ground_group() -> pygame.sprite.Group:
    ground_group = pygame.sprite.Group()
    ground_group.add([Ground(GROUND_WIDTH * i) for i in range(2)])
    return ground_group


def init_pipe_group() -> pygame.sprite.Group:
    pipe_group = pygame.sprite.Group()
    pipe_group.add([get_random_pipes(SCREEN_WIDTH + i * PIPE_X_DISTANCE) for i in range(SCREEN_WIDTH // PIPE_X_DISTANCE)])
    return pipe_group


def remove_and_create_ground(ground_group: pygame.sprite.Group) -> None:
    if is_off_screen(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])
        ground_group.add(Ground(GROUND_WIDTH - 20))


def remove_and_create_pipes(pipe_group: pygame.sprite.Group) -> None:
    if is_off_screen(pipe_group.sprites()[0]):
        pipe_group.remove(pipe_group.sprites()[0])
        pipe_group.remove(pipe_group.sprites()[0])
        pipe_group.add(get_random_pipes(SCREEN_WIDTH))