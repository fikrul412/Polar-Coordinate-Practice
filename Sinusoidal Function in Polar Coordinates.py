import pygame
import numpy as np
""" Wave Equation """
A = 2
w = 0.5
B = 1

def function(dt, A, w):
    return A * np.cos(w*dt) + B * np.sin(w*dt)
dt = 0

""" POLAR COORDINATE """
def xPos(r, theta):
    return r*np.cos(theta)

def yPos(r, theta):
    return r*np.sin(theta)

def thetaPos(x, y):
    return np.arctan(y/x)

def rPos(x, y):
    return np.sqrt((x - WIDTH//2)**2 + (y + HEIGHT//2)**2)

""" PYGAME SET """
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Polar Coordinate")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
FPS = 60

running = True
scalePhase = 0

""" FONT """
pygame.font.init()
font = pygame.font.Font(None, 36)
text_surface = font.render(f"Scale Phase: {scalePhase}", True, BLACK)
while running:
    clock.tick(FPS) 
    """ Counting Position """
    dt+=0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                scalePhase += 1
            elif event.key == pygame.K_DOWN:
                scalePhase -= 1


    screen.fill(BLACK) 
    """ Drawing Circles """
    screen.fill(WHITE)
    for i in range(45):
        pygame.draw.circle(screen, BLACK, (xPos(90*function(dt + i*scalePhase , A, w), i) + WIDTH//2, 
                                           HEIGHT // 2 + yPos(90*function(dt + i*scalePhase, A, w), i)), 5)
    text_surface = font.render(f"Scale Phase: {scalePhase}", True, BLACK)
    screen.blit(text_surface, (WIDTH//24, 50 + HEIGHT//2 + HEIGHT//3))
    pygame.display.flip()  

pygame.quit()
