def accede_gpkg():
    #Ruta del Geopackage
    rutagpkg = r"D:/Curso_II/areas_geoestadisticas/areas_geoestadisticas.gpkg"
    #Se carga el Geopackage en la clase QgsVectorLayer
    layergpkg = QgsVectorLayer (rutagpkg, "test", "ogr")
    #De la clase dataProvider() con el metodo sublLayers() se genera una lista de las capas
    #almacenadas en el Geopackage
    subLayers =layergpkg.dataProvider().subLayers()
    print ("\nCapas Contenidas en el Geopackage")
    for subLayer in subLayers:
        #Se extrae haciendo uso del metodo split el nombre de la capa
        name = subLayer.split('!!::!!')[1]
        #Ubicacion de la capa en el Geopackage almacenada en la variable uri
        uri = "%s|layername=%s" % (rutagpkg , name,)
        #Se carga la informacion de la capa enun clase de tipo QgsVectorLayer
        sub_vlayer = QgsVectorLayer(uri, name, 'ogr')
        #Haciendo uso del metodo featureCount() se verifica que capa tenga informa:
        #en la siguiente condicion
        if (sub_vlayer.featureCount()>0):
            print ("\n",name, sub_vlayer.featureCount())
    print ("\n")

print ("\nInicia")
print ("\n")
accede_gpkg()
print ("\nTermina")
