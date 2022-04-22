# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:43:21 2021

@author: acp
"""

import pandas as pd

fileList = [r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\C09B_Adjusted200210.xlsx",
            r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\C09T_KVV_renameTJT_LK.xlsx",
            r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\C10B_Adjusted200210.xlsx",
            r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\C10T_LK_renamedTJT_LK.xlsx",
            r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\C11B_AdjustedRenamed190925.xlsx",
            r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\C11T_actually_renameTJT.xlsx",
            r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\C12Ba_KVV_renameTJT.xlsx",
            r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\C12Bb_renamedTJT.xlsx",
            r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\C12T_KVV_renameTJT.xlsx",
            r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\C13B_Adjusted200210.xlsx",
            r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\C13T_KVV_renameTJT.xlsx",
            r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\C14B_KVV_renameTJT.xlsx",
            r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\C14T_KVV_renameTJT.xlsx",
            r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\C15B_Adjusted200224.xlsx",
            r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\C15T_KVV_renameTJT_tpin_LK.xlsx",
            r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\C16B_KV_20200303.xlsx",
            r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\C16T_TTMumscrub_LK_AKworking_renameTJT.xlsx",
            r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\C17B_LK_CFSing_AKworkingYAY_renameTJT.xlsx",
            r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\C17T_LK_renameTJT.xlsx",
            r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\GL-02-17_renamedTJT.xlsx",
            r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\GL-03-14 Lower_AdjustedBB190917.xlsx",
            r"C:\Users\acp\Desktop\2021_10_19 Seq B Re-analysis\EQ Load Verification\GL-03-14 Upper_AdjustedBB190917.xlsx"]


offset = 2
sheetName = "Joint Loads - Ground Displ"
totalRows = 0

for file in fileList:
    data = pd.read_excel(file, sheetName)
    totalRows = totalRows + len(data) - offset
    
print(totalRows)
    