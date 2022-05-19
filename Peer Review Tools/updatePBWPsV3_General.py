# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 14:34:45 2022

@author: acp
"""

import updateBraceConnectivityV3
import attach
# import prLibs



# allMems = prLibs.memList()
# panels = prLibs.panelLib()
# memberList = []

# for member in allMems:
#     panel = panels[member]
#     if panel == "C07-17":
#         memberList.append(member)



#IMPORTANT: Remove Blanks from Data First

filePath = r"C:\Users\acp\Desktop\Facad Peer Review\Latest PB WP Data\LMNA_SEQ-C1_Southwest_PB_Update_v2.xlsx"
modelName = "C64-11"
tabName = "C64-11"

frameList = attach.get_list_excel(filePath, tabName, "SAP Name")

b = attach.get_list_excel(filePath, tabName, "Point C GlobalX")   #PB i joint
c = attach.get_list_excel(filePath, tabName, "Point C GlobalY")   #PB i joint
d = attach.get_list_excel(filePath, tabName, "Point C GlobalZ")   #PB i joint
e = attach.get_list_excel(filePath, tabName, "Point B GlobalX")   #PB j joint
f = attach.get_list_excel(filePath, tabName, "Point B GlobalY")   #PB j joint
g = attach.get_list_excel(filePath, tabName, "Point B GlobalZ")   #PB j joint
x = attach.get_list_excel(filePath, tabName, "Point A GlobalX")   #rigid offset point on KH from DJC
y = attach.get_list_excel(filePath, tabName, "Point A GlobalY")   #rigid offset point on KH from DJC
z = attach.get_list_excel(filePath, tabName, "Point A GlobalZ")   #rigid offset point on KH from DJC













rat = updateBraceConnectivityV3.shiftWPs(modelName, frameList, b, c, d, e, f, g, x, y, z)