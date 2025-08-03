from agents import *
from pygame.locals import *
from constants import *
import time
from game_core import *


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

    update_and_draw_groups(screen, [pipe_group, ground_group, bird_group])

    debug_text = f'Frame: {frame}'

    text = font.render(debug_text, True, GREEN, WHITE)
    textRect = text.get_rect()
    textRect[0] = SCREEN_WIDTH // 2
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
