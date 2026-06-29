from unittest import skip

import pygame as py
from pygame import Surface, Font, Rect

from code.Background import Background
from code.Const import TEXT_MENU_C, SCREEN_WIDTH, FIRST_SPAW, INTERVAL_SPAW, \
    ENTITY_HEALTH, COLOR_BAR_HP, COLOR_BAR_HP_BACK, BAR_HP_MAX, COLOR_BLACK, NPC_SPEECHES, PLAYER_SPEECHES, \
    ENTITY_POSITION, SPEECHES_AMOUNT, HEALTH_VARIABLE, INTERVAL_MOVE_POTION, ENERGY_ENTITY, ENERGY_VARIABLE
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
        self.background_list: list[Background] = []
        self.text_bubble_list: list[TextBubble] = []
        self.talk = False

        sound = py.mixer.Sound(f'./assets/Background/Level1Bg/Sound/nature.mp3')
        self.what_health = '1'
        self.what_energy = '1'

        if name == 'Level1':
            self.background_list.extend(EntityFactory.get_entity('Level1Bg'))
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
        if name == "Level2":
            sound = py.mixer.Sound(f'./assets/Background/Level2Bg/Sound/winter.mp3')
            self.background_list.extend(EntityFactory.get_entity('Level2Bg'))
            self.entity_list.append(EntityFactory.get_entity('Enemy3', (FIRST_SPAW, 0)))
            self.entity_list.append(EntityFactory.get_entity('Enemy3', (FIRST_SPAW + SCREEN_WIDTH, 0)))
            self.entity_list.append(EntityFactory.get_entity('Enemy4', (FIRST_SPAW + SCREEN_WIDTH + 100, 0)))
            self.entity_list.append(
                EntityFactory.get_entity('Npc4', (FIRST_SPAW + SCREEN_WIDTH + INTERVAL_SPAW, 0), self.screen, player))
            self.entity_list.append(EntityFactory.get_entity('Enemy3', (FIRST_SPAW + SCREEN_WIDTH + INTERVAL_SPAW * 2, 0)))
            self.entity_list.append(EntityFactory.get_entity('Enemy4', (FIRST_SPAW + SCREEN_WIDTH + INTERVAL_SPAW * 2 + 100, 0)))
            self.entity_list.append(EntityFactory.get_entity('Enemy3', (FIRST_SPAW + SCREEN_WIDTH + INTERVAL_SPAW * 2 + 200, 0)))
            self.entity_list.append(EntityFactory.get_entity('Enemy4', (FIRST_SPAW + SCREEN_WIDTH + INTERVAL_SPAW * 2 + 300, 0)))
            self.entity_list.append(
                EntityFactory.get_entity('Npc5', (FIRST_SPAW + SCREEN_WIDTH + INTERVAL_SPAW * 3, 0), self.screen, player))
            player = EntityFactory.get_entity(self.playerName)
            player.health = HEALTH_VARIABLE['Player']['2']
            player.active_attack2 = True
            self.entity_list.append(player)
            self.entity_list.append(EntityFactory.get_entity('Boss2_1', (FIRST_SPAW + SCREEN_WIDTH + INTERVAL_SPAW * 4, 0)))
            self.entity_list.append(EntityFactory.get_entity('Boss2_2', (FIRST_SPAW + SCREEN_WIDTH + INTERVAL_SPAW * 4 + 200, 0)))
            self.entity_list.append(
                Potion('Potion', (FIRST_SPAW * 8 - 800, INTERVAL_MOVE_POTION['max']), 'Items',
                       'Teleporter'))

            self.text_bubble_list.append(
                TextBubble(self.screen, 40, 'Precione a tecla -b- para usar o novo ataque', (SCREEN_WIDTH / 2, 200),
                           4000))

            self.text_bubble_list.append(
                TextBubble(self.screen, 40,
                           'Você pegou o amuleto teletransportador\n pode avançar para a proxima etapa',
                           (SCREEN_WIDTH / 2, 200),
                           4000))

            self.what_health = '2'
        if name == "Level3":
            sound = py.mixer.Sound(f'./assets/Background/Level3Bg/Sound/suspense.mp3')
            self.background_list.extend(EntityFactory.get_entity('Level3Bg'))
            self.entity_list.append(EntityFactory.get_entity('Enemy5', (FIRST_SPAW, 0)))
            self.entity_list.append(EntityFactory.get_entity('Enemy5', (FIRST_SPAW + SCREEN_WIDTH, 0)))
            self.entity_list.append(EntityFactory.get_entity('Enemy6', (FIRST_SPAW + SCREEN_WIDTH + 100, 0)))
            self.entity_list.append(
                EntityFactory.get_entity('Npc6', (FIRST_SPAW + SCREEN_WIDTH + INTERVAL_SPAW, 0), self.screen, player))
            self.entity_list.append(
                EntityFactory.get_entity('Enemy5', (FIRST_SPAW + SCREEN_WIDTH + INTERVAL_SPAW * 2, 0)))
            self.entity_list.append(
                EntityFactory.get_entity('Enemy6', (FIRST_SPAW + SCREEN_WIDTH + INTERVAL_SPAW * 2 + 100, 0)))
            self.entity_list.append(
                EntityFactory.get_entity('Enemy5', (FIRST_SPAW + SCREEN_WIDTH + INTERVAL_SPAW * 2 + 200, 0)))
            self.entity_list.append(
                EntityFactory.get_entity('Enemy6', (FIRST_SPAW + SCREEN_WIDTH + INTERVAL_SPAW * 2 + 300, 0)))
            self.entity_list.append(
                EntityFactory.get_entity('Npc7', (FIRST_SPAW + SCREEN_WIDTH + INTERVAL_SPAW * 3, 0), self.screen,
                                         player))
            player = EntityFactory.get_entity(self.playerName)
            player.health = HEALTH_VARIABLE['Player']['3']
            player.active_attack2 = True
            player.active_shotAttack = True
            self.entity_list.append(player)
            self.entity_list.append(
                EntityFactory.get_entity('Boss3', (FIRST_SPAW + SCREEN_WIDTH + INTERVAL_SPAW * 4, 0)))
            if self.playerName == 'Player1':
                self.entity_list.append(
                    EntityFactory.get_entity('Player2Npc', (FIRST_SPAW * 8 - 800, 0), self.screen,
                                             player))
            else:
                self.entity_list.append(
                    EntityFactory.get_entity('Player1Npc', (FIRST_SPAW * 8 - 800, 0), self.screen,
                                             player))

            self.text_bubble_list.append(
                TextBubble(self.screen, 40, 'Precione a tecla -f- para usar o novo ataque', (SCREEN_WIDTH / 2, 200),
                           4000))
            if self.playerName == 'Player1':
                self.text_bubble_list.append(
                    TextBubble(self.screen, 40,
                               'Parabens você recuperou sua amada',
                               (SCREEN_WIDTH / 2, 200),
                               4000))
            else:
                self.text_bubble_list.append(
                    TextBubble(self.screen, 40,
                               'Parabens você recuperou seu amado',
                               (SCREEN_WIDTH / 2, 200),
                               4000))

            self.what_health = '3'
            self.what_energy = '1'

        self.level_sound = sound
        self.game_over_sound = py.mixer.Sound(f'./assets/Menu/Sound/GameOver.mp3')
        self.time_creation = py.time.get_ticks()
        self.time_game_over = 0
        self.actual_text = 0

    def run(self):
        clock = py.time.Clock()
        if not py.mixer.Channel(0).get_busy():
            py.mixer.Channel(0).play(self.level_sound, loops=-1)
        while True:
            clock.tick(60)
            found_player = False
            for ent in self.background_list:
                self.screen.blit(source=ent.image, dest=ent.rect)
                ent.update()
                ent.move()
                if self.talk:
                    ent.is_talk = True
                    ent.verify_talk()
                else:
                    ent.is_talk = False

            for ent in self.entity_list:
                self.screen.blit(source=ent.image, dest=ent.rect)
                ent.update()
                ent.move()

                if isinstance(ent, Player):
                    found_player = True

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
                    if shot is not None:
                        self.entity_list.append(shot)
                    if ent.level_finish:
                        self.text_bubble_list[self.actual_text].create = True
                    if ent.active_health2:
                        self.what_health = '2'
                    if ent.active_health3:
                        self.what_health = '3'
                    if ent.active_energy2:
                        self.what_energy = '2'
                    if ent.active_attack2 and self.actual_text == 2:
                        self.text_bubble_list[self.actual_text].create = True
                    if ent.active_shotAttack and self.actual_text == 0 and self.name == 'Level2':
                        self.text_bubble_list[self.actual_text].create = True
                    if ent.active_attack3 and self.actual_text == 0 and self.name == 'Level3':
                        self.text_bubble_list[self.actual_text].create = True

                    self.level_text(20, f'HP', COLOR_BLACK, (35, 40))
                    self.bar('Player', 'Player', ent.health, (30, 50), self.what_health)

                    if ent.active_shotAttack:
                        self.level_text(20, f'Energy', COLOR_BLACK, (48, 80))
                        self.bar('Player', 'Energy', ent.energy, (30, 90), self.what_energy)

                if isinstance(ent, Enemy):
                    shot = ent.shot_ball()
                    if shot is not None:
                        self.entity_list.append(shot)
                    if ent.active_bar_health:
                        if ent.name == 'Boss2_1':
                            self.level_text(20, f'HP', COLOR_BLACK, (240, 620))
                            self.bar('Boss', 'Boss', ent.health, (240, 630), '1')
                        elif ent.name == 'Boss2_2':
                            self.level_text(20, f'HP', COLOR_BLACK, (240, 670))
                            self.bar('Boss', 'Boss', ent.health, (240, 680), '1')
                        else:
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
                            py.mixer.stop()
                            self.level_sound.stop()
                            self.entity_list = []
                            return self.name

                if self.name == "Level2":
                    for text in self.text_bubble_list:
                        text.update()
                        if self.actual_text == 0 and self.text_bubble_list[self.actual_text].finish:
                            self.actual_text += 1
                        if self.actual_text == 1 and self.text_bubble_list[self.actual_text].finish:
                            py.mixer.stop()
                            self.level_sound.stop()
                            self.entity_list = []
                            return self.name

                if self.name == "Level3":
                    for text in self.text_bubble_list:
                        text.update()
                        if self.actual_text == 0 and self.text_bubble_list[self.actual_text].finish:
                            self.actual_text += 1
                        if self.actual_text == 1 and self.text_bubble_list[self.actual_text].finish:
                            py.mixer.stop()
                            self.level_sound.stop()
                            self.entity_list = []
                            return self.name



            if not found_player:
                py.mixer.stop()
                self.entity_list = []
                self.game_over_sound.play()
                return False

            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()

            #print(len(self.entity_list))

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
        if type_bar == 'Energy':
            bar_hp_size = (health / ENERGY_VARIABLE['Player'][what_health]) * ENERGY_VARIABLE['Player'][what_health]
        if bar_hp_size <= 0:
            bar_hp_size = 0
        bar_hp_rect = py.Rect(position[0], position[1], bar_hp_size, 20)
        bar_hp_rect_back = py.Rect(position[0], position[1], HEALTH_VARIABLE[who][what_health], 20)
        if type_bar == 'Energy':
            bar_hp_rect_back = py.Rect(position[0], position[1], ENERGY_VARIABLE['Player'][what_health], 20)
        if who == 'Boss':
            bar_hp_rect_back = py.Rect(position[0], position[1], 800, 20)
        py.draw.rect(self.screen, COLOR_BAR_HP_BACK[type_bar], bar_hp_rect_back,
                     border_radius=3)
        py.draw.rect(self.screen, COLOR_BAR_HP[type_bar], bar_hp_rect, border_radius=3)
