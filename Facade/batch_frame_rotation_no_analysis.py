# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 07:06:45 2022

@author: djc
"""

import attach
import UtilityFuncs as uf
import os.path
import pandas as pd

folder_path = r'C:\Users\djc\Desktop\SAP Working\all models\SEQB'
folder_list = uf.folders_in_folder(folder_path)

a = attach.sapApplication()

def checkret(ret,step):
    if ret:
        print("  error at "+step)
    return 0

compiled_group = []

with open(r'C:\Users\djc\Desktop\SAP Working\lc selection.txt','r') as f:
    cases_to_output = f.read().split("\n")

#initialize lists for results
NumberResults_compiled = []
Obj_compiled = []
Elm_compiled = []
PointElm_compiled = []
LoadCase_compiled = []
StepType_compiled = []
StepNum_compiled = []
F1_compiled = []
F2_compiled = []
F3_compiled = []
M1_compiled = []
M2_compiled = []
M3_compiled = []

compiled_results = [NumberResults_compiled, Obj_compiled, Elm_compiled, PointElm_compiled, LoadCase_compiled, 
    StepType_compiled, StepNum_compiled, 
    F1_compiled, F2_compiled, F3_compiled, 
    M1_compiled, M2_compiled, M3_compiled]

bj_member_connectivity_compiled = dict()

for folder in folder_list:
    file_name = folder

    #open model
    ret = a.SapModel.File.OpenFile(folder_path+os.sep+folder+os.sep+folder+".sdb")
    ret = checkret(ret,"open model "+file_name)
    
    #set units
    ret = a.SapModel.SetPresentUnits(3)
    ret = checkret(ret,"set units "+file_name)
        
    #output frame rotations for mem_bj-start.in and mem_bj-in
    a.select_group("mem_BJ-start.in")
    a.select_group("mem_BJ-in")
    bj_members,_ = a.get_list_sap('frame')
    
    bj_member_rot = dict()
    for member in bj_members:
        member_connectivity = a.SapModel.FrameObj.GetLocalAxes(member)
        ret += member_connectivity[-1]
        bj_member_rot[member] = member_connectivity[:-1]
        
    ret = checkret(ret,"output member connectivity "+file_name)
    
    bj_member_connectivity_compiled.update(bj_member_rot)
    
    #close model
    
    print(file_name + " complete")
