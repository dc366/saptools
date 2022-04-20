# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:39:41 2022

@author: acp
"""
def shiftWPs(modelName, a, b, c, d, e, f, g):

    import attach
    a = attach.sapApplication()

    modelName = modelName
    frameList = a
    i_DelX_List = b
    i_DelY_List = c
    i_DelZ_List = d
    j_DelX_List = e
    j_DelY_List = f
    j_DelZ_List = g

    for k in range(len(frameList)):
        frame = frameList[k]
    
        i_Jt = attach.sapFrame(a, frame).iEnd
        new_i_x =  attach.sapJoint(a, i_Jt).x  + i_DelX_List[k]
        new_i_y =  attach.sapJoint(a, i_Jt).y  + i_DelY_List[k]
        new_i_z =  attach.sapJoint(a, i_Jt).z  + i_DelZ_List[k]
        new_i_ptName = "addJt_" + modelName[0:3] +"_"+str(k+1)  
        ret = a.SapModel.PointObj.AddCartesian(new_i_x, new_i_y, new_i_z, new_i_ptName, new_i_ptName)
        
        j_Jt = attach.sapFrame(a, frame).jEnd
        new_j_x =  attach.sapJoint(a, j_Jt).x  + j_DelX_List[k]
        new_j_y =  attach.sapJoint(a, j_Jt).y  + j_DelY_List[k]
        new_j_z =  attach.sapJoint(a, j_Jt).z  + j_DelZ_List[k]
        new_j_ptName = "addJt_" + modelName[0:3] +"_"+str(k+2)
        ret = a.SapModel.PointObj.AddCartesian(new_j_x, new_j_y, new_j_z, new_j_ptName, new_j_ptName)
        
        ret = a.SapModel.EditFrame.ChangeConnectivity(frame, new_i_ptName, new_j_ptName)
