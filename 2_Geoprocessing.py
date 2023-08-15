import arcpy
import os

#Make overwrite output true to keep from downloading extra stuff
arcpy.env.overwriteOutput = True

arcpy.env.workspace = (r"D:\GISProjects\Programming\ProgrammingProjectTest")
project_path = (r"D:\GISProjects\Programming\ProgrammingProjectTest")
aprx_path = os.path.join(project_path, "programming.aprx")
aprx = arcpy.mp.ArcGISProject(aprx_path)
if os.path.exists(os.path.join(project_path, "ProgrammingProjectTest.aprx")):
    print("Your workspace is set correctly.")
else:
    print("Your workspace is wrong.")


#Establish Feature Classes
#ArcheologyFeatures
print("establishing archeology features")
Cemeteries = r"D:\GISProjects\Programming\ProgrammingProjectTest\ProgrammingProjectTest.gdb\Cemeteries"
Courthouses = r"D:\GISProjects\Programming\ProgrammingProjectTest\ProgrammingProjectTest.gdb\County_Courthouses"
HistoricalMarkers = r"D:\GISProjects\Programming\ProgrammingProjectTest\ProgrammingProjectTest.gdb\HistoricalMarkers"
HistoricHighwaysRoutes =r"D:\GISProjects\Programming\ProgrammingProjectTest\ProgrammingProjectTest.gdb\HistoricHighwaysRoutes"
Museums = r"D:\GISProjects\Programming\ProgrammingProjectTest\ProgrammingProjectTest.gdb\Museums"
NationRegisterHP = r"D:\GISProjects\Programming\ProgrammingProjectTest\ProgrammingProjectTest.gdb\NationalRegisterPT"
NeighborhoodSurveys = r"D:\GISProjects\Programming\ProgrammingProjectTest\ProgrammingProjectTest.gdb\NeighborhoodSurveys"
StateHistoricSites = r"D:\GISProjects\Programming\ProgrammingProjectTest\ProgrammingProjectTest.gdb\StateHistoricSites"
#WetlandsFeatures
print("establishing Wetlands")
HistoricWetlands = r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\TX_geodatabase_wetlands.gdb\TX_Historic_Wetlands"
Riparian = r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\TX_geodatabase_wetlands.gdb\TX_Riparian"
Wetlands = r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\TX_geodatabase_wetlands.gdb\TX_Wetlands"
#EnvironmentalJusticeLayer
EnvironmentalJustice= r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\EJSCREEN_2022_StatePct_with_AS_CNMI_GU_VI.gdb\EJSCREEN_StatePct_with_AS_CNMI_GU_VI"




#BufferFeatures
#ArcheologyFeatures

CemeteryZone = r"D:\GISProjects\Programming\ProgrammingProjectTest\ProgrammingProjectTest.gdb\Cemeteries_Buffer"
CourtHouseZone = r"D:\GISProjects\Programming\ProgrammingProjectTest\ProgrammingProjectTest.gdb\CourtHouse_Buffer"
HistMarkZone = r"D:\GISProjects\Programming\ProgrammingProjectTest\ProgrammingProjectTest.gdb\HistoricalMarker_Buffer"
HistHighwayZone = r"D:\GISProjects\Programming\ProgrammingProjectTest\ProgrammingProjectTest.gdb\HistHighway_Buffer"
MuseumZone = r"D:\GISProjects\Programming\ProgrammingProjectTest\ProgrammingProjectTest.gdb\Museum_Buffer"
NationHPZone = r"D:\GISProjects\Programming\ProgrammingProjectTest\ProgrammingProjectTest.gdb\NationHP_Buffer"
NeighborZone = r"D:\GISProjects\Programming\ProgrammingProjectTest\ProgrammingProjectTest.gdb\Neighbor_Buffer"
StateHistSiteZone = r"D:\GISProjects\Programming\ProgrammingProjectTest\ProgrammingProjectTest.gdb\StateHistSite_Buffer"

#WetlandsFeatures
HistoricWetlandsZone = r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\TX_geodatabase_wetlands.gdb\TX_Historic_Wetlands_Buffer"
RiparianZone = r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\TX_geodatabase_wetlands.gdb\TX_Riparian_Buffer"
WetlandsZone = r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\TX_geodatabase_wetlands.gdb\TX_Wetlands_Buffer"



#Create Buffers
print("buffering archeology")
arcpy.analysis.Buffer(Cemeteries, CemeteryZone, "30 Feet", "FULL", "ROUND", "NONE", None, "PLANAR")
arcpy.analysis.Buffer(Courthouses, CourtHouseZone, "30 Feet", "FULL", "ROUND", "NONE", None, "PLANAR")
arcpy.analysis.Buffer(HistoricalMarkers, HistMarkZone, "30 Feet", "FULL", "ROUND", "NONE", None, "PLANAR")
arcpy.analysis.Buffer(HistoricHighwaysRoutes, HistHighwayZone, "30 Feet", "FULL", "ROUND", "NONE", None, "PLANAR")
arcpy.analysis.Buffer(Museums, MuseumZone, "30 Feet", "FULL", "ROUND", "NONE", None, "PLANAR")
arcpy.analysis.Buffer(NationRegisterHP, NationHPZone, "30 Feet", "FULL", "ROUND", "NONE", None, "PLANAR")
arcpy.analysis.Buffer(NeighborhoodSurveys, NeighborZone, "30 Feet", "FULL", "ROUND", "NONE", None, "PLANAR")
arcpy.analysis.Buffer(StateHistoricSites, StateHistSiteZone, "30 Feet", "FULL", "ROUND", "NONE", None, "PLANAR")
print("buffering historic wetlands")
arcpy.analysis.Buffer(HistoricWetlands, HistoricWetlandsZone, "100 Feet", "FULL", "ROUND", "NONE", None, "PLANAR")
print("buffering riparian")
arcpy.analysis.Buffer(Riparian, RiparianZone, "100 Feet", "FULL", "ROUND", "NONE", None, "PLANAR")
print("the script hangs when buffering this wetlands layer, even up to an hour, so I've commented it out for now [forever]")
#arcpy.analysis.Buffer(Wetlands, WetlandsZone, "100 Feet", "FULL", "ROUND", "NONE", None, "PLANAR")

#Create Feature Layer
#Archeology
print("creating feature layers")
CemeteryZoneLayer = arcpy.management.MakeFeatureLayer(CemeteryZone, "Cemetery Buffer Arch")[0]
CourtHouseZoneLayer = arcpy.management.MakeFeatureLayer(CemeteryZone, "CourtHouse Buffer Arch")[0]
HistMarkZoneLayer = arcpy.management.MakeFeatureLayer(CemeteryZone, "HistMark Buffer Arch")[0]
HistHighwayZoneLayer = arcpy.management.MakeFeatureLayer(CemeteryZone, "HistHighway Buffer Arch")[0]
MuseumZoneLayer = arcpy.management.MakeFeatureLayer(CemeteryZone, "Museum Buffer Arch")[0]
NationHPZoneLayer = arcpy.management.MakeFeatureLayer(CemeteryZone, "NationHP Buffer Arch")[0]
NeighborZoneLayer = arcpy.management.MakeFeatureLayer(CemeteryZone, "NeighborZone Buffer Arch")[0]
StateHistSiteZoneLayer = arcpy.management.MakeFeatureLayer(CemeteryZone, "StateHist Buffer Arch")[0]
#Wetlands
HistoricWetlandsZoneLayer = arcpy.management.MakeFeatureLayer(HistoricWetlandsZone, "Historic Wetlands Buffer Wet")[0]
RiparianZoneLayer = arcpy.management.MakeFeatureLayer(RiparianZone, "Riparian Buffer Wet")[0]
WetlandsZoneLayer = arcpy.management.MakeFeatureLayer(WetlandsZone, "Wetlands Buffer Layer")[0]
#Environmnental Justice
EnvironmentalJusticeLayer = arcpy.management.MakeFeatureLayer(EnvironmentalJustice, "EnvironmentalJusticeIndex")[0]

#Add Archeological Layers to Map
print("addingFeaturestoMap")
m = aprx.listMaps()[0]
m.addLayer(CemeteryZoneLayer, "AUTO_ARRANGE")
m.addLayer(CourtHouseZoneLayer, "AUTO_ARRANGE")
m.addLayer(HistMarkZoneLayer, "AUTO_ARRANGE")
m.addLayer(HistHighwayZoneLayer, "AUTO_ARRANGE")
m.addLayer(MuseumZoneLayer, "AUTO_ARRANGE")
m.addLayer(NationHPZoneLayer, "AUTO_ARRANGE")
m.addLayer(NeighborZoneLayer, "AUTO_ARRANGE")
m.addLayer(StateHistSiteZoneLayer, "AUTO_ARRANGE")
m.addLayer(HistoricWetlandsZoneLayer, "AUTO_ARRANGE")
#Add Wetlands Layers to Map
m.addLayer(RiparianZoneLayer, "AUTO_ARRANGE")
#Add Environmental Justice Layers to Map
m.addLayer(EnvironmentalJusticeLayer, "AUTO_ARRANGE")
aprx.save()
print("Project saved.")
del aprx
print("project unlocked")

