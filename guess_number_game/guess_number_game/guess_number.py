#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 12:56:50 2020

@author: sasaki
"""

import random
import guess_number_game.utils as utils

#class Chosen:
#    """Class of the chosen number.
#
#    min_bound (int>=0): minimum bound of range the program can choose a number from. Default is 0. 
#    max_bound (int>=1): maximum bound of range the program can choose a number from. Default is 10.
#    """
#
#    def __init__(self, min_bound=0, max_bound=11):
#        self.value = random.randint(min_bound, max_bound)
#        self.bound_min = min_bound
#        self.bound_max = max_bound
#        self.digits_sum = None
#        self.parity = None
#
#    def get_digits_sum(self):
#        r = 0
#        n = self.value
#        while n:
#            r, n = r + n % 10, n // 10
#        print(r)
#        self.digits_sum = r
#
#    def get_parity(self):
#        if (self.value % 2) == 0:
#            print('even')
#            self.parity = 'even'
#        else:
#            print('odd')
#            self.parity = 'odd' 


def play_game(min_bound=0, max_bound=11, num_trials=5, seed=False):
    """Program randomly chooses a positive integer. Then prompts the user to guess the chosen number. In each wrong attempt the program will give a hint that the number is greater or smaller than the one guessed. Optionally, the user is also allowed to find out more information about the number, by querying the variable attributes.

Parameters:
    min_bound (int>=0): minimum bound of range the program can choose a number from. Default is 0. 

    max_bound (int>=1): maximum bound of range the program can choose a number from. Default is 10.

    num_trials (int>=1): number of chances user has to guess the correct number. Default is 5.

Returns:
    val (int): 1 if the user huessed correctly, 0 if not.
    """

    # check input parameters make sense
    if max_bound <= min_bound:
        raise ValueError#, ("max_bound should be greater than min_bound.")

    if num_trials <= 0:
        raise ValueError#, ("num_trials needs to be greater than 0.")

    # randonly choose a number
#    chosen = Chosen(min_bound, max_bound)
    if seed:
        random.seed(seed)

    chosen = random.randint(min_bound, max_bound)

    trial = num_trials

    # give the user n goes
    while trial >= 0:

        if trial == 0:
            print("Game over.")

        else:
            print("You have {} goes left.".format(trial))

            # ask the user to guess the number
            guess = int(input("Please guess an integer between {} and {}: ".format(min_bound, max_bound-1)))

            # compare guessed number to chosen number and print hint
            [txt, val] = utils.eval_guess(chosen, guess)
            print(txt)
            trial = trial - 1
            if val == 1:
                break

    return(val)