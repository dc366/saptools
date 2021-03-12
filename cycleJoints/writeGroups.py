# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 19:03:07 2021

@author: ACP
"""
import attach
sapBox = attach.sapApplication()
filePath = r"J:\ENG\1092 LMNA LA\Facade & FRP Analysis Work\ACP\Panel Point Generatior\seq C1 SW\panelEdgePoints.xlsx"
tabName = 'panelEdgePoints'
headerName = 'Col1'

jtNames = attach.get_list_excel(filePath, tabName, headerName)

#sapBox.add_joints_to_group(tabName, jtNames)
      
for i in range(len(jtNames)):  
    sapBox.SapModel.PointObj.SetGroupAssign(jtNames[i],tabName)
            