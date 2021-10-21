# -*- coding: utf-8 -*-
"""D
Created on Tue Mar  9 12:27:48 2021

@author: ACP
"""
##### This tool is for renaming objects that have integer as names in order to 
##### give them a unique name as to avoid conflicts when importing


import attach
from tqdm import tqdm
sapBox = attach.sapApplication()
modelName = sapBox.SapModel.GetModelFilename(False)
n = len(modelName)-4
m = n - 7
#prefix = modelName[m:n]  # This is the prefix that will be used to rename the objects
prefix = 'C3WestTDown'


objectNames = attach.sapGroup(sapBox, "All").ObjectName
objectTypes = attach.sapGroup(sapBox, "All").TypeID

jtCount = 1
areaCount = 1
frameCount = 1

for i in tqdm(range(len(objectNames))):
    name = objectNames[i]
    tipe = objectTypes[i]
    
    try:
        int(name)
        if tipe ==1:
            sapBox.SapModel.PointObj.ChangeName(name,prefix + "-jt-" + str(jtCount))
            jtCount = jtCount + 1
        elif tipe == 2:
            sapBox.SapModel.FrameObj.ChangeName(name,prefix + "-frm-" + str(frameCount))
            frameCount = frameCount + 1
        elif tipe == 5:
            sapBox.SapModel.AreaObj.ChangeName(name,prefix + "-XM-" + str(areaCount))
            areaCount = areaCount + 1
                   
    except ValueError:
        continue
    
    
