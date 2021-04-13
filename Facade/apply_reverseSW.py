# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:37:51 2021

@author: djc
"""

import attach

a = attach.sapApplication()

secondary_group = 'LERA_secondary'

#assign reverseSW to secondary members
a.SapModel.FrameObj.SetLoadGravity(secondary_group,"reverseSW",X=0,Y=0,Z=1.0,Replace=True,ItemType=1)
a.SapModel.AreaObj.SetLoadGravity(secondary_group,"reverseSW",X=0,Y=0,Z=1.0,Replace=True,ItemType=1)
print("Please verify LERA_secondary group to ensure that load is applied to correct members")