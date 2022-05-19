# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 16:24:24 2022

@author: acp
"""
import attach
sapBox = attach.sapApplication()
from tqdm import tqdm

filePath = r"C:\Users\acp\Desktop\Facad Peer Review\2022_04_26 C1 SE Study\2022_04_27 C1 Audit Study_Analysis Releases_PinAtKH.xlsx"

sheetname ="forPython"

memberList = attach.get_list_excel(filePath,sheetname,"Member Label") 
propertyList = attach.get_list_excel(filePath,sheetname,"Property")  
iM2List = attach.get_list_excel(filePath,sheetname,"i-M2") 
iM3List  = attach.get_list_excel(filePath,sheetname,"i-M3") 
iTList = attach.get_list_excel(filePath,sheetname,"i-T") 
iROList = attach.get_list_excel(filePath,sheetname,"i-Rigid Offset") 
jM2List = attach.get_list_excel(filePath,sheetname,"j-M2") 
jM3List  = attach.get_list_excel(filePath,sheetname,"j-M3") 
jTList = attach.get_list_excel(filePath,sheetname,"j-T") 
jROList = attach.get_list_excel(filePath,sheetname,"j-Rigid Offset") 

errorTrk = []

for i in tqdm(range(len(memberList))):
    member = memberList[i]
    iM2 = iM2List[i]
    iM3 = iM3List[i]
    iT = iTList[i]
    jM2 = jM2List[i]
    jM3 = jM3List[i]
    jT = jTList[i]
    iRO = iROList[i]
    jRO = jROList[i]
    a, b, c, d,ret = sapBox.SapModel.FrameObj.GetReleases(member)
    if ret != 0:
        print("Error in getting " + member +" Releases")
    i_release =[False, False, False, iT, iM2, iM3]
    j_release =[False, False, False, jT, jM2, jM3]
    i_release, j_release, c, d, ret = sapBox.SapModel.FrameObj.SetReleases(member, i_release, j_release,c, d)
    if ret != 0:
        print("Error in setting " + member +" Releases")
        print("ret= "+str(ret))
        errorTrk.append(member)
    if propertyList[i] != "no change":
        ret = sapBox.SapModel.FrameObj.SetSection(member, propertyList[i])
        if ret != 0:
            print("Error in setting" + member +" Section Property")
            
    ret = sapBox.SapModel.FrameObj.SetEndLengthOffset(member,AutoOffset=False,Length1=iRO,Length2=jRO,RZ=1.0,ItemType=0)
    if ret!= 0:
        print("Error in setting " + member +" End Length Offset")
        
ret = sapBox.add_frames_to_group("LERA_UpdatedBBOffsets", memberList)