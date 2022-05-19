# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 14:34:45 2022

@author: acp
"""

import updateBraceConnectivityV3
import attach


filePath = r"C:\Users\acp\Desktop\Facad Peer Review\2022_04_26 C1 SE Study\LMNA_SEQ-C1_Southeast_PB_Update_v3_acp.xlsx"
frameList = attach.get_list_excel(filePath, "C20B", "SAP Name")
modelName = "C20B"
b = attach.get_list_excel(filePath, "C20B", "Point C GlobalX")   #PB i joint
c = attach.get_list_excel(filePath, "C20B", "Point C GlobalY")   #PB i joint
d = attach.get_list_excel(filePath, "C20B", "Point C GlobalZ")   #PB i joint
e = attach.get_list_excel(filePath, "C20B", "Point B GlobalX")   #PB j joint
f = attach.get_list_excel(filePath, "C20B", "Point B GlobalY")   #PB j joint
g = attach.get_list_excel(filePath, "C20B", "Point B GlobalZ")   #PB j joint
x = attach.get_list_excel(filePath, "C20B", "Point A GlobalX")   #rigid offset point on KH
y = attach.get_list_excel(filePath, "C20B", "Point A GlobalY")   #rigid offset point on KH
z = attach.get_list_excel(filePath, "C20B", "Point A GlobalZ")   #rigid offset point on KH


rat = updateBraceConnectivityV3.shiftWPs(modelName, frameList, b, c, d, e, f, g, x, y, z)