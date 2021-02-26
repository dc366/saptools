# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:01:58 2021

@author: djc
Applies load patterns and creates load cases
"""

import attach

a = attach.sapApplication()

a.SapModel.LoadPatterns.Add("reverseSW",8)

a.SapModel.LoadCases.StaticNonlinear.SetCase("SERVICE-WIND(+)")
a.SapModel.LoadCases.StaticNonlinear.SetCase("SERVICE-WIND(-)")
a.SapModel.LoadCases.StaticNonlinear.SetCase("DEAD(+)SERVICE-WIND")
a.SapModel.LoadCases.StaticNonlinear.SetCase("DEAD(-)SERVICE-WIND")

a.SapModel.LoadCases.StaticNonlinear.SetLoads("DEAD",2,
                                              ["Load","Load"],
                                              ["DEAD","reverseSW"],
                                              [1.0,1.0])
a.SapModel.LoadCases.StaticNonlinear.SetLoads("SERVICE-WIND(+)",1,["Load"],["WIND(+)"],[1.0])
a.SapModel.LoadCases.StaticNonlinear.SetLoads("SERVICE-WIND(-)",1,["Load"],["WIND(-)"],[1.0])
a.SapModel.LoadCases.StaticNonlinear.SetLoads("DEAD(+)SERVICE-WIND",3,
                                              ["Load","Load","Load"],
                                              ["DEAD","WIND(+)","reverseSW"],
                                              [1.0,1.0,1.0])
a.SapModel.LoadCases.StaticNonlinear.SetLoads("DEAD(-)SERVICE-WIND",3,
                                              ["Load","Load","Load"],
                                              ["DEAD","WIND(-)","reverseSW"],
                                              [1.0,1.0,1.0])
