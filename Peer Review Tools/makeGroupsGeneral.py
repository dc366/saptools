# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 15:20:06 2022

@author: acp
"""

import attach
a = attach.sapApplication()

filePath = r"C:\Users\acp\Desktop\Facad Peer Review\2022_04_26 C1 SE Study\LMNA_SEQ-C1_Southeast_PB_Update_v3_acp.xlsx"
sheetName = "deletedC20B_C60"
header = "deletedPBs"
listA = attach.get_list_excel(filePath,sheetName,header)
listB = [str(x) for x in listA]
#listC = [x[:len(x)-2] for x in listB]

a.add_frames_to_group('LERA_DeletedPBs_C60&C20B',listB)