import pygame as py
from pygame import Font, Surface, Rect

from code.Const import COLOR_BLACK, COLOR_WHITE, ACTIONS_DELAY


class TextBubble:
    def __init__(self, screen: Surface, text_size: int, text: str, text_pos: tuple, lifetime: int):
        self.text_font: Font = py.font.Font('./assets/Fonts/Jersey10-Regular.ttf', size=text_size)
        self.text_surf = None
        self.text_rect = None
        self.screen = screen
        self.text_position = text_pos
        self.text_size = text_size
        self.text = text
        self.writing_process = ''
        self.actual = 0
        self.delay = ACTIONS_DELAY['TextBubble']
        self.full_text_bubble = False
        self.create = False
        self.time_creation_full = None
        self.lifetime = lifetime

    def update(self):
        if self.create:
            if not self.full_text_bubble:
                self.delay -= 1
                if self.delay == 0 and len(self.writing_process) <= len(self.text) - 1:
                    self.writing_process += self.text[self.actual]
                    if self.actual < len(self.text) - 1:
                        self.actual += 1
                    else:
                        self.full_text_bubble = True
                        self.time_creation_full = py.time.get_ticks()

                    self.delay = ACTIONS_DELAY['TextBubble']
            else:
                current_time = py.time.get_ticks()
                if current_time - self.time_creation_full >= self.lifetime:
                    self.create = False

            self.text_surf: Surface = self.text_font.render(self.writing_process, True, COLOR_BLACK).convert_alpha()
            self.text_rect: Rect = self.text_surf.get_rect(center=self.text_position)
            py.draw.rect(self.screen, COLOR_WHITE, self.text_rect.scale_by(1.07), border_radius=4)
            self.screen.blit(source=self.text_surf, dest=self.text_rect)

