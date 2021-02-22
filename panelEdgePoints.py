#This script for create SAP group "panelEdgePoints"
import attach

"""Please input group Name:"""
grandJointGroup = "typeHERE"

#Other Parameters:
grandGroupObjects = attach.sapGroup(grandJointGroup).ObjectName

# Generates List of panel edge points:
    
panelEdgePoints = []
for i in range(len(grandGroupObjects)):
    jtName = grandGroupObjects[i]
    if jtName[8]=="A" or jtName[9]=="A":
        panelEdgePoints.append(jtName)
    if jtName[8]=="B" or jtName[9]=="B":
        panelEdgePoints.append(jtName)
    if jtName[8]=="C" or jtName[9]=="C":
        panelEdgePoints.append(jtName)
    if jtName[8]=="D" or jtName[9]=="D":
        panelEdgePoints.append(jtName)   

# Creates group in SAP:
    
attach.add_joints_to_group("panelEdgePoints", panelEdgePoints)

