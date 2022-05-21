'''
Number of possible permutations and combinations
from a number of n choosings from a set of size k.  
'''
import math

def permutations_calc():
    '''
    Return number of possible permutations and combinations.

    Parameters
    ----------
    n : int
        Size of subset chosen from superset.
    k : int
        Superset size from which subset of size n is chosen from.

    Returns
    -------
    permutations : int 
                   Number of possible permutations.
    combinations : int
                   Number of possible combinations.

    '''
    
    n = int(input('What is the value of n? '))
    
    if n < 0:
        raise ValueError('n must be an integer greater than zero.')
    
    k = int(input('What is the value of k? '))
    
    if k > n:
        raise ValueError('k must be a positive integer less than or equal to n.')
    
    permutations = math.factorial(n) / math.factorial(n - k) 
    permutations = int(permutations)
    
    '''Note permutations and combinations formulas have common inputs.'''
    
    combinations = math.factorial(n) / math.factorial(k) * math.factorial(n - k) 
    combinations = int(combinations)
    print()
    print('{} possible permutations'.format(permutations))
    print('{} possible combinations'.format(combinations))

    return permutations
    return combinations

permutations_calc()










