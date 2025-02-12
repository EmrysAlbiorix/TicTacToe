INITIAL_STATE = '.........'

# Adds a move into the state and returns it as a string
# def successor(state, index, player):
#     board = list(state)
#     board[index] = player
#     return ''.join(board)

# More compact spliced version of function above
def successor(state, index, player):
    return state[:index] + player + state[index+1:]

# Checks remaining legal moves
def legal_moves(state):
    # i is each element in the range of the length of state, only counting if state at i is '.'
    return [i for i in range(len(state)) if state[i] == '.']

# Checks for a winner
def winner(state):
    lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
             [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
             [0, 4, 8], [2, 4, 6]]            # Diagonal
    for line in lines:
        if state[line[0]] == state[line[1]] == state[line[2]]:
            player = state[line[0]]
            if player == 'X':
                return 1
            if player == 'O':
                return -1
    return 0

"""
Return the value of state if it is min (O)'s turn.
"""
def min_value(state):
    if winner(state) != 0:
        return winner(state)
    if not legal_moves(state):
        return winner(state)
    best_value = 2
    for m in legal_moves(state):
        s = successor(state, m, 'O')
        value = max_value(s)
        if value < best_value:
            best_value = value
    return best_value

"""
Return the value of state if it is max (X)'s turn.
"""
def max_value(state):
    if winner(state) != 0:
        return winner(state)
    if not legal_moves(state):
        return winner(state)
    best_value = -2
    for m in legal_moves(state):
        s = successor(state, m, 'X')
        value = min_value(s)
        if value > best_value:
            best_value = value
    return best_value

# This function is the same as lambda a, b: a > b
def greater(a, b):
    return a > b

# This function is the same as lambda a, b: a < b
def lesser(a, b):
    return a < b

def value(state, player, better, bad):
    """
    Returns the value of state if it is player's turn
    :param better takes two values and returns True if the first is better.
    :param bad a value worse than anything we will see.
    lambda just creates an unnamed function that returns the shit after :
    """
    if winner(state) != 0: # Someone has already won
        return winner(state)
    if not legal_moves(state): # Game ended in a tie
        return 0
    best_value = bad
    for m in legal_moves(state):
        s = successor(state, m, player)
        if player == 'X':
            v = value(s, 'O', lambda a, b: a < b, 2)
        else:
            v = value(s, 'X', lambda a, b: a > b, -2)
        if better(v, best_value):
            best_value = v
    return best_value

def best_move_for_x(state):
    best_value = -2
    best_move = None
    for m in legal_moves(state):
        s = successor(state, m, 'X')
        v = value(s, 'O', lesser, 2)
        if v > best_value:
            best_value = v
            best_move = m
    return best_move