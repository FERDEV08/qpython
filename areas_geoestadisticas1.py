print("\nInicia Proceso")
from qgis.core import QgsProject, QgsLayerTreeGroup, QgsVectorLayer

# Ruta al archivo GeoPackage

ruta_geopackage = r'D:/Curso II/areas _geoestadisticas/areas_geoestadisticas.gpkg'
# Nombre del grupo en el árbol de capas

nombre_grupo = 'Areas_geoestadisticas'

# Cargar el GeoPackage en el proyecto de QGIS
capa_geopackage = QgsVectorLayer(ruta_geopackage, '', 'ogr')

# Obtener todas las capas del GeoPackage
capas_geopackage = capa_geopackage .dataProvider().subLayers()

# Crear el grupo en el árbol de capas
grupo = QgsLayerTreeGroup (nombre_grupo)

# Agregar el grupo al proyecto de QGIS
root = QgsProject.instance().layerTreeRoot()
root .insertChildNode(0, grupo)

# Agregar las capas del GeoPackage al grupo

for capa_info in capas_geopackage:
    nombre_capa = capa_info.split('!!::!!')[1]
    ruta_capa = ruta_geopackage + '|layername=' + nombre_capa
    capa = QgsVectorLayer(ruta_capa, nombre_capa, 'ogr')
    QgsProject .instance().addMapLayer (capa, False)
    grupo.addLayer(capa)

# Refrescar el lienzo de QGIS
iface.mapCanvas().refreshAllLayers()

print ("\nWSe Cargo Geopackage con sus capas")
print ("\nTermina Proceso")
