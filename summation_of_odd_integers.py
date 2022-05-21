# -*- coding: utf-8 -*-
"""
Created on Thu May 19 13:23:24 2022

@author: Andy
"""


def summation_of_odd_integers(lower_bound, upper_bound):
    '''
    Return sum of odd integers between an inclusive lower bound and an inclusive upper bound.
    
    Parameters
    ----------
    lower_bound : int
        Lower bound integer.
    upper_bound : int
        Upper bound integer.

    Returns
    -------
    running_total : int
        Sum total of all odd integers from a lower bound to an upper bound both being inclusive.  

    '''
    value = range(lower_bound, upper_bound + 1)

    running_total = 0

    for number in value:
        if number % 2 != 0:
            running_total = running_total + number
    
    print(running_total)
    return running_total


summation_of_odd_integers(3, 99)