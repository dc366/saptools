# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 11:38:45 2021

@author: acp
"""
from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


bin_edges = np.arange(0.5, 3.5+1, 1)
plotList = contCaseNew
ass = plt.hist(plotList, bins = bin_edges, rwidth = 0.7)
plt.xticks(np.arange(0, 3+1, 1), ["", "GRAVITY", "WIND", "SEISMIC"])
plt.title('Controlling Load Case Type')
plt.xlabel('Load Case Type')
plt.ylabel('Number of Members')
plt.ylim((0, 1000))
axes = plt.gca()
axes.yaxis.grid()

print("GRAVITY CASES: " + str(plotList.count(1)))
print("WIND CASES: " + str(plotList.count(2)))
print("EQ CASES: " + str(plotList.count(3)))


df = pd.DataFrame({"chg": chgCont })
#variable=[-0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
variable=[-0.05, 0, 0.05, 0.1, 0.15, 0.2, 0.25,  0.3, 0.35]
#variable=[ -0.45,-0.4, -0.35, -0.3,-0.25, -0.2, -0.15, -0.1, -0.05, 0, 0.05, 0.1, 0.15, 0.2]
arr = df.hist(bins = variable, layout=(1,1), rwidth = 0.9)


#for ax in arr.flatten():
 #   ax.set_xlabel("Increase in Axial Force")
  #  ax.set_ylabel("Number of Members")
    
#arr.set_xticks(-.2, -.1, 0, .1, .2, .3, .4, .5, .6, .7, .8 )

plt.xlabel('Increase in Axial force')
plt.ylabel('Number of Members')
plt.title('Increase in Axial Force')
plt.xticks(variable)
plt.xticks(fontsize = 10)
plt.ylim((0, 900))
ax = plt.axes()


for label in ax.xaxis.get_ticklabels()[::2]:
    label.set_visible(False)


