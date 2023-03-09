import pygame

class Window:
    def __init__(self, width, height, caption=""):
        self.width = width
        self.height = height
        self.caption = caption
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)

    def clear(self):
        self.screen.fill((0, 0, 0))

    def update(self):
        pygame.display.update()
