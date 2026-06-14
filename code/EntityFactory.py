from code.Background import Background
from code.Const import ENTITY_IMAGE_AMOUNT, SCREEN_WIDTH
from code.Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(name: str, position: tuple = (0,0)):
        match name:
            case 'Level1Bg':
                list_bg = []
                for i in range(ENTITY_IMAGE_AMOUNT[name]):
                    if i == ENTITY_IMAGE_AMOUNT[name] - 1:
                        list_bg.append(Background(f'Level1Bg{i}', position, 'Level1Bg', 'init'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH*2, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH*3, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH*4, 0), 'Level1Bg', 'end'))
                    else:
                        list_bg.append(Background(f'Level1Bg{i}', position, 'Level1Bg','middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH,0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH*2,0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH*3,0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH*4,0), 'Level1Bg','middle'))

                return list_bg
            case 'Player1':
                return Player('Player1',(SCREEN_WIDTH/2 -200, 456), 'Player')
            case 'Player2':
                return Player('Player2',(SCREEN_WIDTH/2 -200, 456), 'Player')