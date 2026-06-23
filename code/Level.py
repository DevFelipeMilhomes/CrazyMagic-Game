from unittest import skip

import pygame as py
from pygame import Surface, Font, Rect

from code.Background import Background
from code.Const import TEXT_MENU_C, SCREEN_WIDTH, FIRST_SPAW, INTERVAL_SPAW, \
    ENTITY_HEALTH, COLOR_BAR_HP, COLOR_BAR_HP_BACK, BAR_HP_MAX, COLOR_BLACK, NPC_SPEECHES, PLAYER_SPEECHES, \
    ENTITY_POSITION
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Npc import Npc
from code.Player import Player
from code.TextBubble import TextBubble


class Level:
    def __init__(self, screen: Surface, name: str, player: str):
        self.screen = screen
        self.name = name
        self.playerName = player
        self.entity_list: list[Entity] = []
        self.text_bubble_list: list[TextBubble] = []
        self.talk = False
        if name == 'Level1':
            self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
            self.entity_list.append(EntityFactory.get_entity('Enemy1', (FIRST_SPAW, 0)))
            self.entity_list.append(EntityFactory.get_entity('Npc1', (FIRST_SPAW + INTERVAL_SPAW, 0)))
            self.entity_list.append(EntityFactory.get_entity('Enemy1', (FIRST_SPAW + INTERVAL_SPAW * 2, 0)))
            self.entity_list.append(EntityFactory.get_entity('Enemy2', (FIRST_SPAW + INTERVAL_SPAW * 2 + 100, 0)))
            self.entity_list.append(EntityFactory.get_entity('Npc2', (FIRST_SPAW + INTERVAL_SPAW * 3, 0)))
            self.entity_list.append(EntityFactory.get_entity('Enemy2', (FIRST_SPAW + INTERVAL_SPAW * 4, 0)))
            self.entity_list.append(EntityFactory.get_entity('Enemy1', (FIRST_SPAW + INTERVAL_SPAW * 4 + 100, 0)))
            self.entity_list.append(EntityFactory.get_entity('Enemy2', (FIRST_SPAW + INTERVAL_SPAW * 4 + 200, 0)))
            self.entity_list.append(EntityFactory.get_entity('Npc3', (FIRST_SPAW + INTERVAL_SPAW * 5, 0)))
            self.entity_list.append(EntityFactory.get_entity('Boss1', (FIRST_SPAW + INTERVAL_SPAW * 6, 0)))

            self.text_bubble_list.append(
                TextBubble(self.screen, 40, 'Precione a tecla -a- para atacar', (SCREEN_WIDTH / 2, 100), 3000))
            for i in range(len(NPC_SPEECHES[player]['Npc1'])):
                self.text_bubble_list.append(
                    TextBubble(self.screen, 30, NPC_SPEECHES[player]['Npc1'][i],
                               (ENTITY_POSITION[player][0] + 500,
                                ENTITY_POSITION[player][1] - 70), 10000))
                self.text_bubble_list.append(
                    TextBubble(self.screen, 30, PLAYER_SPEECHES[player]['Npc1'][i], (ENTITY_POSITION[player][0],
                                                                                     ENTITY_POSITION[player][1] - 70),
                               10000))

        self.entity_list.append(EntityFactory.get_entity(self.playerName))
        self.time_creation = py.time.get_ticks()
        self.skip = False
        self.actual_text = 0

    def run(self):
        clock = py.time.Clock()
        while True:
            clock.tick(60)

            for ent in self.entity_list:
                self.screen.blit(source=ent.image, dest=ent.rect)
                ent.update()
                ent.move()

                if isinstance(ent, Npc):
                    if ent.is_talk:
                        self.talk = True

                if self.talk:
                    if isinstance(ent, (Player, Enemy, Background)):
                        ent.is_talk = True
                else:
                    if isinstance(ent, (Player, Enemy, Background)):
                        ent.is_talk = False

                if isinstance(ent, (Background, Player, Npc, Enemy)):
                    ent.verify_talk()

                if isinstance(ent, Player):
                    ent.just_move()
                    shot = ent.shot_ball()
                    if shot is not None:
                        self.entity_list.append(shot)
                    self.level_text(20, f'HP - {ent.health}', COLOR_BLACK, (35, 40))
                    self.health_bar(ent.name, 'Player', ent.health, (30, 50))

                if isinstance(ent, Enemy):
                    if ent.active_bar_health:
                        self.level_text(20, f'HP - {ent.health}', COLOR_BLACK, (240, 640))
                        self.health_bar(ent.name, 'Boss', ent.health, (240, 650))

                if self.name == 'Level1':
                    if self.talk:
                        if self.actual_text == len(NPC_SPEECHES[self.playerName]['Npc1'])*2:
                            self.talk = False
                        else:
                            self.text_bubble_list[self.actual_text].create = True
                            if self.skip:
                                self.text_bubble_list[self.actual_text].create = False
                                self.text_bubble_list[self.actual_text].finish = True
                                self.skip = False
                                self.actual_text += 1
                            if self.text_bubble_list[self.actual_text].finish:
                                self.actual_text += 1

                    for text in self.text_bubble_list:
                        text.update()
                        time_actual = py.time.get_ticks()
                        if time_actual <= self.time_creation + 2000:
                            self.text_bubble_list[self.actual_text].create = True
                        if self.actual_text == 0 and self.text_bubble_list[self.actual_text].finish:
                            self.actual_text += 1

            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()
                if event.type == py.KEYDOWN:
                    if event.key == py.K_g:
                        if self.talk:
                            self.skip = True

            py.display.flip()

            EntityMediator.verify_distance_entity(self.actual_text, entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = py.font.Font('./assets/Fonts/Jersey10-Regular.ttf', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)

    def health_bar(self, who: str, type_bar: str, health: int, position: tuple):
        bar_hp_size = (health / ENTITY_HEALTH[who]) * BAR_HP_MAX[type_bar]
        if bar_hp_size <= 0:
            bar_hp_size = 0
        bar_hp_rect = py.Rect(position[0], position[1], bar_hp_size, 20)
        bar_hp_rect_back = py.Rect(position[0], position[1], BAR_HP_MAX[type_bar], 20)
        py.draw.rect(self.screen, COLOR_BAR_HP_BACK[type_bar], bar_hp_rect_back,
                     border_radius=3)
        py.draw.rect(self.screen, COLOR_BAR_HP[type_bar], bar_hp_rect, border_radius=3)
