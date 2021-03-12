
import attach
sapBox = attach.sapApplication()
from tqdm import tqdm


#This script is for creating groups called panelAreas and flangeAreas
#It also creates allFrames Group


print("Listing all Objects Names and Type Please wait..")
allObjects = attach.sapGroup(sapBox, "All").ObjectName
allTypes =  attach.sapGroup(sapBox, "All").TypeID


grandAreaObjects = []
frameObjects = []
print("creating area and frame lists, please wait...")
for i in tqdm(range(len(allObjects))):
    if allTypes[i] == 5:
        grandAreaObjects.append(allObjects[i])
    elif allTypes[i] == 2:
        frameObjects.append(allObjects[i])
    else:
        continue

flangeAreas=[]
panelAreas=[]
otherAreas = []
print("Separating Flange and Panel Area Lists...")
for i in tqdm(range(len(grandAreaObjects))):
    areaName = grandAreaObjects[i]
    if ("SM" in areaName or "TM" in areaName):  #"SM" and "TM" are in the naming of the flange area elements
        flangeAreas.append(areaName)
    elif ("-M-" in areaName):
        panelAreas.append(areaName)
    else:
        otherAreas.append(areaName)


print("Creating SAP groups, please wait...")
sapBox.add_areas_to_group("flangeAreas",flangeAreas)
sapBox.add_areas_to_group("panelAreas",panelAreas)
sapBox.add_areas_to_group("unknownAreas",otherAreas)
sapBox.add_frames_to_group("allFrames", frameObjects)
print("Done")