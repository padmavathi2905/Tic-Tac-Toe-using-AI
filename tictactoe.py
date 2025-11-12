"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    In initial state, X moves first. Thereafter players alternate.
    For terminal boards, any value is acceptable; we return X.
    """
    # Count moves
    x_count = sum(cell == X for row in board for cell in row)
    o_count = sum(cell == O for row in board for cell in row)
    # X starts; if equal, X to move; else O.
    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    If the board is terminal, any return is acceptable; we return empty set.
    """
    if terminal(board):
        return set()
    moves = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell is EMPTY:
                moves.add((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board
    by the current player. Does not mutate the input board.
    Raises an exception if action is invalid.
    """
    i, j = action
    if i not in range(3) or j not in range(3):
        raise Exception("Action out of bounds")
    if board[i][j] is not EMPTY:
        raise Exception("Invalid action: cell occupied")

    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one; otherwise None.
    """
    lines = []

    # Rows and columns
    for idx in range(3):
        lines.append(board[idx])  # row
        lines.append([board[0][idx], board[1][idx], board[2][idx]])  # column

    # Diagonals
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for line in lines:
        if line[0] is not None and line.count(line[0]) == 3:
            return line[0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    # Any empty?
    return all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    Assumes called only on a terminal board.
    """
    w = winner(board)
    if w == X:
        return 1
    if w == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board using minimax with alpha-beta pruning.
    If the board is terminal, returns None.
    """
    if terminal(board):
        return None

    turn = player(board)

    def max_value(b, alpha=-math.inf, beta=math.inf):
        if terminal(b):
            return utility(b), None
        v = -math.inf
        best_move = None
        for act in sorted(actions(b)):  # sort for deterministic behavior
            val, _ = min_value(result(b, act), alpha, beta)
            if val > v:
                v = val
                best_move = act
                alpha = max(alpha, v)
            if v == 1:  # can't do better
                break
            if alpha >= beta:
                break
        return v, best_move

    def min_value(b, alpha=-math.inf, beta=math.inf):
        if terminal(b):
            return utility(b), None
        v = math.inf
        best_move = None
        for act in sorted(actions(b)):
            val, _ = max_value(result(b, act), alpha, beta)
            if val < v:
                v = val
                best_move = act
                beta = min(beta, v)
            if v == -1:  # can't do better
                break
            if alpha >= beta:
                break
        return v, best_move

    if turn == X:
        _, move = max_value(board)
    else:
        _, move = min_value(board)
    return move
