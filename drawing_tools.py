import pygame
from Pieces.piece import *


def draw_squares(screen, chess_board):
    """ Draws squares on pygame screen
    :param screen: pygame screen object
    :param chess_board: 2D list of BoardSquare objects
    :return: None
    """
    for row in chess_board:
        for square in row:
            surf = pygame.Surface((square.width_height, square.width_height))

            if square.color == "WHITE":
                surf.fill((200, 200, 200))
            else:
                surf.fill((50, 50, 50))

            screen.blit(surf, (square.x_start, square.y_start))

    pygame.display.flip()


def draw_board(screen, chess_board, fen):
    fen = fen.split()
    fen = fen[0].split('/')
    row, col = 0, 0
    for fen_row in fen:
        for c in fen_row:
            square = chess_board[row][col]
            if c == 'p':
                screen.blit(Pawn('BLACK').piece_image, (square.x_start, square.y_start))
            elif c == 'n':
                screen.blit(Knight('BLACK').piece_image, (square.x_start, square.y_start))
            elif c == 'b':
                screen.blit(Bishop('BLACK').piece_image, (square.x_start, square.y_start))
            elif c == 'r':
                screen.blit(Rook('BLACK').piece_image, (square.x_start, square.y_start))
            elif c == 'q':
                screen.blit(Queen('BLACK').piece_image, (square.x_start, square.y_start))
            elif c == 'k':
                screen.blit(King('BLACK').piece_image, (square.x_start, square.y_start))
            elif c == 'P':
                screen.blit(Pawn('WHITE').piece_image, (square.x_start, square.y_start))
            elif c == 'N':
                screen.blit(Knight('WHITE').piece_image, (square.x_start, square.y_start))
            elif c == 'B':
                screen.blit(Bishop('WHITE').piece_image, (square.x_start, square.y_start))
            elif c == 'R':
                screen.blit(Rook('WHITE').piece_image, (square.x_start, square.y_start))
            elif c == 'Q':
                screen.blit(Queen('WHITE').piece_image, (square.x_start, square.y_start))
            elif c == 'K':
                screen.blit(King('WHITE').piece_image, (square.x_start, square.y_start))
            else:
                col += int(c) - 1
            col += 1
        row += 1
        col = 0

        pygame.display.flip()


def assign_pieces(screen, chess_board, fen):
    fen = fen.split()
    fen = fen[0].split('/')
    row, col = 0, 0
    for fen_row in fen:
        for c in fen_row:
            square = chess_board[row][col]
            if c == 'p':
                square.piece = Pawn('BLACK')
                square.piece_FEN = c
            elif c == 'n':
                square.piece = Knight('BLACK')
                square.piece_FEN = c
            elif c == 'b':
                square.piece = Bishop('BLACK')
                square.piece_FEN = c
            elif c == 'r':
                square.piece = Rook('BLACK')
                square.piece_FEN = c
            elif c == 'q':
                square.piece = Queen('BLACK')
                square.piece_FEN = c
            elif c == 'k':
                square.piece = King('BLACK')
                square.piece_FEN = c
            elif c == 'P':
                square.piece = Pawn('WHITE')
                square.piece_FEN = c
            elif c == 'N':
                square.piece = Knight('WHITE')
                square.piece_FEN = c
            elif c == 'B':
                square.piece = Bishop('WHITE')
                square.piece_FEN = c
            elif c == 'R':
                square.piece = Rook('WHITE')
                square.piece_FEN = c
            elif c == 'Q':
                square.piece = Queen('WHITE')
                square.piece_FEN = c
            elif c == 'K':
                square.piece = King('WHITE')
                square.piece_FEN = c
            else:
                col += int(c) - 1
            col += 1
        row += 1
        col = 0

        pygame.display.flip()


def draw_position_by_fen(screen, chess_board, fen):
    """ Draws pieces on BoardSquare objects using a FEN string
    :param screen: pygame screen object
    :param chess_board: 2D list of BoardSquare objects
    :param fen: FEN string
    :return: None
    """
    fen = fen.split()
    fen = fen[0].split('/')
    row, col = 0, 0
    for fen_row in fen:
        for c in fen_row:
            square = chess_board[row][col]
            if c == 'p':
                square.piece = Pawn('BLACK')
                screen.blit(square.piece.piece_image, (square.x_start, square.y_start))
            elif c == 'n':
                chess_board[row][col].piece = Knight('BLACK')
                screen.blit(square.piece.piece_image, (square.x_start, square.y_start))
            elif c == 'b':
                chess_board[row][col].piece = Bishop('BLACK')
                screen.blit(square.piece.piece_image, (square.x_start, square.y_start))
            elif c == 'r':
                chess_board[row][col].piece = Rook('BLACK')
                screen.blit(square.piece.piece_image, (square.x_start, square.y_start))
            elif c == 'q':
                chess_board[row][col].piece = Queen('BLACK')
                screen.blit(square.piece.piece_image, (square.x_start, square.y_start))
            elif c == 'k':
                chess_board[row][col].piece = King('BLACK')
                screen.blit(square.piece.piece_image, (square.x_start, square.y_start))
            elif c == 'P':
                square.piece = Pawn('WHITE')
                screen.blit(square.piece.piece_image, (square.x_start, square.y_start))
            elif c == 'N':
                chess_board[row][col].piece = Knight('WHITE')
                screen.blit(square.piece.piece_image, (square.x_start, square.y_start))
            elif c == 'B':
                chess_board[row][col].piece = Bishop('WHITE')
                screen.blit(square.piece.piece_image, (square.x_start, square.y_start))
            elif c == 'R':
                chess_board[row][col].piece = Rook('WHITE')
                screen.blit(square.piece.piece_image, (square.x_start, square.y_start))
            elif c == 'Q':
                chess_board[row][col].piece = Queen('WHITE')
                screen.blit(square.piece.piece_image, (square.x_start, square.y_start))
            elif c == 'K':
                chess_board[row][col].piece = King('WHITE')
                screen.blit(square.piece.piece_image, (square.x_start, square.y_start))
            else:
                col += int(c) - 1
            col += 1
        row += 1
        col = 0

        pygame.display.flip()


def update_board(screen, chess_board, fen):
    fen = fen.split()
    fen = fen[0].split('/')
    row, col = 0, 0
    print(fen)
    for fen_row in fen:
        c_max = len(fen_row)
        for c in fen_row:
            square = chess_board[row][col]
            if col >= c_max:
                continue
            if c != square.piece_FEN:
                print(square.piece_FEN, square.position, c)
                square.piece_FEN = c
                if c == 'p':
                    square.piece = Pawn('BLACK')
                elif c == 'n':
                    square.piece = Knight('BLACK')
                elif c == 'b':
                    square.piece = Bishop('BLACK')
                elif c == 'r':
                    square.piece = Rook('BLACK')
                elif c == 'q':
                    square.piece = Queen('BLACK')
                elif c == 'k':
                    square.piece = King('BLACK')
                elif c == 'P':
                    square.piece = Pawn('WHITE')
                elif c == 'N':
                    square.piece = Knight('WHITE')
                elif c == 'B':
                    square.piece = Bishop('WHITE')
                elif c == 'R':
                    square.piece = Rook('WHITE')
                elif c == 'Q':
                    square.piece = Queen('WHITE')
                elif c == 'K':
                    square.piece = King('WHITE')
                #print(square.piece)
                screen.blit(square.piece.piece_image, (square.x_start, square.y_start))
            col += 1
        row += 1
        col = 0

        pygame.display.flip()


def update_board2(screen, chess_board, fen):
    fen = fen.split()
    fen = fen[0].split('/')
    print(fen)
    for row, c in zip(range(8), fen):
        row_max = len(c)
        # print(row_max)
        for col in range(8):
            square = chess_board[row][col]
            if col >= row_max:
                continue
            else:
                print(square.piece, c[col])
                # if square.piece != c[col]:
                #    print(square.position, end=" ")
                # print(c[col])

        pygame.display.flip()
