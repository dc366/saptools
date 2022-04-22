# -*- coding: utf-8 -*-
"""
Created on Mon May  3 10:00:39 2021

@author: acp
"""
#before running this script, run "readGroups.py" on model that you wish to get groups from.
#Also go to Run> Configuration per file adn active option called "Run in console's namespae instad of an empty one"

import attach
sapBox = attach.sapApplication()
from tqdm import tqdm


for i in range(len(groupNames)):
    groupNm = groupNames[i]
    print("writing "+groupNm+"...")
    for j in tqdm(range(len(objectLists[i]))):
        objectNm = objectLists[i][j]
        objectType = typeLists[i][j]
        ret = sapBox.SapModel.GroupDef.SetGroup(groupNm)
        if objectType == 1:
            ret = sapBox.SapModel.PointObj.SetGroupAssign(objectNm, groupNm)
            if ret != 0:
                print("error in "+objectNm)
        elif objectType == 2:
            ret = sapBox.SapModel.FrameObj.SetGroupAssign(objectNm, groupNm)
            if ret != 0:
                print("error in "+objectNm)
        elif objectType  == 5:
            ret = sapBox.SapModel.AreaObj.SetGroupAssign(objectNm, groupNm)
            if ret != 0:
                print("error in "+objectNm)
        elif objectType  == 7:
            ret = sapBox.SapModel.LinkObj.SetGroupAssign(objectNm, groupNm)
            if ret != 0:
                print("error in "+objectNm)
        else:
            print("error for object "+objectNm)
            
            
