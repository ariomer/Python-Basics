# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 15:15:42 2020

@author: ts-omer.ari
"""


def member(group_data, n):
    for i in group_data:
        if n == i:
            return True
    return False
print(member([1, 5, 8, 3], 3))
print(member([5, 8, 3], -1))
