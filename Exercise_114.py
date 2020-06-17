# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:17:56 2020

@author: ts-omer.ari
"""


nums = [34, 1, 0, -23]
print("Original numbers in the list: ",nums)
new_nums = list(filter(lambda x: x >0, nums))
print("Positive numbers in the list: ",new_nums)