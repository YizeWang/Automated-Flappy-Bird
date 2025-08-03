from game_base.agents import *
from game_base.constants import *
from game_base.game_core import *
from algorithms.pid_controller import *

from pygame.locals import *

import time


pygame.mixer.init()
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), vsync=True)
pygame.display.set_caption("Flappy Bird")

BACKGROUND = pygame.image.load(BACKGROUND_MAP).convert_alpha()
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
WELCOME_PAGE = pygame.image.load(WELCOME_MAP).convert_alpha()

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 24)

bird_group = init_bird_group()
bird = bird_group.sprites()[0]
ground_group = init_ground_group()
pipe_group = init_pipe_group()


clock = pygame.time.Clock()

frame = 0

not_started = True

while not_started:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
            bird.flap()
            pygame.mixer.Sound(FLAP_AUDIO).play()
            not_started = False

    screen.blit(pygame.image.load(WELCOME_MAP).convert_alpha(), (0, 0))
    pygame.display.update()

last_left_to_exit = True

while True:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == K_UP:
                bird.flap()
                pygame.mixer.Sound(FLAP_AUDIO).play()

    screen.blit(BACKGROUND, (0, 0))

    remove_and_create_ground(ground_group)
    remove_and_create_pipes(pipe_group)

    pipe_gap_rects = get_pipe_gap_rects(pipe_group)

    pid_controller = PIDController(kp=0.1, ki=0.0, kd=0.0)

    target_y = pipe_gap_rects[0][1] + pipe_gap_rects[0][3] // 3 * 2
    error = - target_y + bird_group.sprites()[0].rect[1]

    left_to_exit = bird_group.sprites()[0].rect[0] < pipe_gap_rects[0][0] + PIPE_WIDTH
    target_for_new_pipe = last_left_to_exit and not left_to_exit
    pid_controller.update(target_for_new_pipe=target_for_new_pipe, error=error)
    last_left_to_exit = left_to_exit

    if pid_controller.flap():
        bird.flap()
        pygame.mixer.Sound(FLAP_AUDIO).play()

    update_and_draw_groups(screen, [pipe_group, ground_group, bird_group])

    for rect in pipe_gap_rects:
        pygame.draw.rect(screen, RED, rect, 3)

    debug_text = f'Frame: {frame}, Error: {error}, Last: {last_left_to_exit}, Curr: {left_to_exit}, New: {target_for_new_pipe}'

    text = font.render(debug_text, True, GREEN, WHITE)
    textRect = text.get_rect()
    textRect[0] = 0
    textRect[1] = 0

    screen.blit(text, textRect)

    pygame.display.update()

    if (pygame.sprite.groupcollide(bird_group, ground_group, False, False, pygame.sprite.collide_mask) or
            pygame.sprite.groupcollide(bird_group, pipe_group, False, False, pygame.sprite.collide_mask) or
            bird_group.sprites()[0].hit_boundaries()):
        pygame.mixer.Sound(HIT_AUDIO).play()
        time.sleep(1)
        # pygame.mixer.Sound(FAILURE_AUDIO).play()
        break

    frame += 1
