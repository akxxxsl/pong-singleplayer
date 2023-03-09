import math
import pygame
import random

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.speed = 0.3
        self.dx = 0
        self.dy = 0
        self.isMoving = False


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)

    def launch(self):
        if not self.isMoving:
            self.isMoving = True
            angle = random.uniform(30, 60)
            self.dx = self.speed * math.cos(math.radians(angle))
            self.dy = -self.speed * math.sin(math.radians(angle))

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def reset(self, x, y):
        self.x = x
        self.y = y
        angle = random.uniform(-45, 45)  # angle de départ aléatoire
        self.dx = self.speed * math.cos(math.radians(angle))
        self.dy = -self.speed * math.sin(math.radians(angle))

    def isColliding(self, paddle):
        if self.y + self.radius >= paddle.y and self.y - self.radius <= paddle.y + paddle.height:
            if self.x + self.radius >= paddle.x and self.x - self.radius <= paddle.x + paddle.width:
                return True
        return False
