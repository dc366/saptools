# -*- coding: utf-8 -*-
"""
Created on Thu May  5 12:52:40 2022

@author: acp
"""
#This scripts defines functions that return libraries or lists based with info from the catalogued tertiary information contained in the excel spreadsheet, 
#saved in filePath variable below
#The libaries and lists can then be used to implement changes to SAP models, for example in updateReleases.py

import pandas as pd
import tqdm as tqdm


test = "correct"
filePath = r"C:\Users\acp\Desktop\Facad Peer Review\2022_04_26 C1 SE Study\2022_05_13 C1 Audit Study_Analysis Releases_selectPanels.xlsx"
sheetname = "Member ID Table"

#list_1 = attach.get_list_excel(filePath,sheetname)[1] [3:]


memIndexList =  [1, 2, 3,   4,  5,  6, 7,  8, 14, 15, 16, 17, 18, 19, 20, 21, 12, 13, 25, 26] # list of excel columns that have the catlogued member names 
typeIndexList = [9, 9, 10, 10, 11, 11, 9, 10, 22, 22, 23, 23, 24, 24, 22, 23,  9, 10, 22, 23] # list of excel columns that have the catlogued member names 
innerCols = [2, 4, 6, 15, 17, 19]
outerCols = [1, 3, 5, 14, 16, 18]
phCols = [7, 8, 20, 21]

def panelLib():  #returns library of panel names 
    
    panelLib ={}
    rawPanList = pd.read_excel(filePath, sheetname)[0][3:].tolist()
    
    for i in memIndexList:
        tempList = pd.read_excel(filePath, sheetname)[i][3:].tolist()
        
        for j in range(len(tempList)):
            mem = tempList[j]
            
            if pd.isnull(mem) is False:
                panelLib[str(mem)] = rawPanList[j]
    return panelLib

def memList(): # returns list of member labels that have been catalogued
    memList = []
    for i in memIndexList:
        tempList = pd.read_excel(filePath, sheetname)[i][3:].tolist()
        for j in range(len(tempList)):
            mem = tempList[j]
            
            if pd.isnull(mem) is False:
                memList.append(mem)
    return memList

def typeLib(): # returns library that catalogues the type and similar type of detail in a tuple
    typeList = pd.read_excel(filePath, "Assumption Types Similar")["Type"].tolist()
    simList = pd.read_excel(filePath, "Assumption Types Similar")["Similar To"].tolist()
    simLib = {}
    
    typLib = {}
    
    for i in range(len(typeList)):
        simLib[typeList[i]] = simList[i]
        
    for i in range(len(memIndexList)):
        tempList = pd.read_excel(filePath, sheetname)[memIndexList[i]][3:].tolist()
        otherList = pd.read_excel(filePath, sheetname)[typeIndexList[i]][3:].tolist()
        
        for j in range(len(tempList)):
            mem = tempList[j]
            tipe = otherList[j]
            
            if pd.isnull(mem) is False:
                typLib[str(mem)] = (tipe, simLib[tipe])         
    return typLib


def locLib():
    
    locLib ={}
    
    for i in memIndexList:
        tempList = pd.read_excel(filePath, sheetname)[i][3:].tolist()
        
        for j in range(len(tempList)):
            mem = tempList[j]
            
            if pd.isnull(mem) is False:
                if i in innerCols:
                    loc = "Inner"
                elif i in outerCols:
                    loc = "Outer"
                elif i in  phCols:
                    loc = "PH"
                else:
                    print("error")
                
                locLib[str(mem)] = loc
                                          
    return locLib    


def releaseLib():
    tempList = pd.read_excel(filePath, "Assumption Types")["Index"][4:].tolist()
    releaseLib= {}
    
    
    for i in range(len(tempList)):
        name = tempList[i]
        temp = []
        for j in range(1, 28):
            subList = pd.read_excel(filePath, "Assumption Types")[j][4:].tolist()
            temp.append(subList[i])
        b = tuple(temp)
        releaseLib[name] = b
    return releaseLib
            
    



def memUpdates(memberList): #function that returns library that is a tuple of changes to the member:
    # the library contains: (property Name, iM2 release, iM3 release, iT release, i rigid offset,
    #..........................jM2 release, jM3 release, jT release, j rigid offset)
    print("making release library...")
    releases = releaseLib()
    print("making location library...")
    locs = locLib()
    
    memUpdates = {}

    print("making member update library...")
    
    for i in range(len(memberList)):
        x=memberList[i]
        print("finding updates for "+str(x))
        detType = typeLib()[x][1]
        loc = locs[x]
        
        if loc == "Outer":
            temp = releases[detType][0:9]
        elif loc == "Inner":
            temp = releases[detType][9:18]
        elif loc == "PH":
            temp = releases[detType][18:27]
        else:
            print("error")
        memUpdates[x] = temp
        
    return memUpdates
            
def returnFilePath():
    return filePath


def pbLib():  #creates library that containes tuple of prince braces for each panel that is catalogued
    rawPanList = pd.read_excel(filePath, sheetname)[0][3:].tolist()
    pbLT =  pd.read_excel(filePath, sheetname)[12][3:].tolist()
    pbLB =  pd.read_excel(filePath, sheetname)[13][3:].tolist()
    pbRT =  pd.read_excel(filePath, sheetname)[25][3:].tolist()
    pbRB =  pd.read_excel(filePath, sheetname)[26][3:].tolist()
    pbLib ={}
    
    for i in range(len(rawPanList)):
        temp = [pbLT[i], pbLB[i], pbRT[i], pbRB[i]]
        cleanedlist = [x for x in temp if (pd.isnull(x) == False)]
        pbLib[rawPanList[i]] = tuple(cleanedlist)
        
    return pbLib


def shiftLib(path, shtNm): #returns library of workpoint shifts for given path and sheet name where suches changes are found
    pbList = pd.read_excel(path, shtNm)['SAP Name'].tolist()
    b = pd.read_excel(path, shtNm)["Point C GlobalX"].tolist()   #PB i joint
    c = pd.read_excel(path, shtNm)["Point C GlobalY"].tolist()   #PB i joint
    d = pd.read_excel(path, shtNm)["Point C GlobalZ"].tolist()   #PB i joint
    e = pd.read_excel(path, shtNm)["Point B GlobalX"].tolist()   #PB j joint
    f = pd.read_excel(path, shtNm)["Point B GlobalY"].tolist()   #PB j joint
    g = pd.read_excel(path, shtNm)["Point B GlobalZ"].tolist()   #PB j joint
    x = pd.read_excel(path, shtNm)["Point A GlobalX"].tolist()   #rigid offset point on KH from DJC
    y = pd.read_excel(path, shtNm)["Point A GlobalY"].tolist()   #rigid offset point on KH from DJC
    z = pd.read_excel(path, shtNm)["Point A GlobalZ"].tolist()   #rigid offset point on KH from DJC
    
    shiftLib = {}

    for i in range(len(pbList)):
        temp = (b[i], c[i], d[i], e[i], f[i], g[i], x[i], y[i], z[i])
        shiftLib[pbList[i]] = temp        
    
    return shiftLib


def pbList(panels): #returns list of prince braces for input panel list
    pbList =[]
    for panel in panels:
        shortList = pbLib()[panel]
        for brace in shortList:
            pbList.append(brace)
    return pbList



def shiftList(panList, fPath, tabName): #returns lists of prince brace workpoint changes for the input panel list, filepath and tabName
    braceList = pbList(panList)
    iX =[]
    iY =[]
    iZ =[]
    jX =[]
    jY =[]
    jZ =[]
    cX =[]
    cY =[]
    cZ =[]
    panName =[]
    for brace in braceList:
        (iXt, iYt, iZt, jXt, jYt, jZt, cXt, cYt, cZt) = shiftLib(fPath, tabName)[brace]
        panName.append(panelLib()[brace])
        iX.append(iXt)
        iY.append(iYt)
        iZ.append(iZt)
        jX.append(jXt)
        jY.append(jYt)
        jZ.append(jZt)        
        cX.append(cXt)
        cY.append(cYt)
        cZ.append(cZt)  
    return [braceList, panName, iX, iY, iZ, jX, jY, jZ, cX, cY, cZ]













