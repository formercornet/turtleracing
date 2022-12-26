import pygame
import sys
from random import randint
import sys
import time

winner = ""
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
            gamescreen.blit(red_turtle_image, pos)
        elif color == "green":
            global green_turtle_pos
            global green_turtle_hitbox
            green_turtle_pos = pos
            green_turtle_hitbox = (x, y, 145, 70)
            # pygame.draw.rect(screen, (0, 0, 0), (x, y, 145, 70))
            gamescreen.blit(green_turtle_image, pos)
        elif color == "blue":
            global blue_turtle_pos
            global blue_turtle_hitbox
            blue_turtle_pos = pos
            blue_turtle_hitbox = (x, y, 145, 70)
            # pygame.draw.rect(screen, (0,  0, 0), (x, y, 145, 70))
            gamescreen.blit(blue_turtle_image, pos)
        elif color == "yellow":
            global yellow_turtle_pos
            global yellow_turtle_hitbox
            yellow_turtle_pos = pos
            yellow_turtle_hitbox = (x, y, 145, 70)
            # pygame.draw.rect(screen, (0, 0, 0), (x, y, 145, 70))
            gamescreen.blit(yellow_turtle_image, pos)

def endgame(winner):
    global end_game
    myfont = pygame.font.SysFont("monospace", 50)
    label = myfont.render(winner + " turtle wins!", True, (0, 0, 0))
    gamescreen.blit(label, (70, 300))

def crown_blit(winner):
   x, y = get_turtle_pos(winner)
   gamescreen.blit(crown, (x+113, y-15))

# def winner_image(winner):
#     global red_turtle_image
#     global blue_turtle_image
#     global green_turtle_image
#     global yellow_turtle_image
#     if winner == "red":
#         winner_img = red_turtle_image
#     elif winner == "green":
#         winner_img = green_turtle_image
#     elif winner == "blue":
#         winner_img = blue_turtle_image
#     elif winner == "yellow":
#         winner_img = yellow_turtle_image
#     return winner_img

def get_turtle_pos(color):
    global red_turtle_pos
    global blue_turtle_pos
    global green_turtle_pos
    global yellow_turtle_pos
    if color == "red":
        pos = red_turtle_pos
    elif color == "blue":
        pos = blue_turtle_pos
    elif color == "green":
        pos = green_turtle_pos
    elif color == "yellow":
        pos = yellow_turtle_pos
    return pos

def hit(color, pos):
    x, y, w, z = pos
    global end_game
    global Running
    global winner
    if color == "red":
        if x >= 544:
            end_game = True
            Running = False
            winner = "red"
            # endgame("red")
    if color == "green":
        if x >= 544:
            end_game = True
            Running = False
            winner = "green"
            # endgame("green")
    if color == "blue":
        if x >= 544:
            end_game = True
            Running = False
            winner = "blue"
            # endgame("blue")

    if color == "yellow":
        if x >= 544:
            end_game = True
            Running = False
            winner = "yellow"
            # endgame("yellow")


def startgame():
    global gamescreen
    global clock
    global end_game
    global Running
    global red_turtle_image
    global blue_turtle_image
    global green_turtle_image
    global yellow_turtle_image
    global background
    global finish_line
    global red_turtle_pos
    global green_turtle_pos
    global blue_turtle_pos
    global yellow_turtle_pos
    global red_turtle_hitbox
    global green_turtle_hitbox
    global blue_turtle_hitbox
    global yellow_turtle_hitbox
    global crown
    global user_wallet
    global username_
    user_wallet = sys.argv[1]
    username_ = sys.argv[2]


    pygame.init()
    size = width, height = 800, 700
    gamescreen = pygame.display.set_mode(size)
    pygame.display.set_caption("Turtle Racing")
    clock = pygame.time.Clock()

    red_turtle_image = pygame.image.load("images/redturtle.png").convert_alpha()
    blue_turtle_image = pygame.image.load("images/blueturtle.png").convert_alpha()
    green_turtle_image = pygame.image.load("images/greenturtle.png").convert_alpha()
    yellow_turtle_image = pygame.image.load("images/yellowturtle.png").convert_alpha()
    eve_image = pygame.image.load("images/eve.png").convert_alpha()
    background = pygame.image.load("images/background.jpg")
    finish_line = pygame.image.load("images/finishline.jpg")
    turtle_banner = pygame.image.load("images/turtle_banner_final.png").convert_alpha()
    crown = pygame.image.load("images/crown.png").convert_alpha()

    red_turtle_pos = (0, 25)
    green_turtle_pos = (0, 170)
    blue_turtle_pos = (0, 330)
    yellow_turtle_pos = (0, 500)
    red_turtle_hitbox = pygame.Rect(0, 25, 145, 70)
    green_turtle_hitbox = pygame.Rect(0, 170, 145, 70)
    blue_turtle_hitbox = pygame.Rect(0, 330, 145, 70)
    yellow_turtle_hitbox = pygame.Rect(0, 500, 145, 70)
    end_game = False    #should not be changed
    Running = True
    while True:
        clock.tick(30)
        gamescreen.blit(background, (0, 0))
        gamescreen.blit(finish_line, (685, 0))
        gamescreen.blit(turtle_banner, (0, 565))
        if not Running:
            gamescreen.blit(red_turtle_image, red_turtle_pos)
            gamescreen.blit(green_turtle_image, green_turtle_pos)
            gamescreen.blit(blue_turtle_image, blue_turtle_pos)
            gamescreen.blit(yellow_turtle_image, yellow_turtle_pos)
        if end_game:
            crown_blit(winner)
            endgame(winner)

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

        myfont = pygame.font.SysFont("monospace", 20)
        user_label = myfont.render("username: " + username_, True, (0, 255, 0))
        money_label = myfont.render("balance: " + user_wallet, True, (0, 255, 0))
        gamescreen.blit(user_label, (20, 620))
        gamescreen.blit(money_label, (20, 660))
        # gamescreen.blit(winner_image(winner), (250, 600))
        # gamescreen.blit(crown, (363, 585))
        pygame.display.update()


def bet():
    pass

if __name__ == "__main__":
    startgame()