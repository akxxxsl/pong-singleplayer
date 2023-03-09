import sys
import pygame
import random
import math

from models.game import Game
from models.window import Window
from models.ball import Ball
from models.paddle import Paddle

pygame.init()

game = Game()
window = Window(800, 600, "Pong - Single Player")
ball = Ball(window.width/2, window.height/2)
paddle = Paddle((window.width/2) - window.width/12, window.height - 30, window.width/6, 10, 0.2)

font = pygame.font.Font(None, 36) # définir une police de caractères et une taille pour le texte
start_text = font.render("PRESS ENTER TO START", True, (255, 255, 255)) # créer un texte "PRESS ENTER TO START" en blanc
info_text = font.render(game.__str__(), True, (255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_RETURN: # si la touche Entrée est pressée
                if not ball.isMoving: # si la balle n'est pas déjà en mouvement
                    ball.isMoving = False
                    ball.launch() # lancer la balle avec un angle aléatoire
                    game.score = 0 # réinitialiser le score
                    info_text = font.render(game.__str__(), True,(255, 255, 255))  # mettre à jour le score
                    game.time_elapsed = 0 # réinitialiser le temps écoulé

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move_left()
    if keys[pygame.K_RIGHT]:
        paddle.move_right(window.width)

    #Si la balle est en mouvement
    if ball.isMoving:
        ball.move()
        if ball.y - ball.radius < 0:
            ball.dy *= -1
        if ball.x - ball.radius < 0 or ball.x + ball.radius > window.width:
            ball.dx *= -1
        #Si la balle sort de l'écran on reset tout et on affiche le texte
        if ball.y + ball.radius > window.height:
            ball.isMoving = False
            paddle.x = (window.width / 2) - window.width / 12
            ball.reset(window.width / 2, window.height / 2)
            start_text = font.render("PRESS ENTER TO START", True, (255, 255, 255)) # si la balle sort de l'écran, réafficher le texte
        # Si la balle touche la raquette
        if ball.isColliding(paddle):
            # Augmenter la vitesse sur l'axe y
            ball.dy += max(1, abs(ball.dy))
            # Inverser la direction de la balle
            ball.dy *= -1
            # Calculer la distance entre le centre de la balle et le centre de la raquette
            dist = ball.x - (paddle.x + paddle.width / 2)
            # Normaliser la distance pour obtenir une valeur entre -1 et 1
            dist /= (paddle.width / 2)
            # Calculer l'angle de rebond en fonction de la distance
            angle = dist * math.pi / 2.5
            # Changer la direction de la balle en fonction de l'angle de rebond
            ball.dx = ball.speed * math.sin(angle)
            ball.dy = -ball.speed * math.cos(angle)
            # Augmenter le score
            game.score += 1
            info_text = font.render(game.__str__(), True, (255, 255, 255)) # mettre à jour le score


    window.clear()
    if not ball.isMoving: # si la balle n'est pas en mouvement
        window.screen.blit(start_text, (window.width//2 - start_text.get_width()//2, window.height//2 - start_text.get_height()//2)) # afficher le texte au centre de l'écran
        window.screen.blit(info_text,(10, 10))
    else: # si la balle est en mouvement, l'afficher
        ball.draw(window.screen)
        window.screen.blit(info_text,(10, 10))
    paddle.draw(window.screen)
    window.update()
