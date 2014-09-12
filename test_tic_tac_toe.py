#!/usr/bin/env python

from tic_tac_toe import (print_board, get_player_token_choice,
                         who_goes_first, get_player_move, get_computer_move,
                         is_space_free, is_there_a_win, get_play_again,
                         is_board_full)


def test_print_board():

    board = [None, None, None,
             None, None, None,
             None, None, None]

    expected = ("   |   |   \n"
                " 1 | 2 | 3 \n"
                "   |   |   \n"
                "-----------\n"
                "   |   |   \n"
                " 4 | 5 | 6 \n"
                "   |   |   \n"
                "-----------\n"
                "   |   |   \n"
                " 7 | 8 | 9 \n"
                "   |   |   \n")

    result = print_board(board)

    assert result == expected

    board = ['o', None, 'o',
             'x', None, None,
             'o', None, 'x']

    expected = ("   |   |   \n"
                " O | 2 | O \n"
                "   |   |   \n"
                "-----------\n"
                "   |   |   \n"
                " X | 5 | 6 \n"
                "   |   |   \n"
                "-----------\n"
                "   |   |   \n"
                " O | 8 | X \n"
                "   |   |   \n")

    result = print_board(board)

    assert result == expected


def test_get_player_token_choice():

    result = get_player_token_choice()

    assert result == 'x' or result == 'o'


def test_who_goes_first():

    result = who_goes_first()

    assert result == 'x' or result == 'o'


def test_get_player_move():

    board = ['o', None, 'o',
             'x', None, None,
             'o', None, 'x']

    result = get_player_move(board, 'x')

    assert result in [2, 5, 6, 8]


def test_get_computer_move():

    board = ['o', None, 'o',
             'x', None, None,
             'o', None, 'x']

    result = get_computer_move(board, 'o')

    assert result in [2, 5, 6, 8]


def test_is_space_free():

    board = ['o', 'o', 'x',
             None, None, 'x',
             'o', None, 'x']

    assert is_space_free(board, 4) == True
    assert is_space_free(board, 1) == False


def test_is_there_a_win():

    board = ['o', None, 'o',
             'x', None, None,
             'o', None, 'x']

    result = is_there_a_win(board)

    assert result == 'no'

    board = ['o', 'o', 'o',
             'x', None, 'x',
             'o', 'x', None]

    result = is_there_a_win(board)

    assert result == 'o'

    board = ['o', 'o', 'x',
             None, None, 'x',
             'o', None, 'x']

    result = is_there_a_win(board)

    assert result == 'x'


def test_get_play_again():

    result = get_play_again()

    assert result is True or result is False


def test_is_board_full():

    board = [None, None, None,
             None, None, None,
             None, None, None]

    assert is_board_full(board) == False

    board = ['o', 'o', 'x',
             None, None, 'x',
             'o', None, 'x']

    assert is_board_full(board) == False

    board = ['x', 'o', 'x',
             'x', 'o', 'o',
             'o', 'x', 'x']

    assert is_board_full(board) == True


def run_all_tests():

    tests = [test_print_board,
             test_get_player_token_choice,
             test_who_goes_first,
             test_get_player_move,
             test_get_computer_move,
             test_is_space_free,
             test_is_there_a_win,
             test_get_play_again,
             test_is_board_full]

    for test in tests:
        try:
            test()
        except AssertionError:
            print('The {} failed.'.format(test.func_name))


if __name__ == "__main__":

    run_all_tests()
