#!/usr/bin/env python

# You may need to add import here if you need functions from other modules.
# For example:
#
# import random


def print_board(board):
    """Returns a single string containing a visual representation of the
    board using ASCII text. Calling print() on the result should print the
    board to the screen."""

    # First try to make the test for this pass and if you want to make the
    # board look better then change the test first and then try to get your
    # function to reproduce the test.


def get_player_token_choice():
    """Return the player's choice of token."""

    # This function should make use of raw_input to ask the player what
    # token they'd like to use. The only valid tokens are 'x' and 'o', so
    # make sure to handle other inputs gracefully.


def who_goes_first():
    """Returns either the string 'x' or 'o'."""

    # This function should randomly choose whether the x's or the o's go
    # first.


def get_player_move(board, player_token):
    """Asks the player where they want to place their token 1-9 and returns
    that answer."""

    # Make use of the raw_input to ask the user a question. Make sure only
    # valid inputs work (use is_space_free function). The question should be
    # asked until the player gives a correct place for their token (a while
    # loop can help do that).


def get_computer_move(board, computer_token):
    """Returns the computer's choice of the next place."""

    # This is the AI of the game. It can be as simple as chosing a random
    # free space on the board (use is_space_free!) or more advanced AI that
    # has the best strategy.


def is_space_free(board, number):
    """Returns the boolean True or False. If True the space corresponding to
    the input number does not have an 'x' or a 'o'."""

    # If the player tries to place their 'x' or 'o' on an already occupied,
    # then the player should be asked to choose one of the free spots.


def is_there_a_win(board):
    """Returns either the string 'no', 'x', or 'o'."""

    # Create some logic that reviews the board and determines who wins, if
    # anyone.


def get_play_again():
    """Returns True or False based on the player's input of whether they
    want to play again."""

    # Make use of raw_input to ask the player whether they want to play
    # again.


def is_board_full(board):
    """Returns True or False to determine if the board is full or not."""

    # Review the board and check if it is full.


def main():
    """Starts the main game loop."""

    # main() should implement a while loop that runs through the game
    # sequence, it should end on a win or a draw (full board), and should
    # start over if the player wants to play again.

    # This code should make use of all the above functions as much as
    # possible. You will not be able to test the main program until all the
    # other functions are implemented by the other pairs.


if __name__ == "__main__":

    # This lets you type this in the terminal to run the program:
    #
    # $ python tic_tac_toe.py
    #
    # to start the game.

    main()
