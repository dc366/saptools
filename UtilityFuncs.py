# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 17:44:42 2021

@author: djc
"""

from os import listdir
from os.path import isfile, join

def files_in_folder(path_to_folder):
    """
    

    Parameters
    ----------
    path_to_folder : string
        path to folder that we want a list of files from

    Returns
    -------
    onlyfiles : string
        a list of all files in the folder

    """
    onlyfiles = [f for f in listdir(path_to_folder) if isfile(join(path_to_folder, f))]
    
    return onlyfiles