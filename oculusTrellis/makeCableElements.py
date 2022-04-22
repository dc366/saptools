# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 14:06:44 2022
@author: acp
"""
#This script is intended to be run after "makeInteriorPoints" script
import numpy as np
import attach
a = attach.sapApplication()

# Create Cables starting from Bottom Edge:
botList = list(range(1,39))  
for x in botList:
    numCablesR = 78-2*x
    numCablesL = 2*x  

    for k in range(1, numCablesR+1):
        cableName = "B-" + str(x) + "_CBLR-" + str(k)
        firstX = 10/3 * x + (k-1)*10/6
        firstY = (k-1) * 10/6
        secX = firstX + 10/6
        secY = firstY + 10/6
        pt_i = "B" + str(round( firstX / (10/3), 1 )) +"_L" + str(round(firstY / (10/3),1))
        pt_j = "B" + str(round( secX / (10/3), 1 )) +"_L" + str(round(secY / (10/3),1))
        if k == 1:
            pt_i = "B-"+str(x)       
        if k ==numCablesR:
            pt_j = "R-"+str(39-x)
        ret = a.SapModel.CableObj.AddByPoint(pt_i, pt_j, cableName, "CAB1", cableName)
    for m in range(1, numCablesL+1):
        cableName = "B-" + str(x) + "_CBLL-" + str(m)
        firstX = 10/3 * x - (m-1)*10/6
        firstY = (m-1) * 10/6
        secX = firstX - 10/6
        secY = firstY + 10/6
        pt_i = "B" + str(round( firstX / (10/3), 1 )) +"_L" + str(round(firstY / (10/3),1))
        pt_j = "B" + str(round( secX / (10/3), 1 )) +"_L" + str(round(secY / (10/3),1))
        if m == 1:
            pt_i = "B-"+str(x)       
        if m ==numCablesL:
            pt_j = "L-"+str(x)
        ret = a.SapModel.CableObj.AddByPoint(pt_i, pt_j, cableName, "CAB1", cableName)
        
topList = list(range(1,39))  
for x in topList:
    numCablesR = 78-2*x
    numCablesL = 2*x  

    for k in range(1, numCablesR+1):
        cableName = "T-" + str(x) + "_CBLR-" + str(k)
        firstX = 10/3 * x + (k-1)*10/6
        firstY = 130 - (k-1) * 10/6
        secX = firstX + 10/6
        secY = firstY - 10/6
        pt_i = "B" + str(round( firstX / (10/3), 1 )) +"_L" + str(round(firstY / (10/3),1))
        pt_j = "B" + str(round( secX / (10/3), 1 )) +"_L" + str(round(secY / (10/3),1))
        if k == 1:
            pt_i = "T-"+str(x)       
        if k ==numCablesR:
            pt_j = "R-"+str(x)
        ret = a.SapModel.CableObj.AddByPoint(pt_i, pt_j, cableName, "CAB1", cableName)
    for m in range(1, numCablesL+1):
        cableName = "T-" + str(x) + "_CBLL-" + str(m)
        firstX = 10/3 * x - (m-1)*10/6
        firstY = 130 - (m-1) * 10/6
        secX = firstX - 10/6
        secY = firstY - 10/6
        pt_i = "B" + str(round( firstX / (10/3), 1 )) +"_L" + str(round(firstY / (10/3),1))
        pt_j = "B" + str(round( secX / (10/3), 1 )) +"_L" + str(round(secY / (10/3),1))
        if m == 1:
            pt_i = "T-"+str(x)       
        if m ==numCablesL:
            pt_j = "L-"+str(39-x)
        ret = a.SapModel.CableObj.AddByPoint(pt_i, pt_j, cableName, "CAB1", cableName)
        
        
        
#Cable Diagonals:
    
numCables = 78
for k in range(1, numCables+1):
    cableName = "BL_CBL-"+str(k)
    firstX = firstY = (k-1) * 10/6
    secX = secY = firstX + 10/6
    pt_i = "B" + str(round( firstX / (10/3), 1 )) +"_L" + str(round(firstY / (10/3),1))
    pt_j = "B" + str(round( secX / (10/3), 1 )) +"_L" + str(round(secY / (10/3),1))
    if k == 1:
        pt_i = "BL"      
    if k ==numCables:
        pt_j = "TR"
    ret = a.SapModel.CableObj.AddByPoint(pt_i, pt_j, cableName, "CAB1", cableName)
    
for k in range(1, numCables+1):
    cableName = "TL_CBL-"+str(k)
    firstX = (k-1) * 10/6
    firstY = 130 - (k-1) * 10/6 
    secX = firstX + 10/6
    secY = firstY - 10/6
    pt_i = "B" + str(round( firstX / (10/3), 1 )) +"_L" + str(round(firstY / (10/3),1))
    pt_j = "B" + str(round( secX / (10/3), 1 )) +"_L" + str(round(secY / (10/3),1))
    if k == 1:
        pt_i = "TL"      
    if k ==numCables:
        pt_j = "BR"
    ret = a.SapModel.CableObj.AddByPoint(pt_i, pt_j, cableName, "CAB1", cableName)   
    
    
    
    
    
    
    
    
    
    
    
    

