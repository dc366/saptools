# -*- coding: utf-8 -*-
"""

Take selected frame elements and fix U1,U2,U3 at i and j end, while maintaining other releases

Created on Fri Feb 19 17:56:51 2021

@author: djc
"""

import attach

a = attach.sapApplication()

selectedobj, _ = a.get_list_sap("frame")

for frame in selectedobj:
    i_release,j_release,start_value,end_value,_ = a.SapModel.FrameObj.GetReleases(frame)
    i_release = list(i_release)
    j_release = list(j_release)
    i_release[0:3] = [False,False,False]
    j_release[0:3] = [False,False,False]
    a.SapModel.FrameObj.SetReleases(frame,i_release,j_release,start_value,end_value)