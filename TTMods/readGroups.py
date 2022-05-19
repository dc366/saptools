# -*- coding: utf-8 -*-
"""
Created on Mon May  3 09:28:53 2021

@author: acp
"""
#This script reads the group names listed in an excel file and write the object names and types to variables
#This script is for use with writeGroupFromMem.py

import attach
sapBox = attach.sapApplication()


filePath = r"C:\Users\acp\Desktop\Facad Peer Review\2021_09_27-LERAMODS.xlsx"
sheetName = "readGroups"
columnName = "Group"
groupNames= attach.get_list_excel(filePath, sheetName, columnName) 


objectLists = [0] * len(groupNames)
typeLists = [0] * len(groupNames)



for i in range(len(groupNames)):
    print("Reading Group "+groupNames[i]+" ...")
    try:
        objectLists[i] = attach.sapGroup(sapBox, groupNames[i]).ObjectName
        typeLists[i] = attach.sapGroup(sapBox, groupNames[i]).TypeID
    except:
        print("Error for Group " + groupNames[i])
    