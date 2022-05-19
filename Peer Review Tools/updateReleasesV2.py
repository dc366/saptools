# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 16:24:24 2022

@author: acp
"""
import attach
sapBox = attach.sapApplication()
import prLibs as prLibs
from tqdm import tqdm

errorTrk = []

allMems = prLibs.memList()
panels = prLibs.panelLib()
memberList = []

for member in allMems:
    panel = panels[member]
    if panel == "C18-06" or panel == "C18-17" or panel== "C19-05" or panel== "C19-07" or panel== "C19-08":
        memberList.append(member)

chgLib = prLibs.memUpdates(memberList)


for i in tqdm(range(len(memberList))):
    member = memberList[i]
    values = chgLib[member]
    
    prop = values[0]
    iM2 = bool(values[1])
    iM3 = bool(values[2])
    iT = bool(values[3])
    jM2 = bool(values[5])
    jM3 = bool(values[6])
    jT = bool(values[7])
    iRO = values[4]
    jRO = values[8]
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
    if prop != "no change":
        ret = sapBox.SapModel.FrameObj.SetSection(member, prop)
        if ret != 0:
            print("Error in setting" + member +" Section Property")
            
    ret = sapBox.SapModel.FrameObj.SetEndLengthOffset(member,AutoOffset=False,Length1=iRO,Length2=jRO,RZ=1.0,ItemType=0)
    if ret!= 0:
        print("Error in setting " + member +" End Length Offset")
        
ret = sapBox.add_frames_to_group("LERA_UpdatedBBOffsets", memberList)