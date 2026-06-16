import pygame as py
from pygame import Surface, Font, Rect

from code.Const import MENU_OPTION, TEXT_MENU_C, TEXT_MENU_C_SELECT, SCREEN_WIDTH


class Menu:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.image = py.image.load('./assets/Menu/MenuBg.png').convert_alpha()
        self.rect = self.image.get_rect(left=0, top=0)

    def run(self):

        option = 0
        while True:

            self.screen.blit(source=self.image, dest=self.rect)
            for i in range(len(MENU_OPTION)):
                if i == option:
                    self.menu_text(70, MENU_OPTION[i], TEXT_MENU_C_SELECT, (SCREEN_WIDTH / 2, 500 + 70 * i))
                else:
                    self.menu_text(60, MENU_OPTION[i], TEXT_MENU_C, (SCREEN_WIDTH / 2, 500 + 70 * i))

            for event in py.event.get():
                if event.type == py.KEYDOWN:
                    if event.key == py.K_DOWN:
                        option += 1
                        if option >= len(MENU_OPTION):
                            option = 0
                    if event.key == py.K_UP:
                        option -= 1
                        if option <= -1:
                            option = len(MENU_OPTION) - 1

                    if event.key == py.K_RETURN:
                        return MENU_OPTION[option]

                if event.type == py.QUIT:
                    py.quit()
                    quit()

            py.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = py.font.Font('./assets/Fonts/Jersey10-Regular.ttf', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)