# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 20:22:18 2022

@author: acp
"""

modelName = "TestModel1"
frameList =["testFrame"]
b= [50]
c= [50]
d = [0]
e = [-6]
f = [-50]
g = [0]

import updateBraceConnectivity
answer = 0
answer = updateBraceConnectivity.shiftWPs(modelName, frameList, b, c, d, e, f, g)