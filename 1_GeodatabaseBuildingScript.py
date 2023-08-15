import webbrowser
import requests
import urllib.request
import zipfile
import arcpy

#This script builds a geodatabase of environmental criteria

#Make overwrite output true to keep from download tons of extra stuff
arcpy.env.overwriteOutput = True

#Set Workspace

arcpy.env.workspace = r"D:\GISProjects\Programming\ProgrammingProjectTest"
geodatabase = r"D:\GISProjects\Programming\ProgrammingProjectTest\ProgrammingProjectTest.gdb"

# Paths and URLs for downloaded files
archeology_file_paths = [
    r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\Cemeteries_shp.zip",
    r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\CountyCourthouse_shp.zip",
    r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\HistoricHighwaysRoutes_shp.zip",
    r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\StateHistoricSites_shp.zip",
    r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\HistoricalMarkers_shp.zip",
    r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\Museums_shp.zip",
    r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\NationalRegisterPT_shp.zip",
    r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\NeighborhoodSurveys_shp.zip"
]

wetlands_file_paths = [
    r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\TX_geodatabase_wetlands.zip"
]

envjustice_file_path = r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\TX_geodatabase_envjustice.zip"

archeology_urls = [
    r'https://atlas.thc.state.tx.us/gis-data/Cemeteries_shp.zip',
    r"https://atlas.thc.state.tx.us/gis-data/CountyCourthouse_shp.zip",
    r"https://atlas.thc.state.tx.us/gis-data/HistoricHighwaysRoutes_shp.zip",
    r"https://atlas.thc.state.tx.us/gis-data/StateHistoricSites_shp.zip",
    r"https://atlas.thc.state.tx.us/gis-data/HistoricalMarkers_shp.zip",
    r"https://atlas.thc.state.tx.us/gis-data/Museums_shp.zip",
    r"https://atlas.thc.state.tx.us/gis-data/NationalRegisterPT_shp.zip",
    r"https://atlas.thc.state.tx.us/gis-data/NeighborhoodSurveys_shp.zip"
]

wetlands_urls = [
    r"https://www.fws.gov/wetlands/Data/State-Downloads/TX_geodatabase_wetlands.zip"
]

envjustice_url = r"https://gaftp.epa.gov/EJSCREEN/2022/EJSCREEN_2022_StatePct_with_AS_CNMI_GU_VI.gdb.zip"

# location for extracting zip files
temp_location = r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads"

# Download files
for url, file_path in zip(archeology_urls, archeology_file_paths):
    print("Downloading {}...".format(url))
    urllib

# Unzip the file and extract the contents
print("unzipifyingarcheology")
with zipfile.ZipFile(cem_download_path, 'r') as zip_ref:
    zip_ref.extractall(temp_location)
with zipfile.ZipFile(courthouse_download_path, 'r') as zip_ref:
    zip_ref.extractall(temp_location)
with zipfile.ZipFile(historicalhighway_download_path, 'r') as zip_ref:
    zip_ref.extractall(temp_location)
with zipfile.ZipFile(historicsite_path, 'r') as zip_ref:
    zip_ref.extractall(temp_location)
with zipfile.ZipFile(historicmarker_path, 'r') as zip_ref:
    zip_ref.extractall(temp_location)
with zipfile.ZipFile(museum_path, 'r') as zip_ref:
    zip_ref.extractall(temp_location)
with zipfile.ZipFile(historicproperty_path, 'r') as zip_ref:
    zip_ref.extractall(temp_location)
with zipfile.ZipFile(neighborhoodsurvey_path, 'r') as zip_ref:
    zip_ref.extractall(temp_location)
print("unzipifyingwetlands")
print("This section is commented out due to filesize")
#with zipfile.ZipFile(wetlands_path, 'r') as zip_ref:
#    zip_ref.extractall(temp_location)
#print("Extraction complete.")
print("unzipifyingenvironmentaljustice")
with zipfile.ZipFile(envjustice_path, 'r') as zip_ref:
    zip_ref.extractall(temp_location)
print("unzipped")

#files to send to geodatabase
geodatabase_input_features = [
    r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\Cemeteries.shp",
    r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\County_Courthouses.shp",
    r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\HistoricalMarkers.shp",
    r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\HistoricHighwaysRoutes.shp",
    r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\Museums.shp",
    r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\NationalRegisterPT.shp",
    r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\NeighborhoodSurveys.shp",
    r"D:\GISProjects\Programming\ProgrammingProjectTest\TempDownloads\StateHistoricSites.shp"
]

arcpy.conversion.FeatureClassToGeodatabase(geodatabase_input_features, geodatabase)

arcpy.env.workspace = geodatabase

print("Feature classes:")
for fc in arcpy.ListFeatureClasses():
    print(" - {}".format(fc))
