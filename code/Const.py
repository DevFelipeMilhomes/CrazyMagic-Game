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
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

COLOR_BAR_HP = {
    'Player': (2, 214, 101),
    'Boss': (201, 18, 18)
}
COLOR_BAR_HP_BACK = {
    'Player': (3, 112, 54),
    'Boss': (110, 11, 11)
}

# Physics
GRAVITY = 0.34
VERTICAL_SPEED = 7

# Spaw characters
FIRST_SPAW = 1920
INTERVAL_SPAW = 2 * SCREEN_WIDTH

# Bar
BAR_HP_MAX = {
    'Player': 300,
    'Boss': 800
}

# Speed
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Player1': 3,
    'Player2': 3,
    'Boss1': 2,
    'Enemy1': 4,
    'Enemy2': 2,
    'Npc1': 1,
    'Npc2': 1,
    'Npc3': 1,
}

# Health
ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Player1': 250,
    'Player': 250,
    'Player2': 250,
    'Boss1': 100,
    'Enemy1': 20,
    'Enemy2': 40,
    'Npc1': 90,
    'Npc2': 90,
    'Npc3': 90,
}

# Images
ENTITY_IMAGE_AMOUNT = {
    'Player1': {
        'Attack1': 4,
        'Attack2': 4,
        'Attack3': 14,
        'Dead': 6,
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
        'Idle': 7,
        'Jump': 9,
        'Run': 8,
        'Shot': 10,
        'ShotAttack': 7
    },
    'Boss1': {
        'Attack1': 16,
        'Attack2': 7,
        'Attack3': 10,
        'Dead': 3,
        'Idle': 7,
        'Run': 7,
    },
    'Enemy1': {
        'Attack1': 5,
        'Dead': 4,
        'Idle': 7,
        'Run': 9,
    },
    'Enemy2': {
        'Attack1': 4,
        'Dead': 6,
        'Idle': 6,
        'Run': 8,
    },
    'Npc1': {
        'Idle': 11,
        'Special': 13
    },
    'Npc2': {
        'Idle': 7,
        'Special': 6
    },
    'Npc3': {
        'Idle': 6,
        'Special': 4
    },
    'Level1Bg': 4,
}

# Action Delay
ACTIONS_DELAY = {
    'Player1': {
        'Jump': 3,
        'frames_idle': 0.12,
        'frames_run': 0.10,
        'frames_jump': 0.15,
        'frames_Attack1': 0.13,
        'frames_Attack2': 0.13,
        'frames_Attack3': 0.13,
        'frames_dead': 0.03,
    },
    'Player2': {
        'Jump': 2,
        'Attack': 1,
        'frames_idle': 0.12,
        'frames_run': 0.10,
        'frames_jump': 0.15,
        'frames_Attack1': 0.18,
        'frames_Attack2': 0.13,
        'frames_Attack3': 0.13,
        'frames_dead': 0.03,
    },
    'Boss1': {
        'Run': 20,
        'Attack': 1,
        'frames_idle': 0.12,
        'frames_run': 0.10,
        'frames_attack1': 0.17,
        'frames_attack2': 0.15,
        'frames_attack3': 0.15,
        'frames_dead': 0.01,
    },
    'Enemy1': {
        'Attack': 2,
        'frames_idle': 0.12,
        'frames_run': 0.18,
        'frames_attack1': 0.12,
        'frames_dead': 0.01,
    },
    'Enemy2': {
        'Attack': 2,
        'frames_idle': 0.12,
        'frames_run': 0.13,
        'frames_attack1': 0.12,
        'frames_dead': 0.05,
    },
    'Npc1': {
        'frames_idle': 0.07,
        'frames_special': 0.20
    },
    'Npc2': {
        'frames_idle': 0.12,
        'frames_special': 0.20
    },
    'Npc3': {
        'frames_idle': 0.12,
        'frames_special': 0.20
    },
    'TextBubble': 4,
}

DISTANCE_ATTACK = {
    'Boss1': 250,
    'Enemy1': 190,
    'Enemy2': 190
}

ENTITY_FACTOR_SIZE = {
    'Boss1': 5,
    'Enemy1': 3,
    'Enemy2': 4
}

# Damage
ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Player1': {
        'Attack1': 10,
        'Attack2': 15,
        'Attack3': 10
    },
    'Player2': {
        'Attack1': 5,
        'Attack2': 24,
        'Attack3': 10
    },
    'Boss1': {
        'Attack1': 4,
        'Attack2': 0,
        'Attack3': 0,
    },
    'Enemy1': {
        'Attack1': 10,
        'Attack2': 0,
        'Attack3': 0,
    },
    'Enemy2': {
        'Attack1': 10,
        'Attack2': 0,
        'Attack3': 0,
    },
    'Npc1': 0,
    'Npc2': 0,
    'Npc3': 0,
}

DAMAGE_FRAME = {
    'Player1': {
        'Attack1': [2],
        'Attack2': [2, 3],
        'Attack3': [4, 5, 6, 7, 8, 9, 10],
    },
    'Player2': {
        'Attack1': [8, 9],
        'Attack2': [2],
        'Attack3': [4, 5, 6, 7, 8, 9, 10],
    },
    'Boss1': {
        'Attack1': [5, 6, 7, 8, 9, 10, 11, 12, 13],
        'Attack2': [-1],
        'Attack3': [-1],
    },
    'Enemy1': {
        'Attack1': [3],
        'Attack2': [-1],
        'Attack3': [-1],
    },
    'Enemy2': {
        'Attack1': [2],
        'Attack2': [-1],
        'Attack3': [-1],
    },

}
