import pandas as pd
import panelJoints
"""Inputs: (sheetName must start with H or V)"""
filePath=r"PythonPoints.xlsx"
df = pd.read_excel(filePath, sheet_name="Input") # can also index sheet by name or fetch all sheets
dirtylist = df["jLine"].tolist()

"""List of joint line names:(must start with H or V"""
lineList = [x for x in dirtylist if (pd.isnull(x) == False)]

col1=[]
col2=[]
col3=[]
col4=[]
col5=[]

for i in range(len(lineList)):
    sheetName=lineList[i]
    [a,b,c,d,e]= panelJoints.mapJoints(sheetName, filePath)
    col1.extend(a)
    col2.extend(b)
    col3.extend(c)
    col4.extend(d)
    col5.extend(e)


tempList = [col1, col2, col3, col4, col5]
combinedList= zip(*tempList)
df = pd.DataFrame(combinedList)
writer = pd.ExcelWriter('Output.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name="Output", index=False)
writer.save()
