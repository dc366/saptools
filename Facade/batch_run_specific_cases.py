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

cases_to_run = ['DEAD']

def checkret(ret,step):
    if ret:
        print("  error at "+step)
    return 0

for folder in folder_list:
    file_name = folder

    #open model
    ret = a.SapModel.File.OpenFile(folder_path+os.sep+folder+os.sep+folder+".sdb")
    ret = checkret(ret,"open model "+file_name)
    
    #set no load cases to run
    ret = a.SapModel.Analyze.SetRunCaseFlag(None,False,True)
    ret = checkret(ret,"set no cases to run "+file_name)
    
    #set specific load cases to run
    for case in cases_to_run:
        ret = a.SapModel.Analyze.SetRunCaseFlag(case,True)
    
    #run analysis
    ret = a.SapModel.Analyze.RunAnalysis()
    ret = checkret(ret,"run analysis "+file_name)

    print(file_name + " complete")