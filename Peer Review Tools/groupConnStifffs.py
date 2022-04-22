# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 10:12:20 2022

@author: acp
"""
#Purpose of this script is to create groups for the prince/king truss connstiffs and group them based on length
import attach
a = attach.sapApplication()
from tqdm import tqdm

conStiffLabels = attach.sapGroup(a, "LERA_Tertiary Trusses").ObjectName
#"LERA_Tertiary Trusses" is a group that you make manually
conStiffList = []
shortA =[]
shortB =[]
extensionA = []
extensionB = []

for frame in tqdm(conStiffLabels):
    (propName, SAuto, ret) = a.SapModel.FrameObj.GetSection(frame)
    x1 = attach.sapJoint( a, attach.sapFrame(a, frame).iEnd).x
    y1 = attach.sapJoint( a, attach.sapFrame(a, frame).iEnd).y
    z1 = attach.sapJoint( a, attach.sapFrame(a, frame).iEnd).z
    x2 = attach.sapJoint( a, attach.sapFrame(a, frame).jEnd).x
    y2 = attach.sapJoint( a, attach.sapFrame(a, frame).jEnd).y
    z2 = attach.sapJoint( a, attach.sapFrame(a, frame).jEnd).z  
    length = ((x2-x1)**2 +(y2-y1)**2 + (z2-z1)**2)**(1/2)
    length = round(length, 2)
        
    if propName == "CONN_stiff":
        conStiffList.append(frame)

        if length <= 4.25:
            shortA.append(frame)

        if length ==4.75:
            shortB.append(frame)

        if length > 4.75 and length < 10:
            extensionA.append(frame)

        if length >= 10:
            extensionB.append(frame)

#Create SAP groups:
print("Creating Groups in SAP...")
a.SapModel.GroupDef.Delete("LERA_shortA")
a.SapModel.GroupDef.Delete("LERA_shortB")
a.SapModel.GroupDef.Delete("LERA_conStiffList")
a.SapModel.GroupDef.Delete("LERA_extensionA")
a.SapModel.GroupDef.Delete("LERA_extensionB")

a.SapModel.GroupDef.SetGroup('LERA_shortA', 65280)
a.SapModel.GroupDef.SetGroup('LERA_shortB', 33023)
a.SapModel.GroupDef.SetGroup('LERA_conStiffList', 65535 )
a.SapModel.GroupDef.SetGroup('LERA_extensionA', 255)
a.SapModel.GroupDef.SetGroup('LERA_extensionB', 16711935)


a.add_frames_to_group('LERA_conStiffList',conStiffList)      
a.add_frames_to_group('LERA_shortA',shortA)  
a.add_frames_to_group('LERA_shortB',shortB)  
a.add_frames_to_group('LERA_extensionA',extensionA)  
a.add_frames_to_group('LERA_extensionB',extensionB)    
        


