
import attach
a = attach.sapApplication()
from tqdm import tqdm


#This script is for creating groups called panelAreas and flangeAreas
#It also creates allFrames Group


print("Listing all Objects Names and Type Please wait..")
frameGroup = attach.sapGroup(a, "GROUPY").ObjectName



#flangeAreas=[]
#panelAreas=[]
#otherAreas = []
princeHats = []

print("Finding Prince Hats...")
for i in tqdm(range(len(frameGroup))):
    frameName = frameGroup[i]
    if ("_PH_" in frameName):  #"SM" and "TM" are in the naming of the flange area elements
        princeHats.append(frameName)
    #elif ("-M-" in areaName):
     #   panelAreas.append(areaName)
    #else:
     #   otherAreas.append(areaName)


print("Creating SAP groups, please wait...")
#sapBox.add_areas_to_group("flangeAreas",flangeAreas)
#sapBox.add_areas_to_group("panelAreas",panelAreas)
#sapBox.add_areas_to_group("unknownAreas",otherAreas)
a.add_frames_to_group("LERA_PrinceHats", princeHats)
print("Done")