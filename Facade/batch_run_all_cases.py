# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 07:06:45 2022

@author: djc
"""

import attach
import UtilityFuncs as uf
import os.path

folder_path = r'C:\Users\djc\Desktop\SAP Working\all models\SEQC3'
folder_list = uf.folders_in_folder(folder_path)

a = attach.sapApplication()

compiled_load_cases = {}

def checkret(ret,step):
    if ret:
        print("  error at "+step)
    return 0

for folder in folder_list:
    file_name = folder

    #open model
    ret = a.SapModel.File.OpenFile(folder_path+os.sep+folder+os.sep+folder+".sdb")
    ret = checkret(ret,"open model "+file_name)
    
    #get load cases    
    _, load_cases, ret = a.SapObject.SapModel.LoadCases.GetNameList_1()
    ret = checkret(ret,"get all load case names "+file_name)
    
    #set load cases to run
    ret = a.SapModel.Analyze.SetRunCaseFlag(None,True,True)
    ret = checkret(ret,"set all cases to run "+file_name)
    
    #run analysis
    ret = a.SapModel.Analyze.RunAnalysis()
    ret = checkret(ret,"run analysis "+file_name)

    print(file_name + " complete")