# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 21:18:30 2021

@author: Andy
"""
"""If we list all the natural numbers below 10 that are 
multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these 
multiples is 23. Find the sum of all the multiples any two natural numbers below 1000."""



def sum_multiples_of_nat_nums(nat_num_1, nat_num_2):
    '''
    Find the sum of all the multiples of nat_num_1 and/or nat_num_2 below 1000.

    Parameters
    ----------
    nat_num_1 : int
        First  natural number to find multiples of.
    nat_num_2 : int
        Second natural number to find multiples of.

    Returns
    -------
    sum_total : int
        Total of all natural numbers below 1000 being multipls of nat_num_1 and/or nat_num_2.

    '''
        
    sum_total = 0
    
    for value in range(1, 1000):
        if value % int(nat_num_1) == 0 or value % int(nat_num_2) == 0:
            sum_total = sum_total + value
       
    print('The output is {} '.format(sum_total))
    return sum_total


sum_multiples_of_nat_nums(20, 30)       
       
       
       
