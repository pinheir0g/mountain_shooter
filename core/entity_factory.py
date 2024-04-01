import random

from core.background import Background
from core.const import WIN_WIDTH, WIN_HEIGHT
from core.enemy import Enemy
from core.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'bg0':
                lista_bg = []
                for i in range(7):
                    lista_bg.append(Background(f'bg{i}', position))
                    lista_bg.append(Background(f'bg{i}', (WIN_WIDTH, 0)))
                return lista_bg
            case 'player1':
                return Player('player1', (10, (WIN_HEIGHT / 2) - 30))
            case 'player2':
                return Player('player2', (10, (WIN_HEIGHT / 2) + 30))
            case 'enemy1':
                return Enemy('enemy1', (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT)))
