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
        self.is_attack2 = False
        self.is_attack3 = False
        self.is_shot_attack = False
        self.is_hurt = False
        self.is_dead = False
        self.attack1_dmg = 0
        self.attack2_dmg = 0
        self.attack3_dmg = 0
        self.active_attack1 = True
        self.active_attack2 = True
        self.active_attack3 = True
        self.vertical_speed = VERTICAL_SPEED
        self.gravity = GRAVITY
        self.jump_delay = ACTIONS_DELAY[self.name]['Jump']

    def update(self):

        if self.is_idle:
            self.__idle_move()
        elif self.is_jumping:
            self.__jump_move()
        elif self.is_attack1:
            if self.active_attack1:
                self.__attack_move('Attack1')
        elif self.is_attack2:
            if self.active_attack2:
                self.__attack_move('Attack2')
        elif self.is_attack3:
            if self.active_attack3:
                self.__attack_move('Attack3')
        elif self.is_dead:
            self.__dead_move()


    def move(self):

        key_pressed = py.key.get_pressed()

        if key_pressed[py.K_RIGHT] and not self.is_jumping and not self.is_attack1 and not self.is_attack2 and not self.is_attack3:
            self.actual += ACTIONS_DELAY[self.name]['frames_run']
            if self.actual >= ENTITY_IMAGE_AMOUNT[self.name]['Run']:
                self.actual = 0
            self.image = self.run[int(self.actual)]
            self.update_rect(self.image)
            self.direction = 'R'

        if key_pressed[py.K_LEFT] and not self.is_jumping and not self.is_attack1 and not self.is_attack2 and not self.is_attack3:
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
                self.__is_move('jumping')
        if key_pressed[py.K_a]:
            if self.is_idle:
                self.__is_move('attack1')
        if key_pressed[py.K_x]:
            if self.is_idle:
                self.__is_move('attack2')
        if key_pressed[py.K_f]:
            if self.is_idle:
                self.__is_move('attack3')

    def update_rect(self, image: Surface):
        position_previous = self.rect.right
        self.rect = image.get_rect(left=SCREEN_WIDTH / 2 - 200)
        self.rect.bottom = SCREEN_HEIGHT
        if self.direction == 'L':
            self.rect.right = position_previous

    def hurt(self, imagem: Surface, quantidade):

        filter_bright = py.Surface(imagem.get_size()).convert_alpha()
        filter_bright.fill((quantidade, quantidade, quantidade))
        img_bright = imagem.copy()
        img_bright.blit(filter_bright, (0, 0), special_flags=py.BLEND_RGB_ADD)

        return img_bright

    def __attack_move(self, type_attack: str):
        self.actual += ACTIONS_DELAY[self.name][f'frames_{type_attack}']
        if self.actual >= ENTITY_IMAGE_AMOUNT[self.name][type_attack]:
            self.actual = 0
            if type_attack == 'Attack1':
                self.is_attack1 = False
                self.attack1_dmg = 0
            elif type_attack == 'Attack2':
                self.is_attack2 = False
                self.attack2_dmg = 0
            elif type_attack == 'Attack3':
                self.is_attack3 = False
                self.attack3_dmg = 0
            self.is_idle = True
        if self.direction == 'R':
            if type_attack == 'Attack1':
                self.attack1_dmg += 1
                self.image = self.attack1[int(self.actual)]
                if self.is_hurt:
                    self.image = self.hurt(self.attack1[int(self.actual)], 255)
                    self.is_hurt = False
            elif type_attack == 'Attack2':
                self.attack2_dmg += 1
                self.image = self.attack2[int(self.actual)]
                if self.is_hurt:
                    self.image = self.hurt(self.attack2[int(self.actual)], 255)
                    self.is_hurt = False
            elif type_attack == 'Attack3':
                self.attack3_dmg += 1
                self.image = self.attack3[int(self.actual)]
                if self.is_hurt:
                    self.image = self.hurt(self.attack3[int(self.actual)], 255)
                    self.is_hurt = False
            self.update_rect(self.image)
        else:
            if type_attack == 'Attack1':
                self.attack1_dmg += 1
                self.image = self.attack1[int(self.actual)]
                if self.is_hurt:
                    self.image = self.hurt(self.attack1[int(self.actual)], 255)
                    self.is_hurt = False
            elif type_attack == 'Attack2':
                self.attack2_dmg += 1
                self.image = self.attack2[int(self.actual)]
                if self.is_hurt:
                    self.image = self.hurt(self.attack2[int(self.actual)], 255)
                    self.is_hurt = False
            elif type_attack == 'Attack3':
                self.attack3_dmg += 1
                self.image = self.attack3[int(self.actual)]
                if self.is_hurt:
                    self.image = self.hurt(self.attack3[int(self.actual)], 255)
                    self.is_hurt = False
            self.update_rect(self.image)
            self.image = py.transform.flip(self.image, True, False)

    def __jump_move(self):
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
            if self.is_hurt:
                self.image = self.hurt(self.jump[int(self.actual)], 255)
                self.is_hurt = False
            self.rect = self.image.get_rect(left=SCREEN_WIDTH / 2 - 200)
            self.rect.bottom = bottom_previous
            if self.jump.index(self.image) >= self.jump_delay:
                self.rect.centery -= self.vertical_speed
                self.vertical_speed -= self.gravity
        else:
            bottom_previous = self.rect.bottom
            self.image = self.jump[int(self.actual)]
            if self.is_hurt:
                self.image = self.hurt(self.jump[int(self.actual)], 255)
                self.is_hurt = False
            self.rect = self.image.get_rect(left=SCREEN_WIDTH / 2 - 200)
            self.rect.bottom = bottom_previous
            if self.jump.index(self.image) >= self.jump_delay:
                self.rect.centery -= self.vertical_speed
                self.vertical_speed -= self.gravity
            self.image = py.transform.flip(self.image, True, False)

    def __idle_move(self):
        self.actual += ACTIONS_DELAY[self.name]['frames_idle']
        if self.actual >= ENTITY_IMAGE_AMOUNT[self.name]['Idle']:
            self.actual = 0
        if self.direction == 'R':
            self.image = self.idle[int(self.actual)]
            if self.is_hurt:
                self.image = self.hurt(self.idle[int(self.actual)], 255)
                self.is_hurt = False
            self.update_rect(self.image)
        else:
            self.image = self.idle[int(self.actual)]
            if self.is_hurt:
                self.image = self.hurt(self.idle[int(self.actual)], 255)
                self.is_hurt = False
            self.update_rect(self.image)
            self.image = py.transform.flip(self.image, True, False)

    def __dead_move(self):
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

    def __is_move(self, type_move: str):
        self.actual = 0
        self.is_jumping = False
        self.is_idle = False
        self.is_attack1 = False
        self.is_attack2 = False
        self.is_attack3 = False
        self.is_shot_attack = False
        if type_move == 'jumping': self.is_jumping = True
        if type_move == 'attack1': self.is_attack1 = True
        if type_move == 'attack2': self.is_attack2 = True
        if type_move == 'attack3': self.is_attack3 = True