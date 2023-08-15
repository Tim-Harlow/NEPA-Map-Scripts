import arcpy

#TestPolygon must be placed at the top of the layers in the content pane for all maps to output correctly

#GetProject
aprx = arcpy.mp.ArcGISProject(r"D:\GISProjects\Programming\ProgrammingProjectTest\programming.aprx")
m = aprx.listMaps("Map")[0]

#Establish Project Footprint
lyr = m.listLayers("TestPolygon")[0]

# Set the output file paths
arch_output_file = r'D:\GISProjects\Programming\ProgrammingProjectTest\archeology.pdf'
wetland_output_file = r'D:\GISProjects\Programming\ProgrammingProjectTest\wetlands.pdf'
environmentaljustice_output_file = r'D:\GISProjects\Programming\ProgrammingProjectTest\environmentaljustice.pdf'

# Identify the existing layout (need to figure out how to create this in code)
lyt = aprx.listLayouts("ArchMap")[0]


#Identify the exisitng Map Frame 
mf = lyt.listElements("mapframe_element", "ArchMapFrame")[0]
mf.camera.setExtent(mf.getLayerExtent(lyr, False, True))
new_scale = mf.camera.scale * 20 
mf.camera.scale = new_scale

#Make Legend
legend = lyt.listElements("LEGEND_ELEMENT", "Legend")[0]
legend.title = "Archeology Map"

#Show Archeology Layers
for layer in m.listLayers("*"):
    if "arch" in layer.name.lower() or layer.name == ("TestPolygon") or layer.name == ("World Topographic Map"):
        layer.visible =True
        legend.addItem(layer)
    else:
        layer.visible = False
        


#Make Archeology PDF
print("making archeology map")                    
lyt.exportToPDF(arch_output_file, resolution=300)
for item in legend.items:
    legend.removeItem(item)

#Show Wetland Layers
for layer in m.listLayers("*"):
    if "wet" in layer.name.lower() or layer.name == ("TestPolygon") or layer.name == ("World Topographic Map"):
        layer.visible =True
        legend.addItem(layer)
    else:
        layer.visible = False

        
#Add Wetlands Layers to Legend

#Make Wetlands PDF
legend.title = "Wetlands Map"
print("making wetlands map")                    
lyt.exportToPDF(wetland_output_file, resolution=300)
for item in legend.items:
    legend.removeItem(item)

#Show Environmental Justice Layers
for layer in m.listLayers("*"):
    if "justice" in layer.name.lower() or layer.name == ("TestPolygon") or layer.name == ("World Topographic Map"):
        layer.visible =True
        legend.addItem(layer)
    else:
        layer.visible = False


#Make Environmental Justice PDF
legend.title = "Environmental Justice Map"
print("making environmental justice map")                    
lyt.exportToPDF(environmentaljustice_output_file, resolution=300)
for item in legend.items:
    legend.removeItem(item)

# Clean up
aprx.save()
del aprx
