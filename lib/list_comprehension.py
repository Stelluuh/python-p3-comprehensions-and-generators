#!/usr/bin/env python3

def return_evens(num_list):
    evenNumbers = [num for num in num_list if num % 2 == 0]
    return evenNumbers
 

def make_exclamation(sentence_list):
    #iterate through each sentence in the sentence_list 
    #for each sentence i want to add a "!" at the end.
    #retun the sentence
    return [sentence + "!" for sentence in sentence_list]
    