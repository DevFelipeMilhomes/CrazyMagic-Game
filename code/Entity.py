from abc import ABC, abstractmethod

from pygame import Surface

import pygame as py

from code.Const import ENTITY_SPEED, ENTITY_HEALTH, ENTITY_DAMAGE


class Entity(ABC):
    def __init__(self, name: str, position: tuple, dirname: str):
        self.name = name
        self.image = None
        self.dirname = dirname
        self.position = position
        self.rect = None
        self.speed = ENTITY_SPEED[self.name]
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def move(self):
        pass