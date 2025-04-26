# -*- coding: utf-8 -*-
"""
Created on Mon May  9 16:04:01 2022

@author: djc
"""

import attach

def checkret(ret,step):
    if ret:
        print("  error at "+step)
    return 0

e3_vector_list = [  ["C64-10",[-0.243404,0.041055,0.969056]]
                    ]

dead_WT_horiz = "DEAD-WT Horizontal"
load_case_name = "DEAD: IBP - Horiz"

a = attach.sapApplication()

#unlock model
ret = a.SapModel.SetModelIsLocked(False)
ret = checkret(ret,"unlock model")

#define new load pattern DEAD-WT Horizontal
ret = a.SapModel.LoadPatterns.Add(dead_WT_horiz,8)
ret = checkret(ret,"define load pattern")

#apply load using e3 vector
for vector in e3_vector_list:
    panel = vector[0]
    e3_vector = vector[1]
    
    ret = a.SapModel.AreaObj.SetLoadGravity("panel_"+panel,dead_WT_horiz,e3_vector[0], e3_vector[1], e3_vector[2],ItemType=1)
    ret = checkret(ret,"set gravity area load")
    ret = a.SapModel.FrameObj.SetLoadGravity("panel_"+panel,dead_WT_horiz,e3_vector[0], e3_vector[1], e3_vector[2],ItemType=1)
    ret = checkret(ret,"set gravity line load")

#create new load case DEAD - DEAD-WT Horizontal
ret = a.SapModel.LoadCases.StaticNonlinear.SetCase(load_case_name)
ret = checkret(ret,"create load case")
ret = a.SapModel.LoadCases.StaticNonlinear.SetLoads(load_case_name,2,["Load" for x in range(2)],["DEAD",dead_WT_horiz],[1.0,-1.0])
ret = checkret(ret[-1],"set load case loads")

#save model
#a.SapModel.