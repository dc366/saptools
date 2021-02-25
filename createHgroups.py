#This script for use with standardized excel spreadsheet "pythonMappingInputV2.xlsx"
import attach
import time

start_time = time.time() #track time taken to run
"""Please input filepath of pythong input spreadsheet:"""
filePath = r"C:\Users\ACP\Desktop\Python Stuff\B_East_Test_H1.xlsx"

"""Please input Group Name from SAP"""
grandJointGroup = "panelEdgePoints"

#Other Parameters:
jtLineNames = attach.get_list_excel(filePath, "Input", "jLine") 
grandGroupObjects = attach.sapGroup(grandJointGroup).ObjectName

# Separate Horizontal and Vertical Edge Joints into Separate Lists APPROX 63 SECONDS ON ENG 31D:
ACjoints = []
for i in range(len(grandGroupObjects)):
    jtName = grandGroupObjects[i]
    if jtName[7]=="A" or jtName[8]=="A":
        ACjoints.append(jtName)
    if jtName[7]=="C" or jtName[8]=="C":
        ACjoints.append(jtName)
        
elapsed_time = time.time() - start_time
print("time taken for setup: ")
print(elapsed_time)
start_time2 = time.time() #track time taken to run

# This creates the SAP groups for the Horizontal Joint Lines for use with "panelJoints.py" and "cycleJoints.py"
# APPROX 3-5 SECONDS PER JOINT LINE ON ENG 31D
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
            botJtRoots.append(botPans[k] + "-" + botLetters[k])
        for j in range(len(ACjoints)):
            jtName = ACjoints[j]
            if jtName[0:8] in topJtRoots or jtName[0:9] in topJtRoots:
                HGroupList.append(jtName)
            if jtName[0:8] in botJtRoots or jtName[0:9] in botJtRoots:
                HGroupList.append(jtName)
        attach.add_joints_to_group(tabName,HGroupList)
        
elapsed_time2 = time.time() - start_time2
print("time taken per Joint Line: ")
print(elapsed_time2)  #track time taken to run