# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:06:43 2021

@author: djc
"""

import attach

a = attach.sapApplication()

king_hat_substrings = ['_KH_']

#get all frame definitions
[_,frames,_] = a.SapModel.FrameObj.GetNameList()

#get all king hat elements
king_hats = [s for s in frames if any(sub in s for sub in king_hat_substrings)]

member_pin_list = set()
point_fix_list = set()
point_pin_list = set()

#find king hats with releases. add released joint to fix list, add member with releases to pin list
for kh in king_hats:
    i_release,j_release,start_value,end_value,_ = a.SapModel.FrameObj.GetReleases(kh)
    i_end, j_end, _ = a.SapModel.FrameObj.GetPoints(kh)
    
    if any(i_release):
        member_pin_list.add(kh)
        point_fix_list.add(i_end)
    if any(j_release):
        member_pin_list.add(kh)
        point_fix_list.add(j_end)
        
a.add_frames_to_group('wt_king_hats',king_hats)
a.add_frames_to_group('wt_pin_members',member_pin_list)
a.add_joints_to_group('wt_fix_joints',point_fix_list)

#get all CONNSTIFF members
a.SapModel.SelectObj.PropertyFrame("CONN_stiff")
[connstiff,_] = a.get_list_sap("frame")

#find CONSTIFF members with releases. add released joint to pin list
for cs in connstiff:
    i_release,j_release,start_value,end_value,_ = a.SapModel.FrameObj.GetReleases(cs)
    i_end, j_end, _ = a.SapModel.FrameObj.GetPoints(cs)
    
    if any(i_release):
        point_pin_list.add(i_end)
    if any(j_release):
        point_pin_list.add(j_end)
        
#a.add_joints_to_group('wt_pin_joints',point_pin_list)

