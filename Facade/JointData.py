# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:13:45 2021

@author: djc
"""

import pandas as pd
import os.path
import os 

class JointData:
    """encapsulate the joint results for an entire analysis model"""    
    def __init__(self,csv_folder_path):
        """
        creates a new instance of JointData
        
        Parameters
        ----------
        csv_folder_path : string
            path to folder with csv files

        """           

        self.model_name = "test"
        self.data = {}
        self.load_case = []
        
        csvfiles = JointData.get_file_names(csv_folder_path)
        
        for f in csvfiles:
            (data,load_case) = JointData.get_csv_data(f)
            self.data[load_case] = data
            self.load_case.append(load_case)
        
        return

    
    @staticmethod
    def get_csv_data(filepath):
        """
        returns a dataframe from csv file

        Parameters
        ----------
        filepath : string
            path to csv file to read

        Returns
        -------
        fulldata : pd.dataframe
            contains all the output for this file/loadcase
        load_case : string
            load case name

        """
        fulldata = pd.read_csv(filepath,header=[3])
        
        load_case = fulldata.iat[0,0]
        return fulldata,load_case
    
    @staticmethod
    def get_file_names(folderpath):
        """returns csv files in a folder
        
        Parameters
        ----------
        folderpath : string
            path to folders with csv files
        """
        onlyfiles = [os.path.join(folderpath, f) for f in os.listdir(folderpath) if os.path.isfile(os.path.join(folderpath, f))]
        onlycsv = [f for f in onlyfiles if "csv" in f]
        
        return onlycsv