import pygame as py
import time

from code.Level import Level
from code.OptionLevel import OptionLevel
from code.OptionPlayer import OptionPlayer
from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, MENU_OPTION
from code.Menu import Menu
from code.Ranking import Ranking


class Game:
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.last_level = ['NOVO JOGO']

    def run(self):
        while True:
            py.mixer.music.load('./assets/Menu/Sound/Menu_sound.mp3')
            py.mixer.music.play(-1)
            ranking = Ranking(self.screen)
            menu = Menu(self.screen)
            menu_ret = menu.run()
            if menu_ret == MENU_OPTION[0]:
                option_player = OptionPlayer(self.screen)
                option_player_ret = option_player.run()

                if option_player_ret:
                    start_time = time.time()
                    game_finish = False
                    while True:
                        option_level = OptionLevel(self.screen, self.last_level[len(self.last_level)-1])
                        option_level_ret = option_level.run()

                        if not option_level_ret:
                            break

                        level = Level(self.screen, option_level_ret, option_player_ret)
                        py.mixer.music.stop()
                        level_ret = level.run()

                        if level_ret:
                            py.mixer.music.play(-1)
                            if level_ret == 'Level1':
                                self.last_level.append('Level1')
                            if level_ret == 'Level2':
                                self.last_level.append('Level2')
                            if  level_ret == 'Level3':
                                game_finish = True
                                break
                    if game_finish:
                        end_time = time.time() - start_time
                        ranking.save(int(end_time))
            elif menu_ret == MENU_OPTION[1]:
                ranking.show()
            else:
                py.quit()
                quit()