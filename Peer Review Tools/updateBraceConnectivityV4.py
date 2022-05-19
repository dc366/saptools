# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:39:41 2022
@author: acp
"""
import attach
a = attach.sapApplication()
import prLibs
import pandas as pd

#set filepath location
filePath = r"C:\Users\acp\Desktop\Facad Peer Review\Latest PB WP Data\LMNA_SEQ-C1_Southeast_PB_Update_v2.xlsx"
sheetName = "acpFix"
    
#list of panels to run:
panList =['C18-06', 'C18-17', 'C19-05', 'C19-07', 'C19-08']

print('Creating List of Changes...')
[braceList, panName, iX, iY, iZ, jX, jY, jZ, cX, cY, cZ] = prLibs.shiftList(panList,filePath, sheetName)

panName = panName    #model name used only for naming new special points
frameList = braceList     #List of Frames to be shifted
i_X_List = iX           #List of new x coord
i_Y_List = iY           #List of new y ""
i_Z_List = iZ           #List of new z 
j_X_List = jX           #List of new x 
j_Y_List = jY           #List of new y 
j_Z_List = jZ           #List of new z 
c_X_List = cX          #List of X, Y, Z points for end of new member which starts at joint j point
c_Y_List = cY
c_Z_List = cZ
    
errorTrack = []
newPoints = []
deletePB =[]

print('Applying Changes...')

for k in range(len(frameList)):
    frame = frameList[k]
    modelName = panName[k]
    if pd.isnull(i_X_List[k]):
        deletePB.append(frame)
    else:
        
        print(frame)
    
        new_i_ptName = "newPt_" + modelName +"_"+str(k)+"-i"
        [name1, ret1] = a.SapModel.PointObj.AddCartesian(i_X_List[k], i_Y_List[k], i_Z_List[k], new_i_ptName, new_i_ptName)
        print("ret1 is " + str(ret1))
        print(str(new_i_ptName))
        if ret1 != 0: 
            print("error in creating new i point for "+str(frame))

        new_j_ptName = "newPt_" + modelName +"_"+str(k)+ "-j"

        [name2, ret2] = a.SapModel.PointObj.AddCartesian(j_X_List[k], j_Y_List[k], j_Z_List[k], new_j_ptName, new_j_ptName)
        if ret2 != 0:
            print("error in creating new j point for "+str(frame))      
            
        ret3 = a.SapModel.EditFrame.ChangeConnectivity(frame, new_i_ptName, new_j_ptName)
        if ret3 != 0:
            print("error in changing connectivity for "+str(frame))
        
        if ret1 !=0  or ret2 !=0 or ret3 != 0:
            errorTrack.append("error moving workpoints for " + str(frame))
            
        newPoints.append(new_i_ptName)
        newPoints.append(new_j_ptName)
            #New Rigid Lnk:
                
        new_c_ptName = "addJt_" + modelName +"_"+str(k)+"-c"
        newFrmName = "addFrm_" + modelName +"_"+str(k)
        a.add_frames_to_group('panel_' + modelName,[newFrmName])
        [name1, ret1] = a.SapModel.PointObj.AddCartesian(c_X_List[k], c_Y_List[k], c_Z_List[k], new_c_ptName, new_c_ptName)
        ret2 = a.SapModel.FrameObj.AddByPoint(new_j_ptName, new_c_ptName, newFrmName, "CONN_stiff", newFrmName )
        if ret1 !=0  or ret2 !=0:
            errorTrack.append("error creating rigid offset for " + str(frame))

a.add_frames_to_group('LERA_DeletedPBs',deletePB)            
#return newPoints
#a.add_joints_to_group('LERA_newPB_Points',newPoints) 