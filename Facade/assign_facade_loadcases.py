# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:01:58 2021

@author: djc
Applies load patterns and creates load cases
"""

import attach

a = attach.sapApplication()

a.SapModel.LoadPatterns.Add("reverseSW",8)

a.SapModel.LoadCases.StaticNonlinear.SetCase("DEAD_ALT")
a.SapModel.LoadCases.StaticNonlinear.SetCase("SERVICE-WIND(+)")
a.SapModel.LoadCases.StaticNonlinear.SetCase("SERVICE-WIND(-)")
a.SapModel.LoadCases.StaticNonlinear.SetCase("DEAD_ALT(+)SERVICE_WIND_1.0")
a.SapModel.LoadCases.StaticNonlinear.SetCase("DEAD_ALT(-)SERVICE_WIND_1.0")
a.SapModel.LoadCases.StaticNonlinear.SetCase("DEAD_ALT(+)SERVICE_WIND_0.7")
a.SapModel.LoadCases.StaticNonlinear.SetCase("DEAD_ALT(-)SERVICE_WIND_0.7")
a.SapModel.LoadCases.StaticNonlinear.SetCase("DEAD_ALT(+)SERVICE_WIND_1.0x0.78_ASCE7-16")
a.SapModel.LoadCases.StaticNonlinear.SetCase("DEAD_ALT(-)SERVICE_WIND_1.0x0.78_ASCE7-16")
a.SapModel.LoadCases.StaticNonlinear.SetCase("DEAD_ALT(+)SERVICE_WIND_0.7x0.78_ASCE7-16")
a.SapModel.LoadCases.StaticNonlinear.SetCase("DEAD_ALT(-)SERVICE_WIND_0.7x0.78_ASCE7-16")

a.SapModel.LoadCases.StaticNonlinear.SetLoads("DEAD_ALT",3,
                                              ["Load","Load","Load"],
                                              ["DEAD","reverseSW","SDL_MEP"],
                                              [1.0,1.0,1.0])

a.SapModel.LoadCases.StaticNonlinear.SetLoads("SERVICE-WIND(+)",1,["Load"],["WIND(+)"],[1.0])
a.SapModel.LoadCases.StaticNonlinear.SetLoads("SERVICE-WIND(-)",1,["Load"],["WIND(-)"],[1.0])

a.SapModel.LoadCases.StaticNonlinear.SetLoads("DEAD_ALT(+)SERVICE_WIND_1.0",4,
                                              ["Load","Load","Load","Load"],
                                              ["DEAD","reverseSW","SDL_MEP","WIND(+)"],
                                              [1.0,1.0,1.0,1.0])
a.SapModel.LoadCases.StaticNonlinear.SetLoads("DEAD_ALT(-)SERVICE_WIND_1.0",4,
                                              ["Load","Load","Load","Load"],
                                              ["DEAD","reverseSW","SDL_MEP","WIND(-)"],
                                              [1.0,1.0,1.0,1.0])
a.SapModel.LoadCases.StaticNonlinear.SetLoads("DEAD_ALT(+)SERVICE_WIND_0.7",4,
                                              ["Load","Load","Load","Load"],
                                              ["DEAD","reverseSW","SDL_MEP","WIND(+)"],
                                              [1.0,1.0,1.0,0.7])
a.SapModel.LoadCases.StaticNonlinear.SetLoads("DEAD_ALT(-)SERVICE_WIND_0.7",4,
                                              ["Load","Load","Load","Load"],
                                              ["DEAD","reverseSW","SDL_MEP","WIND(-)"],
                                              [1.0,1.0,1.0,0.7])

a.SapModel.LoadCases.StaticNonlinear.SetLoads("DEAD_ALT(+)SERVICE_WIND_1.0x0.78_ASCE7-16",4,
                                              ["Load","Load","Load","Load"],
                                              ["DEAD","reverseSW","SDL_MEP","WIND(+)"],
                                              [1.0,1.0,1.0,0.78])
a.SapModel.LoadCases.StaticNonlinear.SetLoads("DEAD_ALT(-)SERVICE_WIND_1.0x0.78_ASCE7-16",4,
                                              ["Load","Load","Load","Load"],
                                              ["DEAD","reverseSW","SDL_MEP","WIND(-)"],
                                              [1.0,1.0,1.0,0.78])
a.SapModel.LoadCases.StaticNonlinear.SetLoads("DEAD_ALT(+)SERVICE_WIND_0.7x0.78_ASCE7-16",4,
                                              ["Load","Load","Load","Load"],
                                              ["DEAD","reverseSW","SDL_MEP","WIND(+)"],
                                              [1.0,1.0,1.0,0.546])
a.SapModel.LoadCases.StaticNonlinear.SetLoads("DEAD_ALT(-)SERVICE_WIND_0.7x0.78_ASCE7-16",4,
                                              ["Load","Load","Load","Load"],
                                              ["DEAD","reverseSW","SDL_MEP","WIND(-)"],
                                              [1.0,1.0,1.0,0.546])