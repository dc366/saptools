# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 07:06:45 2022

@author: djc
"""

import attach
import UtilityFuncs as uf
import os.path


parent_folder = r'C:\Users\djc\Desktop\SAP Working\C3 rerun'

folder_list = uf.folders_in_folder(parent_folder)

def checkret(ret,step):
    if ret:
        print("  error at "+step)
    return 0

for folder in folder_list:
    
    folder_path = parent_folder + os.sep + folder
    file_list = uf.files_in_folder(folder_path)
    a = attach.sapApplication()

    for file in file_list:
        
        #check if sdb or something else. if something else, skip
        (file_name,ext) = os.path.splitext(file)
        if ext != ".sdb":
            continue
    
        #open model
        ret = a.SapModel.File.OpenFile(folder_path+os.sep+file)
        ret = checkret(ret,"open model "+file_name)
        
        #set units
        ret = a.SapModel.SetPresentUnits(3)
        ret = checkret(ret,"set units "+file_name)

        #set load cases to run
        ret = a.SapModel.Analyze.SetRunCaseFlag(None,True,True)
        ret = checkret(ret,"set all cases to run "+file_name)
    
        #save it to a subfolder
        os.makedirs(folder_path+os.sep+file_name,exist_ok=True)
        a.SapModel.File.Save(folder_path+os.sep+file_name+os.sep+file)    
    
        #run analysis
        ret = a.SapModel.Analyze.RunAnalysis()
        ret = checkret(ret,"run analysis "+file_name)
    
        print(file_name + " complete")
