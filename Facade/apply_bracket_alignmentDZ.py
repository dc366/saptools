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

def adjust_load_pattern(PatternName,bracket_alignment,switch):
    group = [inputs[0] for inputs in bracket_alignment]
    disp_value = [inputs[1] for inputs in bracket_alignment]
    
    if switch == "linear":
        NumberLoads, LoadType, LoadName, SF, ret = a.SapModel.LoadCases.StaticLinear.GetLoads(PatternName)
    elif switch == "nonlinear":
        NumberLoads, LoadType, LoadName, SF, ret = a.SapModel.LoadCases.StaticNonlinear.GetLoads(PatternName)
    ret = checkret(ret,"get load patterns for "+PatternName)
    
    LoadName = [*LoadName, *group]
    SF = [*SF, *disp_value]
    LoadType = [*LoadType, *["Load" for item in group]]
    NumberLoads = NumberLoads + len(group)
    
    if switch == "linear":
        ret = a.SapModel.LoadCases.StaticLinear.SetLoads(PatternName,NumberLoads,LoadType,LoadName,SF)
    elif switch == "nonlinear":
        ret = a.SapModel.LoadCases.StaticNonlinear.SetLoads(PatternName,NumberLoads,LoadType,LoadName,SF)
    
    ret = checkret(ret[3],"set load patterns for "+PatternName)
        
    return


ibp_brackets = [['TL',-0.005],['TR',0.003],['BL',0.005],['BR',-0.003]]
horiz_brackets = [['TL',0.016],['TR',-0.009],['BL',-0.016],['BR',0.009]]
#must negate vector from load vector database
DZ_vector = [-x for x in [-0.064035,0.725887,0.684827]]

dead = "DEAD"
dead_WT_horiz = "DEAD-WT Horizontal"
ibp_minus_horiz = "DEAD: IBP - Horiz"

a = attach.sapApplication()

#unlock model
ret = a.SapModel.SetModelIsLocked(False)
ret = checkret(ret,"unlock model")

#set units
ret = a.SapModel.SetPresentUnits(3)
ret = checkret(ret,"set units")

#apply unit displacements
for inputs in ibp_brackets:
    group = inputs[0]
    
    #define new load pattern for each bracket
    ret = a.SapModel.LoadPatterns.Add(group,8)
    ret = checkret(ret,"define load pattern" + group)
    
    #apply DZ unit vector to each point
    ret = a.SapModel.PointObj.SetLoadDispl(Name=group,LoadPat=group,Value=[*DZ_vector,0,0,0],Replace=True,CSys="Global",ItemType=1)
    ret = checkret(ret[1],"apply unit displacement - " + group)

#adjust DEAD to include bracket alignment
adjust_load_pattern(dead,ibp_brackets,"nonlinear")

#adjust horiz to include bracket alignment
adjust_load_pattern(dead_WT_horiz,horiz_brackets,"linear")

#adjust IBP-horiz to include bracket alignment
adjust_load_pattern(ibp_minus_horiz,ibp_brackets,"nonlinear")

neg_horiz_brackets = [[i[0],-i[1]] for i in horiz_brackets]
adjust_load_pattern(ibp_minus_horiz,neg_horiz_brackets,"nonlinear")