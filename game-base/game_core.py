from agents import *
from pygame.locals import *
from constants import *
import time
import pygame


def get_random_pipes(xpos: int) -> list[Pipe]:
    pipe_gap = random.randint(PIPE_GAP_MIN, PIPE_GAP_MAX)
    bottom_pipe_height = random.randint(PIPE_MIN_HEIGHT, PIPE_MAX_HEIGHT)
    top_pipe_height = SCREEN_HEIGHT - bottom_pipe_height - pipe_gap
    bottom_pipe = Pipe(inverted=False, x_pos=xpos, y_size=bottom_pipe_height)
    top_pipe = Pipe(inverted=True, x_pos=xpos, y_size=top_pipe_height)
    return [bottom_pipe, top_pipe]


def is_off_screen(sprite) -> bool:
    return (sprite.rect[0] + sprite.rect[2] < 0)


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


def get_pipe_gap_rects(pipe_group: pygame.sprite.Group) -> list[pygame.Rect]:
    pipe_gap_rects = []
    for i in range(len(pipe_group.sprites()) // 2):
        bottom_pipe = pipe_group.sprites()[i * 2]
        top_pipe = pipe_group.sprites()[i * 2 + 1]
        bottom_left = (bottom_pipe.rect[0], bottom_pipe.rect[1])
        top_left = (top_pipe.rect[0], top_pipe.rect[1] + PIPE_HEIGHT)
        pipe_gap_rect = pygame.Rect(
            bottom_left[0], top_left[1], PIPE_WIDTH, bottom_left[1] - top_left[1])
        pipe_gap_rects.append(pipe_gap_rect)
    return pipe_gap_rects
