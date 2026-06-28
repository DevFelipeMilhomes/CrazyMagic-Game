import pygame as py
from pygame import Surface, Font, Rect

from code.Const import TEXT_MENU_C, TEXT_MENU_C_SELECT, PLAYER_OPTION, PLAYER_OPTION_POSITION, LEVEL_OPTION, \
    SCREEN_WIDTH


class OptionLevel:
    def __init__(self, screen: Surface, level_previous: str):
        self.screen = screen
        self.image = py.image.load('./assets/Menu/MenuBg.png').convert_alpha()
        self.rect = self.image.get_rect(left=0,top=0)
        self.level_previous = level_previous

        if level_previous == 'NEW GAME':
            # level option 1
            self.level_option1 = py.image.load('./assets/Menu/Level1Open.png').convert_alpha()
            self.level_option1_rect = self.level_option1.get_rect(left=80, top=270)
            # level option 2
            self.level_option2 = py.image.load('./assets/Menu/Level2Close.png').convert_alpha()
            self.level_option2_rect = self.level_option2.get_rect(left=480, top=270)
            # level option 2
            self.level_option3 = py.image.load('./assets/Menu/Level3Close.png').convert_alpha()
            self.level_option3_rect = self.level_option3.get_rect(left=880, top=270)
        elif level_previous == 'Level1':
            # level option 1
            self.level_option1 = py.image.load('./assets/Menu/Level1Open.png').convert_alpha()
            self.level_option1_rect = self.level_option1.get_rect(left=80, top=270)
            # level option 2
            self.level_option2 = py.image.load('./assets/Menu/Level2Open.png').convert_alpha()
            self.level_option2_rect = self.level_option2.get_rect(left=480, top=270)
            # level option 2
            self.level_option3 = py.image.load('./assets/Menu/Level3Close.png').convert_alpha()
            self.level_option3_rect = self.level_option3.get_rect(left=880, top=270)
        else:
            # level option 1
            self.level_option1 = py.image.load('./assets/Menu/Level1Open.png').convert_alpha()
            self.level_option1_rect = self.level_option1.get_rect(left=80, top=270)
            # level option 2
            self.level_option2 = py.image.load('./assets/Menu/Level2Open.png').convert_alpha()
            self.level_option2_rect = self.level_option2.get_rect(left=480, top=270)
            # level option 2
            self.level_option3 = py.image.load('./assets/Menu/Level3Open.png').convert_alpha()
            self.level_option3_rect = self.level_option3.get_rect(left=880, top=270)

        self.rect_select = self.level_option1_rect


    def run(self):
        option = 1
        while True:
            self.screen.blit(source=self.image,dest=self.rect)
            if self.rect_select is not None:
                py.draw.rect(self.screen,TEXT_MENU_C_SELECT ,self.rect_select.scale_by(1.06))
            self.screen.blit(source=self.level_option1,dest=self.level_option1_rect)
            self.screen.blit(source=self.level_option2, dest=self.level_option2_rect)
            self.screen.blit(source=self.level_option3, dest=self.level_option3_rect)

            self.option_text(50, 'Escolha a fase', TEXT_MENU_C,
                             (SCREEN_WIDTH / 2, 100))
            self.option_text(50, 'Voltar', TEXT_MENU_C,
                             (SCREEN_WIDTH / 2, 600))

            if option == 0:
                self.rect_select = None
                self.option_text(50, 'Voltar', TEXT_MENU_C_SELECT,
                                 (SCREEN_WIDTH / 2, 600))
            elif option == 1:
                self.rect_select = self.level_option1_rect
            elif option == 2:
                self.rect_select = self.level_option2_rect
            else:
                self.rect_select = self.level_option3_rect


            for event in py.event.get():
                if  event.type == py.KEYDOWN:
                    if event.key == py.K_RIGHT:
                        if self.level_previous == 'NEW GAME':
                            option += 1
                            if option >= len(LEVEL_OPTION) - 2:
                                option = 0
                        elif self.level_previous == 'Level1':
                            option += 1
                            if option >= len(LEVEL_OPTION) - 1:
                                option = 0
                        else:
                            option += 1
                            if option >= len(LEVEL_OPTION):
                                option = 0
                    if event.key == py.K_LEFT:
                        if self.level_previous == 'NEW GAME':
                            option += 1
                            if option >= len(LEVEL_OPTION) - 2:
                                option = 0
                        elif self.level_previous == 'Level1':
                            option -= 1
                            if option <= -1:
                                option = len(LEVEL_OPTION) - 2
                        else:
                            option -= 1
                            if option <= -1:
                                option = len(LEVEL_OPTION) - 1

                    if event.key == py.K_RETURN:
                        if option == 0:
                            return False
                        return LEVEL_OPTION[option]

                if event.type == py.QUIT:
                    py.quit()
                    quit()

            py.display.flip()

    def option_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = py.font.Font('./assets/Fonts/Jersey10-Regular.ttf', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)