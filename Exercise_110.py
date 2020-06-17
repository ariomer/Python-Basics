# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:16:06 2020

@author: ts-omer.ari
"""


num_list = [45, 55, 60, 37, 100, 105, 220]
# use anonymous function to filter
result = list(filter(lambda x: (x % 15 == 0), num_list))
print("Numbers divisible by 15 are",result)