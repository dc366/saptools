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

folder_path = r'D:\Working\to_fix'
file_list = uf.files_in_folder(folder_path)

mySapObject = startSap()
SapModel = mySapObject.SapModel

for file in file_list:
    
    #check if sdb or something else. if something else, skip
    (file_name,ext) = os.path.splitext(file)
    if ext != ".sdb":
        continue

    #open model
    SapModel.File.OpenFile(folder_path+os.sep+file)
    
    #select all and delete reverseSW on frames
    SapModel.SelectObj.All()
    SapModel.FrameObj.DeleteLoadGravity(None,"reverseSW",2)
    
    #select all and delete reverseSW on areas
    SapModel.SelectObj.All()
    SapModel.AreaObj.DeleteLoadGravity(None,"reverseSW",2)    
    
    #add reverseSW to correct group
    SapModel.FrameObj.SetLoadGravity("LERA_secondary","reverseSW",0,0,1,ItemType=1)
    SapModel.AreaObj.SetLoadGravity("LERA_secondary","reverseSW",0,0,1,ItemType=1)    
    
    #save results
    SapModel.File.Save()

#cleanup
mySapObject.ApplicationExit(False)
SapModel = None
mySapObject = None
