#This script for create SAP group "panelEdgePoints"
import attach
sapBox = attach.sapApplication()
from tqdm import tqdm

"""Please input group Name:"""
grandJointGroup = "allPanelJoints"

#Other Parameters:
print("Getting allPanelJoints, Please wait...")
grandGroupObjects = attach.sapGroup(sapBox, grandJointGroup).ObjectName

# Generates List of panel edge points:
    
panelEdgePoints = []
for i in tqdm(range(len(grandGroupObjects))):
    jtName = grandGroupObjects[i]
    if "-A-" in jtName:
        panelEdgePoints.append(jtName)
    if "-B-" in jtName:
        panelEdgePoints.append(jtName)
    if "-C-" in jtName:
        panelEdgePoints.append(jtName)
    if "-D-" in jtName:
        panelEdgePoints.append(jtName)   
    if "-E-" in jtName:
        panelEdgePoints.append(jtName)
    if "-V-" in jtName:
        panelEdgePoints.append(jtName)

# Creates group in SAP:
    
sapBox.add_joints_to_group("panelEdgePoints", panelEdgePoints)

