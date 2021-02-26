"""This script for preparing the reduced model used for David's Method"""
import attach

"""Select and Delete Tertiary and Backup Structure"""

frpSections=["ASEC1", "ASEC2", "ASEC3"]
stfnrSections=["FSEC1", "FSEC2", "FSEC3", "FSEC4"]

attach.clear_selection()

for i in range(len(frpSections)):
    attach.select_by_area(frpSections[i])
for i in range(len(stfnrSections)):
    attach.select_by_frame(stfnrSections[i])