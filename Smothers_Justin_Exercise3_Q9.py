# GIS610_ex3
# Justin A. Smothers, MPA
# Question 9

import arcpy
from arcpy import env
import os

current_workspace = r"C:\\Desktop\GIS610\GIS610_ex3\ex3gdb.gdb"
arcpy.env.workspace = current_workspace

arcpy.CreateFeatureclass_management(r"C:\\Desktop\GIS610\GIS610_ex3\ex3gdb.gdb", "VisibleLightColorSpectrumColors", "POINT")

arcpy.AddField_management(r"C:\\Desktop\GIS610\GIS610_ex3\ex3gdb.gdb\ROYGBIV_Colors", "ROYGBIV_Color", "TEXT")

arcpy.CreateDomain_management(r"C:\\Desktop\GIS610\GIS610_ex3\ex3gdb.gdb", "ROYGBIV_Color", "Selected_ROYGBIV_Color", "FLOAT", "CODED", "DUPLICATE", "DEFAULT")

arcpy.AddCodedValueToDomain_management(current_workspace, "ROYGBIV_Color", 0, "RED")
arcpy.AddCodedValueToDomain_management(current_workspace, "ROYGBIV_Color", 1, "ORANGE")
arcpy.AddCodedValueToDomain_management(current_workspace, "ROYGBIV_Color", 2, "YELLOW")
arcpy.AddCodedValueToDomain_management(current_workspace, "ROYGBIV_Color", 3, "GREEN")
arcpy.AddCodedValueToDomain_management(current_workspace, "ROYGBIV_Color", 4, "BLUE")
arcpy.AddCodedValueToDomain_management(current_workspace, "ROYGBIV_Color", 5, "INDIGO")
arcpy.AddCodedValueToDomain_management(current_workspace, "ROYGBIV_Color", 6, "VIOLET")

print("Justin loves astronomy and selected ROYGBIV!")
