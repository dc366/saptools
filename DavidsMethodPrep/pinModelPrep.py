import attach

"""INPUTS"""

frameProp1="CONN_rod"    #Tpin Section Property
frameProp2="CONN_rod_1in"   #Tpin Section Property
ii=[False, False, False, False, False, False]  #end i releases u1, u2, u3, r1 r2 r3
jj=[False, False, False, True, True, True]   #end j releases...
StartValue=[0]*6                              # spring stiffness
EndValue=[0]*6
ItemType1=2 #item type for "selection" = 2
Name="None"
nameList=["20", "21", "23"] #Miscellaeous "t-pins"
ItemType2=0  #item type for member label =0, item type for groups = 1

"""Set Frame Releases for Pinned T-Pins"""

attach.clear_selection()
attach.select_by_frame(frameProp1)
attach.select_by_frame(frameProp2)
attach.SapModel.FrameObj.SetReleases(Name,ii,jj,StartValue,EndValue,ItemType1)
for i in range(len(nameList)):
    ret=attach.SapModel.FrameObj.SetReleases(nameList[i],ii,jj,StartValue,EndValue,ItemType2)
