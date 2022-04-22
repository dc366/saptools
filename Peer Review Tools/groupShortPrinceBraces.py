# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 10:12:20 2022

@author: acp
"""
#Purpose of this script is to create groups for the prince/king truss connstiffs and group them based on length
import attach
a = attach.sapApplication()
from tqdm import tqdm

PBlabels = attach.sapGroup(a, "LERA_Prince Braces").ObjectName
#"LERA_Tertiary Trusses" is a group that you make manually
PB_lessThan12 = []
PB_12to18 = []
PB_18to22 = []
lengths = []


for frame in tqdm(PBlabels):
    x1 = attach.sapJoint( a, attach.sapFrame(a, frame).iEnd).x
    y1 = attach.sapJoint( a, attach.sapFrame(a, frame).iEnd).y
    z1 = attach.sapJoint( a, attach.sapFrame(a, frame).iEnd).z
    x2 = attach.sapJoint( a, attach.sapFrame(a, frame).jEnd).x
    y2 = attach.sapJoint( a, attach.sapFrame(a, frame).jEnd).y
    z2 = attach.sapJoint( a, attach.sapFrame(a, frame).jEnd).z  
    length = ((x2-x1)**2 +(y2-y1)**2 + (z2-z1)**2)**(1/2)
    length = round(length, 2)
    
    lengths.append(length)
        
    if length < 12:
        PB_lessThan12.append(frame)

    if length >= 12 and length <= 18:
        PB_12to18.append(frame)

    if length > 18 and length <= 22:
        PB_18to22.append(frame)




#Create SAP groups:
print("Creating Groups in SAP...")

a.SapModel.GroupDef.Delete("LERA_PB_lessThan12")
a.SapModel.GroupDef.Delete("LERA_PB_12to18")
a.SapModel.GroupDef.Delete("LERA_PB_18to24")
a.SapModel.GroupDef.Delete("LERA_PB_18to22")

 
a.add_frames_to_group('LERA_PB_lessThan12',PB_lessThan12)  
a.add_frames_to_group('LERA_PB_12to18',PB_12to18)  
a.add_frames_to_group('LERA_PB_18to22',PB_18to22)    
        


