# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 07:06:45 2022

@author: djc
"""

import attach
import UtilityFuncs as uf
import os.path
import pandas as pd

folder_path = r'C:\Users\djc\Desktop\SAP Working\batch run'
folder_list = uf.folders_in_folder(folder_path)

a = attach.sapApplication()

def checkret(ret,step):
    if ret:
        print("  error at "+step)
    return 0

compiled_group = []

#initialize lists for results
NumberResults_compiled = []
Obj_compiled = []
ObjSta_compiled = []
Elm_compiled = []
ElmSta_compiled = []
LoadCase_compiled = []
StepType_compiled = []
StepNum_compiled = []
P_compiled = []
V2_compiled = []
V3_compiled = []
T_compiled = []
M2_compiled = []
M3_compiled = []

compiled_results = [NumberResults_compiled, Obj_compiled, ObjSta_compiled, 
    Elm_compiled, ElmSta_compiled, LoadCase_compiled, 
    StepType_compiled, StepNum_compiled, 
    P_compiled, V2_compiled, V3_compiled, 
    T_compiled, M2_compiled, M3_compiled]

bj_member_connectivity_compiled = dict()

joint_name_compiled = []
x_compiled = []
y_compiled = []
z_compiled = []

for folder in folder_list:
    file_name = folder

    #open model
    ret = a.SapModel.File.OpenFile(folder_path+os.sep+folder+os.sep+folder+".sdb")
    ret = checkret(ret,"open model "+file_name)
    
    #set units
    ret = a.SapModel.SetPresentUnits(3)
    ret = checkret(ret,"set units "+file_name)

    #save it to a subfolder
    os.makedirs(folder_path+os.sep+file_name,exist_ok=True)
    a.SapModel.File.Save(folder_path+os.sep+file_name+os.sep+file)    

    #run analysis
    ret = a.SapModel.Analyze.RunAnalysis()
    ret = checkret(ret,"run analysis "+file_name)
    
    #output forces on mem_bj-start.in and mem_bj-in
    try:
        member_results = a.SapModel.Results.FrameForce("mem_BJ-start.in", 2)
    except:
        print("  member force extract error MEM_BJ-start.in "+file_name)
    else:
        ret = member_results[-1]
        ret = checkret(ret,"output mem_bj-start.in "+file_name)
    
        for column,result in zip(compiled_results,member_results[:-1]):
            if type(result) is int:
                result = [result]
            column.extend(list(result))
    
    try:
        member_results = a.SapModel.Results.FrameForce("mem_BJ-in", 2)
    except:
        print("  member force extract error mem_BJ-in"+file_name)
    else:    
        ret = member_results[-1]
        ret = checkret(ret,"output mem_bj-in "+file_name)
    
        for column,result in zip(compiled_results,member_results[:-1]):
            if type(result) is int:
                result = [result]
            column.extend(list(result))
        
    #output joint connectivity for mem_bj-start.in and mem_bj-in
    a.select_group("mem_BJ-start.in")
    a.select_group("mem_BJ-in")
    bj_members,_ = a.get_list_sap('frame')
    
    bj_member_connectivity = dict()
    for member in bj_members:
        member_connectivity = a.SapModel.FrameObj.GetPoints(member)
        ret += member_connectivity[-1]
        bj_member_connectivity[member] = member_connectivity[:-1]
        
    ret = checkret(ret,"output member connectivity "+file_name)
    
    bj_member_connectivity_compiled.update(bj_member_connectivity)
    
    #output joint coordinates for connected joints
    bj_joints = set([joint for joint_pair in bj_member_connectivity.values() for joint in joint_pair])
    
    for joint in bj_joints:
        joint_connectivity = a.SapModel.PointObj.GetCoordCartesian(joint)
        ret += joint_connectivity[-1]
        joint_name_compiled.append(joint)
        x_compiled.append(joint_connectivity[0])
        y_compiled.append(joint_connectivity[1])
        z_compiled.append(joint_connectivity[2]) 
    
    ret = checkret(ret,"output joint coordinate "+file_name)
        
    #close model
    
    print(file_name + " complete")
    
joint_output = {"joint names":joint_name_compiled,
                "x (in.)": x_compiled,
                "y (in.)": y_compiled,
                "z (in.)": z_compiled}

frame_output = {"frame names": list(bj_member_connectivity_compiled.keys()),
                "i end": [i_j[0] for i_j in bj_member_connectivity_compiled.values()],
                "j end": [i_j[1] for i_j in bj_member_connectivity_compiled.values()]}

frame_force_output = {"frame names": Obj_compiled,
                      "frame station": ObjSta_compiled,
                      "load case": LoadCase_compiled,
                      "step type": StepType_compiled,
                      "step number": StepNum_compiled,
                      "P (k.)": P_compiled,
                      "V2 (k.)": V2_compiled,
                      "V3 (k.)": V3_compiled,
                      "T (k-in)":T_compiled,
                      "M2 (k-in)":M2_compiled,
                      "M3 (k-in)":M3_compiled}

ew = pd.ExcelWriter(folder_path+os.sep+"output.xlsx")
pd.DataFrame(joint_output).to_excel(ew,sheet_name="joint output",index=False)
pd.DataFrame(frame_output).to_excel(ew,sheet_name="frame output",index=False)
pd.DataFrame(frame_force_output).to_excel(ew,sheet_name="frame force output",index=False)
ew.save()
ew.close()
