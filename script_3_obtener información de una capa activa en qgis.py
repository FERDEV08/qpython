layer=None
layer = qgis.utils.iface.activeLayer()
print ('Nombre de la capa : '+layer.name())
print ('Ubicacion : '+ layer.source())

#Informacion de una capa activa por su nombre en Qgis
layerList = QgsProject.instance().mapLayersByName('Estados')
print('layer: '+layerList[0]. name())
print('Ubicacion: ' + layerList[0].source())

#Informacipon de las capas cargadas en Qgis
for lyr in QgsProject.instance().mapLayers().values(): #Lista de Layers cargadas
    print('layer: '+lyr.name())
    print('Ubicacion: ' + lyr.source()) 

#Información de las capas cargadas en Qgis 
for lyr in QgsProject.instance().mapLayers().values(): 
    print('layer: ' +lyr.name())
    print('Ubicacion: '+lyr.source())