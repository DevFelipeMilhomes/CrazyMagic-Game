import pygame as py
from pygame import Surface, Rect

from code.Character import Character
from code.Const import ENTITY_IMAGE_AMOUNT, ACTIONS_DELAY, SCREEN_HEIGHT, ENTITY_FACTOR_SIZE
from code.ShotEnemy import ShotEnemy


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
        self.is_attack2 = False
        self.is_attack3 = False
        self.active_shot = False
        self.is_talk = False
        self.attack1_dmg = 0
        self.attack2_dmg = 0
        self.attack3_dmg = 0
        self.act = False
        self.is_hurt = False
        self.is_dead = False
        self.is_dead_frame = False
        self.attack_delay = ACTIONS_DELAY[self.name]['Attack']
        self.active_bar_health = False

        self.act_sound = py.mixer.Sound(f'./assets/Enemy/{self.name}/Sound/Act.mp3')
        self.act_sound.set_volume(0.7)
        self.act_c = None
        if self.name != 'Enemy6':
            self.attack1_sound = py.mixer.Sound(f'./assets/Enemy/{self.name}/Sound/Attack1.mp3')
            self.attack1_sound.set_volume(0.7)
            self.attack1_c = None
        if self.name in ['Boss1']:
            self.attack2_sound = py.mixer.Sound(f'./assets/Enemy/{self.name}/Sound/Attack2.mp3')
            self.attack2_sound.set_volume(0.7)
            self.attack2_c = None
            self.attack3_sound = py.mixer.Sound(f'./assets/Enemy/{self.name}/Sound/Attack3.mp3')
            self.attack3_sound.set_volume(0.7)
            self.attack3_c = None

    def update(self):

        if self.is_dead_frame:
            if self.act_c:
                self.act_c.stop()
            if self.name != 'Enemy6':
                if self.attack1_c:
                    self.attack1_c.stop()
            if self.name in ['Boss1']:
                if self.attack2_c: self.attack2_c.stop()
                if self.attack3_c: self.attack3_c.stop()
            self.__dead_move()

        elif self.is_idle:
            self.__idle_move()

        elif self.is_attack1:
            if self.name != 'Enemy6':
                if self.attack1_c is None or not self.attack1_c.get_busy():
                    self.attack1_c = py.mixer.find_channel()
                    if self.attack1_c:
                        self.attack1_c.play(self.attack1_sound, loops=-1)
                        if self.act_c:
                            self.act_c.stop()
                            self.act_c = None
            self.__attack_move('Attack1')
        elif self.is_attack2:
            if self.name != 'Boss3':
                if self.attack2_c is None or not self.attack2_c.get_busy():
                    self.attack2_c = py.mixer.find_channel()
                    if self.attack2_c:
                        self.attack2_c.play(self.attack2_sound, loops=-1)
                        if self.act_c:
                            self.act_c.stop()
                            self.act_c = None
            self.__attack_move('Attack2')
        elif self.is_attack3:
            if self.name != 'Boss3':
                if self.attack3_c is None or not self.attack3_c.get_busy():
                    self.attack3_c = py.mixer.find_channel()
                    if self.attack3_c:
                        self.attack3_c.play(self.attack3_sound, loops=-1)
                    if self.act_c:
                        self.act_c.stop()
                        self.act_c = None
            self.__attack_move('Attack3')
        elif self.act:
            if self.act_c is None or not self.act_c.get_busy():
                self.act_c = py.mixer.find_channel()
                if self.act_c:
                    self.act_c.play(self.act_sound, loops=-1)
            self.__act_move()

    def move(self):
        pressed_key = py.key.get_pressed()

        if not self.is_talk:
            if pressed_key[py.K_RIGHT]:
                self.rect.centerx -= 4

            if pressed_key[py.K_LEFT]:
                self.rect.centerx += 4

    def verify_talk(self):
        if self.is_talk:
            self.is_idle = True
            self.is_attack1 = False
            self.is_hurt = False
            self.is_attack2 = False
            self.is_attack3 = False
            if self.act_c:
                self.act_c.stop()
            if self.name != 'Enemy6':
                if self.attack1_c:
                    self.attack1_c.stop()
            if self.name in ['Boss1']:
                if self.attack2_c:
                    self.attack2_c.stop()
                if self.attack3_c:
                    self.attack3_c.stop()

    def shot_ball(self):
        if self.active_shot:
            self.active_shot = False
            if self.direction == 'R':
                if self.is_attack2:
                    return ShotEnemy('Shot2', (self.rect.right, self.rect.centery - 90), self.name, self.direction)

                return ShotEnemy('Shot', (self.rect.right, self.rect.centery - 90), self.name, self.direction)

            else:
                if self.is_attack2:
                    return ShotEnemy('Shot2', (self.rect.left, self.rect.centery - 90), self.name, self.direction)
                return ShotEnemy('Shot', (self.rect.left, self.rect.centery - 90), self.name, self.direction)
        else:
            return None

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

    def __idle_move(self):
        self.actual += ACTIONS_DELAY[self.name]['frames_Idle']
        if self.actual >= ENTITY_IMAGE_AMOUNT[self.name]['Idle']:
            self.actual = 0
        if self.direction == 'R':
            self.image = self.idle[int(self.actual)]
            self.update_rect(self.image)
        else:
            self.image = self.idle[int(self.actual)]
            self.image = py.transform.flip(self.image, True, False)
            self.update_rect(self.image)

    def __attack_move(self, type_attack: str):
        self.attack_delay -= 1
        if self.attack_delay == 0:
            self.attack_delay = ACTIONS_DELAY[self.name]['Attack']
            previous = int(self.actual)
            self.actual += ACTIONS_DELAY[self.name][f'frames_{type_attack}']
            current = int(self.actual)

            if self.actual >= ENTITY_IMAGE_AMOUNT[self.name][type_attack]:
                if type_attack == 'Attack1':
                    self.is_attack1 = False
                    self.attack1_dmg = 0
                    if self.name != 'Enemy6':
                        if self.attack1_c:
                            self.attack1_c.stop()
                            self.attack1_c = None
                elif type_attack == 'Attack2':
                    self.is_attack2 = False
                    self.attack2_dmg = 0
                    if self.name != 'Boss3':
                        if self.attack2_c:
                            self.attack2_c.stop()
                            self.attack2_c = None
                elif type_attack == 'Attack3':
                    self.is_attack3 = False
                    self.attack3_dmg = 0
                    if self.name != 'Boss3':
                        if self.attack3_c:
                            self.attack3_c.stop()
                            self.attack3_c = None

                self.actual = 0
                self.is_idle = True

                if self.is_dead_frame:
                    self.is_idle = False
            else:
                if self.direction == 'R':
                    if current != previous:
                        if type_attack == 'Attack1': self.attack1_dmg = int(self.actual)
                        if type_attack == 'Attack2': self.attack2_dmg = int(self.actual)
                        if type_attack == 'Attack3': self.attack3_dmg = int(self.actual)
                    else:
                        if type_attack == 'Attack1': self.attack1_dmg = 0
                        if type_attack == 'Attack2': self.attack2_dmg = 0
                        if type_attack == 'Attack3': self.attack3_dmg = 0
                    if type_attack == 'Attack1':
                        self.image = self.attack1[int(self.actual)]
                        if self.name == 'Enemy6':
                            if self.attack1.index(self.image) == ENTITY_IMAGE_AMOUNT[self.name][type_attack] - 2:
                                if previous != current:
                                    self.active_shot = True
                        if self.is_hurt:
                            self.image = self.hurt(self.attack1[int(self.actual)], 255)
                            self.is_hurt = False
                    if type_attack == 'Attack2':
                        self.image = self.attack2[int(self.actual)]
                        if self.name == 'Boss3':
                            if self.attack2.index(self.image) == ENTITY_IMAGE_AMOUNT[self.name][type_attack] - 2:
                                if previous != current:
                                    self.active_shot = True
                        if self.is_hurt:
                            self.image = self.hurt(self.attack2[int(self.actual)], 255)
                            self.is_hurt = False
                    if type_attack == 'Attack3':
                        self.image = self.attack3[int(self.actual)]
                        if self.name == 'Boss3':
                            if self.attack3.index(self.image) == ENTITY_IMAGE_AMOUNT[self.name][type_attack] - 2:
                                if previous != current:
                                    self.active_shot = True
                        if self.is_hurt:
                            self.image = self.hurt(self.attack3[int(self.actual)], 255)
                            self.is_hurt = False
                    self.update_rect(self.image)

                else:
                    if current != previous:
                        if type_attack == 'Attack1': self.attack1_dmg = int(self.actual)
                        if type_attack == 'Attack2': self.attack2_dmg = int(self.actual)
                        if type_attack == 'Attack3': self.attack3_dmg = int(self.actual)
                    else:
                        if type_attack == 'Attack1': self.attack1_dmg = 0
                        if type_attack == 'Attack2': self.attack2_dmg = 0
                        if type_attack == 'Attack3': self.attack3_dmg = 0
                    if type_attack == 'Attack1':
                        self.image = self.attack1[int(self.actual)]
                        if self.name == 'Enemy6':
                            if self.attack1.index(self.image) == ENTITY_IMAGE_AMOUNT[self.name][type_attack] - 2:
                                if previous != current:
                                    self.active_shot = True
                        if self.is_hurt:
                            self.image = self.hurt(self.attack1[int(self.actual)], 255)
                            self.is_hurt = False
                    if type_attack == 'Attack2':
                        self.image = self.attack2[int(self.actual)]
                        if self.name == 'Boss3':
                            if self.attack2.index(self.image) == ENTITY_IMAGE_AMOUNT[self.name][type_attack] - 2:
                                if previous != current:
                                    self.active_shot = True
                        if self.is_hurt:
                            self.image = self.hurt(self.attack2[int(self.actual)], 255)
                            self.is_hurt = False
                    if type_attack == 'Attack3':
                        self.image = self.attack3[int(self.actual)]
                        if self.name == 'Boss3':
                            if self.attack3.index(self.image) == ENTITY_IMAGE_AMOUNT[self.name][type_attack] - 2:
                                if previous != current:
                                    self.active_shot = True
                        if self.is_hurt:
                            self.image = self.hurt(self.attack3[int(self.actual)], 255)
                            self.is_hurt = False
                    self.image = py.transform.flip(self.image, True, False)
                    self.update_rect(self.image)

    def __act_move(self):
        self.actual += ACTIONS_DELAY[self.name]['frames_Run']
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

    def __dead_move(self):
        self.actual += ACTIONS_DELAY[self.name]['frames_Dead']
        if self.actual >= ENTITY_IMAGE_AMOUNT[self.name]['Dead']:
            self.actual = 0
            self.is_dead = True
            if self.act_c:
                self.act_c.stop()
                self.act_c = None
            if self.name != 'Enemy6':
                if self.attack1_c:
                    self.attack1_c.stop()
                    self.attack1_c = None
            if self.name in ['Boss1']:
                if self.attack2_c:
                    self.attack2_c.stop()
                    self.attack2_c = None
                if self.attack3_c:
                    self.attack3_c.stop()
                    self.attack3_c = None
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
