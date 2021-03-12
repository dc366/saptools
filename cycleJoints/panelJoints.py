def mapJoints(sheetName, filePath):  
    import pandas as pd
    import attach
    sapBox = attach.sapApplication()
    
    
    """Inputs: (sheetName must start with H or V)"""
  
    
    
    """initialize Lists from Excel Spreadsheet:"""
    df = pd.read_excel(filePath, sheet_name=sheetName) # can also index sheet by name or fetch all sheets
    dirtylist = df["top"].tolist()
    """List of top or left panels"""
    topPans = [x for x in dirtylist if (pd.isnull(x) == False)]
    dirtylist = df["bottom"].tolist()   
    """List of bottom or right panels"""
    bottomPans = [x for x in dirtylist if (pd.isnull(x) == False)]
    dirtylist = df["first"].tolist()  
    """Name of first top or left point"""
    first = [x for x in dirtylist if (pd.isnull(x) == False)]
    dirtylist = df["side"].tolist()
    """List of Side conditions(which side is in front?)"""
    sideList = [x for x in dirtylist if (pd.isnull(x) == False)]
    dirtylist = df["dir"].tolist()
    """List of enforced frp mesh local 3 direction(out ofplante)"""
    dirList = [x for x in dirtylist if (pd.isnull(x) == False)]
    
    
    """Get Group Objects from SAP"""
    jtGroup = attach.sapGroup(sapBox,sheetName)
    jtList = jtGroup.ObjectName
    
    
    
    """ Split Joint List into Top and Bottom"""
    topJoints=[]
    bottomJoints=[]
    
    for i in range(len(jtList)):
        jtName=jtList[i]
        panName=jtName[0:6]
        panNameLong=jtName[0:7]
        if panName in topPans:
            topJoints.append(jtName)
        elif panNameLong in topPans:
            topJoints.append(jtName)
        elif panName in bottomPans:
            bottomJoints.append(jtName)
        elif panNameLong in bottomPans:
            bottomJoints.append(jtName)
        else:
            print(jtName + "does not match excel sheet")
            
            
    """Create x y z coordinate arrays for top/left side"""
    xValTop=[]
    yValTop=[]
    zValTop=[]
    for i in range(len(topJoints)):
        coord=attach.sapJoint(sapBox, topJoints[i])
        xValTop.append(coord.x)
        yValTop.append(coord.y)
        zValTop.append(coord.z)
        
    
    """Sort List of Top/Right Joints:"""
    
    topJointsSorted=[0]
    index = topJoints.index(first[0])
    ex=xValTop[index]
    why=yValTop[index]
    zee=zValTop[index]
    lastJt=first[0]
    topJointsSorted[0]=lastJt
    
    for i in range(len(topJoints)-1):
        bestDiff=10000
        bestIndex = 0
        for i in range(len(topJoints)):
    
            if topJoints[i] not in topJointsSorted:
                currJt=topJoints[i]
                index=topJoints.index(currJt)
                xDiff= xValTop[index]-ex
                yDiff= yValTop[index]-why
                zDiff=zValTop[index]-zee
                diff = (xDiff**2+yDiff**2+zDiff**2)**0.5
                if diff < bestDiff:
                    bestDiff=diff
                    bestIndex=index
        lastJt=topJoints[bestIndex]
        topJointsSorted.append(lastJt)
        ex=xValTop[bestIndex]
        why=yValTop[bestIndex]
        zee=zValTop[bestIndex]
            
    
    """Create x y z coordinate arrays for bottom/right side"""
    xValBottom=[]
    yValBottom=[]
    zValBottom=[]
    for i in range(len(bottomJoints)):
        coord=attach.sapJoint(sapBox, bottomJoints[i])
        xValBottom.append(coord.x)
        yValBottom.append(coord.y)
        zValBottom.append(coord.z)
        
    """Find final primary and secondary point list"""
        
    topJointsFinal=[]
    bottomJointsFinal=[]
    lastBestBottom=""
    k=0
    skips=0
    
    for i in range(len(topJointsSorted)):
        topX = xValTop[topJoints.index(topJointsSorted[i])]
        topY = yValTop[topJoints.index(topJointsSorted[i])]
        topZ = zValTop[topJoints.index(topJointsSorted[i])]
        bestDiff=10000
        bestIndex=0
        lastBestDiff=0
        for j in range(len(bottomJoints)):
            xDiff=topX-xValBottom[j]
            yDiff=topY-yValBottom[j]
            zDiff=topZ-zValBottom[j]
            diff = (xDiff**2+yDiff**2+zDiff**2)**0.5
            if diff < bestDiff:
                bestDiff=diff
                bestIndex=j
        bestMatch=bottomJoints[bestIndex]
        """if Matched Point Repeated"""
        if bestMatch == lastBestBottom:   
            if bestDiff < lastBestDiff:
                topJointsFinal[k-1]=topJointsSorted[i]
                bottomJointsFinal[k-1] = bestMatch
                lastBestBottom = bestMatch
                lastBestDiff = bestDiff
            elif bestDiff >= lastBestDiff:
                skips=skips+1
            else:
                print("error in density mismatch")
        else:
            topJointsFinal.append(0)
            topJointsFinal[k] = topJointsSorted[i]
            bottomJointsFinal.append(0)
            bottomJointsFinal[k]=bestMatch
            k=k+1
            lastBestBottom = bestMatch
            lastBestDiff = bestDiff
            
    """Parallel Point Generation"""
    listLength = len(topJointsFinal)
    thirdPointsFinal=[0]*listLength
    
    
    if sheetName[0]=="H":
        for i in range(listLength-1):
            thirdPointsFinal[i] = topJointsFinal[i+1]
        thirdPointsFinal[listLength-1] = topJointsFinal[listLength-2]
        typeFinal=["Horiz"]*listLength
        
    elif sheetName[0] == "V":
        for i in range(listLength-1):
            thirdPointsFinal[i+1] = topJointsFinal[i]
        thirdPointsFinal[0] = topJointsFinal[1]
        typeFinal=["Vert"]*listLength
        
    
    """side and dir list generations"""
        
    sideFinal=[0]*listLength
    dirFinal=[0]*listLength
          
    for i in range(listLength):
        panName=topJointsFinal[i][0:6]
        panNameLong=topJointsFinal[i][0:7]
        
     
        if panName in topPans:
            index = topPans.index(panName)
            sideFinal[i]=sideList[index]
            dirFinal[i] = dirList[index]
        elif panNameLong in topPans:
            index = topPans.index(panNameLong)
            sideFinal[i]=sideList[index]
            dirFinal[i]= dirList[index]
            
    
    return  [topJointsFinal, bottomJointsFinal, thirdPointsFinal, sideFinal, typeFinal, dirFinal]

    