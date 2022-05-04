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
        
        helper = comtypes.client.CreateObject('SAP2000v1.Helper')
        helper = helper.QueryInterface(comtypes.gen.SAP2000v1.cHelper)
        
        try:
            #get the active SapObject
            
            mySapObject = helper.GetObject("CSI.SAP2000.API.SapObject")
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
        
    def checkret(self,ret,step):
        if ret:
            print("  error at "+step)
        return 0
    
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
        
        _, objtype, jointname, ret = self.SapModel.SelectObj.GetSelected()
        ret = self.checkret(ret,"get selected items")
        
        
        jointmask = [i in obj_type_list for i in objtype]
        
        selectedobjs = list(compress(jointname,jointmask))
        selectedobj_types = list(compress(objtype,jointmask))
        
        return selectedobjs,selectedobj_types

    def add_joints_to_group(self,groupname, joints):
        """
        assign joints in list joints to group groupname. Creates group groupname if it does not exist
        """
        
        ret = self.SapModel.GroupDef.SetGroup(groupname)
        ret = self.checkret(ret,"get items in group "+groupname)
        #for ETABS
        #ret = SapModel.GroupDef.SetGroup_1(groupname)
        
        for j in joints:
            ret = self.SapModel.PointObj.SetGroupAssign(str(j),groupname)
            ret = self.checkret(ret,"add joint " + j + " in " + groupname)
            
    def add_areas_to_group(self,groupname, areas):
        """
        assign joints in list joints to group groupname. Creates group groupname if it does not exist
        """
        
        ret = self.SapModel.GroupDef.SetGroup(groupname)
        ret = self.checkret(ret,"get items in group "+groupname)
        #for ETABS
        #ret = SapModel.GroupDef.SetGroup_1(groupname)
        
        for j in areas:
            ret = self.SapModel.AreaObj.SetGroupAssign(str(j),groupname)
            ret = self.checkret(ret,"add area " + j + " in " + groupname)
    
    def add_frames_to_group(self,groupname,frames):
        """
        assign frames in list frames to group groupname. Creates group groupname if it does not exist
        """
        
        ret = self.SapModel.GroupDef.SetGroup(groupname)
        ret = self.checkret(ret,"get items in group "+groupname)
        #for ETABS
        #ret = SapModel.GroupDef.SetGroup_1(groupname)
        
        for j in frames:
            ret = self.SapModel.FrameObj.SetGroupAssign(str(j),groupname)
            ret = self.checkret(ret,"add frame " + j + " in " + groupname)
            
    def select_group(self, groupname):
        ret = self.SapModel.SelectObj.Group(groupname)
        ret = self.checkret(ret,"select group "+groupname)
    
    def clear_selection(self):
        ret = self.SapModel.SelectObj.ClearSelection()
        ret = self.checkret(ret,"clear selection")
            
    def get_groups(self, groupnames):
        """
        

        Parameters
        ----------
        groupnames : string
            List of group names

        Returns
        -------
        group_dict : dictionary of lists
            Dictionary where group_dict[groupname] = [ObjectType, ObjectName].

        """
        group_dict = {}
        for group in groupnames:
            _, ObjectType, ObjectName, ret = self.SapModel.GroupDef.GetAssignments(group)
            ret = self.checkret(ret,"get items in group "+group)
            group_dict[group] = [ObjectType, ObjectName]
        
        return group_dict
    
    def write_groups(self, group_dict):
        
        write_dict = {1:self.SapModel.PointObj.SetGroupAssign, #point
                      2:self.SapModel.FrameObj.SetGroupAssign, #frame
                      3:self.SapModel.CableObj.SetGroupAssign, #cable
                      4:self.SapModel.TendonObj.SetGroupAssign,#tendon
                      5:self.SapModel.AreaObj.SetGroupAssign,  #area
                      6:self.SapModel.SolidObj.SetGroupAssign, #solid
                      7:self.SapModel.LinkObj.SetGroupAssign}  #link
        
        for group in group_dict:
            
            ret = self.SapModel.GroupDef.SetGroup(group)
            ret = self.checkret(ret,"add group "+group)
            
            ObjectTypes, ObjectNames = group_dict[group]
            
            for obj_type, obj_name in zip(ObjectTypes,ObjectNames):
                ret = write_dict[obj_type](obj_name,group)
                ret = self.checkret(ret,"add object "+obj_name + " to group " +group)
                
        return
            
                
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
                self.sapElements.append(sapJoint(sapApplication_instance,self.ObjectName[i]))
                
            elif(current_typeID==5):
                self.sapElements.append(sapArea(sapApplication_instance, self.ObjectName[i]))
                
            elif(current_typeID==2):
                self.sapElements.append(sapFrame(sapApplication_instance,self.ObjectName[i]))
                
                
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
class sapArea:
    """
    sapJoint contains the name of an area. Initialize using sapJoint(sapApplication_instance, areaID)


    sapJoint.areaID tells the name of the area

    """
    def __init__(self, sapApplication_instance, areaID):
        
        self.SapModel = sapApplication_instance.SapModel
        
        self.areaID = areaID
        

    
class sapFrame:

    """
    sapFrame contains a frame element. Initialize using sapFrame(sapApplication_instance,ID)

    sapFrame.ID tells the name of the frame
    sapFrame.iEnd tells the point Object name of the i End
    sapFrame.iEnd tells the point Object name of the j End
    """
    def __init__(self,sapApplication_instance,ID):
        
        self.SapModel = sapApplication_instance.SapModel
        
        self.ID = ID
        
        (iEnd, jEnd, ret) = self.SapModel.frameObj.GetPoints(ID)
        self.iEnd = iEnd
        self.jEnd = jEnd
        if ret !=0:
            print ("error!")


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



