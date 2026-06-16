from readline import backend

import pygame as py
from pygame import Surface, Font, Rect

from code.Background import Background
from code.Const import TEXT_MENU_C, SCREEN_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player
from code.TextBubble import TextBubble


class Level:
    def __init__(self, screen: Surface, name: str, player: str):
        self.screen = screen
        self.name = name
        self.playerName = player
        self.entity_list: list[Entity] = []
        if name == 'Level1':
            self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity(self.playerName))
        self.text = TextBubble(self.screen,40,'Press a for attack',(SCREEN_WIDTH/2,100))


    def run(self):
        clock = py.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.screen.blit(source=ent.image,dest=ent.rect)
                ent.update()
                ent.move()
                if isinstance(ent, Player):
                    ent.just_move()

            if self.text.actual <= len(self.text.text) -1:
                self.text.write()

            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()


            py.display.flip()
