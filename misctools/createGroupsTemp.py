# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 15:16:45 2022

@author: acp
"""

import attach
a = attach.sapApplication()

filePath = r"C:\Users\acp\Desktop\2022_01_20 Sequence D2\temp.xlsx"
sheetName = "Sheet1"
header = "tempList"
listB = attach.get_list_excel(filePath,sheetName,header)
a.add_joints_to_group('LERA_WTpinPoints',listB)