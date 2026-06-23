import pygame as py
from pygame import Surface, Rect

from code.Character import Character
from code.Const import ENTITY_IMAGE_AMOUNT, ACTIONS_DELAY, SCREEN_HEIGHT


class Npc(Character):
    def __init__(self, name, position, dirname):
        super().__init__(name, position, dirname)
        self.idle = []
        for i in range(ENTITY_IMAGE_AMOUNT[name]['Idle']):
            img = py.image.load(f'./assets/{dirname}/{name}/Idle/Idle{i}.png').convert_alpha()
            img = py.transform.scale_by(img, 4)
            self.idle.append(img)
        self.special = []
        for i in range(ENTITY_IMAGE_AMOUNT[name]['Special']):
            img = py.image.load(f'./assets/{dirname}/{name}/Special/Special{i}.png').convert_alpha()
            img = py.transform.scale_by(img, 4)
            self.special.append(img)

        self.actual = 0

        self.image: Surface = self.idle[self.actual]
        self.rect: Rect = self.image.get_rect(left=position[0], top=position[1])

        self.direction = 'L'

        self.is_idle = True
        self.is_special = False
        self.frame_talk = False
        self.is_talk = False
        self.closed_speech = False

    def update(self):

        if self.is_idle:
            self.actual += ACTIONS_DELAY[self.name]['frames_Idle']
            if self.actual >= ENTITY_IMAGE_AMOUNT[self.name]['Idle']:
                self.actual = 0
            if self.direction == 'R':
                self.image = self.idle[int(self.actual)]
                self.is_special = False
                self.update_rect(self.image)
            else:
                self.image = self.idle[int(self.actual)]
                if self.frame_talk:
                    self.image = self.special[ENTITY_IMAGE_AMOUNT[self.name]['Special']-1]
                self.update_rect(self.image)
                self.is_special = False
                self.image = py.transform.flip(self.image, True, False)

        elif self.is_special:
            self.actual += ACTIONS_DELAY[self.name]['frames_Special']
            if self.actual >= ENTITY_IMAGE_AMOUNT[self.name]['Special']:
                self.frame_talk = True
                self.actual = 0
            else:
                if self.direction == 'R':
                    self.image = self.special[int(self.actual)]
                    if self.frame_talk:
                        self.image = self.special[ENTITY_IMAGE_AMOUNT[self.name]['Special'] - 1]
                    self.update_rect(self.image)
                else:
                    self.image = self.special[int(self.actual)]
                    if self.frame_talk:
                        self.image = self.special[ENTITY_IMAGE_AMOUNT[self.name]['Special'] - 1]
                    self.update_rect(self.image)
                    self.image = py.transform.flip(self.image, True, False)

    def move(self):
        pressed_key = py.key.get_pressed()

        if not self.is_talk:
            if pressed_key[py.K_RIGHT]:
                self.rect.centerx -= 4

            if pressed_key[py.K_LEFT]:
                self.rect.centerx += 4

    def verify_talk(self):
        pass


    def update_rect(self, image: Surface):
        position_previous = self.rect.right
        center_position = self.rect.center
        self.rect = image.get_rect(center=center_position)
        self.rect.bottom = SCREEN_HEIGHT
        if self.direction == 'L':
            self.rect.right = position_previous
