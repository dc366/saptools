# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 15:20:06 2022

@author: acp
"""

import attach
a = attach.sapApplication()

filePath = r"C:\Users\acp\Desktop\P1092 Occulus Trellis Work\2022_02_15 SS Pipe Design.xlsx"
sheetName = "Pivot Table"
header = "Temp"
listA = attach.get_list_excel(filePath,sheetName,header)
listB = [str(x) for x in listA]
listC = [x[:len(x)-2] for x in listB]

a.add_frames_to_group('LERA_Controlling Frames',listC)