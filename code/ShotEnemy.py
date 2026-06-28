import pygame as py
from pygame import Surface, Rect

from code.Const import ENTITY_IMAGE_AMOUNT, ACTIONS_DELAY, ENTITY_DAMAGE
from code.Entity import Entity


class ShotEnemy(Entity):

    def __init__(self, name, position, dirname, direction: str):
        super().__init__(name,position,dirname)
        self.shot = []
        for i in range(ENTITY_IMAGE_AMOUNT[dirname][name]):
            img = py.image.load(f'./assets/Enemy/{dirname}/{name}/Shot{i}.png').convert_alpha()
            img = py.transform.scale_by(img, 3)
            self.shot.append(img)
        self.actual = 0
        self.dirname = dirname
        self.image: Surface = self.shot[self.actual]
        self.rect: Rect = self.image.get_rect(left=position[0], top=position[1])
        self.direction = direction
        self.damage = ENTITY_DAMAGE[dirname]['Shot']
        self.attack1_dmg = 0
        self.attack2_dmg = 0
        self.attack3_dmg = 0
        self.is_dead = False
        self.is_hurt = False
        self.is_attack1 = False
        self.is_idle = False
        self.is_talk = False
        self.act = False
        self.shot_attack_sound = py.mixer.Sound(f'./assets/Enemy/{dirname}/Sound/ShotAttack.mp3')
        self.shot_attack_c = None

    def update(self):
        if self.shot_attack_c is None or not self.shot_attack_c.get_busy():
            self.shot_attack_c = py.mixer.find_channel()
            if self.shot_attack_c:
                self.shot_attack_c.play(self.shot_attack_sound)
        self.actual += ACTIONS_DELAY[self.dirname]['frames_Shot']
        if self.actual >= ENTITY_IMAGE_AMOUNT[self.dirname]['Shot']:
            if self.shot_attack_c:
                self.shot_attack_c.stop()
                self.shot_attack_c = None
            self.actual = 0
            self.health = 0
        else:
            if self.direction == 'R':
                self.image = self.shot[int(self.actual)]
                self.rect.centerx += self.speed
            else:
                self.image = self.shot[int(self.actual)]
                self.image = py.transform.flip(self.image, True, False)
                self.rect.centerx -= self.speed

    def move(self):
        pass