# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 15:25:29 2021

@author: ACP
"""
#This tool groups picture frames objects separate from typical stiffeners
import attach
sapBox = attach.sapApplication()
import numpy as np
#from tqdm import tqdm
groupName = "allFrames"
frameList = attach.sapGroup(sapBox,groupName).ObjectName
panelList = []
dotTolerance = 0.6
picFrames = []
typFrames = []

for frame in frameList:
    panel = frame[0:7]  
    if panel not in panelList:
        print("Working on panel " + panel+"...")
        list1 = []
        list2 = []     
        counter = 0
        for i in range(len(frameList)):                    
            if panel in frameList[i]:
                if counter == 0:        
                    (jt1, jt2, ret) = sapBox.SapModel.FrameObj.getPoints(frameList[i])
                    x1 = attach.sapJoint(sapBox, jt1).x
                    y1 = attach.sapJoint(sapBox, jt1).y
                    z1 = attach.sapJoint(sapBox, jt1).z
                    x2 = attach.sapJoint(sapBox, jt2).x
                    y2 = attach.sapJoint(sapBox, jt2).y
                    z2 = attach.sapJoint(sapBox, jt2).z 
                    refVec = np.array([x2-x1, y2-y1, z2- z1])
                    norm = np.linalg.norm(refVec)
                    refVec = refVec/norm
                    list1.append(frameList[i])
                elif counter > 0:
                    (jt1, jt2, ret) = sapBox.SapModel.FrameObj.getPoints(frameList[i])
                    x1 = attach.sapJoint(sapBox, jt1).x
                    y1 = attach.sapJoint(sapBox, jt1).y
                    z1 = attach.sapJoint(sapBox, jt1).z
                    x2 = attach.sapJoint(sapBox, jt2).x
                    y2 = attach.sapJoint(sapBox, jt2).y
                    z2 = attach.sapJoint(sapBox, jt2).z 
                    vec = np.array([x2-x1, y2-y1, z2- z1])
                    norm = np.linalg.norm(vec)
                    vec = vec/norm      
                    dotProd = np.dot(refVec, vec)
                    if np.abs(dotProd) > dotTolerance:
                        list1.append(frameList[i])
                    elif np.abs(dotProd) <= dotTolerance:
                        list2.append(frameList[i])
                counter = counter + 1                                   
        if len(list1) > len(list2):
            typFrames.extend(list1)
            picFrames.extend(list2)
        elif len(list1) < len(list2):
            typFrames.extend(list2)
            picFrames.extend(list1)
        panelList.append(panel)                
        
sapBox.add_frames_to_group("picFrames",picFrames)
sapBox.add_frames_to_group("typFrames",typFrames)