#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 12:57:15 2020

@author: sasaki

Notes: Working directory should be guess_number_game.
Run as python -m pytest ./tests/test_utils.py
"""

import pytest
import guess_number_game.utils as utils


def test_for_right_guess():
    assert utils.eval_guess(2, 2) == ("Well done!", 1)


def test_for_larger_guess():

    assert utils.eval_guess(2, 3) == ("Guess lower!", 0)


def test_for_smaller_guess():

    assert utils.eval_guess(2, 1) == ("Guess higher!", 0)


 
##!/usr/bin/env python3
## -*- coding: utf-8 -*-
#"""
#Created on Sun Mar  8 12:57:15 2020
#
#@author: sasaki
#
#Notes: Working directory should be guess_number_game.
#Run as python -m pytest ./tests/test_utils.py
#"""
#
#import pytest
#import guess_number_game.utils as utils
#
#
#def test_for_right_guess():
#
#    actual = utils.eval_guess(2, 2)
#    expected = ("Well done!", 1)
#    message = ("The number guessed should be the same as the number chosen.")
#    assert actual is expected, message
#
#
#def test_for_larger_guess():
#
#    actual = utils.eval_guess(2, 3)
#    expected = ("Guess lower!", 0)
#    message = ("The number guessed should be larger than the number chosen.")
#    assert actual is expected, message
#
#
#def test_for_smaller_guess():
#
#    actual = utils.eval_guess(2, 1)
#    expected = ("Guess higher!", 0)
#    message = ("The number guessed should be smaller than the number chosen.")
#    assert actual is expected, message
#    