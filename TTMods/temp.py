# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 16:45:34 2021

@author: acp
"""

import attach
sapBox = attach.sapApplication()

filePath = r"C:\Users\acp\Desktop\2021_09_20 Seq A West\2021_09_27-LERAMODS.xlsx"
sheetName = "temp"

jointNames= attach.get_list_excel(filePath, sheetName, "temp") 

sapBox.add_links_to_group("wt_KHLinks_zz", jointNames)