# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 17:56:59 2021

@author: acp
"""
#This tool sums reactions at pinned supports.  Must first group support points for each panel into a different group

import attach
sapBox = attach.sapApplication()

#group names documented in an excel file:
filePath = r"C:\Users\ACP\Desktop\2021_04_26 SeqB-Redo\2021_04_26_MB TT Updates.xlsx"
sheetName = "BEastPanelWeights"
groupNames= attach.get_list_excel(filePath, sheetName, "GroupName") 

#Sap results setup commands, pick load case:
ret = sapBox.SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput
ret = sapBox.SapModel.Results.Setup.SetCaseSelectedForOutput("DEAD-LINEAR")

#Cycles through groups and points in groups and prints out the sum of F3 reaction for each group:
for i in range(len(groupNames)):  
    group = groupNames[i]
    #print(group+":")
    objectList = attach.sapGroup(sapBox, group).ObjectName
    total = 0
    for j in objectList:
        #print(j+" Reaction: ")
        (NumberResults, Obj, Elm, LoadCase, StepType, StepNum, F1, F2, F3, M1, M2, M3, ret) = sapBox.SapModel.Results.JointReact(j, 0)
        
        total = total +F3[0]
    print(group+" weight is "+str(total)+" kips")
