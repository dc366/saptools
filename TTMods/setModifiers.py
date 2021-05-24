# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 22:19:23 2021

@author: acp
"""

import attach
sapBox = attach.sapApplication()

filePath = r"C:\Users\ACP\Desktop\2021_04_26 SeqB-Redo\2021_04_26_MB TT Updates-LERAMOD.xlsx"
sheetName = "BWestMods-LERA"

frameNames= attach.get_list_excel(filePath, sheetName, "Member ID" ) 
IxMod = attach.get_list_excel(filePath, sheetName, "Mod Ix" ) 
IyMod = attach.get_list_excel(filePath, sheetName, "Mod Iy" ) 
AMod = attach.get_list_excel(filePath, sheetName, "Mod A" ) 
WMod = attach.get_list_excel(filePath, sheetName, "Mod W" ) 
MMod = attach.get_list_excel(filePath, sheetName, "Mod M" ) 


item = 0

for j in range(len(frameNames)):
    value =[1]*8
    value[0] = AMod[j]
    value[4] = IyMod[j]
    value[5] = IxMod[j]
    value[6] = MMod[j]
    value[7] = WMod[j]
    [b, ret] = sapBox.SapModel.FrameObj.SetModifiers(frameNames[j], value)
    if ret != 0:
        print("error in " + frameNames[j])