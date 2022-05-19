# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 07:06:45 2022

@author: djc
"""

import attach
import UtilityFuncs as uf
import os.path
import pandas as pd

folder_path = r'C:\Users\djc\Desktop\SAP Working\all models\SEQC1'
folder_list = uf.folders_in_folder(folder_path)

a = attach.sapApplication()

def checkret(ret,step):
    if ret:
        print("  error at "+step)
    return 0

compiled_group = []

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
    
    #output joint connectivity for all frames
    a.SapModel.SelectObj.All()
    bj_members,_ = a.get_list_sap('frame')
    
    bj_member_connectivity = dict()
    for member in bj_members:
        member_connectivity = a.SapModel.FrameObj.GetPoints(member)
        ret += member_connectivity[-1]
        member_connectivity[0] = folder + "_" + member_connectivity[0]
        member_connectivity[1] = folder + "_" + member_connectivity[1]
        bj_member_connectivity[member] = member_connectivity[:-1]
        
    ret = checkret(ret,"output member connectivity "+file_name)
    
    bj_member_connectivity_compiled.update(bj_member_connectivity)
    
    #output joint coordinates for connected joints
    bj_joints = set([joint for joint_pair in bj_member_connectivity.values() for joint in joint_pair])
    
    for joint in bj_joints:
        joint = joint[len(folder + "_"):]
        joint_connectivity = a.SapModel.PointObj.GetCoordCartesian(joint)
        ret += joint_connectivity[-1]
        joint_name_compiled.append(folder + "_" + joint)
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


ew = pd.ExcelWriter(folder_path+os.sep+"output_geom_unique_points.xlsx")
pd.DataFrame(joint_output).to_excel(ew,sheet_name="joint output",index=False)
pd.DataFrame(frame_output).to_excel(ew,sheet_name="frame output",index=False)
ew.save()
