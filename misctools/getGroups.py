# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:41:46 2022

@author: acp
"""

import attach
a = attach.sapApplication()

#(color, a, b, c, d, e, f, g, h, i, j, k, ret) = a.SapModel.GroupDef.GetGroup('LERA_LessThan0')
#(color, a, b, c, d, e, f, g, h, i, j, k, ret) = a.SapModel.GroupDef.GetGroup('LERA_0-10')
(color, a, b, c, d, e, f, g, h, i, j, k, ret) = a.SapModel.GroupDef.GetGroup('LERA_5-10')
#a.add_frames_to_group('LERA_0-10',grp2)
#a.add_frames_to_group('LERA_10-20',grp3)
#a.add_frames_to_group('LERA_GreaterThan20',grp4)
#a.add_frames_to_group('LERA_WeightStudy',frameList)

print(color)