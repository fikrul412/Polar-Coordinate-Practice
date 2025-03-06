import pygame
import numpy as np
from random import randint, choice
""" PYGAME TEMPLATE """
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 40

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (243, 247, 111)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Polar Coordinate")

clock = pygame.time.Clock()

running = True
radius = 0
theta = 0


""" POLAR COORDINATE"""
scale = 0
start_pos = 60
initiate_pos = start_pos + randint(0, 180)

def xPos(r, theta):
    return r*np.cos(theta)

def yPos(r, theta):
    return r*np.sin(theta)

def thetaPos(x, y):
    return np.arctan(y/x)

def rPos(x, y):
    return np.sqrt((x - WIDTH//2)**2 + (y + HEIGHT//2)**2)

def generate_map():
    global start_pos
    global scale
    scale = choice([-15,-11,8,-5, 5, 8, 11, 15])
    initiate_pos = start_pos + randint(0, 180)
    xCoordinates = [xPos((i+1)*0.1, (i+1)*0.001*scale + initiate_pos) for i in range(3000)]
    yCoordinates = [yPos((i+1)*0.1, (i+1)*0.001*scale + initiate_pos) for i in range(3000)]
    return [[x, y] for x, y in zip(xCoordinates, yCoordinates)]

baseCoordinates = generate_map()
""" TARGET COORDINATE """
targetCoordinate = [[randint(50, 750), randint(25, 575)]]

""" PLAYER CLASS """
class Player():
    def __init__(self, angle, r):
        self.angle = angle
        self.r = r
        self.dt = 0
        self.speed = 2
    def move(self):
        keyEvent = pygame.key.get_pressed()
        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_SPACE:
        #             self.r += 1
        #             self.dt = 0 
        if keyEvent[pygame.K_UP]:
            self.r += 1*self.speed
            self.dt = 0 
        if keyEvent[pygame.K_DOWN]:
            self.r -= 1*self.speed
            self.dt = 0 
        # if keyEvent[pygame.K_LEFT]:
        #     self.angle -= 180/np.pi/self.r*0.1
        # if keyEvent[pygame.K_LEFT]:
        #     self.xPos -= 1
        # if keyEvent[pygame.K_UP]: 
        #     self.yPos -= 1
        # if keyEvent[pygame.K_DOWN]:
        #     self.yPos += 1
    def moveAuto(self):
        self.angle += 180/np.pi/self.r*0.01*scale
        self.dt += 0.05
        self.r -= self.dt

        # self.angle += 0.008
    def collision(self, listCoordinate):
        global targetCoordinate
        global baseCoordinates
        for x, y in listCoordinate[::10]: 
            distance = np.sqrt((WIDTH//2 + xPos(self.r, self.angle) - (WIDTH//2 + x))**2 + 
                            (HEIGHT//2 + yPos(self.r, self.angle) - (HEIGHT//2 + y))**2)
            if distance < 6:  
                self.r = 60
                self.angle = 60
                self.dt = 0
                baseCoordinates = generate_map()
                targetCoordinate = [[randint(50, 750), randint(25, 575)]]
                return
    def collision2(self, listCoordinate):
        global baseCoordinates
        global targetCoordinate
        for x, y in listCoordinate: 
            distance = np.sqrt((WIDTH//2 + xPos(self.r, self.angle) - (x))**2 + 
                            (HEIGHT//2 + yPos(self.r, self.angle) - (y))**2)
            if distance < 10:  
                self.r = 60
                self.angle = 60
                self.dt = 0
                baseCoordinates = generate_map()
                targetCoordinate = [[randint(50, 750), randint(25, 575)]]
                return

    def spawn(self):
        pygame.draw.circle(screen, WHITE, (WIDTH//2 + xPos(self.r, self.angle), HEIGHT//2 + yPos(self.r, self.angle)), 5)

player = Player(start_pos, 60)
finish = False
""" GAME LOOP """
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.speed = 4
        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    player.speed = 1

    """UPDATE PLACE"""
    
    if not finish:
        screen.fill(BLACK)
        for x, y in baseCoordinates:
            pygame.draw.circle(screen, WHITE, (x + WIDTH//2, y+HEIGHT//2), 5)
        
        player.moveAuto()
        player.move()
        player.spawn()
        player.collision(baseCoordinates)
        for x, y in targetCoordinate:
            pygame.draw.circle(screen, YELLOW, (x, y), 5)
        player.collision2(targetCoordinate)

    pygame.display.update() 

pygame.quit()