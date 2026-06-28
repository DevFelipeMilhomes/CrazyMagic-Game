from pygame import Rect, Surface

from code.Const import SCREEN_WIDTH, ENTITY_SPEED, ENTITY_IMAGE_AMOUNT
from code.Entity import Entity
import pygame as py

BG_SPEED = {
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
}


class Background(Entity):
    def __init__(self, name, position, dirname: str, type_bg: str):
        super().__init__(name, position, dirname)
        img = py.image.load(f'./assets/Background/{dirname}/{name}.png').convert_alpha()
        img = py.transform.scale_by(img, 2)
        self.image: Surface = img
        self.rect: Rect = self.image.get_rect(left=position[0], top=position[1])
        self.typeBg = type_bg
        self.speed = BG_SPEED[self.name]
        self.is_talk = False

    def move(self):
        pressed_key = py.key.get_pressed()

        if not self.is_talk:
            if pressed_key[py.K_RIGHT]:
                if self.typeBg == 'end':
                    if self.rect.right <= SCREEN_WIDTH + 5:
                        for i in range(ENTITY_IMAGE_AMOUNT[self.dirname]):
                            BG_SPEED[f'{self.dirname}{i}'] = 0
                    else:
                        for i in range(ENTITY_IMAGE_AMOUNT[self.dirname]):
                            BG_SPEED[f'{self.dirname}{i}'] = ENTITY_SPEED[f'{self.dirname}{i}']
                        self.speed = BG_SPEED[self.name]
                        self.rect.centerx -= self.speed
                else:
                    self.speed = BG_SPEED[self.name]
                    self.rect.centerx -= self.speed

            if pressed_key[py.K_LEFT]:
                if self.typeBg == 'init':
                    if self.rect.left >= -5:
                        for i in range(ENTITY_IMAGE_AMOUNT[self.dirname]):
                            BG_SPEED[f'{self.dirname}{i}'] = 0
                    else:
                        for i in range(ENTITY_IMAGE_AMOUNT[self.dirname]):
                            BG_SPEED[f'{self.dirname}{i}'] = ENTITY_SPEED[f'{self.dirname}{i}']
                        self.speed = BG_SPEED[self.name]
                        self.rect.centerx += self.speed
                else:
                    self.speed = BG_SPEED[self.name]
                    self.rect.centerx += self.speed

    def update(self):
        pass

    def verify_talk(self):
        pass
