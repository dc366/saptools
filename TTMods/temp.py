# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 16:45:34 2021

@author: acp
"""

import attach
sapBox = attach.sapApplication()

filePath = r"C:\Users\ACP\Desktop\2021_04_XX Seq C1 NE\2021_05_12-LERAMOD.xlsx"
sheetName = "temp"

jointNames= attach.get_list_excel(filePath, sheetName, "temp") 

sapBox.add_joints_to_group("LERA-All TPin Ends", jointNames)