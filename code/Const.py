# Screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Menu texts
MENU_OPTION = (
    'NEW GAME',
    'SCORE',
    'EXIT'
)

PLAYER_OPTION = (
    'FELIPE',
    'YASMIN'
)

PLAYER_OPTION_POSITION = {
    'FELIPE': 320,
    'YASMIN': 760
}

LEVEL_OPTION = (
    'Level1',
    'Level2',
    'Level3'
)

# Colors
TEXT_MENU_C = (255, 255, 255)
TEXT_MENU_C_SELECT = (24, 204, 72)
COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0,0,0)

# Speed
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Player1': 3,
    'Player2': 1,
}

# Health
ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Player1': 500,
    'Player2': 500,
}

# Damage
ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Player1': 50,
    'Player2': 500,
}

# Images
ENTITY_IMAGE_AMOUNT = {
    'Player1': {
        'Attack1': 4,
        'Attack2': 4,
        'Attack3': 14,
        'Dead': 6,
        'Hurt': 3,
        'Idle': 7,
        'Jump': 10,
        'Run': 8,
        'Shot': 12,
        'ShotAttack': 8
    },
    'Player2': {
        'Attack1': 10,
        'Attack2': 4,
        'Attack3': 13,
        'Dead': 5,
        'Hurt': 3,
        'Idle': 7,
        'Jump': 9,
        'Run': 8,
        'Shot': 10,
        'ShotAttack': 7
    },
    'Level1Bg': 4,
}

# Physics
GRAVITY = 0.34
VERTICAL_SPEED = 7

# Action Delay
ACTIONS_DELAY = {
    'Player1': {
        'Attack': 20,
        'Jump': 3,
        'frames_idle': 0.12,
        'frames_run': 0.10,
        'frames_jump': 0.15,
        'frames_attack1': 0.13
    },
    'Player2': {
        'Attack': 20,
        'Jump': 2,
        'frames_idle': 0.12,
        'frames_run': 0.10,
        'frames_jump': 0.15,
        'frames_attack1': 0.20
    }
}
