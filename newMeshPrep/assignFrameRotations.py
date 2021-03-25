# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 09:51:00 2021

@author: ACP
"""




import attach
sapBox = attach.sapApplication()


filePath = r"J:\ENG\1092 LMNA LA\Facade & FRP Analysis Work\ACP\Temp Models\2021_03_19_C1_SE DXF Export\Local Axesv2.xlsx"

list1 = attach.get_list_excel(filePath, "acpWorking", 'Line1')

list1rot = attach.get_list_excel(filePath, "acpWorking", 'Line1_rot')

list2 = attach.get_list_excel(filePath, "acpWorking", 'Line2')

list2rot = attach.get_list_excel(filePath, "acpWorking", 'Line2_rot')

for i in range(len(list1)):
    ret = sapBox.SapModel.FrameObj.SetLocalAxes(list1[i], list1rot[i])
    
for i in range(len(list2)):
    ret = sapBox.SapModel.FrameObj.SetLocalAxes(list2[i], list2rot[i])