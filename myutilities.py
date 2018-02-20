# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 15:38:52 2018

@author: Ethan
"""

def divby2(l):
    ''' Function that accepts a list and returns all values from that list that are divisible by 2'''

    return [i for i in l if i % 2 ==0]