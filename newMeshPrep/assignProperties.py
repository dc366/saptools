# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 19:34:37 2021

@author: ACP
"""
import attach
sapBox = attach.sapApplication()

changeASEC1 = 'Layered-Shell-Coat-Scaled'
changeASEC2 = 'Layered-Shell-Coat-Scaled-Flanges'
changeASEC3 = 'Layered-Shell-Coat-Scaled+PV'
changeFSEC1 = '4.5" Trap Hat'
changeFSEC2 = 'Z-shaped Stiffener'
changeFSEC3 = '2.25" Trap Hat'
changeFSEC4 = '0.5" Trap Hat'
changeFSEC5 = 'gutterStiffenerV1'

changeASECList = [changeASEC1, changeASEC2, changeASEC3]
changeFSECList = [changeFSEC1, changeFSEC2,changeFSEC3, changeFSEC4, changeFSEC5]

panelThickness = 0.4275


sapBox.clear_selection()
for i in range(len(changeASECList)):
    propToChange = "ASEC"+str(i+1)
    ret = sapBox.SapModel.SelectObj.PropertyArea(propToChange)
    selected, _ = sapBox.get_list_sap("area")
    for area in selected:
        sapBox.SapModel.AreaObj.SetProperty(area, changeASECList[i])
    sapBox.clear_selection()
    
sapBox.clear_selection()
for i in range(len(changeFSECList)):
    propToChange = "FSEC"+str(i+1)
    ret = sapBox.SapModel.SelectObj.PropertyFrame(propToChange)
    selected, _ = sapBox.get_list_sap("frame")
    for frame in selected:
        sapBox.SapModel.FrameObj.SetSection(frame, changeFSECList[i])
    sapBox.clear_selection()
    
    
#Assign Insertion Points to frame Elements: