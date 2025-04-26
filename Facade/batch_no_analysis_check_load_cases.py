# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 07:06:45 2022

@author: djc
"""

import attach
import UtilityFuncs as uf
import os.path
import pandas as pd

folder_path = r'C:\Users\djc\Desktop\SAP Working\B and C1 Subset'
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
    
    compiled_load_cases[folder] = load_cases
    
    print(file_name + " complete")


ew = pd.ExcelWriter(folder_path+os.sep+"load_cases.xlsx")
pd.DataFrame({ key:pd.Series(value) for key, value in compiled_load_cases.items() }).to_excel(ew,sheet_name="loadcase",index=False)
ew.save()