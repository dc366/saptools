# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 07:06:45 2022

@author: djc
"""

import attach
import UtilityFuncs as uf
import os.path
import pandas as pd
from shutil import copyfile

folder_path = r'C:\Users\djc\Desktop\SAP Working\Single Panel Models\StiffStudies\Run\Run'
folder_list = uf.folders_in_folder(folder_path)
remote_path = r'J:\ENG\1092 LMNA LA\Facade Peer Review\Panel Scanning Validation\Rhino - Minds Final QAQC\SAP Output'

a = attach.sapApplication()

def checkret(ret,step):
    if ret:
        print("  error at "+step)
    return 0

cases_to_output = ['DEAD',"DEAD-WT Horizontal","DEAD: IBP - Horiz","+Thermal15","-Thermal15"]

for folder in folder_list:
    file_name = folder

    #open model
    ret = a.SapModel.File.OpenFile(folder_path+os.sep+folder+os.sep+folder+".sdb")
    ret = checkret(ret,"open model "+file_name)
    
    #set units
    ret = a.SapModel.SetPresentUnits(3)
    ret = checkret(ret,"set units "+file_name)
    
    #set force output parameters
    ret = a.SapModel.Results.Setup.SetOptionNLStatic(3)
    ret = checkret(ret,"set output step "+file_name)
    
    ret = a.SapObject.SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput()
    ret = checkret(ret,"deselect all cases "+file_name)
    
    for lc in cases_to_output:
        ret += a.SapModel.Results.Setup.SetCaseSelectedForOutput(lc,True)
    ret = checkret(ret,"toggle cases to output "+file_name)
    
    #output joint displacements
    try:
        joint_results = a.SapModel.Results.JointDispl("panel_face", 2)
    except:
        print("  joint displacement extract error "+file_name)
    else:
        ret = joint_results[-1]
        ret = checkret(ret,"output joint displacement "+file_name)
        
    #output joint connectivity for area elements
    a.select_group("panel_face")
    bj_members,_ = a.get_list_sap('area')
    
    bj_member_connectivity = dict()
    for member in bj_members:
        member_connectivity = a.SapModel.AreaObj.GetPoints(member)
        ret += member_connectivity[-1]
        bj_member_connectivity[member] = member_connectivity[:-1]
        
    ret = checkret(ret,"output member connectivity "+file_name)
    
    #output joint coordinates for joints in group
    bj_joints,_ = a.get_list_sap('point')
    
    x_compiled = []
    y_compiled = []
    z_compiled = []
    joint_name_compiled = []
    
    for joint in bj_joints:
        joint_connectivity = a.SapModel.PointObj.GetCoordCartesian(joint)
        ret += joint_connectivity[-1]
        joint_name_compiled.append(joint)
        x_compiled.append(joint_connectivity[0])
        y_compiled.append(joint_connectivity[1])
        z_compiled.append(joint_connectivity[2]) 
    
    ret = checkret(ret,"output joint coordinate "+file_name)
        
    joint_output = {"joint names":joint_name_compiled,
                    "x (in.)": x_compiled,
                    "y (in.)": y_compiled,
                    "z (in.)": z_compiled}

    joint_1 = []
    joint_2 = []
    joint_3 = []
    joint_4 = []

    for area_elm in bj_member_connectivity.values():
        for j,jlist in zip(area_elm[1],[joint_1,joint_2,joint_3,joint_4]):
            jlist.append(j)
        if area_elm[0] == 3:
            joint_4.append("")

    area_output = {"area names": list(bj_member_connectivity.keys()),
                "joint 1": joint_1,
                "joint 2": joint_2,
                "joint 3": joint_3,
                "joint 4": joint_4}
    
    
    
    frame_joint_disp_output = {"joint names": joint_results[1],
                          "load case": joint_results[3],
                          "step type": joint_results[4],
                          "step number": joint_results[5],
                          "U1 (in.)": joint_results[6],
                          "U2 (in.)": joint_results[7],
                          "U3 (in.)": joint_results[8],
                          "R1 (rad.)":joint_results[9],
                          "R2 (rad.)":joint_results[10],
                          "R3 (rad.)":joint_results[11]}

    ew = pd.ExcelWriter(folder_path+os.sep+folder+os.sep+"output.xlsx")
    pd.DataFrame(joint_output).to_excel(ew,sheet_name="joint output",index=False)
    pd.DataFrame(area_output).to_excel(ew,sheet_name="area output",index=False)
    pd.DataFrame(frame_joint_disp_output).to_excel(ew,sheet_name="joint disp output",index=False)
    ew.save()
    
    os.makedirs(remote_path+os.sep+folder,exist_ok=True)
    copyfile(folder_path+os.sep+folder+os.sep+"output.xlsx",remote_path+os.sep+folder+os.sep+"output.xlsx")

    print(file_name + " complete")
