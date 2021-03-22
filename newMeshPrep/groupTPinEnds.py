# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 16:28:44 2021

@author: ACP
"""

import attach
sapBox = attach.sapApplication()

sapBox.clear_selection()
ret = sapBox.SapModel.SelectObj.PropertyFrame("CONN_rod_1in")
ret = sapBox.SapModel.SelectObj.PropertyFrame("CONN_rod")

selected, _ = sapBox.get_list_sap("frame")

jEnds=[]

#creates list for i ends and j ends:
for i in range(len(selected)):   
    jEndName = attach.sapFrame(sapBox,selected[i]).jEnd
    jEnds.append(jEndName)
    

sapBox.add_joints_to_group("LERA - allTPinEnds",jEnds)
sapBox.clear_selection()