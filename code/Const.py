# Screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Menu texts
MENU_OPTION = (
    'NOVO JOGO',
    'RANKING',
    'SAIR'
)

PLAYER_OPTION = (
    'Voltar',
    'FELIPE',
    'YASMIN'
)

PLAYER_OPTION_POSITION = {
    'Voltar': 0,
    'FELIPE': 320,
    'YASMIN': 760
}

LEVEL_OPTION = (
    'Voltar',
    'Level1',
    'Level2',
    'Level3',
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
COLOR_YELLOW = (232, 190, 5)

COLOR_BAR_HP = {
    'Player': (7, 199, 4),
    'Boss': (201, 18, 18),
    'Energy': (7, 160, 237),
}
COLOR_BAR_HP_BACK = {
    'Player': (3, 112, 54),
    'Boss': (110, 11, 11),
    'Energy': (1, 58, 87)
}

ENERGY_ENTITY = {
    'Player': 300
}

POWER_ENERGY = {
    'Shot': 60,
    'Attack3': 200
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
    'Level1Bg1': 2,
    'Level1Bg2': 3,
    'Level1Bg3': 4,

    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 1,
    'Level2Bg3': 2,
    'Level2Bg4': 2,
    'Level2Bg5': 2,
    'Level2Bg6': 3,
    'Level2Bg7': 3,
    'Level2Bg8': 4,
    'Level2Bg9': 4,

    'Level3Bg0': 0,
    'Level3Bg1': 1,
    'Level3Bg2': 1,
    'Level3Bg3': 2,
    'Level3Bg4': 2,
    'Level3Bg5': 3,
    'Level3Bg6': 4,

    'Player1': 3,
    'Player2': 3,
    'Boss1': 2,
    'Boss2_1': 2,
    'Boss2_2': 2,
    'Boss3': 2,
    'Enemy1': 4,
    'Enemy2': 2,
    'Enemy3': 2,
    'Enemy4': 3,
    'Enemy5': 3,
    'Enemy6': 2,
    'Npc1': 1,
    'Npc2': 1,
    'Npc3': 1,
    'Npc4': 1,
    'Npc5': 1,
    'Npc6': 1,
    'Npc7': 1,
    'Shot': 8,
    'Shot2': 8,
    'Potion': 1,
}

# Health
ENTITY_HEALTH = {
    'Level1Bg0': 99,
    'Level1Bg1': 99,
    'Level1Bg2': 99,
    'Level1Bg3': 99,
    'Level2Bg0': 99,
    'Level2Bg1': 99,
    'Level2Bg2': 99,
    'Level2Bg3': 99,
    'Level2Bg4': 99,
    'Level2Bg5': 99,
    'Level2Bg6': 99,
    'Level2Bg7': 99,
    'Level2Bg8': 99,
    'Level2Bg9': 99,
    'Level3Bg0': 99,
    'Level3Bg1': 99,
    'Level3Bg2': 99,
    'Level3Bg3': 99,
    'Level3Bg4': 99,
    'Level3Bg5': 99,
    'Level3Bg6': 99,
    'Player1': 250,
    'Player2': 250,
    'Boss1': 350,
    'Boss2_1': 350,
    'Boss2_2': 350,
    'Boss3': 400,
    'Enemy1': 30,
    'Enemy2': 50,
    'Enemy3': 80,
    'Enemy4': 80,
    'Enemy5': 80,
    'Enemy6': 80,
    'Npc1': 90,
    'Npc2': 90,
    'Npc3': 90,
    'Npc4': 90,
    'Npc5': 90,
    'Npc6': 90,
    'Npc7': 90,
    'Shot': 1,
    'Shot2': 1,
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

ENERGY_VARIABLE = {
    'Player': {
        '1': 300,
        '2': 350,
    }
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
    'Boss2_1': {
        'Attack1': 5,
        'Dead': 5,
        'Idle': 10,
        'Run': 11,
    },
    'Boss2_2': {
        'Attack1': 5,
        'Dead': 5,
        'Idle': 10,
        'Run': 11,
    },
    'Boss3': {
        'Attack1': 7,
        'Attack2': 7,
        'Attack3': 6,
        'Dead': 4,
        'Idle': 8,
        'Run': 8,
        'Shot': 5,
        'Shot2': 9
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
    'Enemy3': {
        'Attack1': 3,
        'Dead': 6,
        'Idle': 6,
        'Run': 8,
    },
    'Enemy4': {
        'Attack1': 11,
        'Dead': 3,
        'Idle': 7,
        'Run': 7,
    },
    'Enemy5': {
        'Attack1': 4,
        'Dead': 4,
        'Idle': 7,
        'Run': 8,
    },
    'Enemy6': {
        'Attack1': 8,
        'Dead': 4,
        'Idle': 7,
        'Run': 12,
        'Shot': 8,
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
    'Npc4': {
        'Idle': 10,
        'Special': 16
    },
    'Npc5': {
        'Idle': 6,
        'Special': 4
    },
    'Npc6': {
        'Idle': 11,
        'Special': 3
    },
    'Npc7': {
        'Idle': 10,
        'Special': 8
    },
    'Level1Bg': 4,
    'Level2Bg': 10,
    'Level3Bg': 7,
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
    'Boss2_1': {
        'Run': 20,
        'Attack': 1,
        'frames_Idle': 0.12,
        'frames_Run': 0.10,
        'frames_Attack1': 0.17,
        'frames_Dead': 0.05,
    },
    'Boss2_2': {
        'Run': 20,
        'Attack': 1,
        'frames_Idle': 0.12,
        'frames_Run': 0.10,
        'frames_Attack1': 0.17,
        'frames_Dead': 0.05,
    },
    'Boss3': {
        'Jump': 2,
        'Attack': 1,
        'frames_Idle': 0.12,
        'frames_Run': 0.10,
        'frames_Attack1': 0.18,
        'frames_Attack2': 0.14,
        'frames_Attack3': 0.13,
        'frames_Shot': 0.15,
        'frames_Dead': 0.05,
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
    'Enemy3': {
        'Attack': 2,
        'frames_Idle': 0.12,
        'frames_Run': 0.18,
        'frames_Attack1': 0.15,
        'frames_Dead': 0.07,
    },
    'Enemy4': {
        'Attack': 2,
        'frames_Idle': 0.12,
        'frames_Run': 0.13,
        'frames_Attack1': 0.15,
        'frames_Dead': 0.07,
    },
    'Enemy5': {
        'Attack': 2,
        'frames_Idle': 0.12,
        'frames_Run': 0.18,
        'frames_Attack1': 0.15,
        'frames_Dead': 0.03,
    },
    'Enemy6': {
        'Attack': 2,
        'frames_Idle': 0.12,
        'frames_Run': 0.13,
        'frames_Attack1': 0.15,
        'frames_Shot': 0.15,
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
    'Npc4': {
        'frames_Idle': 0.08,
        'frames_Special': 0.20
    },
    'Npc5': {
        'frames_Idle': 0.12,
        'frames_Special': 0.20
    },
    'Npc6': {
        'frames_Idle': 0.12,
        'frames_Special': 0.20
    },
    'Npc7': {
        'frames_Idle': 0.08,
        'frames_Special': 0.15
    },
    'TextBubble': 1,
    'Energy': 4,
}

DISTANCE_ATTACK = {
    'Boss1': 250,
    'Boss2_1': 230,
    'Boss2_2': 230,
    'Boss3': 400,
    'Enemy1': 190,
    'Enemy2': 190,
    'Enemy3': 190,
    'Enemy4': 190,
    'Enemy5': 190,
    'Enemy6': 500,
    'Npc1': 500,
    'Npc2': 500,
    'Npc3': 500,
    'Npc4': 500,
    'Npc5': 500,
    'Npc6': 500,
    'Npc7': 500,
    'Player1': 300,
    'Player2': 300
}

ENTITY_FACTOR_SIZE = {
    'Boss1': 5,
    'Boss2_1': 4,
    'Boss2_2': 4,
    'Boss3': 4,
    'Enemy1': 3,
    'Enemy2': 4,
    'Enemy3': 4,
    'Enemy4': 4,
    'Enemy5': 4,
    'Enemy6': 4,
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
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Level2Bg6': 0,
    'Level2Bg7': 0,
    'Level2Bg8': 0,
    'Level2Bg9': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Level3Bg4': 0,
    'Level3Bg5': 0,
    'Level3Bg6': 0,
    'Shot': 1,
    'Shot2': 1,
    'Player1': {
        'Attack1': 10,
        'Attack2': 16,
        'Attack3': 14,
        'Shot': 30,
    },
    'Player2': {
        'Attack1': 5,
        'Attack2': 32,
        'Attack3': 14,
        'Shot': 30,
    },
    'Boss1': {
        'Attack1': 5,
        'Attack2': 10,
        'Attack3': 12,
    },
    'Boss2_1': {
        'Attack1': 15,
        'Attack2': 0,
        'Attack3': 0,
    },
    'Boss2_2': {
        'Attack1': 15,
        'Attack2': 0,
        'Attack3': 0,
    },
    'Boss3': {
        'Attack1': 12,
        'Attack2': 0,
        'Attack3': 0,
        'Shot': 25,
        'Shot2': 25,
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
    'Enemy3': {
        'Attack1': 5,
        'Attack2': 0,
        'Attack3': 0,
    },
    'Enemy4': {
        'Attack1': 7,
        'Attack2': 0,
        'Attack3': 0,
    },
    'Enemy5': {
        'Attack1': 5,
        'Attack2': 0,
        'Attack3': 0,
    },
    'Enemy6': {
        'Attack1': 7,
        'Attack2': 0,
        'Attack3': 0,
        'Shot': 20
    },
    'Npc1': 0,
    'Npc2': 0,
    'Npc3': 0,
    'Npc4': 0,
    'Npc5': 0,
    'Npc6': 0,
    'Npc7': 0,
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
    'Boss2_1': {
        'Attack1': [3],
        'Attack2': [-1],
        'Attack3': [-1],
    },
    'Boss2_2': {
        'Attack1': [3],
        'Attack2': [-1],
        'Attack3': [-1],
    },
    'Boss3': {
        'Attack1': [3, 4, 5],
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
    'Enemy3': {
        'Attack1': [1],
        'Attack2': [-1],
        'Attack3': [-1],
    },
    'Enemy4': {
        'Attack1': [5, 6, 7, 8, 9, 10, 11, 12, 13],
        'Attack2': [-1],
        'Attack3': [-1],
    },
    'Enemy5': {
        'Attack1': [2],
        'Attack2': [-1],
        'Attack3': [-1],
    },
    'Enemy6': {
        'Attack1': [-1],
        'Attack2': [-1],
        'Attack3': [-1],
    },
    'Shot': {
        'Attack1': [-1],
        'Attack2': [-1],
        'Attack3': [-1],
    },
    'Shot2': {
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
        'Npc4': [
            "Felipe:\nEstou tranquilo, quero nada não",
            "Felipe:\nNão, a ultima vez que eu tomei isso...\n acordei na tumba do faraó",
            "Felipe:\nEsse cara é bom, sempre tem de tudo",
        ],
        'Npc5': [
            "Felipe:\nQuem é desse vez?",
            "Felipe:\nDe novo isso?\nNão vai vir com mais uma porção né?",
            "Felipe:\nO criador desse jogo precisa de mais criatividade.",
        ],
        'Npc6': [
            "Felipe:\nNão é todo dia que se luta com medusas, minotauros...",
            "Felipe:\nPor que tu fica gemendo?",
            "Felipe:\nParece que ele não aprende",
        ],
        'Npc7': [
            "Felipe:\nQuem é esse doido, o que que ele esta falando.",
            "Felipe:\nCara que brisa é essa?",
            "Felipe:\nSabias palavras",
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
        ],
        'Npc4': [
            "Yasmin:\nTem o kit de pele da principia?",
            "Yasmin:\nEntão não vou levar nada não",
            "Yasmin:\nVamos ver no que vai dar"
        ],
        'Npc5': [
            "Yasmin:\nQuem é desse vez?",
            "Yasmin:\nDe novo isso?\nNão vai vir com mais uma porção né?",
            "Yasmin:\nO criador desse jogo precisa de mais criatividade.",
        ],
        'Npc6': [
            "Yasmin:\nNão é todo dia que se luta com medusas, minotauros...",
            "Yasmin:\nPor que tu fica gemendo?",
            "Felipe:\nParece que ele não aprende",
        ],
        'Npc7': [
            "Yasmin:\nQuem é esse doido, o que que ele esta falando.",
            "Yasmin:\nCara que brisa é essa?",
            "Yasmin:\nSabias palavras",
        ],

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
        'Npc4': [
            "Joab:\nVai ser o que hoje meu patrão?\nTem de tudo um pouco",
            "Joab:\nNão vai levar nada?\nNem o sulco gástrico do dragão da colina?.",
            "Joab:\nEntão tome pelo menos o básico\nPegue essa porção de atirar fogo",
        ],
        'Npc5': [
            "José:\nEi você ai...",
            "José:\nVocê vai enfrentar os chifrudos fraco assim?",
            "José:\nPega mais uma porção ai só para não perder o costume",
        ],
        'Npc6': [
            "Nicolas:\nParece que a vida hummm não ta fácil parceiro",
            "Nicolas:\nSei como é hummmmm, quer uma ajudinha? humm.",
            "Nicolas:\nPega isso ai que vai lhe ajudar hummm.",
        ],
        'Npc7': [
            "Mateus:\nAi, você sabia que o numero 3, esta presente\n em todo o universo",
            "Mateus:\nO numero mais importante da história\n apreciar algo 3 vezes é mais que suficiente",
            "Mateus:\n2 vezes você não mata a vontade... 4 você entre no vicio\n 3 é o numero perfeito\n enfim pega mais uma porção ai....",
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
        'Npc4': [
            "Joab:\nVai ser o que hoje minha patroa?\nTem de tudo um pouco",
            "Joab:\nNão eu só trabalho com o básico.",
            "Joab:\nEntão, por conta da casa\nPegue essa porção de atirar bolas de raio",
        ],
        'Npc5': [
            "José:\nEi você ai...",
            "José:\nVocê vai enfrentar os chifrudos fraca assim?",
            "José:\nPega mais uma porção ai só para não perder o costume",
        ],
        'Npc6': [
            "Nicolas:\nParece que a vida hummm não ta fácil parceiro",
            "Nicolas:\nSei como é hummmmm, quer uma ajudinha? humm.",
            "Nicolas:\nPega isso ai que vai lhe ajudar hummm.",
        ],
        'Npc7': [
            "Mateus:\nAi, você sabia que o numero 3, esta presente\n em todo o universo",
            "Mateus:\nO numero mais importante da história\n apreciar algo 3 vezes é mais que suficiente",
            "Mateus:\n2 vezes você não mata a vontade... 4 você entre no vicio\n 3 é o numero perfeito\n enfim pega mais uma porção ai....",
        ],
    },
}

SPEECHES_AMOUNT = {
    'Npc1': 4,
    'Npc2': 3,
    'Npc3': 3,
    'Npc4': 3,
    'Npc5': 3,
    'Npc6': 3,
    'Npc7': 3,
}
