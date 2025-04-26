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

#new load pattern has SP- as a prefix
patterns_to_swap = ["CDL-Model","SDL","SDL-Landscape","LL-NR","LL<=100"]
modify_lookup = dict([(pattern, "SP-" + pattern) for pattern in patterns_to_swap])

_, _, member_list,ret = a.SapModel.SelectObj.GetSelected()
ret = checkret(ret,"get selected objects")

for member in member_list:
    
    deleted_load_list_distributed = []
    deleted_load_list_point = []
    
    #distributed load transfer
    try:
        NumberItems, FrameName, LoadPat, MyType, CSys, Dir, RD1, RD2, Dist1, Dist2, Val1, Val2, ret = a.SapModel.FrameObj.GetLoadDistributed(member)
    except:
        print(" no distributed loads on " + member)
    else:
        ret = checkret(ret,"get distributed loads on " + member)
        for i in range(NumberItems):
            if LoadPat[i] in patterns_to_swap:
                if modify_lookup[LoadPat[i]] not in deleted_load_list_distributed:
                    ret = checkret(a.SapModel.FrameObj.DeleteLoadDistributed(member,modify_lookup[LoadPat[i]]),"delete loads "+modify_lookup[LoadPat[i]])
                    deleted_load_list_distributed.append(modify_lookup[LoadPat[i]])
                ret = checkret(a.SapModel.FrameObj.SetLoadDistributed(member, modify_lookup[LoadPat[i]], MyType[i], Dir[i], Dist1[i], Dist2[i], Val1[i], Val2[i], CSys[i], RelDist=False, Replace=True),"set distributed load " + LoadPat[i] + "on " + member)
    
    #point load transfer
    try:
        NumberItems, FrameName, LoadPat, MyType, CSys, Dir, RelDist, Dist, Val, ret = a.SapModel.FrameObj.GetLoadPoint(member)
    except:
        print(" no point loads on " + member)
    else:
        ret = checkret(ret,"get point loads on " + member)
        for i in range(NumberItems):
            if LoadPat[i] in patterns_to_swap:
                if modify_lookup[LoadPat[i]] not in deleted_load_list_point:
                    ret = checkret(a.SapModel.FrameObj.DeleteLoadPoint(member,modify_lookup[LoadPat[i]]),"delete loads "+modify_lookup[LoadPat[i]])
                    deleted_load_list_point.append(modify_lookup[LoadPat[i]])
                ret = checkret(a.SapModel.FrameObj.SetLoadPoint(member, modify_lookup[LoadPat[i]], MyType[i], Dir[i], RelDist[i], Val[i], CSys[i], RelDist=True, Replace=True),"set point load " + LoadPat[i] + "on " + member)