import pygame as py
from pygame import Surface, Rect

from code.Character import Character
from code.Const import ENTITY_IMAGE_AMOUNT, ACTIONS_DELAY, SCREEN_HEIGHT, ENTITY_FACTOR_SIZE


class Enemy(Character):
    def __init__(self, name, position, dirname):
        super().__init__(name, position, dirname)
        self.idle = []
        for i in range(ENTITY_IMAGE_AMOUNT[name]['Idle']):
            img = py.image.load(f'./assets/{dirname}/{name}/Idle/Idle{i}.png').convert_alpha()
            img = py.transform.scale_by(img, ENTITY_FACTOR_SIZE[self.name])
            self.idle.append(img)
        self.run = []
        for i in range(ENTITY_IMAGE_AMOUNT[name]['Run']):
            img = py.image.load(f'./assets/{dirname}/{name}/Run/Run{i}.png').convert_alpha()
            img = py.transform.scale_by(img, ENTITY_FACTOR_SIZE[self.name])
            self.run.append(img)
        self.dead = []
        for i in range(ENTITY_IMAGE_AMOUNT[name]['Dead']):
            img = py.image.load(f'./assets/{dirname}/{name}/Dead/Dead{i}.png').convert_alpha()
            img = py.transform.scale_by(img, ENTITY_FACTOR_SIZE[self.name])
            self.dead.append(img)
        self.attack1 = []
        for i in range(ENTITY_IMAGE_AMOUNT[name]['Attack1']):
            img = py.image.load(f'./assets/{dirname}/{name}/Attack1/Attack{i}.png').convert_alpha()
            img = py.transform.scale_by(img, ENTITY_FACTOR_SIZE[self.name])
            self.attack1.append(img)
        if self.name in ('Boss1', 'Boss3'):
            self.attack2 = []
            for i in range(ENTITY_IMAGE_AMOUNT[name]['Attack2']):
                img = py.image.load(f'./assets/{dirname}/{name}/Attack2/Attack{i}.png').convert_alpha()
                img = py.transform.scale_by(img, ENTITY_FACTOR_SIZE[self.name])
                self.attack2.append(img)
            self.attack3 = []
            for i in range(ENTITY_IMAGE_AMOUNT[name]['Attack3']):
                img = py.image.load(f'./assets/{dirname}/{name}/Attack3/Attack{i}.png').convert_alpha()
                img = py.transform.scale_by(img, ENTITY_FACTOR_SIZE[self.name])
                self.attack3.append(img)

        self.actual = 0

        self.image: Surface = self.idle[self.actual]
        self.rect: Rect = self.image.get_rect(left=position[0], top=position[1])

        self.direction = 'L'

        self.is_idle = True
        self.is_attack1 = False
        self.attack1_dmg = 0
        self.attack2_dmg = 0
        self.attack3_dmg = 0
        self.act = False
        self.is_hurt = False
        self.is_dead = False
        self.attack_delay = ACTIONS_DELAY[self.name]['Attack']
        self.active_bar_health = False

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
                self.image = py.transform.flip(self.image, True, False)
                self.update_rect(self.image)
        elif self.is_attack1:
            self.attack_delay -= 1
            if self.attack_delay == 0:
                self.attack_delay = ACTIONS_DELAY[self.name]['Attack']
                self.actual += ACTIONS_DELAY[self.name]['frames_attack1']
                if self.actual >= ENTITY_IMAGE_AMOUNT[self.name]['Attack1']:
                    self.attack1_dmg = 0
                    self.actual = 0
                    self.is_attack1 = False
                    self.is_idle = True
                    self.attack1_dmg = 0
                if self.direction == 'R':
                    self.attack1_dmg += 1
                    self.image = self.attack1[int(self.actual)]
                    if self.is_hurt:
                        self.image = self.hurt(self.attack1[int(self.actual)],255)
                        self.is_hurt = False
                    self.update_rect(self.image)
                else:
                    self.attack1_dmg += 1
                    self.image = self.attack1[int(self.actual)]
                    if self.is_hurt:
                        self.image = self.hurt(self.attack1[int(self.actual)],255)
                        self.is_hurt = False
                    self.image = py.transform.flip(self.image, True, False)
                    self.update_rect(self.image)
        elif self.act:
            self.actual += ACTIONS_DELAY[self.name]['frames_run']
            if self.actual >= ENTITY_IMAGE_AMOUNT[self.name]['Run']:
                self.actual = 0
            if self.direction == 'R':
                self.image = self.run[int(self.actual)]
                if self.is_hurt:
                    self.image = self.hurt(self.run[int(self.actual)], 255)
                    self.is_hurt = False
                self.update_rect(self.image)
                self.rect.centerx += self.speed
            else:
                self.image = self.run[int(self.actual)]
                if self.is_hurt:
                    self.image = self.hurt(self.run[int(self.actual)], 255)
                    self.is_hurt = False
                self.image = py.transform.flip(self.image, True, False)
                self.update_rect(self.image)
                self.rect.centerx -= self.speed
        elif self.is_dead:

            self.actual += ACTIONS_DELAY[self.name]['frames_dead']
            if self.actual >= ENTITY_IMAGE_AMOUNT[self.name]['Dead']:
                self.actual = 0
                self.is_dead = True
                self.is_idle = True
            else:
                if self.direction == 'R':
                    self.is_dead = False
                    self.image = self.dead[int(self.actual)]
                    self.update_rect(self.image)
                else:
                    self.is_dead = False
                    self.image = self.dead[int(self.actual)]
                    self.image = py.transform.flip(self.image, True, False)
                    self.update_rect(self.image)

    def move(self):
        pressed_key = py.key.get_pressed()

        if pressed_key[py.K_RIGHT]:
            self.rect.centerx -= 4

        if pressed_key[py.K_LEFT]:
            self.rect.centerx += 4

    def update_rect(self, image: Surface):
        center_position = self.rect.center
        self.rect = image.get_rect(center=center_position)
        self.rect.bottom = SCREEN_HEIGHT

    def hurt(self,imagem: Surface, quantidade):

        filter_bright = py.Surface(imagem.get_size()).convert_alpha()
        filter_bright.fill((quantidade, quantidade, quantidade))
        img_bright = imagem.copy()
        img_bright.blit(filter_bright, (0, 0), special_flags=py.BLEND_RGB_ADD)

        return img_bright

