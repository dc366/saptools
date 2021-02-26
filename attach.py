import sys
import comtypes.client
import pandas as pd
import os.path
from itertools import compress
from itertools import chain

class sapApplication:
    def __init__(self,modelname=None,modelpath=None):
        if (modelname and modelpath):
            self.SapObject = sapApplication.startSap(modelname,modelpath)
            self.SapModel = self.SapObject.SapModel
        else:
            self.SapObject = sapApplication.attachSap()
            self.SapModel = self.SapObject.SapModel

    @staticmethod
    def attachSap():
        try:
            #get the active SapObject
            
            mySapObject = comtypes.client.GetActiveObject("CSI.SAP2000.API.SapObject")
            #mySapObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
            print("attached!")
        
        except (OSError, comtypes.COMError):
        
            print("No running instance of the program found or failed to attach.")
        
            sys.exit(-1)
        
        
        return mySapObject
    
    @staticmethod
    def startSap(modelname,modelfolder):        
        
        #full path to the model
        #set it to the desired path of your model
        
        APIPath = modelfolder
        
        if not os.path.exists(APIPath):
        
            try: os.makedirs(APIPath)
    
            except OSError: pass
        
        ModelPath = APIPath + os.sep + modelname
        
        #create API helper object
        helper = comtypes.client.CreateObject('SAP2000v1.Helper')
        helper = helper.QueryInterface(comtypes.gen.SAP2000v1.cHelper)

        try:

            #create an instance of the SAPObject from the latest installed SAP2000
            mySapObject = helper.CreateObjectProgID("CSI.SAP2000.API.SapObject")

        except (OSError, comtypes.COMError):

            print("Cannot start a new instance of the program.")
            sys.exit(-1)

        #start SAP2000 application
    
        mySapObject.ApplicationStart()
        mySapObject.SapModel.File.OpenFile(ModelPath)
        
        return mySapObject

    def closeSapModel(self):
        print (self.SapObject.ApplicationExit(False))
        self.SapModel = None
        self.SapObject = None
    
    def get_list_sap(self,*args):
        
        objtype_dict = {"point":1,
                        "frame":2,
                        "cable":3,
                        "tendon":4,
                        "area":5,
                        "solid":6,
                        "link":7,
                        }
        """
        
    
        Returns
        -------
        selectedobjs : str list
            A list of all selected objects in the currently attached SAP instance.
    
        """
        obj_type_list = [objtype_dict[i] for i in args]
        
        selectedobjs = self.SapModel.SelectObj.GetSelected()
        
        objtype = selectedobjs[1]
        jointname = selectedobjs[2]
        
        
        jointmask = [i in obj_type_list for i in objtype]
        
        selectedobjs = list(compress(jointname,jointmask))
        selectedobj_types = list(compress(objtype,jointmask))
        
        return selectedobjs,selectedobj_types

    def add_joints_to_group(self,groupname, joints):
        """
        assign joints in list joints to group groupname. Creates group groupname if it does not exist
        """
        
        ret = self.SapModel.GroupDef.SetGroup(groupname)
        #for ETABS
        #ret = SapModel.GroupDef.SetGroup_1(groupname)
        if ret != 0:
            print ("error!")
        
        for j in joints:
            ret = self.SapModel.PointObj.SetGroupAssign(str(j),groupname)
            
            if ret != 0:
                print ("error!")
            
    def add_areas_to_group(self,groupname, areas):
        """
        assign joints in list joints to group groupname. Creates group groupname if it does not exist
        """
        
        ret = self.SapModel.GroupDef.SetGroup(groupname)
        #for ETABS
        #ret = SapModel.GroupDef.SetGroup_1(groupname)
        if ret != 0:
            print ("error!")
        
        for j in areas:
            ret = self.SapModel.AreaObj.SetGroupAssign(str(j),groupname)
            
            if ret != 0:
                print ("error!")
    
    def add_frames_to_group(self,groupname,frames):
        """
        assign frames in list frames to group groupname. Creates group groupname if it does not exist
        """
        
        ret = self.SapModel.GroupDef.SetGroup(groupname)
        #for ETABS
        #ret = SapModel.GroupDef.SetGroup_1(groupname)
        if ret != 0:
            print ("error!")
        
        for j in frames:
            ret = self.SapModel.FrameObj.SetGroupAssign(str(j),groupname)
            
            if ret != 0:
                print ("error!")
            
                
class sapGroup:
    """
    sapGroup contains the elements in groupName. Initialize using sapGroup(sapApplication_instance,groupName)
    
    sapGroup.groupName contains the name of the group
    sapGroup.numberItems tells the number of elements
    sapGroup.TypeID contains the type of each element (list) 
        (1 = joint, 2 = frame, 3 = cable, 4 = tendon, 5 = area, 6 = solid, 7 = link)
    sapGroup.ObjectName tells the name of each element (list)
    sapGroup.sapElements is a list of all the element objects
    
    sapGroup.select() selects the group in SAP
    
    """
    
    def __init__(self, sapApplication_instance,groupName):
        
        self.SapModel = sapApplication_instance.SapModel
        
        (self.numberItems, self.TypeID, self.ObjectName, ret) = self.SapModel.GroupDef.GetAssignments(groupName)
        
        if ret != 0:
            print ("error!")
        
        self.groupName = groupName
        self.sapElements = []
        
        for i in range(self.numberItems):
            # need to update this section after adding classes for frame, cable, tendon, area, solid, link
            current_typeID = self.TypeID[i]
            
            if(current_typeID==1):
                self.sapElements.append(sapJoint(self.SapModel,self.ObjectName[i]))
            elif(current_typeID==2):
                self.sapElements.append(sapFrame(self.SapModel,self.ObjectName[i]))
            else:
                self.sapElements.append()

    def select(self):
         
        self.SapModel.SelectObj.Group(self.groupName)

class sapGroupList:
    """
    sapGroupList contains the all the group names in the SAP model. Initialize using sapGroupList(sapApplication_instance)

    sapGroupList.numberItems tells the number of groups
    sapGroupList.groupNames contains the list of group names
    """
    def __init__(self,sapApplication_instance):
        
        self.SapModel = sapApplication_instance.SapModel
        
        (self.numberItems, self.groupNames, ret) = self.SapModel.GroupDef.GetNameList()
        
        if ret != 0:
            print ("error!")
            
class sapJoint:
    """
    sapJoint contains the coordinates of a joint. Initialize using sapJoint(sapApplication_instance,jointID)

    sapJoint.jointID tells the name of the joint
    sapJoint.x contains the x coordinate
    sapJoint.y contains the y coordinate
    sapJoint.z contains the z coordinate
    """
    def __init__(self,sapApplication_instance,jointID):
        
        self.SapModel = sapApplication_instance.SapModel
        
        self.jointID = jointID
        [self.x, self.y, self.z, ret] = self.SapModel.PointObj.GetCoordCartesian(jointID)
        
        if ret != 0:
            print ("error!")

class sapFrame:
    """
    sapJoint contains a frame element. Initialize using sapFrame(sapApplication_instance,ID)

    sapJoint.ID tells the name of the frame
    """
    def __init__(self,sapApplication_instance,jointID):
        
        self.SapModel = sapApplication_instance.SapModel
        
        self.ID = ID


def get_list_excel(filepath,sheetname,header):
    """

    Parameters
    ----------
    filepath : str
        Full path to Excel File to read
    sheetname : str
        Name of worksheet to read
    header : str
        Name of first cell in column to read. All values should be strings

    Returns
    -------
    cleanedlist : str list
        a list of all items in the column chosen

    """
    
    df = pd.read_excel(filepath, sheet_name=sheetname) # can also index sheet by name or fetch all sheets
    dirtylist = df[header].tolist()
    
    cleanedlist = [x for x in dirtylist if (pd.isnull(x) == False)]
    
    return cleanedlist


