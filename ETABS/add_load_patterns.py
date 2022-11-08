# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 10:56:08 2022

@author: djc
"""

import attach_ETABS

def checkret(ret,step):
    if ret:
        print("  error at "+step)
    return 0

a = attach_ETABS.sapApplication()

patterns_to_swap = ["CDL-Model","SDL","SDL-Landscape","LL-NR","LL<=100"]
modify_lookup = dict([(pattern, "SP-" + pattern) for pattern in patterns_to_swap])

for (old_load,new_load) in modify_lookup.items():
    ret = a.SapModel.LoadPatterns.Add(new_load,8,0,True)
    checkret(ret,"add load pattern "+new_load)