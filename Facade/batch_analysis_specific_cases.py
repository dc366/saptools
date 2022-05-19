# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 07:06:45 2022

@author: djc
"""

import attach
import UtilityFuncs as uf
import os.path

cases_to_run = ['DEAD']

parent_folder = r'C:\Users\djc\Desktop\SAP Working\Single Panel Models\Studyv1'
file_list = uf.files_in_folder(parent_folder)

folder_list = uf.folders_in_folder(parent_folder)

a = attach.sapApplication()

def checkret(ret,step):
    if ret:
        print("  error at "+step)
    return 0

for file in file_list:
    
    #check if sdb or something else. if something else, skip
    (file_name,ext) = os.path.splitext(file)
    if ext != ".sdb":
        continue

    #open model
    ret = a.SapModel.File.OpenFile(parent_folder+os.sep+file)
    ret = checkret(ret,"open model "+file_name)
    
    #set units
    ret = a.SapModel.SetPresentUnits(3)
    ret = checkret(ret,"set units "+file_name)

    #set no load cases to run
    ret = a.SapModel.Analyze.SetRunCaseFlag(None,False,True)
    ret = checkret(ret,"set no cases to run "+file_name)
    
    #set specific load cases to run
    for case in cases_to_run:
        ret = a.SapModel.Analyze.SetRunCaseFlag(case,True)
        ret = checkret(ret,"enable case " + case + " in " + file_name)
    
    #save it to a subfolder
    os.makedirs(parent_folder+os.sep+file_name,exist_ok=True)
    a.SapModel.File.Save(parent_folder+os.sep+file_name+os.sep+file)    

    #run analysis
    ret = a.SapModel.Analyze.RunAnalysis()
    ret = checkret(ret,"run analysis "+file_name)

    print(file_name + " complete")
