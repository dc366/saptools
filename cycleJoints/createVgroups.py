#This script for use with standardized excel spreadsheet "pythonMappingInputV2.xlsx"
import attach
sapBox = attach.sapApplication()

"""Please input filepath of pythong input spreadsheet:"""
filePath = r"J:\ENG\1092 LMNA LA\Facade & FRP Analysis Work\ACP\Panel Point Generatior\Seq A West\2021_09_23_A_West_Mapping.xlsx"

"""Please input Group Name from SAP"""
grandJointGroup = "panelEdgePoints"


#Other Parameters:
jtLineNames = attach.get_list_excel(filePath, "Input", "jLine") 
print("Getting Joint Names from SAP, Please Wait...")
grandGroupObjects = attach.sapGroup(sapBox, grandJointGroup).ObjectName

# Separate Vertical Edge Joints into Separate Lists APPROX 63 SECONDS ON ENG 31D:
BDjoints = []
ACjoints = []

for i in range(len(grandGroupObjects)):
    jtName = grandGroupObjects[i]
    if ("-B-" in jtName) or ("-D-" in jtName) or ("-E-" in jtName):
        BDjoints.append(jtName)
    if ("-A-" in jtName) or ("-C-" in jtName):
        ACjoints.append(jtName)

# This creates the SAP groups for the Vertical Joint Lines for use with "panelJoints.py" and "cycleJoints.py"
# APPROX 30 SECONDS PER JOINT LINE ON ENG 31D
for i in range(len(jtLineNames)):
    tabName = jtLineNames[i]
    VGroupListLeft = []
    VGroupListRight = []
    print("For Joint Line "+str(tabName)+":")

    if tabName[0]=="V":
        topPans = attach.get_list_excel(filePath, tabName,"top") #("filepath", "tab", "column header")
        botPans = attach.get_list_excel(filePath, tabName,"bottom") 
        topLetters = attach.get_list_excel(filePath, tabName,"top letter")
        botLetters = attach.get_list_excel(filePath, tabName,"bot letter")
        
        counter = [0]*len(topPans)
        print("Finding Left Side Points...")
        for k in range(len(topPans)):  #Cycle through list of top/left panels

            currentRoot = topPans[k] + "-" + topLetters[k]

        ##############  Adds Side (B and D) Points ###########################
            
            for j in range(len(BDjoints)):
                jtName = BDjoints[j]
                if currentRoot in jtName:
                    VGroupListLeft.append(jtName)
                    counter[k] = counter[k] + 1
            sapBox.add_joints_to_group(tabName,VGroupListLeft)
        ######################################################################            
            
        print("Finding Left Side Corner Points...")    
        for k in range(len(topPans)):    
            ##########  Adds Corner (A and C) Points  Please note, it assumes they are A and C Points  ###############

            cPt1Root = topPans[k]+"-A"
            cPt2Root = topPans[k]+"-C"

            vPt1 = topPans[k]+"-" + topLetters[k] + "-1"
            vPt2 = topPans[k]+"-" + topLetters[k] + "-" + str(counter[k])
       
            vPts = [vPt1, vPt2]
            
            cPtRoots = [cPt1Root, cPt2Root]
            minDist= [99999999999999999999999999]*2
            cJoints= [0]*2
           
            
           
            for q in range(len(minDist)):
                    vPtRef = vPts[q]
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
        

        
        
        
        
        
        counter = [0]* len(botPans)
        print("Finding Right Side Points...")
        for k in range(len(botPans)):  #Cycle through list of top/left panels
  #creating list of point root names e.f. "C13-02-B"

            currentRoot = botPans[k] + "-" + botLetters[k]
            
            ##########  Adds Corner (A and C) Points  Please note, it assumes they are A and C Points  ###############
            for j in range(len(BDjoints)):
                jtName = BDjoints[j]

                if currentRoot in jtName:
                    VGroupListRight.append(jtName)
                    counter[k] = counter[k] + 1
            sapBox.add_joints_to_group(tabName,VGroupListRight)
        print("Finding Right Side Corner Points...")  
        for k in range(len(botPans)):
            cPt3Root = botPans[k]+"-A"
            cPt4Root = botPans[k]+"-C"

            vPt3 = botPans[k]+"-" + botLetters[k] +"-1"
            vPt4 = botPans[k]+"-" + botLetters[k] + "-" + str(counter[k])         
            vPts = [vPt3, vPt4]
            
            cPtRoots = [cPt3Root, cPt4Root]
            minDist= [99999999999999999999999999]*2
            cJoints= [0]*2
           
            
           
            for q in range(len(minDist)):
                    vPtRef = vPts[q]
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

        ######################################################################  
        
  
    


                            
                        








