
#For some reason, you have to run this script a few times for it to group all the areas correctly
import attach

#Before running this script, create a group called "allAreas" and assign all area elements to it
grandAreaGroup = "allAreas"

#Other Parameters:
grandAreaObjects = attach.sapGroup(grandAreaGroup).ObjectName


flangeAreas=[]
for i in range(len(grandAreaObjects)):
    areaName = grandAreaObjects[i]
    if ("SM" in areaName or "TM" in areaName):  #"SM" and "TM" are in the naming of the flange area elements
        flangeAreas.append(areaName)

panelAreas=[]
for i in range(len(grandAreaObjects)):
    areaName = grandAreaObjects[i]
    if ("-M" in areaName):   #"-M" is in the naming of the flange area elements
        panelAreas.append(areaName)

attach.add_areas_to_group("flangeAreas",flangeAreas)
attach.add_areas_to_group("panelAreas",panelAreas)