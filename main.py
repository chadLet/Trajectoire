# Import des librairies
import pygame
import sys
import numpy as np

pygame.init()

# Création de la liste nous servant d'échelle de temps
t = np.arange(0, 50, .05)

# Initialisation d'une liste de positions pour la souris
positions = [[0, 0], [0, 0]]

# Variable nous donnant des informations sur l'état du mouvement de la balle
moving = True
finished = False

# Setup de la fenêtre et de l'horloge
width, height = 2560, 1440
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
black = 39, 48, 48
cyan = 149, 191, 187
screen.fill(cyan)

# Variable de gravité (modifié pour coller à l'échelle)
g = 50

# Initialisation de la boucle
i = 0
while i <= len(t):
    # FPS
    clock.tick(144)
    # Sert à s'assurer que la fenetre se ferme correctement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Si le clic droit est enfoncé, la balle suivra la souris
    buttons = pygame.mouse.get_pressed()
    if buttons[0]:
        if not finished:
            i = 0
        finished = False
        moving = True
        x, y = pygame.mouse.get_pos()
        positions.append(pygame.mouse.get_pos())
        screen.fill(cyan)
        pygame.draw.ellipse(screen, black, [x - 50, y - 50, 100, 100])
    else:
        # Si la balle ne suit plus la souris, on simule sa trajectoire
        moving = False
        if not moving and not finished:
            # Calcul des vitesses avant lancer
            Vx = (positions[-1][0] - positions[-2][0]) / (1 / 10)
            Vy = ((height - positions[-1][1]) - (height - positions[-2][1])) / (1 / 10)
            screen.fill(cyan)
            # Equations paraboliques sans frottements de l'air (programme de terminale)
            pygame.draw.ellipse(screen, black, [Vx * t[i] + positions[-1][0] - 50,
                                                (g * t[i] ** 2) / 2 - Vy * t[i] + positions[-1][1] - 50, 100, 100])
            # Sert à s'assurer que la simulation commence bien à t = 0
            i += 1
            if i == len(t):
                i = 0
                finished = True

    # Update de la fenêtre
    pygame.display.flip()
