# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 09:42:04 2021
@author: ACP
"""
import attach
sapBox = attach.sapApplication()
import numpy as np
from tqdm import tqdm
groupName= "panelAreas"
areaList = attach.sapGroup(sapBox,groupName).ObjectName
origDistList=[]

done = input('set Model units to inches, press enter when done')
print("Please choose a reference point, try a lower left or right corner of the panel mesh model")
xRef = float(input('type reference x coord in inches'))
yRef = float(input('type reference y coord in inches'))
zRef = float(input('type reference z coord in inches'))


print("sorting areas:")
for area in tqdm(areaList):
    (numberPoints, Points, ret) = sapBox.SapModel.AreaObj.GetPoints(area)
    firstPoint = Points[0]
    x1 = attach.sapJoint(sapBox, firstPoint).x - xRef
    y1 = attach.sapJoint(sapBox, firstPoint).y - yRef
    z1 = attach.sapJoint(sapBox, firstPoint).z - zRef
    origDist = (x1**2 + y1**2 + z1**2)**0.5
    origDistList.append(origDist)
     
#Sort Lists in order of ascending distance from origin - the point is to have them next to each other in order
zipped_lists = zip(origDistList, areaList)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
origDistList, areaList = [ list(tuple) for tuple in tuples] 

flipArea =[]
axis3prev =[ 0, 0 , 0 ]
####################Goes through
print("calculating flip grouping:")
for i in tqdm(range(len(areaList))):
    (numberPoints, Points, ret) = sapBox.SapModel.AreaObj.GetPoints(areaList[i])
    x1 = attach.sapJoint(sapBox, Points[0]).x
    y1 = attach.sapJoint(sapBox, Points[0]).y
    z1 = attach.sapJoint(sapBox, Points[0]).z
    x2 = attach.sapJoint(sapBox, Points[1]).x
    y2 = attach.sapJoint(sapBox, Points[1]).y
    z2 = attach.sapJoint(sapBox, Points[1]).z
    x3 = attach.sapJoint(sapBox, Points[2]).x
    y3 = attach.sapJoint(sapBox, Points[2]).y
    z3 = attach.sapJoint(sapBox, Points[2]).z
    v23 = np.array( [x3-x2, y3-y2, z3-z2] )    
    v21 = np.array( [x1-x2, y1-y2, z1-z2] )  
    axis3 = np.cross(v23, v21)    
    if i == 0:
        flip = input("first area is " + areaList[i] + ", do you want to flip? type yes or no :")
        if flip == "yes":
            axis3 = np.cross(v21, v23)
            flipArea.append(areaList[i])
    elif i > 0 :    
        check = np.dot(axis3, axis3prev)
        if np.sign(check) == -1:
            axis3 = np.cross(v21, v23)
            flipArea.append(areaList[i])
    axis3prev = axis3
    
print("creating sap group 'flipArea', please wait...")        
sapBox.add_areas_to_group("flipArea",flipArea)
print("Done!")  
    