# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 15:30:46 2021

@author: djc


Torsion releases:
    C01B_mem_171

Flip releases:
    C59T_PP_002
    C59T_PP_003
    
    
Fix joint:
    %C59T_T2b-S-R
    %C59T_T2b-S-L
    
C64Bb - fix prince hat member framing (8 members total)
"""

import attach
path = r"C:\Users\acp\Desktop\2021_05_06 C3 WEST\debug.xlsx"




x= attach.get_list_excel(path, "Sheet1", "x" )  
y= attach.get_list_excel(path, "Sheet1", "y" )    
z = attach.get_list_excel(path, "Sheet1", "z" ) 

a = attach.sapApplication()

unique = list(set(zip(x,y,z)))
name_list = []

for joint in unique:
    new_joint = a.SapModel.PointObj.AddCartesian(X=joint[0],Y=joint[1],Z=joint[2],UserName="acp-"+str(unique.index(joint)),MergeOff=True)
    name_list.append(new_joint[0])

a.add_joints_to_group("instabilities",name_list)