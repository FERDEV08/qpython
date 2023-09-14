print ("wWinicia")

#Ubicacion del Geopackage

rutagpkg = 'D:/Curso _II/insumos_gpkg/E14C56.gpkg'

#Nombre de la capa

name = 'altimetria 1'

#Ubicacion de la capa en el Geopackage almacenada en la variable uri

uri = "%s|layername=%s" % (rutagpkg , name,);

#Se carga la informacion de la capa altimetria 1 un clase de tipo QgsVectorLayer
lyr = QgsVectorLayer(uri, name, 'ogr') #Se agregan los valores de la variable uri
print ("Total de registros : ",lyr.featureCount ())

QgsProject. instance() . addMapLayer (lyr)

print ("Wtermina")
