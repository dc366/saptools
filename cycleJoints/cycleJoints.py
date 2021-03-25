import pandas as pd
import panelJoints
"""Inputs: (sheetName must start with H or V)"""
filePath = r"J:\ENG\1092 LMNA LA\Facade & FRP Analysis Work\ACP\Panel Point Generatior\Seq C1 SE Redo\2021_03_16_C1SERedo_Mapping.xlsx"
df = pd.read_excel(filePath, sheet_name="Input") # can also index sheet by name or fetch all sheets
dirtylist = df["jLine"].tolist()

"""List of joint line names:(must start with H or V"""
lineList = [x for x in dirtylist if (pd.isnull(x) == False)]

col1=[]
col2=[]
col3=[]
col4=[]
col5=[]
col6=[]

for i in range(len(lineList)):
    sheetName=lineList[i]
    print(sheetName)
    [a,b,c,d,e,f]= panelJoints.mapJoints(sheetName, filePath)
    col1.extend(a)
    col2.extend(b)
    col3.extend(c)
    col4.extend(d)
    col5.extend(e)
    col6.extend(f)


tempList = [col1, col2, col3, col4, col5, col6]
combinedList= zip(*tempList)
df = pd.DataFrame(combinedList)
writer = pd.ExcelWriter('Output.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name="Output", index=False)
writer.save()
