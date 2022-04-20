# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 14:34:45 2022

@author: acp
"""

import updateBraceConnectivityV2
import attach


filePath = r"C:\Users\acp\Desktop\Facad Peer Review\2022_04_18 C11B Updated PB WPs Test\LMNA_SEQ-B_East_PB_Update_acpTemp.xlsx"
frameList = attach.get_list_excel(filePath, "C11B", "SAP Name")
modelName = "C11B"
b = attach.get_list_excel(filePath, "C11B", "New JointI GlobalX")
c = attach.get_list_excel(filePath, "C11B", "New JointI GlobalY")
d = attach.get_list_excel(filePath, "C11B", "New JointI GlobalZ")
e = attach.get_list_excel(filePath, "C11B", "New JointJ GlobalX")
f = attach.get_list_excel(filePath, "C11B", "New JointJ GlobalY")
g = attach.get_list_excel(filePath, "C11B", "New JointJ GlobalZ")


updateBraceConnectivityV2.shiftWPs(modelName, frameList, b, c, d, e, f, g)