# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 09:14:30 2021

@author: djc
"""

import attach
import UtilityFuncs as uf
import os

a = attach.sapApplication()

folder_path = r'D:\Working\Sequence C1 - Base Models'
file_list = uf.files_in_folder(folder_path)

frame_sections = set()

def check_dupes(base_set,new_elements):
    unique_elements = []
    
    for e in new_elements:
        if e in base_set:
            pass
        else:
            base_set.add(e)
            unique_elements.append(e)
    
    return unique_elements
            
i = 0

for file in file_list:

    #check if sdb or something else. if something else, skip
    (_,ext) = os.path.splitext(file)
    if ext != ".sdb":
        continue

    #open model
    a.SapModel.File.OpenFile(folder_path+os.sep+file)

    #get frame section names
    sections = a.SapModel.PropFrame.GetNameList()

    #find uniques
    uniques = check_dupes(frame_sections,sections[1])
    print(f"uniques in {file}:{uniques}")
    
    #increment folder count
    i = i + 1
    
#cleanup
a.SapObject.ApplicationExit(False)
a.SapModel = None
a.SapObject = None