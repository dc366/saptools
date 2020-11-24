import sys
import comtypes.client
import pandas as pd
from itertools import compress

try:

    #get the active SapObject

    mySapObject = comtypes.client.GetActiveObject("CSI.SAP2000.API.SapObject")
    #mySapObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
    print("attached!")

except (OSError, comtypes.COMError):

    print("No running instance of the program found or failed to attach.")

    sys.exit(-1)

#create SapModel object

SapModel = mySapObject.SapModel

def closeSapModel():
    global mySapObject
    global SapModel
    print (mySapObject.ApplicationExit(False))
    SapModel = None
    mySapObject = None
    
class sapGroup:
    """
    sapGroup contains the elements in groupName. Initialize using sapGroup(groupName)

    sapGroup.numberItems tells the number of elements
    sapGroup.TypeID contains the type of each element (list) 
        (1 = joint, 2 = frame, 3 = cable, 4 = tendon, 5 = area, 6 = solid, 7 = link)
    sapGroup.ObjectName tells the name of each element (list)
    sapGroup.sapElements is a list of all the element objects
    """
    
    def __init__(self, groupName):
        global SapModel
        (self.numberItems, self.TypeID, self.ObjectName, ret) = SapModel.GroupDef.GetAssignments(groupName)
        
        if ret != 0:
            print ("error!")
        
        self.sapElements = []
        
        for i in range(self.numberItems):
            # need to update this section after adding classes for frame, cable, tendon, area, solid, link
            current_typeID = self.TypeID[i]
            
            if(current_typeID==1):
                self.sapElements.append(sapJoint(self.ObjectName[i]))
            else:
                self.sapElements.append()
            

class sapGroupList:
    """
    sapGroupList contains the all the group names in the SAP model. Initialize using sapGroupList()

    sapGroupList.numberItems tells the number of groups
    sapGroupList.groupNames contains the list of group names
    """
    def __init__(self):
        global SapModel
        (self.numberItems, self.groupNames, ret) = SapModel.GroupDef.GetNameList()
        
        if ret != 0:
            print ("error!")
            
class sapJoint:
    """
    sapJoint contains the coordinates of a joint. Initialize using sapJoint(jointID)

    sapJoint.jointID tells the name of the joint
    sapJoint.x contains the x coordinate
    sapJoint.y contains the y coordinate
    sapJoint.z contains the z coordinate
    """
    def __init__(self,jointID):
        global SapModel
        self.jointID = jointID
        [self.x, self.y, self.z, ret] = SapModel.PointObj.GetCoordCartesian(jointID)
        
        if ret != 0:
            print ("error!")

def add_joints_to_group(groupname, joints):
    """
    assign joints in list joints to group groupname. Creates group groupname if it does not exist
    """
    
    SapModel.GroupDef.SetGroup_1(groupname)
    
    for j in joints:
        SapModel.PointObj.SetGroupAssign(str(j),groupname)

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

def get_list_sap():
    """
    

    Returns
    -------
    selectedjoints : str list
        A list of all selected joints in the currently attached SAP instance

    """
    
    selectedobjs = SapModel.SelectObj.GetSelected()
    
    objtype = selectedobjs[1]
    jointname = selectedobjs[2]
    
    jointmask = [i == 1 for i in objtype]
    
    selectedjoints = list(compress(jointname,jointmask))
    
    return selectedjoints