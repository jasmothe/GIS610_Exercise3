# GIS610_ex3
# Justin A. Smothers, MPA
# Question 10

import arcpy
from arcpy import env
import os

arcpy.env.overWriteOutput = True

arcpy.env.workspace = r"C:\Users\jasmothe\Desktop\GIS610\GIS610_ex3\ex3gdb.gdb"

workspace = r"C:\Users\jasmothe\Desktop\GIS610\GIS610_ex3\ex3gdb.gdb"
outworkspace = r"C:\Users\jasmothe\Desktop\GIS610\GIS610_ex3\ex3gdb.gdb\Spatial_Join"
targetFeatures = os.path.join(workspace, "Tracts")
joinFeatures = os.path.join(workspace, "General_Offense")

arcpy.SpatialJoin_analysis(targetFeatures, joinFeatures, outworkspace)

print("Spatial_Join complete!")
