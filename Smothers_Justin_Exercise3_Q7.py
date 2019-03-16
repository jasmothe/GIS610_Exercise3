# GIS610_ex3
# Justin A. Smothers, MPA
# Question 7

import arcpy
from arcpy import env
import os


arcpy.env.workspace = r"C:\Users\jasmothe\Desktop\GIS610\GIS610_ex3\ex3gdb.gdb"

featureClass = r"C:\Users\jasmothe\Desktop\GIS610\GIS610_ex3\ex3gdb.gdb\CallsforService"

fieldList = ["CFSType","Crime_Explanation"]


arcpy.SelectLayerByAttribute_management (featureClass, "NEW_CFSType_SELECTION", CFSType = "BurglaryCall") 

arcpy.CopyFeatures_management (featureClass,"Burglary_Selection")

print("Burglary Selections Completed!")
