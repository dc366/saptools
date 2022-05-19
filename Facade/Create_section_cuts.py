# -*- coding: utf-8 -*-
"""
Created on Mon May 17 15:32:21 2021

@author: djc
"""

import attach

a = attach.sapApplication()

group_list = ['C26-06_sc',
'C27-03_sc',
'C26-07_sc',
'C26-08_sc',
'C27-04_sc',
'C24-18_sc',
'C25-19_sc',
'C26-21_sc',
'C28-16_sc',
'C27-17_sc',
'C29-16_sc']

for group in group_list:
    
    _,obj_type,objs,ret = a.SapModel.GroupDef.GetAssignments(group)
        
    for item in zip(obj_type,objs):
        if item[0] == 1:
            _,point_obj_types,point_objs,_,point_ret = a.SapModel.PointObj.GetConnectivity(item[1])
            for point_item in zip(point_obj_types,point_objs):
                if point_item[0] == 5:
                    a.SapModel.AreaObj.SetGroupAssign(point_item[1],group)
    
    a.SapModel.SectCut.SetByGroup(group,group,1)