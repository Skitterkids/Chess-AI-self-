import chess.svg
from chessboard import display
import random
from time import sleep


def evaluate_position(fen):
    """ Evaluates the position of the board based on material
    :param fen:
    :return: evaluation
    """
    valuations = {'K': 100, 'Q': 9, 'R': 5, 'N': 3, 'B': 3, 'P': 1,  # White
                  'k': -100, 'q': -9, 'r': -5, 'n': -3, 'b': -3, 'p': -1,  # Black
                  }
    evaluation = 0
    for s in fen:
        # Only look at the characters that are actually in the dictionary
        if s in valuations:
            evaluation += valuations[s]
        # Only look at the part of fen that relates to pieces
        if s == ' ':
            break

    return evaluation


def find_best_move(b):
    """ Checks position evaluation in depth 1 search and chooses best move for player
    :param b:
    :return move:
    """
    moves = list(b.legal_moves)
    vs = {}
    [vs.setdefault(i, []) for i in range(-50, 50, 1)]

    for i, move in zip(range(len(moves)), moves):
        b.push(move)
        v = evaluate_position(b.fen())
        vs[v].append(move)
        #print("here", b.fen)
        b.pop()
        #print("here2", b.fen)

    for i in range(-50, 50, 1):
        if not vs[i]: vs.pop(i)

    if b.turn:
        move = random.choice(vs[max(vs)])
    else:
        move = random.choice(vs[min(vs)])
    return move
