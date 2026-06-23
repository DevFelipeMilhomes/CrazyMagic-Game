from code.Background import Background
from code.Const import ENTITY_IMAGE_AMOUNT, SCREEN_WIDTH, ENTITY_POSITION
from code.Enemy import Enemy
from code.Npc import Npc
from code.Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(name: str, position: tuple = (0, 0)):
        match name:
            case 'Level1Bg':
                list_bg = []
                for i in range(ENTITY_IMAGE_AMOUNT[name]):
                    if i == ENTITY_IMAGE_AMOUNT[name] - 1:
                        list_bg.append(Background(f'Level1Bg{i}', position, 'Level1Bg', 'init'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 2, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 3, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 4, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 5, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 6, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 7, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 8, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 9, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 10, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 11, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 12, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 13, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 14, 0), 'Level1Bg', 'end'))
                    else:
                        list_bg.append(Background(f'Level1Bg{i}', position, 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 2, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 3, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 4, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 4, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 5, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 6, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 7, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 8, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 9, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 10, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 11, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 12, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 13, 0), 'Level1Bg', 'middle'))
                        list_bg.append(Background(f'Level1Bg{i}', (SCREEN_WIDTH * 14, 0), 'Level1Bg', 'middle'))

                return list_bg
            case 'Player1':
                return Player('Player1', (ENTITY_POSITION['Player1'][0],ENTITY_POSITION['Player1'][1]), 'Player')
            case 'Player2':
                return Player('Player2', (ENTITY_POSITION['Player2'][0],ENTITY_POSITION['Player2'][1]), 'Player')
            case 'Boss1':
                return Enemy('Boss1', (position[0], position[1]), 'Enemy')
            case 'Enemy1':
                return Enemy('Enemy1', (position[0],position[1]),'Enemy')
            case 'Enemy2':
                return Enemy('Enemy2', (position[0], position[1]), 'Enemy')
            case 'Npc1':
                return Npc('Npc1', (position[0], position[1]), 'Npc')
            case 'Npc2':
                return Npc('Npc2', (position[0], position[1]), 'Npc')
            case 'Npc3':
                return Npc('Npc3', (position[0], position[1]), 'Npc')
