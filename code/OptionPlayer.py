import pygame as py
from pygame import Surface, Font, Rect

from code.Const import TEXT_MENU_C, TEXT_MENU_C_SELECT, PLAYER_OPTION, PLAYER_OPTION_POSITION, SCREEN_WIDTH


class OptionPlayer:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.image = py.image.load('./assets/Menu/MenuBg.png').convert_alpha()
        self.rect = self.image.get_rect(left=0, top=0)
        # player option 1
        self.player_option1 = py.image.load('./assets/Player/Player1/Attack3/Attack2.png').convert_alpha()
        self.player_option1 = py.transform.scale_by(self.player_option1, 5)
        self.player_option1_rect = self.player_option1.get_rect(left=PLAYER_OPTION_POSITION[PLAYER_OPTION[1]], top=200)
        # player option 2
        self.player_option2 = py.image.load('./assets/Player/Player2/Attack2/Attack1.png').convert_alpha()
        self.player_option2 = py.transform.scale_by(self.player_option2, 5)
        self.player_option2_rect = self.player_option2.get_rect(left=PLAYER_OPTION_POSITION[PLAYER_OPTION[2]], top=200)

    def run(self):
        option = 1
        while True:
            self.screen.blit(source=self.image, dest=self.rect)
            self.screen.blit(source=self.player_option1, dest=self.player_option1_rect)
            self.screen.blit(source=self.player_option2, dest=self.player_option2_rect)

            self.option_text(50, 'Escolha o jogador', TEXT_MENU_C,
                             (SCREEN_WIDTH / 2, 100))
            if option == 0:
                self.option_text(50, 'Voltar', TEXT_MENU_C_SELECT,
                                 (SCREEN_WIDTH / 2, 600))
            else:
                self.option_text(50, 'Voltar', TEXT_MENU_C,
                                 (SCREEN_WIDTH / 2, 600))

            for i in range(1, len(PLAYER_OPTION)):
                if i == option:
                    self.option_text(50, PLAYER_OPTION[i], TEXT_MENU_C_SELECT,
                                     (PLAYER_OPTION_POSITION[PLAYER_OPTION[i]] + 60, 550))
                else:
                    self.option_text(50, PLAYER_OPTION[i], TEXT_MENU_C,
                                     (PLAYER_OPTION_POSITION[PLAYER_OPTION[i]] + 60, 550))

            for event in py.event.get():
                if event.type == py.KEYDOWN:
                    if event.key == py.K_RIGHT:
                        option += 1
                        if option >= len(PLAYER_OPTION):
                            option = 0
                    if event.key == py.K_LEFT:
                        option -= 1
                        if option <= -1:
                            option = len(PLAYER_OPTION) - 1

                    if event.key == py.K_RETURN:
                        if option == 0:
                            return False
                        if PLAYER_OPTION[option] == 'FELIPE':
                            return 'Player1'
                        else:
                            return 'Player2'

                if event.type == py.QUIT:
                    py.quit()
                    quit()

            py.display.flip()

    def option_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = py.font.Font('./assets/Fonts/Jersey10-Regular.ttf', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)
