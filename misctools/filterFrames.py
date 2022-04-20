# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 11:50:37 2021

@author: acp
"""

import attach
#a = attach.sapApplication()
import pandas as pd
filePath = r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\2021_11_04 Member Changes.xlsx"
sheetName = "BEast"
header = "Special"
listA = attach.get_list_excel(filePath,sheetName,header)
filterChg =[]
filterMaxNew = []
filterMaxOld = []


for i in range(len(listA)):
    if listA[i] in frameList:
        index = frameList.index(listA[i])
        filterChg.append(chgCont[index])
        filterMaxNew.append(max(newComp[index], newTens[index]))
        filterMaxOld.append(max(oldComp[index], oldTens[index]))
    else:
        filterChg.append(0)
        print(listA[i]+" not in frameList")
        
cf = pd.DataFrame({"chgSub": subChg })        
df = pd.DataFrame({"chg": filterChg })


#df.plot.hist(bins=20)


from matplotlib import pyplot as plt

#variable=[0, 0.05, 0.1, 0.15, 0.2]
#variable=[-0.05, 0, 0.05, 0.1, 0.15, 0.2, 0.25,  0.3, 0.35]
#variable=[-0.3,-0.25, -0.2, -0.15, -0.1, -0.05, 0, 0.05, 0.1]
variable=[-0.35, -0.3,-0.25, -0.2, -0.15, -0.1, -0.05, 0, 0.05, 0.1, 0.15]
#plt.hist(subChg, bins = variable, layout=(1,1), rwidth = 0.9)
#plt.hist(filterChg, bins = variable, layout=(1,1), rwidth = 0.9)
plt.hist(subChg, bins = variable, rwidth = 0.9, label= "All Members > 2kips")
plt.hist(filterChg, bins = variable, rwidth = 0.9, label = "Flagged for Screw Increase", color = "magenta")
plt.xlabel('Increase in Axial force')
plt.ylabel('Number of Members')
plt.title('Increase in Axial Force')
plt.xticks(variable)
plt.ylim((0, 40))
plt.legend(loc = 'upper right')
ax = plt.axes()


for label in ax.xaxis.get_ticklabels()[::2]:
    label.set_visible(False)

#a.add_frames_to_group('LERA_TTIncrease',listA)

tempList = [listA, filterMaxOld, filterMaxNew]
combinedList= zip(*tempList)
df = pd.DataFrame(combinedList)
writer = pd.ExcelWriter('Output.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name="Output", index=False)
writer.save()