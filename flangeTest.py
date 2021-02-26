
import attach



#Other Parameters:
grandAreaObjects = []
allIDs = attach.sapGroup("All").TypeID
allObjects = attach.sapGroup("All").ObjectName

for i in range(len(allIDs)):
    if allIDs[i]==5:
        grandAreaObjects.append(allObjects[i])
        


flangeAreas=[]
for i in range(len(grandAreaObjects)):
    areaName = grandAreaObjects[i]
    if ("SM" in areaName or "TM" in areaName):
        flangeAreas.append(areaName)

panelAreas=[]
for i in range(len(grandAreaObjects)):
    areaName = grandAreaObjects[i]
    if ("-M" in areaName):
        panelAreas.append(areaName)

attach.add_areas_to_group("flangeAreas",flangeAreas)
attach.add_areas_to_group("panelAreas",panelAreas)