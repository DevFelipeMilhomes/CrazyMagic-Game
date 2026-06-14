from pygame import Rect, Surface

from code.Const import SCREEN_WIDTH, ENTITY_SPEED
from code.Entity import Entity
import pygame as py

BG_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 2,
    'Level1Bg2': 3,
    'Level1Bg3': 4,
}


class Background(Entity):
    def __init__(self, name,position, dirname: str, typeBg: str):
        super().__init__(name, position, dirname)
        img = py.image.load(f'./assets/Background/{dirname}/{name}.png').convert_alpha()
        img = py.transform.scale_by(img, 2)
        self.image: Surface = img
        self.rect: Rect = self.image.get_rect(left=position[0], top=position[1])
        self.typeBg = typeBg
        self.speed = BG_SPEED[self.name]

    def move(self):
        pressed_key = py.key.get_pressed()

        if pressed_key[py.K_RIGHT]:
            if self.typeBg == 'end':
                if self.rect.right <= SCREEN_WIDTH+5:
                    for i in range(len(BG_SPEED)):
                        BG_SPEED[f'{self.dirname}{i}'] = 0
                else:
                    for i in range(len(BG_SPEED)):
                        BG_SPEED[f'{self.dirname}{i}'] = 0 + i*1 +1
                    self.speed = BG_SPEED[self.name]
                    self.rect.centerx -= self.speed
            else:
                self.speed = BG_SPEED[self.name]
                self.rect.centerx -= self.speed

        if pressed_key[py.K_LEFT]:
            if self.typeBg == 'init':
                if self.rect.left >= -5:
                    for i in range(len(BG_SPEED)):
                        BG_SPEED[f'{self.dirname}{i}'] = 0
                else:
                    for i in range(len(BG_SPEED)):
                        BG_SPEED[f'{self.dirname}{i}'] = 0 + i*1 +1
                    self.speed = BG_SPEED[self.name]
                    self.rect.centerx += self.speed
            else:
                self.speed = BG_SPEED[self.name]
                self.rect.centerx += self.speed

    def update(self):
        pass