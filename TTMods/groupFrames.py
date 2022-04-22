# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 21:13:24 2021

@author: acp
"""

import attach
sapBox = attach.sapApplication()

filePath = r"C:\Users\ACP\Desktop\2021_04_26 SeqB West Redo\2021_04_26_MB TT Updates.xlsx"
sheetName = "BEastMods"

frameNames= attach.get_list_excel(filePath, sheetName, "Member ID" ) 

sapBox.add_frames_to_group("LERA-moddedFrames", frameNames)