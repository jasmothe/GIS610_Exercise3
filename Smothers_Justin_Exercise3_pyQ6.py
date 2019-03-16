# GIS610_ex3
# Justin A. Smothers, MPA
# Question 6
# 6 -- Using the CallsforService feature class that you’ve been given, 
# add a field called ‘Crime_Explanation’ with the data type Text/String. 
# Then, if the value of field ‘CFSType’ is Burglary Call, write ‘This is a burglary’
# into the field that you just added.

import arcpy
import os

arcpy.env.overWriteOutput = True

arcpy.env.workspace = r"C:\\Desktop\GIS610\GIS610_ex3\ex3gdb.gdb"

arcpy.AddField_management == ("CallsforService", "Crime_Explanation", "CFSType")

featureClass = r"C:\\Desktop\GIS610\GIS610_ex3\ex3gdb.gdb\CallsforService"

def callsforServiceFieldList = [("CFSType", "Crime_Explanation", "BurglaryCall")]

with arcpy.UpdateCursor("featureClass", "fieldList") as cursor:
    for row in cursor: 
        if [row (0,1,2,3,4,5) == "BurglaryCall"]:
             row[0] = "This is a burglary"
  
