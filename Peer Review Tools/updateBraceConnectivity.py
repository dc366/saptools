# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:39:41 2022

@author: acp
"""
def shiftWPs(modelName, frameList, b, c, d, e, f, g):  #This function shifts the workpoints for SAP2000 frames. A SAP2000 model has o be open. Inputs for function as summarized below

    import attach
    a = attach.sapApplication()

    modelName = modelName     #model name used only for naming new special points
    frameList = frameList     #List of Frames to be shifted
    i_DelX_List = b           #List of x direction shift for point i
    i_DelY_List = c           #List of y direction shift for point i
    i_DelZ_List = d           #List of z direction shift for point i
    j_DelX_List = e           #List of x direction shift for point j
    j_DelY_List = f           #List of y direction shift for point j
    j_DelZ_List = g           #List of z direction shift for point j
    
    errorTrack = []

    for k in range(len(frameList)):
        frame = frameList[k]
        print("on frame "+frame)
    
        i_Jt = attach.sapFrame(a, frame).iEnd
        new_i_x =  attach.sapJoint(a, i_Jt).x  + i_DelX_List[k]
        new_i_y =  attach.sapJoint(a, i_Jt).y  + i_DelY_List[k]
        new_i_z =  attach.sapJoint(a, i_Jt).z  + i_DelZ_List[k]
        new_i_ptName = "addJt_" + modelName[0:3] +"_"+str(k+1)  
        [name1, ret1] = a.SapModel.PointObj.AddCartesian(new_i_x, new_i_y, new_i_z, new_i_ptName, new_i_ptName)
        
        
        j_Jt = attach.sapFrame(a, frame).jEnd
        new_j_x =  attach.sapJoint(a, j_Jt).x  + j_DelX_List[k]
        new_j_y =  attach.sapJoint(a, j_Jt).y  + j_DelY_List[k]
        new_j_z =  attach.sapJoint(a, j_Jt).z  + j_DelZ_List[k]
        new_j_ptName = "addJt_" + modelName[0:3] +"_"+str(k+2)
        [name2, ret2] = a.SapModel.PointObj.AddCartesian(new_j_x, new_j_y, new_j_z, new_j_ptName, new_j_ptName)
        ret3 = a.SapModel.EditFrame.ChangeConnectivity(frame, new_i_ptName, new_j_ptName)
        
        
        if ret1 !=0  or ret2 !=0 or ret3 != 0:
            errorTrack.append("error for Frame Object " + str(frame))
        
        return errorTrack