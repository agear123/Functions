# -*- coding: utf-8 -*-
"""
Created on Sat May  7 13:09:22 2022

@author: Andy
"""

def word_count(filepath):
    '''
    Count the number of unique words and total number of words in a text.

    Parameters
    ----------
    filepath : str
               Name of the text file.

    Returns
    -------
    None.

    '''
    
    with open(filepath) as file:
        text = file.read()
        file.close()
        words_list = text.split()
        number_of_words = 0
        number_of_words += len(words_list)
        print()
        
    '''    
    Eliminate punctuation and capitalization differences to get 
    accurate unique word count.
    '''    
    from collections import Counter

    lower_case_text = text.casefold().replace(',', '')
    count_words = Counter(lower_case_text.split()).most_common()
        
    print()
    print(text)
    print()
    print('Word Occurance Count')
    print()
    for words in count_words:
        print('{} : {}'.format(words[0], words[1]))
        
    print()
    print('{} unique words in text.' .format(len(count_words)))
    print('{} words in text.'.format(number_of_words))
    

word_count('useful_text.txt') 

        
