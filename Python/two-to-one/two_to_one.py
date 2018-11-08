#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 01:09:57 2018

@author: yotroz
"""

#%%


def longest(s1, s2):
    
    def bubble(lst):
        for j in range(0, len(lst) - 1):
            for i in range(0, len(lst) - j - 1):
                if lst[i] > lst[i + 1]:
                    temp = lst[i]
                    lst[i] = lst[i + 1]
                    lst[i + 1] = temp
                    
        return lst
        
    
    def binary_search(elem, lst):    
    
    #I altered this binary search to 
    #return a boolean instead of
    #returning  an index.
    #This is more usefull for the implementeation in my searches
    
        low = 0
        high = len(lst) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if lst[mid] > elem:
                high = mid - 1
            elif lst[mid] < elem:
                low = mid + 1
            else:
                return True 
            
        return False


    s1 = list(s1)

    s2 = list(s2)
  
    
    unsorted = [letter for letter in s1 if binary_search(letter, s2) == False]
    
    unsorted = unsorted + [letter for letter in s2 if binary_search(letter, s1) == False]
    
    unsorted = unsorted + [letter for letter in s2 if binary_search(letter, s1) == True]
    
    
    unsorted_unique = list(set(unsorted))
    
    sorted_unique = bubble(unsorted_unique)
    
    
    
    return "".join(sorted_unique)




#%%
    
def longest2(a1, a2):
    return "".join(sorted(set(a1 + a2)))





#%%
def longest3(a1, a2): 
    return "".join(sorted(set(a1 + a2)))
    