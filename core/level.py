import pygame.display
from pygame import Surface, Rect
from pygame.font import Font
from core.const import COLOR_WHITE, MENU_OPTION, EVENT_ENEMY
from core.entity import Entity
from core.entity_factory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('bg0'))
        self.entity_list.append(EntityFactory.get_entity('player1'))
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('player2'))
        pygame.time.set_timer(EVENT_ENEMY, 2000)

    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # desenha entidades
                self.level_text(15, f'FPS: {clock.get_fps():.2f}', COLOR_WHITE, (10, 10))
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Ending Game")
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('enemy1'))
            pygame.display.flip()

    def level_text(self, text_size, text, text_color, text_pos):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
