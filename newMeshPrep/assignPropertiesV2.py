# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 19:34:37 2021

@author: ACP
"""

#This script assigns area and frame section properties per the following matching
#and also assigns insertion points and offsets for the stiffeners:
#COnsidering changing this script from Sap selection based to Sap group based to make it faster

from tqdm import tqdm
import attach
sapBox = attach.sapApplication()

ASEC1 = 'Layered-Shell-Coat-Scaled'
ASEC2 = 'Layered-Shell-Coat-Scaled-Flanges'
ASEC3 = 'Layered-Shell-Coat-Scaled+PV'
FSEC1 = '4.5" Trap Hat'
FSEC2 = 'Z-shaped Stiffener'
FSEC3 = '2.25" Trap Hat'
FSEC4 = '0.5" Trap Hat'
FSEC5 = 'gutterStiffenerV1'

changeASECList = [changeASEC1, changeASEC2, changeASEC3]
changeFSECList = [changeFSEC1, changeFSEC2,changeFSEC3, changeFSEC4, changeFSEC5]





#Define the panel thickness to be used for stiffener offset
panThick = 0.49


sapBox.clear_selection()
for i in range(len(changeASECList)):
    propToChange = "ASEC"+str(i+1)
    ret = sapBox.SapModel.SelectObj.PropertyArea(propToChange)
    selected, _ = sapBox.get_list_sap("area")
    print("assigning "+ changeASECList[i])
    for area in tqdm(selected):
        sapBox.SapModel.AreaObj.SetProperty(area, changeASECList[i])
    sapBox.clear_selection()
    
sapBox.clear_selection()
for i in range(len(changeFSECList)):
    propToChange = "FSEC"+str(i+1)
    ret = sapBox.SapModel.SelectObj.PropertyFrame(propToChange)
    selected, _ = sapBox.get_list_sap("frame")
    print("assigning "+ changeFSECList[i])
    for frame in tqdm(selected):
        sapBox.SapModel.FrameObj.SetSection(frame, changeFSECList[i])
    sapBox.clear_selection()
    
    
#Assign Insertion Points and offsets to frame Elements:
    
for i in range(len(changeFSECList)):
    prop = changeFSECList[i]
    ret = sapBox.SapModel.SelectObj.PropertyFrame(prop)
    selected, _ = sapBox.get_list_sap("frame")
    print("assigning stiffener offsets")
    for frame in tqdm(selected):
        if 'gutter' in prop: #gutter members are special:
            ret = sapBox.SapModel.FrameObj.SetInsertionPoint(frame, 10, False, True, [0, -3.64, -6], [0, -3.64, -6] )
        else: #typical stiffeners are inserted at top center and offset by half the panel thickness in the local 2 direction:
            ret = sapBox.SapModel.FrameObj.SetInsertionPoint(frame, 8, False, True, [0, panThick/2, 0], [0,panThick/2,0] )
    sapBox.clear_selection()
    