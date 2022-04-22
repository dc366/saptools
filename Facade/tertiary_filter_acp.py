# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:48:09 2021

@author: djc

IMPORTANT: This script does not assign CONN_stiff members to either secondary or tertiary
        This section has a mass/weight multiplier of 0 and any reverseSW assignment is moot

"""

import attach

a = attach.sapApplication()

tertiary_substrings = ['_KH_','_PB_','_PH_','_BB_','spTert']
tertiary_sections = ['CONN_rod','CONN_rod_1in', 'CONN_rod_0.7in', 'CON_rod_additional']
stiffener_substrings = ['-S-']
stiffener_sections = ['0.5" Hat Stiffener','Z-shaped Stiffener','2.5" Trap Hat','4.5" Trap Hat']
connSTIFF_sections = ['CONN_stiff']
tertiary_members = set()
secondary_members = set()
connSTIFF_members = set()
stiffener_members = set()

#search all frames for tertiary substrings and move them to another group
[_,frames,_] = a.SapModel.FrameObj.GetNameList()
frames_list = list(frames)

#tertiary_members = [frame in frames if any(sub in frame for sub in tertiary_substrings)]
#secondary_members = [frame in frames if not any(sub in frame for sub in tertiary_substrings)]

for frame in frames:
    if any(sub in frame for sub in tertiary_substrings):
        tertiary_members.add(frame)
    elif any(sub in frame for sub in stiffener_substrings):
        stiffener_members.add(frame)
    else:
        secondary_members.add(frame)

#search remaining unfiltered frames for sections that are tertiary and move them to another group

""" List Comprehension alternatives, to be tested
getsection = a.SapModel.FrameObj.GetSection
frame_sections = [(frame,getsection(frame)) for frame in secondary_members]
tertiary_section_check = [frame for (frame,section) in frame_sections if section in tertiary_sections]
connSTIFF_section_check = [frame for (frame,section) in frame_sections if section in connSTIFF_sections]

tertiary_members = tertiary_members | tertiary_section_check
connSTIFF_members = connSTIFF_members | connSTIFF_section_check
secondary_members = secondary_members - tertiary_section_check
secondary_members = secondary_members - connSTIFF_section_check
"""

for frame in secondary_members.copy():
    frame_section,_,_ = a.SapModel.FrameObj.GetSection(frame)
    if frame_section in tertiary_sections:
        tertiary_members.add(frame)
        secondary_members.remove(frame)
    elif frame_section in stiffener_sections:
        stiffener_members.add(frame)
        secondary_members.remove(frame)
    elif frame_section in connSTIFF_sections:
        connSTIFF_members.add(frame)
        secondary_members.remove(frame)


#create 3 groups     
a.add_frames_to_group('LERA_tertiary',tertiary_members)
a.add_frames_to_group('LERA_secondary',secondary_members)
a.add_frames_to_group('LERA_CONNstiff',connSTIFF_members)
a.add_frames_to_group('LERA_stiffeners',stiffener_members)

#add WW elements to secondary members group
a.SapModel.SelectObj.PropertyArea("WW")
[ww_elems,_] = a.get_list_sap("area")
a.add_areas_to_group('LERA_secondary',ww_elems)
