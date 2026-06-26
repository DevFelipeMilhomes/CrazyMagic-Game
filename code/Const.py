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

ENTITY_POSITION = {
    'Player1': (SCREEN_WIDTH / 2 - 200, 456),
    'Player2': (SCREEN_WIDTH / 2 - 200, 456),
}

# Colors
TEXT_MENU_C = (255, 255, 255)
TEXT_MENU_C_SELECT = (24, 204, 72)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

COLOR_BAR_HP = {
    'Player': (7, 199, 4),
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
    'Shot': 8,
    'Potion': 1,
}

# Health
ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Player1': 250,
    'Player2': 250,
    'Boss1': 350,
    'Enemy1': 30,
    'Enemy2': 50,
    'Npc1': 90,
    'Npc2': 90,
    'Npc3': 90,
    'Shot': 1,
    'Potion': 1,
}

HEALTH_VARIABLE = {
    'Player': {
        '1': 250,
        '2': 300,
        '3': 350
    },
    'Boss': {
        '1': 350
    },
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
        'frames_Idle': 0.12,
        'frames_Run': 0.10,
        'frames_Jump': 0.15,
        'frames_Attack1': 0.13,
        'frames_Attack2': 0.13,
        'frames_Attack3': 0.13,
        'frames_ShotAttack': 0.15,
        'frames_Shot': 0.15,
        'frames_Dead': 0.05,
    },
    'Player2': {
        'Jump': 2,
        'Attack': 1,
        'frames_Idle': 0.12,
        'frames_Run': 0.10,
        'frames_Jump': 0.15,
        'frames_Attack1': 0.18,
        'frames_Attack2': 0.14,
        'frames_Attack3': 0.13,
        'frames_ShotAttack': 0.15,
        'frames_Shot': 0.15,
        'frames_Dead': 0.05,
    },
    'Boss1': {
        'Run': 20,
        'Attack': 1,
        'frames_Idle': 0.12,
        'frames_Run': 0.10,
        'frames_Attack1': 0.17,
        'frames_Attack2': 0.15,
        'frames_Attack3': 0.13,
        'frames_Dead': 0.01,
    },
    'Enemy1': {
        'Attack': 2,
        'frames_Idle': 0.12,
        'frames_Run': 0.18,
        'frames_Attack1': 0.15,
        'frames_Dead': 0.03,
    },
    'Enemy2': {
        'Attack': 2,
        'frames_Idle': 0.12,
        'frames_Run': 0.13,
        'frames_Attack1': 0.15,
        'frames_Dead': 0.07,
    },
    'Npc1': {
        'frames_Idle': 0.04,
        'frames_Special': 0.20
    },
    'Npc2': {
        'frames_Idle': 0.12,
        'frames_Special': 0.20
    },
    'Npc3': {
        'frames_Idle': 0.12,
        'frames_Special': 0.20
    },
    'TextBubble': 1,
}

DISTANCE_ATTACK = {
    'Boss1': 300,
    'Enemy1': 190,
    'Enemy2': 190,
    'Npc1': 500,
    'Npc2': 500,
    'Npc3': 500,
}

ENTITY_FACTOR_SIZE = {
    'Boss1': 5,
    'Enemy1': 3,
    'Enemy2': 4
}

INTERVAL_MOVE_POTION = {
    'min': 640,
    'max': 670
}

# Damage
ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Shot': 1,
    'Player1': {
        'Attack1': 10,
        'Attack2': 15,
        'Attack3': 10,
        'Shot': 1,
    },
    'Player2': {
        'Attack1': 5,
        'Attack2': 24,
        'Attack3': 10,
        'Shot': 1,
    },
    'Boss1': {
        'Attack1': 5,
        'Attack2': 10,
        'Attack3': 12,
    },
    'Enemy1': {
        'Attack1': 5,
        'Attack2': 0,
        'Attack3': 0,
    },
    'Enemy2': {
        'Attack1': 7,
        'Attack2': 0,
        'Attack3': 0,
    },
    'Npc1': 0,
    'Npc2': 0,
    'Npc3': 0,
    'Potion': 0,
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
        'Attack2': [3, 4],
        'Attack3': [6, 7, 8, 9],
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
    'Shot': {
        'Attack1': [-1],
        'Attack2': [-1],
        'Attack3': [-1],
    }
}

PLAYER_SPEECHES = {
    'Player1': {
        'Npc1': [
            "Felipe:\nPensou: ''esse maluco quebrou o goró'' \nCalma cara, só quero uma informação",
            "Felipe:\nVocê viu um cara todo de preto por aqui?",
            "Felipe:\nEsse mesmo, para onde ele foi?",
            "Felipe:\nObrigado de verdade, e...\nVe se da uma maneirada na bebida e no cigarro",
        ],
        'Npc2': [
            "Felipe:\nSai dai doido, com essas ideias\nQuem é tu tatu?",
            "Felipe:\nE você quer que eu faça o que?",
            "Felipe:\nTu acha mesmo que vou tomar uma porção\n de um maluco aleatório em uma floresta?",
        ],
        'Npc3': [
            "Felipe:\nPensa numa floresta que ter gente doida...",
            "Felipe:\nE quem é essa?\nPelo nome não da medo não",
            "Felipe:\nDe novo com isso\nAs pessoas daqui são preparadas"
        ],

    },
    'Player2': {
        'Npc1': [
            "Yasmin:\nPensou: ''esse maluco quebrou o goró'' \nCalma cara, só quero uma informação",
            "Yasmin:\nVocê viu um cara todo de preto por aqui?",
            "Yasmin:\nEsse mesmo, para onde ele foi?",
            "Yasmin:\nObrigado de verdade, e...\nVe se da uma maneirada na bebida e no cigarro",
        ],
        'Npc2': [
            "Yasmin:\nClaro que vou...\nEu sirvo cunt",
            "Yasmin:\nTa dizendo que só por que sou mulher não vou conseguir?\nE você quer que eu faça o que?",
            "Yasmin:\nTu acha mesmo que vou tomar uma porção\n de um maluco aleatório em uma floresta?",
        ],
        'Npc3': [
            "Yasmin:\nFraquinha? O que...\nSò por que sou mulher?",
            "Yasmin:\nE quem é essa?\nPelo nome não da medo não",
            "Yasmin:\nDe novo com isso\nAs pessoas daqui são preparadas"
        ]

    },

}

NPC_SPEECHES = {
    'Player1': {
        'Npc1': [
            'Breno:\nQuem é você?\nNão vai roubar meu goró!',
            'Breno:\nEntão tudo bem',
            "Breno:\nO que tava sequestrando uma mulher?",
            "Breno:\nApenas mais um dia normal por aqui...\nPode seguir reto que você encontra ele",
        ],
        'Npc2': [
            'Lindomar:\nAi cara será que eu poderia ver a sua espada?',
            'Lindomar:\nÉ uma boa lamina...\nMas não vai ir muito longe nessa floresta\n se usar apenas um tipo de ataque',
            "Lindomar:\nBebe essa parada ai...\nÉ bom demaizeee",
        ],
        'Npc3': [
            "Alexandre:\nTu ta bem fraquinho ein...",
            "Alexandre:\nSe seguir enfrente desse jeito, vai morrer fácil para\nAntônia...",
            "Alexandre:\nÉ o demônio em 'pessoa'\nMas pega isso ai que vai ser easy",
        ],
    },
    'Player2': {
        'Npc1': [
            'Breno:\nQuem é você?\nNão vai roubar meu goró!',
            'Breno:\nEntão tudo bem',
            "Breno:\nO que tava sequestrando uma Homem?",
            "Breno:\nApenas mais um dia normal por aqui...\nPode seguir reto que você encontra ele",
        ],
        'Npc2': [
            'Lindomar:\nVocê ai...\nAté que tem um bom ataque, mas não vai ir muito longe',
            'Lindomar:\nCom apenas um ataque?...\nTem um bixo medonho vindo ai',
            "Lindomar:\nBebe essa parada ai...\nÉ bom demaizeee",
        ],
        'Npc3': [
            "Alexandre:\nTu ta bem fraquinha ein...",
            "Alexandre:\nSe seguir enfrente desse jeito, vai morrer fácil para\nAntônia...",
            "Alexandre:\nÉ o demônio em 'pessoa'\nMas pega isso ai mona que vai ser easy",
        ],
    },
}

SPEECHES_AMOUNT = {
    'Npc1': 4,
    'Npc2': 3,
    'Npc3': 3,
}
