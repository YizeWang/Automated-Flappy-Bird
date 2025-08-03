# Game Parameters
FPS = 60
X_SPEED = 5

# Window parameters
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# Bird parameters
FLAP_Y_SPEED = 8
Y_GRAVITY = 0.5
BIRD_INIT_Y_POS = SCREEN_HEIGHT / 2
BIRD_X_POS = SCREEN_WIDTH / 6

# Ground parameters
GROUND_WIDTH = 2 * SCREEN_WIDTH
GROUND_HEIGHT = 100

# Pipe parameters
PIPE_WIDTH = 80
PIPE_HEIGHT = 500
PIPE_GAP_MAX = 200
PIPE_GAP_MIN = 120
PIPE_MAX_HEIGHT = 300
PIPE_MIN_HEIGHT = GROUND_HEIGHT
PIPE_X_DISTANCE = 400

# Audio files
FLAP_AUDIO = 'game_base/assets/audio/flap.wav'
HIT_AUDIO = 'game_base/assets/audio/hit.wav'
FAILURE_AUDIO = 'game_base/assets/audio/failure.wav'

# Map files
BACKGROUND_MAP = 'game_base/assets/images/background-day.png'
WELCOME_MAP = 'game_base/assets/images/welcome-page.png'
BLUEBIRD_DOWNFLAP_MAP = 'game_base/assets/images/blue-bird-down-flap.png'
BLUEBIRD_MIDFLAP_MAP = 'game_base/assets/images/blue-bird-middle-flap.png'
BLUEBIRD_UPFLAP_MAP = 'game_base/assets/images/blue-bird-up-flap.png'
PIPE_MAP = 'game_base/assets/images/green-pipe.png'
GROUND_MAP = 'game_base/assets/images/ground.png'

# Colors
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
