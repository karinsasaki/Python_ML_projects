#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 12:57:15 2020

@author: sasaki
"""


def eval_guess(chosen, guess):

    """Check if the number guessed by the user is the same as the number chosen by the program.

    Parameters:
        chosen (int>=0): Number chosen by the program.

        guess (int>=0): Number guessed by the user.

    Returns:
        (str): Hint to help the user in the next guess; one of: "Well done!", "Guess lower!", "Guess higher!".

        (int): 1 if the guess is the same as the chosen; 0 otherwise.
    """

    if guess == chosen:
        val = 1
        return("Well done!", val)

    elif guess > chosen:
        val = 0
        return("Guess lower!", val)

    else:
        val = 0
        return("Guess higher!", val)

