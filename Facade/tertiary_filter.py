# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:48:09 2021

@author: djc

IMPORTANT: This script does not assign CONN_stiff members to either secondary or tertiary
        This section has a mass/weight multiplier of 0 and any reverseSW assignment is moot

"""

import attach

a = attach.sapApplication()

tertiary_substrings = ['_KH_','_PB_','_PH_','_BB_']
tertiary_sections = ['CONN_rod','CONN_rod_1in']
connSTIFF_sections = ['CONN_stiff']
tertiary_members = set()
secondary_members = set()
connSTIFF_members = set()

#search all frames for tertiary substrings and move them to another group
[_,frames,_] = a.SapModel.FrameObj.GetNameList()
frames_list = list(frames)

for frame in frames:
    if any(sub in frame for sub in tertiary_substrings):
        tertiary_members.add(frame)
    else:
        secondary_members.add(frame)

#search remaining unfiltered frames for sections that are tertiary and move them to another group
for frame in secondary_members.copy():
    frame_section,_,_ = a.SapModel.FrameObj.GetSection(frame)
    if frame_section in tertiary_sections:
        tertiary_members.add(frame)
        secondary_members.remove(frame)
    elif frame_section in connSTIFF_sections:
        connSTIFF_members.add(frame)
        secondary_members.remove(frame)

#create 3 groups     
a.add_frames_to_group('LERA_tertiary',tertiary_members)
a.add_frames_to_group('LERA_secondary',secondary_members)
a.add_frames_to_group('LERA_CONNstiff',connSTIFF_members)

#assign reverseSW to secondary members
a.SapModel.FrameObj.SetLoadGravity("LERA_secondary","reverseSW",X=0,Y=0,Z=-1.0,ItemType=1)