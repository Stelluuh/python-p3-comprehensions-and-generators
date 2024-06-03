#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]
    # Loop through each number in num_list. For each iteration, the current element of 'num_list' is assigned to the variable num.
    #condition is to check if each number is even by seeing if the num divided by 2 is zero. if it is, then that number is even. 
    
 

def make_exclamation(sentence_list):
    #iterate through each sentence in the sentence_list 
    #for each sentence i want to add a "!" at the end.
    #retun the sentence
    return [sentence + "!" for sentence in sentence_list]
    