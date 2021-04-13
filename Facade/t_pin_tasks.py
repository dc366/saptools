# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 11:07:56 2021

@author: djc
"""

import attach

a = attach.sapApplication()

tpin_sections = ['CONN_rod','CONN_rod_1in']

for ts in tpin_sections:
    a.SapModel.SelectObj.PropertyFrame(ts)

#set rigid zone factor
a.SapModel.FrameObj.SetEndLengthOffset(Name=None,AutoOffset=False,Length1=3.5,Length2=0,RZ=0.45,ItemType=2)

#set end releases
a.SapModel.FrameObj.SetReleases(None,
                                (False,False,False,False,False,False),
                                (False,False,False,False,False,False),
                                            StartValue=(0,0,0,0,0,0),
                                            EndValue=(0,0,0,0,0,0),
                                            ItemType=2
                                            )

#create t-pin group
[t_pins,_] = a.get_list_sap("frame")
a.add_frames_to_group('LERA_T-pins',t_pins)

#find t-pin end joints and create group
j_end = []
for tp in t_pins:
    [_,j,_] = a.SapModel.FrameObj.GetPoints(tp)
    j_end.append(j)
a.add_joints_to_group('LERA_T-pin_ends',j_end)