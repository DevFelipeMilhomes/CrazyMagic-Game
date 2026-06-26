import pygame as py

from code.Level import Level
from code.OptionLevel import OptionLevel
from code.OptionPlayer import OptionPlayer
from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, MENU_OPTION
from code.Menu import Menu


class Game:
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.screen)
            menu_ret = menu.run()
            if menu_ret == MENU_OPTION[0]:
                option_player = OptionPlayer(self.screen)
                option_player_ret = option_player.run()

                if option_player_ret:
                    option_level = OptionLevel(self.screen, 'NEW GAME')
                    option_level_ret = option_level.run()
                    if option_level_ret:
                        level = Level(self.screen, option_level_ret, option_player_ret)
                        level_ret = level.run()

                        if level_ret:
                            option_level = OptionLevel(self.screen, level_ret[1])
                            option_level_ret = option_level.run()
