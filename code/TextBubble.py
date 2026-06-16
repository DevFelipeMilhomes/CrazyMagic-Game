import pygame as py
from pygame import Font, Surface, Rect

from code.Const import COLOR_BLACK, COLOR_WHITE

class TextBubble:
    def __init__(self, screen: Surface, text_size: int, text: str, text_center_pos: tuple):
        self.text_font: Font = py.font.Font('./assets/Fonts/Jersey10-Regular.ttf', size=text_size)
        self.text_surf = None
        self.text_rect = None
        self.screen = screen
        self.text_position = text_center_pos
        self.text_size = text_size
        self.text = text
        self.tex = ''
        self.actual = 0
        self.delay = 7

    def write(self):
        self.delay -= 1
        if self.delay == 0 and len(self.tex)<=len(self.text) - 1:
            self.tex += self.text[self.actual]
            if self.actual < len(self.text) - 1:
                self.actual += 1
            self.delay = 7

        if self.actual <= len(self.text) -1:
            self.text_surf: Surface = self.text_font.render(self.tex, True, COLOR_BLACK).convert_alpha()
            self.text_rect: Rect = self.text_surf.get_rect(center=self.text_position)
            py.draw.rect(self.screen, COLOR_WHITE, self.text_rect.scale_by(1.06))
            self.screen.blit(source=self.text_surf, dest=self.text_rect)