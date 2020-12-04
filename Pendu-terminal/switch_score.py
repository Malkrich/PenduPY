#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 17:43:19 2020

@author: lemarie
"""

def switch_score(essais,score):
    
    if score<essais:
        return essais,True
    
    return score,False