# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 07:06:45 2022

@author: djc
"""

import attach
import UtilityFuncs as uf
import os.path

folder_path = r'D:\Working\P1092\groupsa'
file_list = uf.files_in_folder(folder_path)

a = attach.sapApplication()

def checkret(ret,step):
    if ret:
        print("error at "+step)
        quit()

compiled_group = []


for file in file_list:
    
    #check if sdb or something else. if something else, skip
    (file_name,ext) = os.path.splitext(file)
    if ext != ".sdb":
        continue

    #open model
    ret = a.SapModel.File.OpenFile(folder_path+os.sep+file)
    checkret(ret,"open model "+file_name)
    
    #get mem_BJOUT group
    NumberItems, ObjectType, ObjectName,ret = a.SapModel.GroupDef.GetAssignments("mem_BJ-out")
    checkret(ret,"get group "+file_name)
    
    [compiled_group.append(mem) for mem in ObjectName]
    
