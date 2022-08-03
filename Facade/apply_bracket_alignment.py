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

ibp_brackets = [["TL",[-0.0086,-0.0419,0.0184]],["TR",[-0.0361,-0.0382,-0.0078]],["BL",[0.0352,0.04,0.0223]],["BR",[0.0096,0.0401,-0.0329]]]
horiz_brackets = [["TL",[0.0077,-0.0326,0.0092]],["TR",[-0.0392,-0.0302,0.0032]],["BL",[0.0213,0.0474,0.0218]],["BR",[0.0102,0.0154,-0.0342]]]

dead = "DEAD"
dead_WT_horiz = "DEAD-WT Horizontal"

a = attach.sapApplication()

#unlock model
ret = a.SapModel.SetModelIsLocked(False)
ret = checkret(ret,"unlock model")

#set units
ret = a.SapModel.SetPresentUnits(3)
ret = checkret(ret,"set units")

#apply in-building position bracket alignments
for inputs in ibp_brackets:
    group = inputs[0]
    disp_vector = inputs[1]
    
    ret = a.SapModel.PointObj.SetLoadDispl(Name=group,LoadPat=dead,Value=[*disp_vector,0,0,0],Replace=True,CSys="Global",ItemType=1)
    ret = checkret(ret[1],"set in-building position alignment - " + group)

#apply horiz position bracket alignments
for inputs in horiz_brackets:
    group = inputs[0]
    disp_vector = inputs[1]
    
    ret = a.SapModel.PointObj.SetLoadDispl(Name=group,LoadPat=dead_WT_horiz,Value=[*disp_vector,0,0,0],Replace=True,CSys="Global",ItemType=1)
    ret = checkret(ret[1],"set horiz position alignment - " + group)


