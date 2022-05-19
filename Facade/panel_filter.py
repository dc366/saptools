# -*- coding: utf-8 -*-
"""

@author: djc

"""

import attach

a = attach.sapApplication()

#place elements with these substrings into separate groups

panel_substrings = ['C23-05']

area_dict = {}
for sub in panel_substrings:
    area_dict[sub] = []

#search all areas for panel substrings and move them to another group
[_,areas,_] = a.SapModel.AreaObj.GetNameList()
area_list = list(areas)

for area in areas:
    for sub in panel_substrings:
        if sub in area:
            area_dict[sub].append(area)

#create groups for each panel   
for sub in panel_substrings:
    a.add_areas_to_group('panel_' + sub , area_dict[sub])