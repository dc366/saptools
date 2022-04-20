# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 10:25:37 2022

@author: acp
"""

import attach
a = attach.sapApplication()

a.clear_selection()

a.select_group("MEM_BJ-in")
a.select_group("MEM_BJ-start.in")
ret = a.SapModel.SelectObj.PropertyLink("ballGapTemp")
ret = a.SapModel.SelectObj.PropertyLink("slotGapTemp")