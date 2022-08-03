# -*- coding: utf-8 -*-
"""
Created on Mon May 17 15:32:21 2021

@author: djc
"""

import attach

a = attach.sapApplication()

group_list = ['TL','TR','BL','BR']

for group in group_list:
    ret = a.SapModel.GroupDef.SetGroup(group)