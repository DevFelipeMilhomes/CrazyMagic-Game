from time import sleep

from pygame import Surface, Rect

from code.Character import Character
from code.Const import ENTITY_IMAGE_AMOUNT, SCREEN_HEIGHT, SCREEN_WIDTH
import pygame as py


class Player(Character):
    def __init__(self, name, position, dirname):
        super().__init__(name, position, dirname)
        self.idle = []
        for i in range(ENTITY_IMAGE_AMOUNT[name]['Idle']):
            img = py.image.load(f'./assets/{dirname}/{name}/Idle/Idle{i}.png').convert_alpha()
            img = py.transform.scale_by(img, 4)
            self.idle.append(img)
        self.run = []
        for i in range(ENTITY_IMAGE_AMOUNT[name]['Run']):
            img = py.image.load(f'./assets/{dirname}/{name}/Run/Run{i}.png').convert_alpha()
            img = py.transform.scale_by(img, 4)
            self.run.append(img)
        self.jump = []
        for i in range(ENTITY_IMAGE_AMOUNT[name]['Jump']):
            img = py.image.load(f'./assets/{dirname}/{name}/Jump/Jump{i}.png').convert_alpha()
            img = py.transform.scale_by(img, 4)
            self.jump.append(img)
        self.hurt = []
        for i in range(ENTITY_IMAGE_AMOUNT[name]['Hurt']):
            img = py.image.load(f'./assets/{dirname}/{name}/Hurt/Hurt{i}.png').convert_alpha()
            img = py.transform.scale_by(img, 4)
            self.hurt.append(img)
        self.dead = []
        for i in range(ENTITY_IMAGE_AMOUNT[name]['Dead']):
            img = py.image.load(f'./assets/{dirname}/{name}/Dead/Dead{i}.png').convert_alpha()
            img = py.transform.scale_by(img, 4)
            self.dead.append(img)
        self.attack1 = []
        for i in range(ENTITY_IMAGE_AMOUNT[name]['Attack1']):
            img = py.image.load(f'./assets/{dirname}/{name}/Attack1/Attack{i}.png').convert_alpha()
            img = py.transform.scale_by(img, 4)
            self.attack1.append(img)
        self.attack2 = []
        for i in range(ENTITY_IMAGE_AMOUNT[name]['Attack2']):
            img = py.image.load(f'./assets/{dirname}/{name}/Attack2/Attack{i}.png').convert_alpha()
            img = py.transform.scale_by(img, 4)
            self.attack2.append(img)
        self.attack3 = []
        for i in range(ENTITY_IMAGE_AMOUNT[name]['Attack3']):
            img = py.image.load(f'./assets/{dirname}/{name}/Attack3/Attack{i}.png').convert_alpha()
            img = py.transform.scale_by(img, 4)
            self.attack3.append(img)
        self.shot_attack = []
        for i in range(ENTITY_IMAGE_AMOUNT[name]['ShotAttack']):
            img = py.image.load(f'./assets/{dirname}/{name}/ShotAttack/Attack{i}.png').convert_alpha()
            img = py.transform.scale_by(img, 4)
            self.shot_attack.append(img)

        self.actual = 0

        self.image: Surface = self.idle[self.actual]
        self.rect: Rect = self.image.get_rect(left=position[0], top=position[1])

        self.direction = 'R'

    def update(self):
        self.actual += 0.10
        if self.actual >= ENTITY_IMAGE_AMOUNT[self.name]['Idle']:
            self.actual = 0
        if self.direction == 'R':
            self.image = self.idle[int(self.actual)]
        else:
            self.image = self.idle[int(self.actual)]
            self.image = py.transform.flip(self.image, True, False)

    def move(self):

        key_pressed = py.key.get_pressed()

        key_press = py.key.get_just_pressed()

        if key_pressed[py.K_RIGHT]:
            self.actual += 0.10
            if self.actual >= ENTITY_IMAGE_AMOUNT[self.name]['Run']:
                self.actual = 0
            self.image = self.run[int(self.actual)]
            self.direction = 'R'

        if key_pressed[py.K_LEFT]:
            self.actual += 0.10
            if self.actual >= ENTITY_IMAGE_AMOUNT[self.name]['Run']:
                self.actual = 0
            self.image = self.run[int(self.actual)]
            self.image = py.transform.flip(self.image, True, False)
            self.direction = 'L'

            if key_pressed[py.K_UP]:
                self.actual += 0.05
                if self.actual >= ENTITY_IMAGE_AMOUNT[self.name]['Jump']:
                    self.actual = 0

                if self.actual >= ENTITY_IMAGE_AMOUNT[self.name]['Jump'] / 2:
                    self.rect.centery -= 1
                else:
                    self.rect.centery += 1

                self.image = self.jump[int(self.actual)]
