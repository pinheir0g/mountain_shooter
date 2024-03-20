from core.background import Background
from core.const import WIN_WIDTH


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
