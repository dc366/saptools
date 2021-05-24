# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 15:41:07 2021

@author: acp
"""

import attach
sapBox = attach.sapApplication()

filePath = r"C:\Users\ACP\Desktop\2021_04_26 SeqB-Redo\2021_04_26_MB TT Updates.xlsx"
sheetName = "BWestSuperElevations"

jointNames= attach.get_list_excel(filePath, sheetName, "Joint ID") 
superElev = attach.get_list_excel(filePath, sheetName, "SuperElevation") 
loadPat = attach.get_list_excel(filePath, sheetName, "Load Pattern Name") 
 
sapBox.add_joints_to_group("LERA-superElev", jointNames)

for i in range(len(jointNames)):
    value = [0]*6
    value[2] = superElev[i]
    b, ret = sapBox.SapModel.PointObj.SetLoadDispl(jointNames[i], loadPat[i], value, True, "Global")
    if ret != 0:
        print("error")