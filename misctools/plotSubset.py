# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 09:41:58 2021

@author: acp
"""
import pandas as pd
subList =[]
subChg =[]
contAxSub = []

for i in range(len(frameList)):
    if newComp[i] > 2 or newTens[i] > 2:
        subList.append(frameList[i])
        subChg.append(chgCont[i])
        greater = max(newComp[i], newTens[i])
        contAxSub.append(greater)
    else:
        continue
    
    
    
df = pd.DataFrame({"chg": subChg })

#df.plot.hist(bins=20)


from matplotlib import pyplot as plt

#variable=[-0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
#variable=[-0.05, 0, 0.05, 0.1, 0.15, 0.2, 0.25,  0.3, 0.35]
variable=[ -0.45,-0.4, -0.35, -0.3,-0.25, -0.2, -0.15, -0.1, -0.05, 0, 0.05, 0.1, 0.15, 0.2]
#variable=[-0.35, -0.3,-0.25, -0.2, -0.15, -0.1, -0.05, 0, 0.05, 0.1, 0.15]

arr = df.hist(bins = variable, layout=(1,1), rwidth = 0.9)
plt.xlabel('Increase in Axial force')
plt.ylabel('Number of Members')
plt.title('Increase in Axial Force')
plt.xticks(variable)
plt.ylim((0, 400))
ax = plt.axes()


for label in ax.xaxis.get_ticklabels()[::2]:
    label.set_visible(False)
