# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 09:41:24 2021

@author: ACP
"""
#This script creates a group for the "TP" Points in the SAP Model########3



import attach
sapBox = attach.sapApplication()
from tqdm import tqdm

#Before running this script, create a group called "allJoints" and assign the joints or subgroup of joints that contain the TP Joints
jointGroup = "allJoints"

#Other Parameters:
jointList = attach.sapGroup(sapBox, jointGroup).ObjectName

tpJoints=[]
for i in tqdm(range(len(jointList))):
    jointName= jointList[i]
    if ("TP" in jointName):  #"TP" are the Joints at T-pin ends in Rick's naming convention
        tpJoints.append(jointName)
print("creating TP group")
sapBox.add_joints_to_group("tpJoints",tpJoints)