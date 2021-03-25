#This script for use with standardized excel spreadsheet "pythonMappingInputV2.xlsx"
import attach
from tqdm import tqdm
sapBox = attach.sapApplication()

"""Please input filepath of pythong input spreadsheet:"""
filePath = r"J:\ENG\1092 LMNA LA\Facade & FRP Analysis Work\ACP\Panel Point Generatior\Seq C1 SE Redo\2021_03_16_C1SERedo_Mapping.xlsx"

"""Please input Group Name from SAP"""
grandJointGroup = "panelEdgePoints"

#Other Parameters:
jtLineNames = attach.get_list_excel(filePath, "Input", "jLine") 

print("Getting panelEdgePoints, Please Wait...")
grandGroupObjects = attach.sapGroup(sapBox, grandJointGroup).ObjectName

# Separate Horizontal and Vertical Edge Joints into Separate Lists:
ACjoints = []
print("Making A-C Joint List")
for i in tqdm(range(len(grandGroupObjects))):
    jtName = grandGroupObjects[i]
    if "-A-" in jtName:
        ACjoints.append(jtName)
    if "-C-" in jtName:
        ACjoints.append(jtName)
        

# This creates the SAP groups for the Horizontal Joint Lines for use with "panelJoints.py" and "cycleJoints.py"

for i in range(len(jtLineNames)):
    tabName = jtLineNames[i]
    HGroupList = []
    topJtRoots = []
    botJtRoots = []
    if tabName[0]=="H":
        topPans = attach.get_list_excel(filePath, tabName,"top") #("filepath", "tab", "column header")
        botPans = attach.get_list_excel(filePath, tabName,"bottom") 
        topLetters = attach.get_list_excel(filePath, tabName,"top letter")
        botLetters = attach.get_list_excel(filePath, tabName,"bot letter")
        for k in range(len(topPans)):
            topJtRoots.append(topPans[k] + "-" + topLetters[k])
        for m in range(len(botPans)):
            botJtRoots.append(botPans[m] + "-" + botLetters[m])
        
        print("Making "+tabName + " Group List")
        for j in tqdm(range(len(ACjoints))):
            jtName = ACjoints[j]
            if jtName[0:8] in topJtRoots or jtName[0:9] in topJtRoots:
                HGroupList.append(jtName)
            if jtName[0:8] in botJtRoots or jtName[0:9] in botJtRoots:
                HGroupList.append(jtName)
        print("Making " + tabName + " Group in SAP...")
        sapBox.add_joints_to_group(tabName,HGroupList)
        
