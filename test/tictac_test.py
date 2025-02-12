from tictactoe import *

# Tests if a move is added correctly and a string is returned
def test_finds_successor():
    assert successor(INITIAL_STATE, 1, 'X') == '.X.......'

# Test to find the remaining legal moves
def test_finds_legal_moves():
    assert legal_moves('.X...O...') == [0, 2, 3, 4, 6, 7, 8]

# Tests if X won
def test_finds_win_for_x():
    assert winner('...XXX.OO') == 1
    assert winner('.XOOX..X.') == 1

# Tests if O won
def test_finds_win_for_o():
    assert winner('...X.XOOO') == -1

# Test for no winner
def test_finds_no_winner():
    assert winner('..OXOOXOX') == 0

# Finds total final result
def test_finds_value_at_end_of_game():
    assert min_value('...XXX.OO') == 1
    assert max_value('...XXX.OO') == 1
    assert min_value('OOOXOXXOX') == -1
    assert max_value('OOOXOXXOX') == -1

# Finds if there is a win in a single move
def test_finds_win_in_one_move():
    assert max_value('XX....O.O') == 1

# Finds if there is a win or loss after two moves
def test_finds_value_after_two_moves():
    assert min_value('XOXXXOO..') == 0

# Finds value after three moves
def test_finds_value_after_three_moves():
    assert min_value('.X.X.O.O.') == -1
    assert max_value('.X.X.O.O.') == 1
    assert value('.X.X.O.O.', 'X', greater, -2) == 1
    assert value('.X.X.O.O.', 'O', lesser, 2) == -1

def test_finds_best_move_depth_1():
    assert best_move_for_x('XX.O....O') == 2

def test_finds_best_move_deep():
    assert best_move_for_x('X..OO...X') == 5