import pygame


class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.width = width
        self.height = height
        self.color = "#FFFFFF"
        self.x = x
        self.y = y
        self.speed = speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed

    def move_right(self, screen_width):
        if self.x + self.width < screen_width:
            self.x += self.speed

    def hits_ball(self, ball):
        if self.x <= ball.x <= self.x + self.width and self.y <= ball.y <= self.y + self.height:
            return True
        return False
