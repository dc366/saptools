# -*- coding: utf-8 -*-
"""

@author: djc

"""

import attach

a = attach.sapApplication()

#place elements with these substrings into separate groups

panel_substrings = ['C27-17']

area_dict = {}
frame_dict = {} #
for sub in panel_substrings:
    area_dict[sub] = []
    frame_dict[sub] = [] #

#search all areas for panel substrings and move them to another group
[_,areas,_] = a.SapModel.AreaObj.GetNameList()
[_,frames,_] = a.SapModel.FrameObj.GetNameList() #
area_list = list(areas)
frame_list = list(frames) #

for area in areas:
    for sub in panel_substrings:
        if sub in area:
            area_dict[sub].append(area)

####
for frame in frames:
    for sub in panel_substrings:
        if sub in frame:
            frame_dict[sub].append(frame)
####

#create groups for each panel   
for sub in panel_substrings:
    a.add_areas_to_group('panel_' + sub , area_dict[sub])
    a.add_frames_to_group('panel_'+ sub , frame_dict[sub]) #