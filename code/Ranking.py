from datetime import datetime

import pygame as py
from pygame import Font, Surface, Rect, KEYDOWN
from pygame.constants import K_RETURN, K_BACKSPACE, K_ESCAPE

from code.Const import MENU_OPTION, COLOR_WHITE, SCREEN_WIDTH, COLOR_YELLOW
from code.DBProxy import DBProxy


class Ranking:
    def __init__(self, screen):
        self.screen = screen
        self.surf = py.image.load('./assets/Menu/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, time:int):

        name = ''
        while True:
            db_proxy = DBProxy('DBRanking')
            self.screen.blit(source=self.surf, dest=self.rect)
            self.ranking_text(50, 'VOCÊ GANHOU!!', COLOR_WHITE, (SCREEN_WIDTH / 2, 100))

            self.ranking_text(35, 'Digite seu nome (5 caracteres)', COLOR_WHITE, (SCREEN_WIDTH / 2, 200))

            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 5:
                        db_proxy.save({'name': name, 'time': time, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 5:
                            name += event.unicode
            self.ranking_text(35, name, COLOR_WHITE, (SCREEN_WIDTH / 2, 300))
            py.display.flip()

    def show(self):
        self.screen.blit(source=self.surf, dest=self.rect)
        self.ranking_text(48, 'TOP 10 TEMPOS', COLOR_WHITE, (SCREEN_WIDTH / 2, 100))
        self.ranking_text(30, 'NOME         TEMPO          DATA    ', COLOR_YELLOW, (SCREEN_WIDTH / 2 - 40, 150))
        db_proxy = DBProxy('DBRanking')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()
        i = 0
        for player_score in list_score:
            i += 1
            id_, name, time, date = player_score

            minutes = int(time // 60)
            seconds = int(time % 60)

            time_formatted = f"{minutes:02d}:{seconds:02d}"

            self.ranking_text(30, f'{name}         {time_formatted}          {date}', COLOR_WHITE,
                            (SCREEN_WIDTH / 2, 150 + 50 * i) )
            print(i)
        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()
                if event.type == py.KEYDOWN:
                    if event.key == K_ESCAPE:
                        return

            py.display.flip()


    def ranking_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = py.font.Font('./assets/Fonts/Jersey10-Regular.ttf', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
