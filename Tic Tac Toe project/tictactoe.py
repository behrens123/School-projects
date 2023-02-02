import pygame
from pygame.locals import *
import pygame_gui
import random
from tkinter import *
from tkinter import messagebox

# class contains win condition, game reset, and random color change function.
class TicTacToe():

    def __init__(self):
        pass

    def win():

        global winner
        if (box_1ox != None and box_1ox%2 != 0) and (box_2ox != None and box_2ox%2 != 0) and (box_3ox != None and box_3ox%2 != 0):
        #X wins
            pygame.display.set_caption('X WINS!!! (press r to restart)')
            winner = True
            
        elif (box_7ox != None and box_7ox%2 != 0) and (box_8ox != None and box_8ox%2 != 0) and (box_9ox != None and box_9ox%2 != 0):
        #X wins
            pygame.display.set_caption('X WINS!!! (press r to restart)')
            winner = True

        elif (box_1ox != None and box_1ox%2 != 0) and (box_4ox != None and box_4ox%2 != 0) and (box_7ox != None and box_7ox%2 != 0):
        #X wins
            pygame.display.set_caption('X WINS!!! (press r to restart)')
            winner = True

        elif (box_2ox != None and box_2ox%2 != 0) and (box_5ox != None and box_5ox%2 != 0) and (box_8ox != None and box_8ox%2 != 0):
        #X wins
            pygame.display.set_caption('X WINS!!! (press r to restart)')
            winner = True

        elif (box_4ox != None and box_4ox%2 != 0) and (box_5ox != None and box_5ox%2 != 0) and (box_6ox != None and box_6ox%2 != 0):
        #X wins
            pygame.display.set_caption('X WINS!!! (press r to restart)')
            winner = True

        elif (box_3ox != None and box_3ox%2 != 0) and (box_6ox != None and box_6ox%2 != 0) and (box_9ox != None and box_9ox%2 != 0):
        #X wins
            pygame.display.set_caption('X WINS!!! (press r to restart)')
            winner = True

        elif (box_1ox != None and box_1ox%2 != 0) and (box_5ox != None and box_5ox%2 != 0) and (box_9ox != None and box_9ox%2 != 0):
        #X wins
            pygame.display.set_caption('X WINS!!! (press r to restart)')
            winner = True

        elif (box_3ox != None and box_3ox%2 != 0) and (box_5ox != None and box_5ox%2 != 0) and (box_7ox != None and box_7ox%2 != 0):
        #X wins
            pygame.display.set_caption('X WINS!!! (press r to restart)')
            winner = True

        elif (box_1ox != None and box_1ox%2==0) and (box_2ox != None and box_2ox%2==0) and (box_3ox != None and box_3ox%2==0):
        #O wins
            pygame.display.set_caption('O WINS!!! (press r to restart)')
            winner = True

        elif (box_4ox != None and box_4ox%2==0) and (box_5ox != None and box_5ox%2==0) and (box_6ox != None and box_6ox%2==0):
        #O wins
            pygame.display.set_caption('O WINS!!! (press r to restart)')
            winner = True

        elif (box_7ox != None and box_7ox%2==0) and (box_8ox != None and box_8ox%2==0) and (box_9ox != None and box_9ox%2==0):
        #O wins
            pygame.display.set_caption('O WINS!!! (press r to restart)')
            winner = True

        elif (box_1ox != None and box_1ox%2==0)  and (box_4ox != None and box_4ox%2==0) and (box_7ox != None and box_7ox%2==0):
        #O wins
            pygame.display.set_caption('O WINS!!! (press r to restart)')
            winner = True

        elif (box_2ox != None and box_2ox%2==0) and (box_5ox != None and box_5ox%2==0) and (box_8ox != None and box_8ox%2==0):
        #O wins
            pygame.display.set_caption('O WINS!!! (press r to restart)')
            winner = True

        elif (box_3ox != None and box_3ox%2==0) and (box_6ox != None and box_6ox%2==0) and (box_9ox != None and box_9ox%2==0):
        #O wins
            pygame.display.set_caption('O WINS!!! (press r to restart)')
            winner = True

        elif (box_1ox != None and box_1ox%2==0) and (box_5ox != None and box_5ox%2==0) and (box_9ox != None and box_9ox%2==0):
        #O wins
            pygame.display.set_caption('O WINS!!! (press r to restart)')
            winner = True

        elif (box_3ox != None and box_3ox%2==0) and (box_5ox != None and box_5ox%2==0) and (box_7ox != None and box_7ox%2==0):
        #O wins
            pygame.display.set_caption('O WINS!!! (press r to restart)')
            winner = True

        elif box_1_full and box_2_full and box_3_full and box_4_full and box_5_full and box_6_full and box_7_full and box_8_full and box_9_full==True:
        #TIE
            pygame.display.set_caption('TIE!!! (press r to restart)')
            winner = True

    def game_reset():
#resets all necessary variables and starts a new game
        global box_1_full, box_2_full, box_3_full, box_4_full, box_5_full, box_6_full, box_7_full, box_8_full, box_9_full
        global box_1ox, box_2ox, box_3ox, box_4ox, box_5ox, box_6ox, box_7ox, box_8ox, box_9ox
        global sw
        global winner

        box_1_full = False
        box_2_full = False
        box_3_full = False
        box_4_full = False
        box_5_full = False
        box_6_full = False
        box_7_full = False
        box_8_full = False
        box_9_full = False

        winner = False

        box_1ox=None
        box_2ox=None
        box_3ox=None
        box_4ox=None
        box_5ox=None
        box_6ox=None
        box_7ox=None
        box_8ox=None
        box_9ox=None

        game_display.fill(colors[rc])
        game_display.blit(board, (-50, 100))
        sw = 0
        pygame.display.set_caption('Tacky Toe')
 #Changes the color of the background each time game is played
    def change_color():
        rc=random.randint(0,12)
        game_display.fill(colors[rc])
        game_display.blit(board, (-50, 100))
    





# object hitboxes for each individual square labeled 1-9
box_1 = pygame.Rect(200, 140, 110, 110)
box_1_full = False
box_2 = pygame.Rect(350, 140, 110, 110)
box_2_full = False
box_3 = pygame.Rect(510, 140, 110, 110)
box_3_full = False
box_4 = pygame.Rect(200, 300, 110, 115)
box_4_full = False
box_5 = pygame.Rect(350, 300, 110, 115)
box_5_full = False
box_6 = pygame.Rect(510, 300, 110, 115)
box_6_full = False
box_7 = pygame.Rect(200, 460, 110, 110)
box_7_full = False
box_8 = pygame.Rect(350, 460, 110, 110)
box_8_full = False
box_9 = pygame.Rect(510, 460, 110, 110)
box_9_full = False

winner = False

box_1ox=None
box_2ox=None
box_3ox=None
box_4ox=None
box_5ox=None
box_6ox=None
box_7ox=None
box_8ox=None
box_9ox=None

# game setup variables
pygame.init()
display_width = 800
display_height = 700

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue=(0,0,255)
yellow=(255,255,0)
pink=(255,0,255)
turquoise=(0,255,255)
dark_green=(0,128,0)
navy=(0,0,128)
lilac=(153,153,255)
bright_red = (255, 0, 0)
green = (0, 200, 0)
bright_green = (0, 255, 0)
crimson = (220, 20, 60)
boxes=[box_1ox,box_2ox,box_3ox,box_4ox,box_5ox,box_6ox,box_7ox,box_8ox,box_9ox]
colors=[white,yellow,pink,turquoise,dark_green,navy,lilac,red,bright_red,blue,green,bright_green,crimson]
rc=random.randint(0,12)
rb=random.randint(0,8)
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tacky Toe')
clock = pygame.time.Clock()
title = pygame.image.load('tackytoe.png')
scaled_title = pygame.transform.scale(title, (500, 150))
board = pygame.image.load('tic_board.png')
x = pygame.image.load('tic_x.png')
o = pygame.image.load('tic_o.png')
sw = 0
clicked=False
rb_not_full=False
manager = pygame_gui.UIManager((800, 700), 'theme.json')
one_player_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100,275), (200,100)), text='one player', manager=manager)
two_player_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 275), (200, 100)), text='two player', manager=manager)
rules_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 500), (100, 50)), text='rules', manager=manager)

background = pygame.Surface((800, 700))
background.fill(pygame.Color(crimson))

# main game play


# menu (JSON File needed for optimized menu design)
running = True

while running == True:

    game_display.blit(background, (0, 0))
    game_display.blit(scaled_title, (150, 75))

    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_q:
                pygame.quit()
                quit()

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == two_player_button:
                running = False
            if event.ui_element == one_player_button:
                #this is the 1 player game mode code below
                game_over = False
                game_display.fill(colors[rc])
                game_display.blit(board, (-50, 100))
                while not game_over:
                    
                    TicTacToe()

                    mouse_x, mouse_y = pygame.mouse.get_pos()
#This is the code used to get the players placement
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
        
                        if event.type == pygame.KEYDOWN:
                            if event.key == K_r:
                                TicTacToe.game_reset()
                                TicTacToe.change_color()
                            if event.key == K_q:
                                pygame.quit()
                                quit()
                        clicked=False
                        sw=1
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if box_1.collidepoint(event.pos):
                                if box_1_full == False and winner == False:
                                    box_1_full = True
                                    box_1ox = sw
                                    game_display.blit(x, (200, 150))
                                    clicked=True

                            if box_2.collidepoint(event.pos):
                                if box_2_full == False and winner == False:
                                    box_2_full = True
                                    box_2ox = sw
                                    game_display.blit(x, (353, 150))
                                    clicked=True
        
            
                            if box_3.collidepoint(event.pos):
                                if box_3_full == False and winner == False:
                                    box_3_full = True
                                    box_3ox = sw
                                    game_display.blit(x, (510, 150))
                                    clicked=True
            

                            if box_4.collidepoint(event.pos):
                                if box_4_full == False and winner == False:
                                    box_4_full = True
                                    box_4ox = sw
                                    game_display.blit(x, (200, 300))
                                    clicked=True
            
            
                            if box_5.collidepoint(event.pos):
                                if box_5_full == False and winner == False:
                                    box_5_full = True
                                    box_5ox = sw
                                    game_display.blit(x, (353, 300))
                                    clicked=True
            
            
                            if box_6.collidepoint(event.pos):
                                if box_6_full == False and winner == False:
                                    box_6_full = True
                                    box_6ox = sw
                                    game_display.blit(x, (510, 300))
                                    clicked=True
            
            
                            if box_7.collidepoint(event.pos):
                                if box_7_full == False and winner == False:
                                    box_7_full = True
                                    box_7ox = sw
                                    game_display.blit(x, (200, 460))
                                    clicked=True
            
            
                            if box_8.collidepoint(event.pos):
                                if box_8_full == False and winner == False:
                                    box_8_full = True
                                    box_8ox = sw
                                    game_display.blit(x, (353, 460))
                                    clicked=True
            
            
                            if box_9.collidepoint(event.pos):
                                if box_9_full == False and winner == False:
                                    box_9_full = True
                                    box_9ox = sw
                                    game_display.blit(x, (510, 460))
                                    clicked=True
                    

                            TicTacToe.win()
                            sw=2
                            rb_not_full=False
                            rb=random.randint(0,8)
                            #Code for the AI placement of O
                            while rb_not_full is not True and winner == False:
                                if boxes[rb] != None:
                                    rb=random.randint(0,8)
                                elif boxes[rb] == None:
                                    rb_not_full=True
                                    
                            if clicked == True and winner == False:
                                if boxes[rb] == box_1ox:
                                    if box_1_full == False and winner == False:
                                        box_1ox = sw
                                        game_display.blit(o, (200, 150))
                                        box_1_full = True

                                elif boxes[rb] == box_9ox:
                                    if box_9_full == False and winner == False:
                                        box_9ox = sw
                                        game_display.blit(o, (510, 460))
                                        box_9_full = True

                                elif boxes[rb] == box_3ox:
                                    if box_3_full == False and winner == False:
                                        box_3ox = sw
                                        game_display.blit(o, (510, 150))
                                        box_3_full = True

                                elif boxes[rb] == box_2ox:
                                    if box_2_full == False and winner == False:
                                        box_2ox = sw
                                        game_display.blit(o, (353, 150))
                                        box_2_full = True
                                
                                elif boxes[rb] == box_6ox:
                                    if box_6_full == False and winner == False:
                                        box_6ox = sw
                                        game_display.blit(o, (510, 300))
                                        box_6_full = True

                                elif boxes[rb] == box_4ox:
                                    if box_4_full == False and winner == False:
                                        box_4ox = sw
                                        game_display.blit(o, (200, 300))
                                        box_4_full = True

                                elif boxes[rb] == box_8ox:
                                    if box_8_full == False and winner == False:
                                        box_8ox = sw
                                        game_display.blit(o, (353, 460))
                                        box_8_full = True

                                elif boxes[rb] == box_5ox:
                                    if box_5_full == False and winner == False:
                                        box_5ox = sw
                                        game_display.blit(o, (353, 300))
                                        box_5_full = True
                                
                                elif boxes[rb] == box_7ox:
                                    if box_7_full == False and winner == False:
                                        box_7ox = sw
                                        game_display.blit(o, (200, 460))
                                        box_7_full = True
                    
                    clock.tick(10)
                    pygame.display.update()
                    TicTacToe.win()
                    
            if event.ui_element == rules_button:
                Tk().wm_withdraw() #to hide the main window
                messagebox.showinfo('Rules',' 1. The game is played on a grid that 3 squares by 3 squares. \n \n 2. You are X, your friend is O. Players take turns putting their marks in empty squares. \n \n 3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner. \n \n 4. When all 9 squares are full, the game is over ( press R to reset). If no player has 3 marks in a row, the game ends in a tie. ')
            
            
        
    manager.process_events(event)

    manager.update(time_delta)
    manager.process_events(event)
    manager.draw_ui(game_display)
    pygame.display.update()


game_over = False
game_display.fill(colors[rc])
game_display.blit(board, (-50, 100))
#Below is the 2 player part of the game below
while not game_over:

    TicTacToe()

    mouse_x, mouse_y = pygame.mouse.get_pos()
#This is the code to get the placement of both players
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == K_r:
                #Key to reset game
                TicTacToe.game_reset()
                TicTacToe.change_color()
            if event.key == K_q:
                #Key to quit
                pygame.quit()
                quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if box_1.collidepoint(event.pos):
                if box_1_full == False and winner == False:
                    box_1_full = True
                    sw += 1
                    box_1ox = sw
                    if sw % 2 == 0:
                        game_display.blit(o, (200, 150))
                    
                    else:
                        game_display.blit(x, (200, 150))

            if box_2.collidepoint(event.pos):
                if box_2_full == False and winner == False:
                    box_2_full = True
                    sw += 1
                    box_2ox = sw
                    if sw % 2 == 0:
                        game_display.blit(o, (353, 150))
                
                    else:
                        game_display.blit(x, (353, 150))
        
            
            if box_3.collidepoint(event.pos):
                if box_3_full == False and winner == False:
                    box_3_full = True
                    sw += 1
                    box_3ox = sw
                    if sw % 2 == 0:
                        game_display.blit(o, (510, 150))
                
                    else:
                        game_display.blit(x, (510, 150))
            

            if box_4.collidepoint(event.pos):
                if box_4_full == False and winner == False:
                    box_4_full = True
                    sw += 1
                    box_4ox = sw
                    if sw % 2 == 0:
                        game_display.blit(o, (200, 300))
                
                    else:
                        game_display.blit(x, (200, 300))
            
            
            if box_5.collidepoint(event.pos):
                if box_5_full == False and winner == False:
                    box_5_full = True
                    sw += 1
                    box_5ox = sw
                    if sw % 2 == 0:
                        game_display.blit(o, (353, 300))
                
                    else:
                        game_display.blit(x, (353, 300))
            
            
            if box_6.collidepoint(event.pos):
                if box_6_full == False and winner == False:
                    box_6_full = True
                    sw += 1
                    box_6ox = sw
                    if sw % 2 == 0:
                        game_display.blit(o, (510, 300))
                
                    else:
                        game_display.blit(x, (510, 300))
            
            
            if box_7.collidepoint(event.pos):
                if box_7_full == False and winner == False:
                    box_7_full = True
                    sw += 1
                    box_7ox = sw
                    if sw % 2 == 0:
                        game_display.blit(o, (200, 460))
                
                    else:
                        game_display.blit(x, (200, 460))
            
            
            if box_8.collidepoint(event.pos):
                if box_8_full == False and winner == False:
                    box_8_full = True
                    sw += 1
                    box_8ox = sw
                    if sw % 2 == 0:
                        game_display.blit(o, (353, 460))
                
                    else:
                        game_display.blit(x, (353, 460))
            
            
            if box_9.collidepoint(event.pos):
                if box_9_full == False and winner == False:
                    box_9_full = True
                    sw += 1
                    box_9ox = sw
                    if sw % 2 == 0:
                        game_display.blit(o, (510, 460))
                
                    else:
                        game_display.blit(x, (510, 460))


    clock.tick(10)
    pygame.display.update()
    TicTacToe.win()


pygame.quit()
quit()
