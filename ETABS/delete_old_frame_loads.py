# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:20:43 2022

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

_, _, member_list,ret = a.SapModel.SelectObj.GetSelected()
ret = checkret(ret,"get selected objects")

for old_load,new_load in modify_lookup.items():
    for member in member_list:
        ret = a.SapModel.FrameObj.DeleteLoadDistributed(member,old_load)
        checkret(ret,"delete distributed loads " + old_load + " on " + member)
        
        ret = a.SapModel.FrameObj.DeleteLoadPoint(member,old_load)
        checkret(ret,"delete point loads " + old_load + " on " + member)