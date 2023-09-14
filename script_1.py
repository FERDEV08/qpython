from qgis.core import QgsVectorFileWriter, QgsVectorLayer
print ("\nInicia")

layer = QgsProject.instance().layerStore().mapLayersByName('estados_wgs84')[0]
#layer = QgsVectorLayer("D:/Curso_II/Insumos/estados_wgs84.shp","MyShp","ogr")
epsg = QgsCoordinateReferenceSystem('EPSG:4326')
capa_base = QgsVectorFileWriter.writeAsVectorFormat(layer,"D:/Curso_II/Pruebas/estados_kml.kml","UTF-8",epsg,driverName="KML")
if capa_base[0] == QgsVectorFileWriter.NoError:
    print("\nSe creo el archivo Kml!")
capa_base = QgsVectorFileWriter.writeAsVectorFormat(layer,"D:/Curso_II/Pruebas/estados.shp","UTF-8",epsg,driverName="ESRI Shapefile")
if capa_base[0] == QgsVectorFileWriter.NoError:
    print("\nSe creo el archivo Shape!")
capa_base = QgsVectorFileWriter.writeAsVectorFormat(layer,"D:/Curso_II/Pruebas/estados.geojson","UTF-8",epsg,driverName="GEOJSON")
if capa_base[0] == QgsVectorFileWriter.NoError:
    print("\nSe creo el archivo GeoJson!")
capa_base = QgsVectorFileWriter.writeAsVectorFormat(layer,"D:/Curso_II/Pruebas/estados.gpkg", "UTF-8", epsg, driverName="GPKG")
if capa_base[0] == QgsVectorFileWriter.NoError:
    print("\nSe creo el archivo Geopackage!")
print ("\nTermina")
