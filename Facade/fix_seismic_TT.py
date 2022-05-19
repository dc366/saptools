# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 12:12:20 2022

@author: djc
"""

import attach
import UtilityFuncs as uf
import os.path

folder_path = r'D:\Working\P1092\fix_seismic\bot'
file_list = uf.files_in_folder(folder_path)

a = attach.sapApplication()

load_combos = ['5.1_1.2D+1.0L+1.0Eh(+100/+30)+1.0Ev',
'5.2_1.2D+1.0L+1.0Eh(+100/-30)+1.0Ev',
'5.3_1.2D+1.0L+1.0Eh(+30/-100)+1.0Ev',
'5.4_1.2D+1.0L+1.0Eh(-30/-100)+1.0Ev',
'5.5_1.2D+1.0L+1.0Eh(-100/-30)+1.0Ev',
'5.6_1.2D+1.0L+1.0Eh(-100/+30)+1.0Ev',
'5.7_1.2D+1.0L+1.0Eh(-30/+100)+1.0Ev',
'5.8_1.2D+1.0L+1.0Eh(+30/+100)+1.0Ev',
'6.1.1_0.9D+1.0Eh(+100/+30)-1.0Ev',
'6.1.2_0.9D+1.0Eh(+100/-30)-1.0Ev',
'6.1.3_0.9D+1.0Eh(+30/-100)-1.0Ev',
'6.1.4_0.9D+1.0Eh(-30/-100)-1.0Ev',
'6.1.5_0.9D+1.0Eh(-100/-30)-1.0Ev',
'6.1.6_0.9D+1.0Eh(-100/+30)-1.0Ev',
'6.1.7_0.9D+1.0Eh(-30/+100)-1.0Ev',
'6.1.8_0.9D+1.0Eh(+30/+100)-1.0Ev',
'7.1.1_0.9D+1.0Eh(+100/+30)+1.0Ev',
'7.1.2_0.9D+1.0Eh(+100/-30)+1.0Ev',
'7.1.3_0.9D+1.0Eh(+30/-100)+1.0Ev',
'7.1.4_0.9D+1.0Eh(-30/-100)+1.0Ev',
'7.1.5_0.9D+1.0Eh(-100/-30)+1.0Ev',
'7.1.6_0.9D+1.0Eh(-100/+30)+1.0Ev',
'7.1.7_0.9D+1.0Eh(-30/+100)+1.0Ev',
'7.1.8_0.9D+1.0Eh(+30/+100)+1.0Ev']

Ev_factor = 0.218
Eh_factor = 0.33


def checkret(ret,step):
    if ret:
        print("error at "+step)
        quit()


for file in file_list:
    
    #check if sdb or something else. if something else, skip
    (file_name,ext) = os.path.splitext(file)
    if ext != ".sdb":
        continue

    #open model
    ret = a.SapModel.File.OpenFile(folder_path+os.sep+file)
    checkret(ret,"open model "+file_name)
    
    #modify EX and EY load pattern
    (DirFlag, Eccen, UserZ, TopZ, BottomZ, c, k, ret) = a.SapModel.LoadPatterns.AutoSeismic.GetUserCoefficient("E-X")
    checkret(ret,"get E-X "+file_name)
    
    ret = a.SapModel.LoadPatterns.AutoSeismic.SetUserCoefficient("E-X",DirFlag,Eccen,UserZ,TopZ,BottomZ,Eh_factor,k)
    checkret(ret,"set E-X "+file_name)
    
    (DirFlag, Eccen, UserZ, TopZ, BottomZ, c, k, ret) = a.SapModel.LoadPatterns.AutoSeismic.GetUserCoefficient("E-Y")
    checkret(ret,"get E-Y "+file_name)    
    
    ret = a.SapModel.LoadPatterns.AutoSeismic.SetUserCoefficient("E-Y",DirFlag,Eccen,UserZ,TopZ,BottomZ,Eh_factor,k)
    checkret(ret,"set E-Y "+file_name)
    
    #modify seismic load combos
    for combo in load_combos:
        #get load combo
        (NumberLoads, LoadType, LoadName, SF, ret) = a.SapModel.LoadCases.StaticNonlinear.GetLoads(combo)
        checkret(ret,"get load case "+ combo + ","+ file_name)
        
        #find ez
        EZ_index = LoadName.index("E-Z")
        
        #create new input lists
        LoadName_rev = list(LoadName)
        SF_rev = list(SF)
        LoadType_rev = list(LoadType)
        
        #modify load case names E-Z -> DEAD, SDL_MEP
        LoadName_rev[EZ_index] = "DEAD"
        LoadName_rev.append("SDL_MEP")
        
        #increment loads by 1
        NumberLoads = NumberLoads + 1
        
        #get Ev load factor (+/- 1.0)
        Ev_loadfactor = SF[EZ_index]
        
        #store new Ev load factor, using old factor's sign
        SF_rev[EZ_index] = Ev_factor * Ev_loadfactor
        SF_rev.append(Ev_factor * Ev_loadfactor)
        
        #add 1 more loadtype to account for additional load pattern
        LoadType_rev.append("Load")
        
        #write new load case
        _,_,_,ret = a.SapModel.LoadCases.StaticNonlinear.SetLoads(combo,NumberLoads,LoadType_rev,LoadName_rev,SF_rev)
        checkret(ret,"set load case "+ combo + ","+ file_name)

    #set analysis flags
    #set all to not run
    ret = a.SapModel.Analyze.SetRunCaseFlag(None,False,True)
    checkret(ret,"set all cases to not run "+file_name)
    
    #set selected combos to run
    for combo in load_combos:
        ret = a.SapModel.Analyze.SetRunCaseFlag(combo,True)
        checkret(ret,"set case to run, "+combo+","+file_name)

    #save file
    ret = a.SapModel.File.Save()
    checkret(ret,"save "+file_name)


