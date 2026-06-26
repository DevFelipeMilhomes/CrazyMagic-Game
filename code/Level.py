from unittest import skip

import pygame as py
from pygame import Surface, Font, Rect

from code.Background import Background
from code.Const import TEXT_MENU_C, SCREEN_WIDTH, FIRST_SPAW, INTERVAL_SPAW, \
    ENTITY_HEALTH, COLOR_BAR_HP, COLOR_BAR_HP_BACK, BAR_HP_MAX, COLOR_BLACK, NPC_SPEECHES, PLAYER_SPEECHES, \
    ENTITY_POSITION, SPEECHES_AMOUNT, HEALTH_VARIABLE, INTERVAL_MOVE_POTION
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Npc import Npc
from code.Player import Player
from code.Potion import Potion
from code.TextBubble import TextBubble


class Level:
    def __init__(self, screen: Surface, name: str, player: str):
        self.screen = screen
        self.name = name
        self.playerName = player
        self.entity_list: list[Entity] = []
        self.text_bubble_list: list[TextBubble] = []
        self.talk = False
        self.level_sound = py.mixer.Sound(f'./assets/Background/Level1Bg/Sound/nature.mp3')
        if name == 'Level1':
            self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
            self.entity_list.append(EntityFactory.get_entity('Enemy1', (FIRST_SPAW, 0)))
            self.entity_list.append(
                EntityFactory.get_entity('Npc1', (FIRST_SPAW + INTERVAL_SPAW, 0), self.screen, player))
            self.entity_list.append(EntityFactory.get_entity('Enemy1', (FIRST_SPAW + INTERVAL_SPAW * 2, 0)))
            self.entity_list.append(EntityFactory.get_entity('Enemy2', (FIRST_SPAW + INTERVAL_SPAW * 2 + 100, 0)))
            self.entity_list.append(
                EntityFactory.get_entity('Npc2', (FIRST_SPAW + INTERVAL_SPAW * 3, 0), self.screen, player))
            self.entity_list.append(EntityFactory.get_entity('Enemy2', (FIRST_SPAW + INTERVAL_SPAW * 4, 0)))
            self.entity_list.append(EntityFactory.get_entity('Enemy1', (FIRST_SPAW + INTERVAL_SPAW * 4 + 100, 0)))
            self.entity_list.append(EntityFactory.get_entity('Enemy2', (FIRST_SPAW + INTERVAL_SPAW * 4 + 200, 0)))
            self.entity_list.append(
                EntityFactory.get_entity('Npc3', (FIRST_SPAW + INTERVAL_SPAW * 5, 0), self.screen, player))
            self.entity_list.append(EntityFactory.get_entity(self.playerName))
            self.entity_list.append(EntityFactory.get_entity('Boss1', (FIRST_SPAW + INTERVAL_SPAW * 6, 0)))
            self.entity_list.append(
                Potion('Potion', (FIRST_SPAW * 10 - 800, INTERVAL_MOVE_POTION['max']), 'Items',
                       'Teleporter'))

            self.text_bubble_list.append(
                TextBubble(self.screen, 40, 'Precione a tecla -a- para atacar', (SCREEN_WIDTH / 2, 200), 4000))

            self.text_bubble_list.append(
                TextBubble(self.screen, 40, 'Precione a tecla -g- para pular falas', (SCREEN_WIDTH / 2, 200), 4000))

            self.text_bubble_list.append(
                TextBubble(self.screen, 40, 'Precione a tecla -x- para usar o novo ataque', (SCREEN_WIDTH / 2, 200),
                           4000))

            self.text_bubble_list.append(
                TextBubble(self.screen, 40,
                           'Você pegou o amuleto teletransportador\n pode avançar para a proxima etapa',
                           (SCREEN_WIDTH / 2, 200),
                           4000))

        self.time_creation = py.time.get_ticks()
        self.actual_text = 0
        self.what_health = '1'

    def run(self):
        clock = py.time.Clock()
        while True:
            self.found_boss = False
            clock.tick(60)

            for ent in self.entity_list:
                self.screen.blit(source=ent.image, dest=ent.rect)
                ent.update()
                ent.move()

                if isinstance(ent, Npc):
                    ent.is_talking()
                    ent.verify_talk()
                    potion = ent.give_potion_now()
                    if potion is not None:
                        self.entity_list.append(potion)
                    if ent.is_talk:
                        if ent.name == 'Npc1' and self.actual_text == 1:
                            self.text_bubble_list[self.actual_text].create = True
                        self.talk = True
                    if ent.closed_speech:
                        self.talk = False

                if self.talk:
                    if isinstance(ent, (Player, Enemy, Background, Potion)):
                        ent.is_talk = True
                        ent.verify_talk()
                else:
                    if isinstance(ent, (Player, Enemy, Background, Potion)):
                        ent.is_talk = False

                if isinstance(ent, Player):
                    ent.just_move()
                    shot = ent.shot_ball()
                    if ent.level_finish:
                        self.text_bubble_list[self.actual_text].create = True
                    if shot is not None:
                        self.entity_list.append(shot)
                    if ent.active_health2:
                        self.what_health = '2'
                    if ent.active_attack2 and self.actual_text == 2:
                        self.text_bubble_list[self.actual_text].create = True

                    self.level_text(20, f'HP', COLOR_BLACK, (35, 40))
                    self.bar('Player', 'Player', ent.health, (30, 50), self.what_health)

                if isinstance(ent, Enemy):
                    if ent.active_bar_health:
                        self.level_text(20, f'HP', COLOR_BLACK, (240, 640))
                        self.bar('Boss', 'Boss', ent.health, (240, 650), '1')

                if self.name == 'Level1':

                    for text in self.text_bubble_list:
                        text.update()
                        time_actual = py.time.get_ticks()
                        if time_actual <= self.time_creation + 2000:
                            self.text_bubble_list[self.actual_text].create = True
                        if self.actual_text == 0 and self.text_bubble_list[self.actual_text].finish:
                            self.actual_text += 1
                        if self.actual_text == 1 and self.text_bubble_list[self.actual_text].finish:
                            self.actual_text += 1
                        if self.actual_text == 2 and self.text_bubble_list[self.actual_text].finish:
                            self.actual_text += 1
                        if self.actual_text == 3 and self.text_bubble_list[self.actual_text].finish:
                            self.entity_list = []
                            return ['WIN', self.name, self.playerName]

                    if not py.mixer.Channel(0).get_busy():
                        py.mixer.Channel(0).play(self.level_sound, loops=-1)

            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()

            py.display.flip()

            EntityMediator.verify_distance_entity(self.actual_text, entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = py.font.Font('./assets/Fonts/Jersey10-Regular.ttf', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)

    def bar(self, who: str, type_bar: str, health: int, position: tuple, what_health: str):
        bar_hp_size = (health / HEALTH_VARIABLE[who][what_health]) * HEALTH_VARIABLE[who][what_health]
        if who == 'Boss':
            bar_hp_size = (health / HEALTH_VARIABLE[who][what_health]) * 800
        if bar_hp_size <= 0:
            bar_hp_size = 0
        bar_hp_rect = py.Rect(position[0], position[1], bar_hp_size, 20)
        bar_hp_rect_back = py.Rect(position[0], position[1], HEALTH_VARIABLE[who][what_health], 20)
        if who == 'Boss':
            bar_hp_rect_back = py.Rect(position[0], position[1], 800, 20)
        py.draw.rect(self.screen, COLOR_BAR_HP_BACK[type_bar], bar_hp_rect_back,
                     border_radius=3)
        py.draw.rect(self.screen, COLOR_BAR_HP[type_bar], bar_hp_rect, border_radius=3)
