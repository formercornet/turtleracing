import pygame
import sys
from random import randint
import time


def move(color, pos):
    global end_game
    if not end_game:
        x, y = pos
        x += randint(0, 3)
        pos = x, y
        if color == "red":
            global red_turtle_pos
            global red_turtle_hitbox
            red_turtle_pos = pos
            red_turtle_hitbox = pygame.Rect(x, y, 145, 70)
            # pygame.draw.rect(screen, (0, 0, 0), (x, y, 145, 70))
            screen.blit(red_turtle_image, pos)
        elif color == "green":
            global green_turtle_pos
            global green_turtle_hitbox
            green_turtle_pos = pos
            green_turtle_hitbox = (x, y, 145, 70)
            # pygame.draw.rect(screen, (0, 0, 0), (x, y, 145, 70))
            screen.blit(green_turtle_image, pos)
        elif color == "blue":
            global blue_turtle_pos
            global blue_turtle_hitbox
            blue_turtle_pos = pos
            blue_turtle_hitbox = (x, y, 145, 70)
            # pygame.draw.rect(screen, (0,  0, 0), (x, y, 145, 70))
            screen.blit(blue_turtle_image, pos)
        elif color == "yellow":
            global yellow_turtle_pos
            global yellow_turtle_hitbox
            yellow_turtle_pos = pos
            yellow_turtle_hitbox = (x, y, 145, 70)
            # pygame.draw.rect(screen, (0, 0, 0), (x, y, 145, 70))
            screen.blit(yellow_turtle_image, pos)

def endgame(color):
    pass



def hit(color, pos):
    x, y, w, z = pos
    global end_game
    if color == "red":
        if x >= 544:
            end_game = True
            endgame("red")
    if color == "green":
        if x >= 544:
            end_game = True
            endgame("green")
    if color == "blue":
        if x >= 544:
            end_game = True
            endgame("blue")

    if color == "yellow":
        if x >= 544:
            end_game = True
            endgame("yellow")




pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Turtle Racing")
clock = pygame.time.Clock()


red_turtle_image = pygame.image.load("images/redturtle.png").convert_alpha()
blue_turtle_image = pygame.image.load("images/blueturtle.png").convert_alpha()
green_turtle_image = pygame.image.load("images/greenturtle.png").convert_alpha()
yellow_turtle_image = pygame.image.load("images/yellowturtle.png").convert_alpha()
background = pygame.image.load("images/background.jpg")
finish_line = pygame.image.load("images/finishline.jpg")

red_turtle_pos = (0, 25)
green_turtle_pos = (0, 170)
blue_turtle_pos = (0, 330)
yellow_turtle_pos = (0, 500)
red_turtle_hitbox = pygame.Rect(0, 25, 145, 70)
green_turtle_hitbox = pygame.Rect(0, 170, 145, 70)
blue_turtle_hitbox = pygame.Rect(0, 330, 145, 70)
yellow_turtle_hitbox = pygame.Rect(0, 500, 145, 70)
end_game = False
Running = True
while True:

    clock.tick(30)
    screen.blit(background, (0, 0))
    screen.blit(finish_line, (685, 0))
    if not Running:
        screen.blit(red_turtle_image, red_turtle_pos)
        screen.blit(green_turtle_image, green_turtle_pos)
        screen.blit(blue_turtle_image, blue_turtle_pos)
        screen.blit(yellow_turtle_image, yellow_turtle_pos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if Running:
        move("red", red_turtle_pos)
        move("blue", blue_turtle_pos)
        move("green", green_turtle_pos)
        move("yellow", yellow_turtle_pos)
        hit("red", red_turtle_hitbox)
        hit("green", green_turtle_hitbox)
        hit("blue", blue_turtle_hitbox)
        hit("yellow", yellow_turtle_hitbox)
    if end_game == False:
        pygame.display.update()
