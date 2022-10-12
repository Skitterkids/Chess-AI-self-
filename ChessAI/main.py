import random
import chess.svg
import pygame.display
from chessboard import display
from time import sleep
from pathlib import Path

TIME = .1

#Pieces
b = pygame.image.load("./images/BB.png")
k = pygame.image.load("./images/BK.png")
n = pygame.image.load("./images/BN.png")
p = pygame.image.load("./images/BP.png")
q = pygame.image.load("./images/BQ.png")
r = pygame.image.load("./images/BR.png")
B = pygame.image.load("./images/WB.png")
K = pygame.image.load("./images/WK.png")
N = pygame.image.load("./images/WN.png")
P = pygame.image.load("./images/WP.png")
Q = pygame.image.load("./images/WQ.png")
R = pygame.image.load("./images/WR.png")


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        white = (118, 150, 86)
        black = (238, 238, 210)
        self.screen.fill(white)
        cnt = 0
        for x in range(8):
            for y in range(8):
                if (cnt % 2 != 0):
                    pygame.draw.rect(self.screen, black, [(100 * x) , (100 * y) , 100, 100])
                cnt += 1
            cnt -= 1

    def gameloop(self):
        board = chess.Board()
        pygame.display.set_caption('Chess')
        screen = self.screen
        for i in list(board.piece_map()):
            x = i % 8
            y = i // 8
            piece = board.piece_map()[i].symbol()
            if(piece == "p"):
                screen.blit(p, ((x * 100)+10, (y * 100)+10))
            elif (piece == "n"):
                screen.blit(n, ((x * 100)+10, (y * 100)+10))
            elif (piece == "b"):
                screen.blit(b, ((x * 100)+10, (y * 100)+10))
            elif (piece == "r"):
                screen.blit(r, ((x * 100)+10, (y * 100)+10))
            elif (piece == "q"):
                screen.blit(q, ((x * 100)+10, (y * 100)+10))
            elif (piece == "k"):
                screen.blit(b, ((x * 100)+10, (y * 100)+10))

            if (piece == "P"):
                screen.blit(P, ((x * 100)+10, (y * 100)+10))
            elif (piece == "N"):
                screen.blit(N, ((x * 100)+10, (y * 100)+10))
            elif (piece == "B"):
                screen.blit(B, ((x * 100)+10, (y * 100)+10))
            elif (piece == "R"):
                screen.blit(R, ((x * 100)+10, (y * 100)+10))
            elif (piece == "Q"):
                screen.blit(Q, ((x * 100)+10, (y * 100)+10))
            elif (piece == "K"):
                screen.blit(K, ((x * 100)+10, (y * 100)+10))
            self.screen = pygame.display.update()
        #sleep(10)

#window = Main()
#window.gameloop()

#Pseudo: in a while loop inside the main while loop (that acts as the human move, ie, wait for input of piece),
# have the two clicks (and in the future a drag), that together make a UCI move and check it against legal moves. then
# make that move the 'enginemove' and update BOTH squares of the move (incase there is a capture).

#- the mouse_x position relative to the screen is going to be in relation to the monitor so: x_real = (monitor_dimension_x / 2) - 400
#- the drag (like in chess.com) remains true as long as a) the mouse stops on a legal move, b) lands inside the display

#while 1:
#    for event in pygame.event.get():
#        if event.type in (QUIT, KEYDOWN):
#            sys.exit()
#    move_and_draw_all_game_objects()

#while not display.check_for_quit(): #display remains open until true
#    legal_moves = list(board.legal_moves) #uci list
#    enginemove = random.choice(legal_moves) #real engine move (e2e4)
#    board.san_and_push(enginemove)
#    valid_fen = board.fen()
#    display.update(valid_fen, game_board)
#    sleep(TIME)