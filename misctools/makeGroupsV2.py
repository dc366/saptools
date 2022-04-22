# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:56:23 2021

@author: acp
"""

import attach
a = attach.sapApplication()

grp1 = set()
grp2 = set()
grp3 = set()
grp4 = set()
grp5 = set()


for j in range(len(chgCont)):
    if chgCont[j]<0:
        grp1.add(frameList[j])
    elif 0<=chgCont[j]< 0.05:
        grp2.add(frameList[j])
    elif 0.05<=chgCont[j]< 0.1:
        grp3.add(frameList[j])
    elif 0.1<=chgCont[j]< 0.2:
        grp4.add(frameList[j])
    elif chgCont[j]>= 0.2:
        grp5.add(frameList[j])
        
a.SapModel.GroupDef.SetGroup('LERA_LessThan0', 255)
a.SapModel.GroupDef.SetGroup('LERA_0-5', 16711935)
a.SapModel.GroupDef.SetGroup('LERA_5-10', 65280)
a.SapModel.GroupDef.SetGroup('LERA_10-20', 65535)
        
a.add_frames_to_group('LERA_LessThan0',grp1)
a.add_frames_to_group('LERA_0-5',grp2)
a.add_frames_to_group('LERA_5-10',grp3)
a.add_frames_to_group('LERA_10-20',grp4)
a.add_frames_to_group('LERA_GreaterThan20',grp5)
a.add_frames_to_group('LERA_WeightStudy',frameList)

filePath = r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\2021_11_04 Member Changes.xlsx"
sheetName = "BEast"
header = "Special"
listB = attach.get_list_excel(filePath,sheetName,header)
a.add_frames_to_group('LERA_WeightStudy',listB)