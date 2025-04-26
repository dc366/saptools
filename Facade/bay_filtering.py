# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:20:11 2021

@author: djc

Puts elements with substrings in bad_bay into a temp group for evaluation/deletion

"""

#bad_bay = ['C17T','C18T','C19T','C20T','C21T']
#bad_bay = ['C17-11','C17-12','C17-13','C17-14','C17-15','C17-16','C17-17','C17-18',
#           'C18-11','C18-12','C18-13','C18-14','C18-15','C18-16','C18-17','C18-18',
#           'C19-12','C19-13','C19-14','C19-15','C19-16','C19-17','C19-18','C19-19','C19-20',
#           'C20-13','C20-14','C20-15','C20-16','C20-17','C20-18','C20-19','C20-20',
#           'C21-09','C21-10','C21-11','C21-12','C21-13','C21-14','C21-15','C21-16','C21-17']
#bad_bay = ['C02T',	'C03T',	'C04T',	'C05T',	'C06T',	'C07T',	'C08T',	'C09T']
"""
bad_bay = ['C02-09','C02-10','C02-11','C02-12','C02-13','C02-14','C02-15','C02-16',
           'C03-07','C03-08','C03-09','C03-10','C03-11','C03-12','C03-13','C03-14',
           'C04-07','C04-08','C04-09','C04-10','C04-11','C04-12','C04-13','C04-14',
           'C05-08','C05-09','C05-10','C05-11','C05-12','C05-13','C05-14','C05-15',
           'C06-08','C06-09','C06-10','C06-11','C06-12','C06-13','C06-14','C06-15',
           'C07-09','C07-10','C07-11','C07-12','C07-13','C07-14','C07-15','C07-16','C07-17',
           'C08-11','C08-12','C08-13','C08-14','C08-15','C08-16','C08-17','C08-18',
           'C09-10','C09-11','C09-12','C09-13','C09-14','C09-15']

bad_bay = ['C06-07','C09-09']

bad_bay = ['C09T',
'C10T',
'C11T',
'C12T', 
'C13T',
'C14T',
'C15T',
'C16T',
'C17T', 'GL-03']


bad_bay = ['C17-11',	'C16-09',	'C15-09',	'C14-09',	'C13-10',	'C12-11',	'C11-08',	'C10-07',	'C09-08']
"""
bad_bay = ['PB']
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

#for joint in point_list[0]:
#    for bay in bad_bay:
#        if bay in joint:
#            bad_bay_group_joint.append(joint)
#for area in area_list[0]:
#    for bay in bad_bay:
#        if bay in area:
#            bad_bay_group_area.append(area)
for frame in frame_list[0]:
    for bay in bad_bay:
        if bay in frame:
            bad_bay_group_frame.append(frame)
#for link in link_list[0]:
#    for bay in bad_bay:
#        if bay in link:
#            bad_bay_group_link.append(link)

#a.add_joints_to_group('top_truss',bad_bay_group_joint)          
#a.add_areas_to_group('C02-C05',bad_bay_group_area)
a.add_frames_to_group('PB',bad_bay_group_frame)