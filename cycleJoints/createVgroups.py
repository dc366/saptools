#This script for use with standardized excel spreadsheet "pythonMappingInputV2.xlsx"
import attach
import time
sapBox = attach.sapApplication()

start_time = time.time() #track time taken to run
"""Please input filepath of pythong input spreadsheet:"""
filePath = r"J:\ENG\1092 LMNA LA\Facade & FRP Analysis Work\ACP\Panel Point Generatior\seq C1 SW\2021_03_01_C1SW_Mapping.xlsx"

"""Please input Group Name from SAP"""
grandJointGroup = "panelEdgePoints"


#Other Parameters:
jtLineNames = attach.get_list_excel(filePath, "Input", "jLine") 
grandGroupObjects = attach.sapGroup(sapBox, grandJointGroup).ObjectName

# Separate Vertical Edge Joints into Separate Lists APPROX 63 SECONDS ON ENG 31D:
BDjoints = []
ACjoints = []
for i in range(len(grandGroupObjects)):
    jtName = grandGroupObjects[i]
    if jtName[7]=="B" or jtName[8]=="B":
        BDjoints.append(jtName)
    if jtName[7]=="D" or jtName[8]=="D":
        BDjoints.append(jtName)
    if jtName[7]=="A" or jtName[8]=="A":
        ACjoints.append(jtName)
    if jtName[7]=="C" or jtName[8]=="C":
        ACjoints.append(jtName)
        
elapsed_time = time.time() - start_time
print("time taken for setup: ")
print(elapsed_time)
start_time2 = time.time() #track time taken to run

# This creates the SAP groups for the Vertical Joint Lines for use with "panelJoints.py" and "cycleJoints.py"
# APPROX 30 SECONDS PER JOINT LINE ON ENG 31D
for i in range(len(jtLineNames)):
    tabName = jtLineNames[i]
    VGroupList = []
    topJtRoots = []
    botJtRoots = []
    if tabName[0]=="V":
        topPans = attach.get_list_excel(filePath, tabName,"top") #("filepath", "tab", "column header")
        botPans = attach.get_list_excel(filePath, tabName,"bottom") 
        topLetters = attach.get_list_excel(filePath, tabName,"top letter")
        botLetters = attach.get_list_excel(filePath, tabName,"bot letter")
        
        
        for k in range(len(topPans)):  #Cycle through list of top/left panels
            topJtRoots.append(topPans[k] + "-" + topLetters[k])  #creating list of point root names e.f. "C13-02-B"

            
            ##########  Adds Corner (A and C) Points  Please note, it assumes they are A and C Points  ###############

            cPt1Root = topPans[k]+"-A"
            cPt2Root = topPans[k]+"-C"

            vPt1 = topPans[k]+"-" + topLetters[k]
            vPt2 = vPt1
       
            vPts = [vPt1, vPt2]
            
            cPtRoots = [cPt1Root, cPt2Root]
            minDist= [99999999999999999999999999]*2
            cJoints= [0]*2
           
            
           
            for q in range(len(minDist)):
                    vPtRef = vPts[q] + str(-4)
                    refX = attach.sapJoint(sapBox, vPtRef).x
                    refY = attach.sapJoint(sapBox, vPtRef).y
                    refZ = attach.sapJoint(sapBox, vPtRef).z
                    
                    cPtRoot= cPtRoots[q] 
                    
                    for p  in range(len(ACjoints)):
                        cJoint = ACjoints[p]
                        if cPtRoot in cJoint: 

                            cX=attach.sapJoint(sapBox, cJoint).x
                            cY=attach.sapJoint(sapBox, cJoint).y
                            cZ=attach.sapJoint(sapBox, cJoint).z
                            xDiff = refX-cX
                            yDiff = refY-cY
                            zDiff = refZ-cZ
                            diff =(xDiff**2 + yDiff**2 + zDiff**2)**0.5
                            if diff < minDist[q]:
                                cJoints[q] =cJoint
                                minDist[q] = diff            
            sapBox.add_joints_to_group(tabName, cJoints)                
           

            
            ###########################################################
        
        ##############  Adds Side (B and D) Points ###########################
        for j in range(len(BDjoints)):
            jtName = BDjoints[j]
            if jtName[0:8] in topJtRoots or jtName[0:9] in topJtRoots:
                VGroupList.append(jtName)
        sapBox.add_joints_to_group(tabName,VGroupList)
        ######################################################################
        
        
        
        
        
        
        for k in range(len(botPans)):  #Cycle through list of top/left panels
  #creating list of point root names e.f. "C13-02-B"
            botJtRoots.append(botPans[k] + "-" + botLetters[k])
            
            ##########  Adds Corner (A and C) Points  Please note, it assumes they are A and C Points  ###############


            cPt3Root = botPans[k]+"-A"
            cPt4Root = botPans[k]+"-C"

            vPt3 = botPans[k]+"-" + botLetters[k]
            vPt4 = vPt3           
            vPts = [vPt3, vPt4]
            
            cPtRoots = [cPt3Root, cPt4Root]
            minDist= [99999999999999999999999999]*2
            cJoints= [0]*2
           
            
           
            for q in range(len(minDist)):
                    vPtRef = vPts[q] + str(-4)
                    refX = attach.sapJoint(sapBox, vPtRef).x
                    refY = attach.sapJoint(sapBox, vPtRef).y
                    refZ = attach.sapJoint(sapBox, vPtRef).z
                    
                    cPtRoot= cPtRoots[q] 
                    
                    for p  in range(len(ACjoints)):
                        cJoint = ACjoints[p]
                        if cPtRoot in cJoint: 

                            cX=attach.sapJoint(sapBox, cJoint).x
                            cY=attach.sapJoint(sapBox, cJoint).y
                            cZ=attach.sapJoint(sapBox, cJoint).z
                            xDiff = refX-cX
                            yDiff = refY-cY
                            zDiff = refZ-cZ
                            diff =(xDiff**2 + yDiff**2 + zDiff**2)**0.5
                            if diff < minDist[q]:
                                cJoints[q] =cJoint
                                minDist[q] = diff            
            sapBox.add_joints_to_group(tabName, cJoints)                
           

            
            ###########################################################
        
        ##############  Adds Side (B and D) Points ###########################
        for j in range(len(BDjoints)):
            jtName = BDjoints[j]

            if jtName[0:8] in botJtRoots or jtName[0:9] in botJtRoots:
                VGroupList.append(jtName)
        sapBox.add_joints_to_group(tabName,VGroupList)
        ######################################################################  
        
  
    
  
    
elapsed_time2 = time.time() - start_time2
print("time taken per Joint Line: ")
print(elapsed_time2)  #track time taken to run

                            
                        








