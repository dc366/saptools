# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 10:56:41 2022

@author: acp
"""

#This script creates a point at each cable mesh intersection
import numpy as np
import attach
a = attach.sapApplication()

xgrid = 0
ygrid = 0

coordX = np.linspace(10/3/2, 39*10/3-10/3/2, 77)   # x coordinates for loop
coordYeven = np.linspace(10/3, 38*10/3, 38)          # y coordinates for loop even counter
coordYodd = np.linspace(10/3/2, 39*10/3 - 10/3/2, 39)   # y coordinates for loop odd counter
counter = 0

for x in coordX:
    counter = counter +1
    xNum = round(x/(10/3),1)
    
    if counter % 2 ==0:
    
        for y in coordYeven:
            yNum = round(y/(10/3),1)
            ptName = "B"+str(xNum)+"_L"+ str(yNum)
            ret = a.SapModel.PointObj.AddCartesian(x, y, 0, ptName, ptName)
            
    elif counter % 2 == 1:
        for y in coordYodd:
            yNum = round(y/(10/3),1)
            ptName = "B"+str(xNum)+"_L"+ str(yNum)
            ret = a.SapModel.PointObj.AddCartesian(x, y, 0, ptName, ptName)
            
            
            
# This next part creates the cable elements: