layer = QgsVectorLayer("D:\curso_qpy\shp\México_Estados.shp","Estados","ogr")
#Crea objeto Layer
if not layer.isValid(): #si el layer es valido lo carga a Qgis
 print ("Error al cargar la capa!")
else: 
    QgsProject.instance().addMapLayer(layer) # Carga el objeto a Qgis