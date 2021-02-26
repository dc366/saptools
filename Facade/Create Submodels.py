# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 10:25:41 2021

@author: djc
"""

import os
import sys
import comtypes.client

modelfolder = 'D:\Working\BallHitchPin_TPinsReleased'
modelname = '210111- Combined_Model_SEQ_B_EAST_V26_ballHitchPin_TPinReleased.sdb'
 
def startSap(modelname,modelfolder):
    #set the following flag to True to attach to an existing instance of the program
    #otherwise a new instance of the program will be started
    AttachToInstance = False
    
     
    
    #set the following flag to True to manually specify the path to SAP2000.exe
    #this allows for a connection to a version of SAP2000 other than the latest installation
    #otherwise the latest installed version of SAP2000 will be launched
    SpecifyPath = False
     
    
    #full path to the model
    #set it to the desired path of your model
    
    APIPath = modelfolder
    
    if not os.path.exists(APIPath):
    
            try:
    
                os.makedirs(APIPath)
    
            except OSError:
    
                pass
    
    ModelPath = APIPath + os.sep + modelname
    
     
    
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

groups = ['bayC10',
          'bayC11',
          'bayC12',
          'bayC13',
          'bayC14',
          'bayC15',
          'bayC16',
          'bayC17']

mySapObject = startSap(modelname,modelfolder)

for group in groups:
    
    SapModel = mySapObject.SapModel    
    
    SapModel.File.OpenFile(modelfolder+os.sep+modelname)
    
    SapModel.SelectObj.Group(group)
    SapModel.SelectObj.InvertSelection()
    SapModel.AreaObj.Delete("",2)
    
    SapModel.SelectObj.Group(group)
    SapModel.SelectObj.InvertSelection()    
    SapModel.FrameObj.Delete("",2)
    
    SapModel.SelectObj.Group(group)
    SapModel.SelectObj.InvertSelection()
    SapModel.PointObj.DeleteSpecialPoint("",2)
    
    
    SapModel.File.Save(modelfolder+os.sep+group+".sdb")
    
    