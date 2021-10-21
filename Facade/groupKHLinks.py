# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 10:48:01 2021

@author: acp
"""


import attach

a = attach.sapApplication()

king_hat_substrings = ['_KHLink_']

#get all frame definitions
[_,linkList,_] = a.SapModel.LinkObj.GetNameList()

#get all king hat elements
link_hats = [s for s in linkList if any(sub in s for sub in king_hat_substrings)]



        
a.add_links_to_group('wt_KHLinks', link_hats)
