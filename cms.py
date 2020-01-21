# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 22:32:20 2020

@author: bhavn
converts feet and inches to cms
"""

def cms (feet, inch):
    cm = (feet * 12 * 2.54) + (inch * 2.54)
    return cm