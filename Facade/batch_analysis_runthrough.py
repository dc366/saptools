# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 07:06:45 2022

@author: djc
"""

import attach
import UtilityFuncs as uf
import os.path

folder_path = r'C:\Users\djc\Desktop\SAP Working\all models\SEQB'
file_list = uf.files_in_folder(folder_path)

a = attach.sapApplication()

for file in file_list:
    
    #check if sdb or something else. if something else, skip
    (file_name,ext) = os.path.splitext(file)
    if ext != ".sdb":
        continue

    #open model
    ret = a.SapModel.File.OpenFile(folder_path+os.sep+file)

    a.SapModel.File.Save()    

    print(file_name + " complete")
