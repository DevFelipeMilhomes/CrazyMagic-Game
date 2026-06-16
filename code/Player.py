from time import sleep

from pygame import Surface, Rect

from code.Character import Character
from code.Const import ENTITY_IMAGE_AMOUNT, SCREEN_HEIGHT, SCREEN_WIDTH, ACTIONS_DELAY, VERTICAL_SPEED, GRAVITY
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

        self.is_jumping = False
        self.is_idle = True
        self.is_attack1 = False
        self.attack_delay = ACTIONS_DELAY[self.name]['Attack']
        self.vertical_speed = VERTICAL_SPEED
        self.gravity = GRAVITY
        self.jump_delay = ACTIONS_DELAY[self.name]['Jump']

    def update(self):

        if self.is_idle:
            self.actual += ACTIONS_DELAY[self.name]['frames_idle']
            if self.actual >= ENTITY_IMAGE_AMOUNT[self.name]['Idle']:
                self.actual = 0
            if self.direction == 'R':
                self.image = self.idle[int(self.actual)]
                self.update_rect(self.image)
            else:
                self.image = self.idle[int(self.actual)]
                self.update_rect(self.image)
                self.image = py.transform.flip(self.image, True, False)

        elif self.is_jumping:
            self.actual += ACTIONS_DELAY[self.name]['frames_jump']
            if self.actual >= ENTITY_IMAGE_AMOUNT[self.name]['Jump']:
                self.actual = 0
                self.vertical_speed = VERTICAL_SPEED
                self.gravity = GRAVITY
                self.is_jumping = False
                self.is_idle = True
            if self.direction == 'R':
                bottom_previous = self.rect.bottom
                self.image = self.jump[int(self.actual)]
                self.rect = self.image.get_rect(left=SCREEN_WIDTH / 2 - 200)
                self.rect.bottom = bottom_previous
                if self.jump.index(self.image) >= self.jump_delay:
                    self.rect.centery -= self.vertical_speed
                    self.vertical_speed -= self.gravity
            else:
                bottom_previous = self.rect.bottom
                self.image = self.jump[int(self.actual)]
                self.rect = self.image.get_rect(left=SCREEN_WIDTH / 2 - 200)
                self.rect.bottom = bottom_previous
                if self.jump.index(self.image) >= self.jump_delay:
                    self.rect.centery -= self.vertical_speed
                    self.vertical_speed -= self.gravity
                self.image = py.transform.flip(self.image, True, False)

        elif self.is_attack1:
            self.actual += ACTIONS_DELAY[self.name]['frames_attack1']
            if self.actual >= ENTITY_IMAGE_AMOUNT[self.name]['Attack1']:
                self.actual = 0
                self.is_attack1 = False
                self.is_idle = True
            if self.direction == 'R':
                self.image = self.attack1[int(self.actual)]
                self.update_rect(self.image)
            else:
                self.image = self.attack1[int(self.actual)]
                self.update_rect(self.image)
                self.image = py.transform.flip(self.image, True, False)


    def move(self):

        key_pressed = py.key.get_pressed()

        if key_pressed[py.K_RIGHT] and not self.is_jumping and not self.is_attack1:
            self.actual += ACTIONS_DELAY[self.name]['frames_run']
            if self.actual >= ENTITY_IMAGE_AMOUNT[self.name]['Run']:
                self.actual = 0
            self.image = self.run[int(self.actual)]
            self.update_rect(self.image)
            self.direction = 'R'

        if key_pressed[py.K_LEFT] and not self.is_jumping and not self.is_attack1:
            self.actual += ACTIONS_DELAY[self.name]['frames_run']
            if self.actual >= ENTITY_IMAGE_AMOUNT[self.name]['Run']:
                self.actual = 0
            self.image = self.run[int(self.actual)]
            self.update_rect(self.image)
            self.image = py.transform.flip(self.image, True, False)
            self.direction = 'L'


    def just_move(self):
        key_pressed = py.key.get_just_pressed()

        if key_pressed[py.K_UP]:
            if self.is_idle:
                self.actual = 0
                self.is_jumping = True
                self.is_idle = False
                self.is_attack1 = False
        if key_pressed[py.K_a]:
            if self.is_idle:
                self.actual = 0
                self.is_jumping = False
                self.is_idle = False
                self.is_attack1 = True


    def update_rect(self, image: Surface):
        position_previous = self.rect.right
        self.rect = image.get_rect(left=SCREEN_WIDTH / 2 - 200)
        self.rect.bottom = SCREEN_HEIGHT
        if self.direction == 'L':
            self.rect.right = position_previous
