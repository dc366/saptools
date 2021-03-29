# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:20:11 2021

@author: djc

Puts elements with substrings in bad_bay into a temp group for evaluation/deletion

"""

bad_bay = ['C03']

import attach

a = attach.sapApplication()

point_list = a.get_list_sap('point')
area_list = a.get_list_sap('area')
frame_list = a.get_list_sap('frame')
link_list = a.get_list_sap('link')

a.SapModel.SelectObj.ClearSelection()

bad_bay_group_joint = []
bad_bay_group_area = []
bad_bay_group_frame = []
bad_bay_group_link = []

for joint in point_list[0]:
    for bay in bad_bay:
        if bay in joint:
            bad_bay_group_joint.append(joint)
for area in area_list[0]:
    for bay in bad_bay:
        if bay in area:
            bad_bay_group_area.append(area)
for frame in frame_list[0]:
    for bay in bad_bay:
        if bay in frame:
            bad_bay_group_frame.append(frame)
for link in link_list[0]:
    for bay in bad_bay:
        if bay in link:
            bad_bay_group_link.append(link)

a.add_joints_to_group('temp',bad_bay_group_joint)          
a.add_areas_to_group('temp',bad_bay_group_area)
a.add_frames_to_group('temp',bad_bay_group_frame)