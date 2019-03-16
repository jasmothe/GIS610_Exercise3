# GIS610_ex3
# Justin A. Smothers, MPA
# Question 8

import arcpy
from arcpy import env
import os

arcpy.env.overWriteOutput = True

arcpy.env.workspace = r"C:\Users\jasmothe\Desktop\GIS610\GIS610_ex3\ex3gdb.gdb"


featureClass = r"C:\Users\jasmothe\Desktop\GIS610\GIS610_ex3\ex3gdb.gdb\CallsforService"

fieldList = ["CFSType","Crime_Explanation","OBJECTID"]
crimeCount = 0

result = arcpy.getCount_Management(featureClass)
print("Crime Count Results Completed!")
