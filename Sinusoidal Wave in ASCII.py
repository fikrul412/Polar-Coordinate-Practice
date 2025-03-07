import numpy as np 
import time
import os
import keyboard
size = 40
m = [[0 for _ in range(size)] for _ in range(size)]
m_text = "\n".join(str(row) for row in m)

A = 5
w = 4
B = 1

def function(dt, A, w):
    return A * np.cos(w*dt) + B * np.sin(w*dt)

class Point():
    def __init__(self, xCor, yCor, val, screen):
        self.x = xCor
        self.y = yCor
        self.val = val
        self.screen = screen 
        self.spawn(self.screen)

    def spawn(self, screen):
        screen[self.x][self.y] = self.val
    
list_point = [Point(7, i, 1, m) for i in range(size)]
dt = 0
while True:
    if keyboard.is_pressed("q"):  
        print("\nExiting animation...")
        exit()
    dt+= 0.1
    os.system("cls" if os.name == "nt" else "clear")
    m = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(len(list_point)):
        list_point[i].x = round(size//2 + function(dt + i*0.1, A, w))

    for point in list_point:
        point.spawn(m)
    for row in m:
        print(" ".join('0' if cell == 1 else ' ' for cell in row))

    time.sleep(0.1)

