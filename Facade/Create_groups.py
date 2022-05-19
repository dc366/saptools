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
    ret = a.SapModel.GroupDef.SetGroup(group)