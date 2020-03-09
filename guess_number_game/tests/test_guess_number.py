#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 12:56:50 2020

@author: sasaki


Notes: Working directory should be guess_number_game.
Run as python -m pytest ./tests/test_guess_number.py
"""

import pytest
from unittest import mock
import guess_number_game.guess_number as guess_number


# test max_bound > min_bound or raises ValueError
def test_bounds():
    with pytest.raises(ValueError):
        guess_number.play_game(min_bound=2, max_bound=1)

    #assert exception_info.match("max_bound should be greater than min_bound.")


# test num_trials > 0 or raises Value Error
def test_num_trials():

    with pytest.raises(ValueError):
        guess_number.play_game(num_trials=0)

    #assert exception_info.match("num_trials needs to be greater than 0.")


# test output when correctly guessed within num_trials
def test_correct_guess():

    with mock.patch('builtins.input', return_value=8):
        assert guess_number.play_game(seed=30, num_trials=1) == 1


# test output when could not guess chosen num
#def test_no_correct_guess():
#
#    with mock.patch('builtins.input', return_value=7):
#        assert guess_number.play_game(seed=30, num_trials=1) == 0
