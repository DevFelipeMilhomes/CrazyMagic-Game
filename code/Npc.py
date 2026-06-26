import pygame as py
from pygame import Surface, Rect

from code.Character import Character
from code.Const import ENTITY_IMAGE_AMOUNT, ACTIONS_DELAY, SCREEN_HEIGHT, SPEECHES_AMOUNT, NPC_SPEECHES, \
    ENTITY_POSITION, PLAYER_SPEECHES, INTERVAL_MOVE_POTION
from code.Potion import Potion
from code.TextBubble import TextBubble


class Npc(Character):
    def __init__(self, name, position, dirname, screen: Surface, player: str):
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
        self.screen = screen

        self.is_idle = True
        self.is_special = False
        self.frame_talk = False
        self.is_talk = False
        self.closed_speech = False
        self.moment_create = True
        self.last_text_create = 0
        self.skip = False
        self.text_count = 0
        self.test = 0
        self.text_bubble_list: list[TextBubble] = []

        for i in range(SPEECHES_AMOUNT[name]):
            self.text_bubble_list.append(
                TextBubble(self.screen, 30, NPC_SPEECHES[player][name][i],
                           (ENTITY_POSITION[player][0] + 500,
                            ENTITY_POSITION[player][1] - 70), 10000))

            self.text_bubble_list.append(
                TextBubble(self.screen, 30, PLAYER_SPEECHES[player][name][i],
                           (ENTITY_POSITION[player][0],
                            ENTITY_POSITION[player][1] - 70), 10000))

        self.special_sound = py.mixer.Sound(f'./assets/Npc/{self.name}/Sound/Special.mp3')
        self.special_c = None
        self.frame_sound = 0
        self.sound_now = True
        self.give_potion = False

    def update(self):

        if self.is_idle:
            self.actual += ACTIONS_DELAY[self.name]['frames_Idle']
            if self.actual >= ENTITY_IMAGE_AMOUNT[self.name]['Idle']:
                self.actual = 0
            if self.direction == 'R':
                self.image = self.idle[int(self.actual)]
                self.update_rect(self.image)
            else:
                self.image = self.idle[int(self.actual)]
                self.update_rect(self.image)
                self.image = py.transform.flip(self.image, True, False)

        elif self.is_special:
            if self.sound_now:
                if self.special_c is None or not self.special_c.get_busy():
                    self.special_c = py.mixer.find_channel()
                    if self.special_c:
                        self.special_c.play(self.special_sound)
                        self.sound_now = False

            self.actual += ACTIONS_DELAY[self.name]['frames_Special']
            if self.actual >= ENTITY_IMAGE_AMOUNT[self.name]['Special']:
                if self.name == 'Npc1':
                    self.frame_talk = True
                    if self.special_c:
                        self.special_c.stop()
                        self.special_c = None
                if self.name in ['Npc2','Npc3']:
                    self.give_potion = True
                    self.is_idle = True
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
        pressed_just_key = py.key.get_just_pressed()

        if self.is_talk:
            if pressed_just_key[py.K_g]:
                self.skip = True

    def is_talking(self):
        if self.is_talk:
            for text in self.text_bubble_list:

                text_not_created = not text.finish and not text.create
                text_created_not_finalized = not text.finish and text.create
                text_finalized = text.finish and not text.create

                if self.moment_create:
                    if self.text_bubble_list.index(text) == 0:
                        self.actual = 0
                    if text_not_created:
                        text.create = True
                        self.moment_create = False
                        self.last_text_create = self.text_bubble_list.index(text)

                else:
                    if text_finalized:
                        if self.text_bubble_list.index(text) == SPEECHES_AMOUNT[self.name] * 2 - 1:
                            self.closed_speech = True
                        if self.last_text_create == self.text_bubble_list.index(text):
                            self.moment_create = True

                if self.name == 'Npc1':
                    if self.text_bubble_list.index(text) == 0 and text_created_not_finalized:
                        self.is_special = True
                        self.is_idle = False
                    if self.text_bubble_list.index(text) == 2 and text_created_not_finalized:
                        self.is_special = False
                        self.is_idle = True

                if self.name in ['Npc2', 'Npc3']:
                    if self.text_bubble_list.index(text) == 4 and text_created_not_finalized and not self.is_special:
                        self.is_special = True
                        self.is_idle = False

                if self.skip and text_created_not_finalized:
                    text.finish = True
                    text.create = False
                    if self.last_text_create != SPEECHES_AMOUNT[self.name] * 2 - 1:
                        self.moment_create = True
                    self.skip = False

                if self.closed_speech:
                    self.is_talk = False
                text.update()

    def give_potion_now(self):
        if self.give_potion:
            self.give_potion = False
            return Potion('Potion',(self.rect.left - 30, INTERVAL_MOVE_POTION['max']),'Items', self.name)
        return None

    def update_rect(self, image: Surface):
        position_previous = self.rect.right
        center_position = self.rect.center
        self.rect = image.get_rect(center=center_position)
        self.rect.bottom = SCREEN_HEIGHT
        if self.direction == 'L':
            self.rect.right = position_previous
