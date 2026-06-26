from pygame import Rect

from code.Const import INTERVAL_MOVE_POTION
from code.Entity import Entity
import pygame as py


class Potion(Entity):
    def __init__(self, name, position, dirname, npc: str):
        super().__init__(name,position, dirname)
        img = py.image.load(f'./assets/{dirname}/{name}/Icon/Potion.png').convert_alpha()
        img = py.transform.scale_by(img, 2)
        if npc == 'Teleporter':
            img = py.image.load(f'./assets/{dirname}/{name}/Icon/Teleporter.png').convert_alpha()
            img = py.transform.scale_by(img, 3)
        self.image = img
        self.rect: Rect = self.image.get_rect(left=position[0], top=position[1])
        self.going_up = True
        self.npc = npc
        self.is_talk = False
        self.is_dead = False
        self.is_hurt = False
        self.is_attack1 = False
        self.is_idle = False
        self.act = False
        self.is_dead_frame = True
        self.potion_sound = py.mixer.Sound(f'./assets/Items/Potion/Sound/Potion.mp3')
        if npc == 'Teleporter':
            self.potion_sound = py.mixer.Sound(f'./assets/Items/Potion/Sound/Teleporter.mp3')
        self.potion_c = None

    def update(self):
        if self.going_up:
            self.rect.centery -= self.speed
            if self.rect.centery == INTERVAL_MOVE_POTION['min']:
                self.going_up = False
        else:
            self.rect.centery += self.speed
            if self.rect.centery == INTERVAL_MOVE_POTION['max']:
                self.going_up = True




    def move(self):
        pressed_key = py.key.get_pressed()

        if not self.is_talk:
            if pressed_key[py.K_RIGHT]:
                self.rect.centerx -= 4

            if pressed_key[py.K_LEFT]:
                self.rect.centerx += 4

    def verify_talk(self):
        pass