# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 00:37:59 2021

@author: ACP
"""

import attach
sapBox = attach.sapApplication()
suction = 25/1000/144
pressure = -20/1000/144
oPanGroup = "overPanels"  #Confirm group name of overhead panels in SAP
bPanGroup = "bellyPanels"  #Confirm group name of belly panels in SAP

 



sapBox.clear_selection()
ret = sapBox.SapModel.SelectObj.PropertyArea("Layered-Shell-Coat-Scaled")
ret = sapBox.SapModel.SelectObj.PropertyArea("Layered-Shell-Coat-Scaled+PV")

SelectedObjects = 2
ret= sapBox.SapModel.AreaObj.SetLoadUniform("", "WIND(+)", pressure, 3, True, "Local", SelectedObjects)  #Confirm Load Pattern Name in SAP
ret= sapBox.SapModel.AreaObj.SetLoadUniform("", "WIND(-)", suction, 3, True, "Local", SelectedObjects)   #Confirm Load Pattern Name in SAP

sapBox.clear_selection()
ret = sapBox.SapModel.SelectObj.Group(bPanGroup) #selects objects in bPanGroup
ret= sapBox.SapModel.AreaObj.SetLoadUniform("", "WIND(+)Belly", pressure, 3, True, "Local", SelectedObjects)   #Confirm Load Pattern Name in SAP
ret= sapBox.SapModel.AreaObj.SetLoadUniform("", "WIND(-)Belly", suction, 3, True, "Local", SelectedObjects)   #Confirm Load Pattern Name in SAP

sapBox.clear_selection()
ret = sapBox.SapModel.SelectObj.Group(oPanGroup) #False selects objects in oPanGroup
ret= sapBox.SapModel.AreaObj.SetLoadUniform("", "WIND(+)OverHead", pressure, 3, True, "Local", SelectedObjects)   #Confirm Load Pattern Name in SAP
ret= sapBox.SapModel.AreaObj.SetLoadUniform("", "WIND(-)OverHead", suction, 3, True, "Local", SelectedObjects)   #Confirm Load Pattern Name in SAP

sapBox.clear_selection()