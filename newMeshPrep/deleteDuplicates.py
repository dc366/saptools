# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:44:28 2021
@author: ACP
"""
###################For deleting Duplicate Frame Elements##################
#This script creates groups for the frame objects in group "frameList"
#This script only works for a max of 1 duplicate in the same location, it doesn't work if there are 2 or more duplicates

import attach
sapBox = attach.sapApplication()

frameGroupName = "allFrames"   #create this group in SAP and put your suspected duplicates in this group

#Other Parameters:
frameObjects = attach.sapGroup(sapBox, frameGroupName).ObjectName

iEnds=[]
jEnds=[]

#creates list for i ends and j ends:
for i in range(len(frameObjects)):   
    iEndName = attach.sapFrame(sapBox,frameObjects[i]).iEnd
    jEndName = attach.sapFrame(sapBox,frameObjects[i]).jEnd
    
    iEnds.append(iEndName)
    jEnds.append(jEndName)

dupListA=[]
dupListB=[]

#cross checks ends points of each frame and makes two lists of duplciates
for i in range(len(frameObjects)):      
    for k in range(len(frameObjects)):
        if i != k:
            if ((iEnds[i]==iEnds[k]) or (iEnds[i]== jEnds[k])):
                if ((jEnds[i]==jEnds[k]) or (jEnds[i]== iEnds[k])):
                    if frameObjects[i] not in dupListB: #if the next point is not already in list B:
                        dupListA.append(frameObjects[i])
                        dupListB.append(frameObjects[k])
                        
#create group for duplicates

sapBox.add_frames_to_group("dupListA",dupListA)
sapBox.add_frames_to_group("dupListB",dupListB)