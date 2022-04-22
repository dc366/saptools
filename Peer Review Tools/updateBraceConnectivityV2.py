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
    i_X_List = b           #List of new x coord
    i_Y_List = c           #List of new y ""
    i_Z_List = d           #List of new z 
    j_X_List = e           #List of new x 
    j_Y_List = f           #List of new y 
    j_Z_List = g           #List of new z 
    
    errorTrack = []

    for k in range(len(frameList)):
        frame = frameList[k]
        print(frame)
    

        new_i_ptName = "addJt_" + modelName[0:3] +"_"+str(k)+"-i"
        [name1, ret1] = a.SapModel.PointObj.AddCartesian(i_X_List[k], i_Y_List[k], i_Z_List[k], new_i_ptName, new_i_ptName)
        
        

        new_j_ptName = "addJt_" + modelName[0:3] +"_"+str(k)+ "-j"
        
        [name2, ret2] = a.SapModel.PointObj.AddCartesian(j_X_List[k], j_Y_List[k], j_Z_List[k], new_j_ptName, new_j_ptName)
        
        ret3 = a.SapModel.EditFrame.ChangeConnectivity(frame, new_i_ptName, new_j_ptName)
        
        
        if ret1 !=0  or ret2 !=0 or ret3 != 0:
            errorTrack.append("error for Frame Object " + str(frame))
            
    return errorTrack