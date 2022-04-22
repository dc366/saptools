# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 11:53:14 2021

@author: acp
"""

# This script compares "P" from frame forces extrated from two models
# Delete first row of frame output
# The two excel files must be the same length and frames selected output


import pandas as pd
from tqdm import tqdm

sheetName = "Element Forces - Frames"
#sheetName = "Test"

print("Gathering Data")
#dataOld = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\211021- Combined_Model_SEQ_B_EAST_oldWeightV2_secondary.xlsx", sheetName)
#dataNew = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\211021- Combined_Model_SEQ_B_EAST_newWeightV2_Secondary.xlsx", sheetName)

dataOld = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\211021- Combined_Model_SEQ_B_EAST_oldWeightV2_reverted.xlsx", sheetName)
dataNew = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\211021- Combined_Model_SEQ_B_EAST_newWeightV2_Reverted.xlsx", sheetName)

#dataOld = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\C14T_KVV_renameTJT_frameForces.xlsx", sheetName)
#dataNew = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\C14T_KVV_renameTJT_NewV1_frameForces.xlsx", sheetName)

#dataOld = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\211021- Combined_Model_SEQ_B_EAST_oldWeightV2_reverted.xlsx", sheetName)
#dataNew = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\211021- Combined_Model_SEQ_B_EAST_newWeightV3_Reverted.xlsx", sheetName)

#dataNew = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\C14T_KVV_renameTJT_NewV1_straps.xlsx", sheetName)
#dataOld = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\C14T_KVV_renameTJT_straps.xlsx", sheetName)


#dataOld = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\C16B_KV_20200303_frameForces.xlsx", sheetName)
#dataNew = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\C16B_KV_20200303_NewV1.xlsx", sheetName)

#dataOld = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\C14B_KVV_renameTJT.xlsx", sheetName)
#dataNew = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\C14B_KVV_renameTJT_NewV1.xlsx", sheetName)

#dataOld = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\C14T_KVV_renameTJT.xlsx", sheetName)
#dataNew = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\C14T_KVV_renameTJT_NewV1.xlsx", sheetName)

#dataOld = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\C13B_Adjusted200210_frameForces.xlsx", sheetName)
#dataNew = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\C13B_Adjusted200210_NewV1.xlsx", sheetName)

#dataOld = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\C15T_KVV_renameTJT_tpin_LK_frameForces.xlsx", sheetName)
#dataNew = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\C15T_KVV_renameTJT_tpin_LK_NewV1.xlsx", sheetName)

#dataOld = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\C06B_AK_AKrename_TJT (2).xlsx", sheetName)
#dataNew = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\C06B_AK_AKrename_TJT (2)_NewV1.xlsx", sheetName)

#dataOld = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\211021- Combined_Model_SEQ_B_EAST_oldWeightV2_reverted_noVertSeis.xlsx", sheetName)
#dataNew = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\211021- Combined_Model_SEQ_B_EAST_oldWeightV2_reverted.xlsx", sheetName)

#dataOld = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\211021- Combined_Model_SEQ_B_EAST_oldWeightV2_reverted_noVertSeis.xlsx", sheetName)
#dataNew = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\211021- Combined_Model_SEQ_B_EAST_newWeightV2_Reverted_noVertSeis.xlsx", sheetName)

#dataOld = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\211021- Combined_Model_SEQ_B_EAST_oldWeightV2_reverted_noVertSeis.xlsx", sheetName)
#dataNew = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\211021- Combined_Model_SEQ_B_EAST_newWeightV3_Reverted_noVertSeis.xlsx", sheetName)

#dataOld = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\211021- Combined_Model_SEQ_B_EAST_newWeightV2_Reverted_noVertSeis.xlsx", sheetName)
#dataNew = pd.read_excel(r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\weightStudyFrameForces\211021- Combined_Model_SEQ_B_EAST_newWeightV2_Reverted.xlsx", sheetName)

dataNew = dataNew.drop(0)
dataOld = dataOld.drop(0)

#frameList = dataNew["Frame"].drop_duplicates().tolist()

frameList = dataNew["Frame"].unique().tolist()
#frameList = dataOld["Frame"].unique().tolist()

print(frameList)

oldMin = []
oldComp = []
newMin = []
newComp =[]
oldMax = []
oldTens = []
newMax = [] 
newTens = []
chgTens = []
chgComp = []
chgCont = []
loadCaseM1 = []
loadCaseM2 = []
contCaseOld = []
contCaseNew = []
caseOld = []
caseNew = []

# find Max and Mins

for frame in frameList:
    memberForces = dataNew[dataNew["Frame"] == frame]
    maxVal = memberForces["P"].max()
    minVal = memberForces["P"].min()
    
    #Determine which type of Load Case Controls:
    if abs(minVal)> abs(maxVal):
        index = memberForces["P"].tolist().index(minVal)
    else:
        index = memberForces["P"].tolist().index(maxVal)
    case = memberForces["OutputCase"].tolist()[index] 
    caseNew.append(case)
    if "E" in case:  #Assign 3 for EQ Cases
        contCaseNew.append(3)
    elif "W" in case:  #Assign 2 for Wind Cases
        contCaseNew.append(2)
    else:                   #For gravity, assign 1
        contCaseNew.append(1)
        
    if maxVal > 0:
        newTens.append(maxVal)
    else:
        newTens.append(0)
    if minVal < 0:
        newComp.append(abs(minVal))
    else:
        newComp.append(0)
        
    memberForces = dataOld[dataOld["Frame"] == frame]
    maxVal = memberForces["P"].max()
    minVal = memberForces["P"].min()
    
    if abs(minVal)> abs(maxVal):
        index = memberForces["P"].tolist().index(minVal)
    else:
        index = memberForces["P"].tolist().index(maxVal)
    case = memberForces["OutputCase"].tolist()[index] 
    caseOld.append(case)
    if "E" in case:  #Assign 3 for EQ Cases
        contCaseOld.append(3)
    elif "W" in case:  #Assign 2 for Wind Cases
        contCaseOld.append(2)
    else:                   #For gravity, assign 1
        contCaseOld.append(1)    
    
    
    if maxVal > 0:
        oldTens.append(maxVal)
    else:
        oldTens.append(0)
    if minVal < 0:
        oldComp.append(abs(minVal))
    else:
        oldComp.append(0)
        
        
for i in range(len(frameList)):
    try:
        chgTens.append((newTens[i]-oldTens[i])/oldTens[i])
    except:
        chgTens.append(0)
        
    try:
        chgComp.append((newComp[i]-oldComp[i])/oldComp[i])
    except:
        chgComp.append(0)
        
    if oldComp[i] > oldTens[i]:
        chgCont.append((newComp[i]-oldComp[i])/oldComp[i])
    else:
        chgCont.append((newTens[i]-oldTens[i])/oldTens[i])
        
    
df = pd.DataFrame({"chg": chgCont })

df.plot.hist(bins=20)
    
    
    
    
    
    
    