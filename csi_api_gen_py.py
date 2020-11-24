# -*- coding: utf-8 -*-
"""
Generates .py file for CSI API (located in %SYSTEM TEMP%\gen_py\)
"""
from win32com.client import gencache

# CSI V1 API
CSI = gencache.EnsureModule('{F896D55D-8BDF-4232-B9AB-4B210897A81D}', 0, 1, 0)

# ETABS V17 API
ETABS = gencache.EnsureModule('{21C35BDB-0953-491B-A20D-F621B1C1994A}', 0, 17, 0)