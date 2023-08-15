import arcpy
import os
import sys
import random




# Set workspace and project paths
workspace_path = r"D:\GISProjects\Programming\ProgrammingProjectTest"
project_path = os.path.join(workspace_path, "Programming.aprx")

# Create an ArcGISProject object
project = arcpy.mp.ArcGISProject(project_path)

# Get the map and EJ Layer
map_name = "Map"
layer_name = "EnvironmentalJusticeIndex"
map_obj = project.listMaps(map_name)[0]
layer_obj = map_obj.listLayers(layer_name)[0]
sym = layer_obj.symbology

# Symbolize the layer
if hasattr(sym, 'renderer'):
    if sym.renderer.type == 'SimpleRenderer':
        sym.updateRenderer('GraduatedColorsRenderer')
        classification_field = 'EXCEED_COUNT_80'
        sym.renderer.classificationField = classification_field
#The following breakcount assignment does not seem to work. Produces 5 every time.
        sym.renderer.breakCount = 6
        sym.renderer.colorRamp = project.listColorRamps('Cyan to Purple')[0]
        layer_obj.symbology = sym

#Randomly symbolize all the other layers
layernames = ["Riparian Buffer Wet", "Historic Wetlands Buffer Wet", "StateHist Buffer Arch", "NeighborZone Buffer Arch", "NationHP Buffer Arch", "Museum Buffer Arch", "HistHighway Buffer Arch"]
for layer in layernames:
    map_obj = project.listMaps(map_name)[0]
    layer_obj = map_obj.listLayers(layer)[0]
    sym = layer_obj.symbology
    if hasattr(sym, 'renderer'):
        if sym.renderer.type == 'SimpleRenderer':
            randomvalues = [10, 40, 80, 90, 100, 105, 110, 120, 160, 170]
            r = random.choice(randomvalues)
            g= random.choice(randomvalues)
            b= random.choice(randomvalues)
            sym.renderer.symbol.color = {'RGB' : [r, g, b, 60]}
            layer_obj.symbology = sym
    
# Save the project
project.save()

# Delete the ArcGISProject object
del project
