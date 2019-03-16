# GIS610_ex3
# Justin A. Smothers, MPA
# Question 5

import arcpy
from arcpy import env
import os

arcpy.env.overWriteOutput = True
arcpy.CreateFileGDB_management(r"C:\Users\jasmothe\Desktop\GIS610\Exercise3", "q5.gdb")

featureList = ["CapitalCities", "Landmarks", "HistoricPlaces", "StateNames", "Nationalities", "Rivers"]

current_workspace = (r"C:\Users\jasmothe\Desktop\GIS610\Exercise3\q5.gdb")

geometry_type_polygon = "POLYGON"
geometry_type_line = "POLYLINE"
geometry_type_point = "POINT"

spatial_reference = arcpy.SpatialReference(102100)



def createPolygonFeatureClass(in_fc_name,overwriteSetting):
    arcpy.env.overWriteOutput = overwriteSetting
    arcpy.CreateFeatureclass_management(current_workspace, in_fc_name, geometry_type_polygon,"", "DISABLED", "DISABLED", spatial_reference)
def createLineFeatureClass(in_fc_name,overwriteSetting):
    arcpy.env.overWriteOutput = overwriteSetting
    arcpy.CreateFeatureclass_management(current_workspace, in_fc_name, geometry_type_line,"", "DISABLED", "DISABLED", spatial_reference)
def createPointFeatureClass(in_fc_name,overwriteSetting):
    arcpy.env.overWriteOutput = overwriteSetting
    arcpy.CreateFeatureclass_management(current_workspace, in_fc_name, geometry_type_point,"", "DISABLED", "DISABLED", spatial_reference)

for feature in featureList:
    if (feature == "Rivers"):
      print(feature)
      createLineFeatureClass(feature,True)
    elif (feature == "Landmarks" or "HistoricPlaces"):
       print(feature)
       createPointFeatureClass(feature,True)
    else:
       print(feature)
       createPolygonFeatureClass(feature,True)
