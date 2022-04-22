# -*- coding: utf-8 -*-
"""
Created on Mon May  3 16:16:28 2021

@author: acp
"""

import attach
sapBox = attach.sapApplication()
from tqdm import tqdm

#group names documented in an excel file:
filePath = r"C:\Users\acp\Desktop\2021_08_26 Seq A East\2021_09_08-LERAMODS.xlsx"
sheetName = "panelWeightSummary"

groupNames= attach.get_list_excel(filePath, sheetName, "sapGroup") 
mods= attach.get_list_excel(filePath, sheetName, "SAP Weight Modifier") 

for i in range(len(groupNames)):
    try:
        objects = attach.sapGroup(sapBox, groupNames[i]).ObjectName
        objIDs = attach.sapGroup(sapBox, groupNames[i]).TypeID
        print("Applying Modifiers to Group: " + groupNames[i])
        for j in tqdm(range(len(objIDs))):
            ID = objIDs[j]
            objName = objects[j]
            frmValue = [1, 1, 1, 1, 1, 1, mods[i], mods[i]]
            areaValue = [1, 1, 1, 1, 1, 1, 1, 1, mods[i], mods[i]]
            
            if ID == 2:
                [b, ret] = sapBox.SapModel.FrameObj.SetModifiers(objName, frmValue)
                if ret != 0:
                    print("error in " + objName)
                    
            elif ID== 5:
                [b, ret] = sapBox.SapModel.AreaObj.SetModifiers(objName, areaValue)
                if ret != 0:
                    print("error in " + objName)   
            else:
                print("Object Type not Supported: "+ str(objName))
    except:
        print('Group not Found: '+groupNames[i])
                