from readline import backend

import pygame as py
from pygame import Surface

from code.Background import Background
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player


class Level:
    def __init__(self, screen: Surface, name: str, player: str):
        self.screen = screen
        self.name = name
        self.playerName = player
        self.entity_list: list[Entity] = []
        if name == 'Level1':
            self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity(self.playerName))


    def run(self):
        clock = py.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.screen.blit(source=ent.image,dest=ent.rect)
                ent.update()
                ent.move()

            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()

            py.display.flip()