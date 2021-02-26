# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 10:25:41 2021

@author: djc

use grep to check log files:
    
    grep -r -i --include=*.LOG 'w a r n i n g' /d/Working/Sequence\ C1\ -\ Base\ Models/
"""

import os
import sys
import comtypes.client
import UtilityFuncs as uf

modelfolder = 'D:\Working\BallHitchPin_TPinsReleased'
modelname = '210111- Combined_Model_SEQ_B_EAST_V26_ballHitchPin_TPinReleased.sdb'
 
def startSap():
    #set the following flag to True to attach to an existing instance of the program
    #otherwise a new instance of the program will be started
    AttachToInstance = False
    
     
    
    #set the following flag to True to manually specify the path to SAP2000.exe
    #this allows for a connection to a version of SAP2000 other than the latest installation
    #otherwise the latest installed version of SAP2000 will be launched
    SpecifyPath = False
       
     
    
    if AttachToInstance:
        #attach to a running instance of SAP2000
        try:
            #get the active SapObject
            mySapObject = comtypes.client.GetActiveObject("CSI.SAP2000.API.SapObject")
    
        except (OSError, comtypes.COMError):
            print("No running instance of the program found or failed to attach.")
            sys.exit(-1)
    
    else:
    
        #create API helper object
        helper = comtypes.client.CreateObject('SAP2000v1.Helper')
        helper = helper.QueryInterface(comtypes.gen.SAP2000v1.cHelper)
        if SpecifyPath:
    
            try:
    
                #'create an instance of the SAPObject from the specified path
                mySapObject = helper.CreateObject(ProgramPath)
    
            except (OSError, comtypes.COMError):
    
                print("Cannot start a new instance of the program from " + ProgramPath)
                sys.exit(-1)
    
        else:
    
            try:
    
                #create an instance of the SAPObject from the latest installed SAP2000
                mySapObject = helper.CreateObjectProgID("CSI.SAP2000.API.SapObject")
    
            except (OSError, comtypes.COMError):
    
                print("Cannot start a new instance of the program.")
                sys.exit(-1)
    
     
    
        #start SAP2000 application
    
        mySapObject.ApplicationStart()
        
        return mySapObject

folder_path = r'D:\Working\Sequence C1 - Base Models\test'
file_list = uf.files_in_folder(folder_path)

cases_to_run = ["DEAD"]

mySapObject = startSap()
SapModel = mySapObject.SapModel

for file in file_list:
    
    #check if sdb or something else. if something else, skip
    (file_name,ext) = os.path.splitext(file)
    if ext != ".sdb":
        continue

    #open model
    SapModel.File.OpenFile(folder_path+os.sep+file)
    
    #save it to a subfolder
    os.makedirs(folder_path+os.sep+file_name,exist_ok=True)
    SapModel.File.Save(folder_path+os.sep+file_name+os.sep+file)
    
    #set standard solver
    SapModel.Analyze.SetSolverOption_2(0,0,0)
    
    #get all load case names
    [_,load_cases,_,_] = SapModel.Analyze.GetCaseStatus()
    
    #turn off all cases
    SapModel.Analyze.SetRunCaseFlag(None,False,True)
    
    #turn on specified load cases
    for lc in cases_to_run:
        SapModel.Analyze.SetRunCaseFlag(lc,True)
    
    #run analysis
    ret = SapModel.Analyze.RunAnalysis()
    if ret:
        print(f'{file} had an error')
    else:
        print(f'{file} ran successfully')
        
    #save results
    SapModel.File.Save()

#cleanup
mySapObject.ApplicationExit(False)
SapModel = None
mySapObject = None
