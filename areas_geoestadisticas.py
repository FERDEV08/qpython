path = r'D:/Curso_II/areas_geoestadisticas/'


def generaGpkg (GpName, shape): #define una función llamada generaGpkg que acepta dos argumentos
    layer = QgsVectorLayer (path+shape+".shp", shape, "ogr")
    layercount = layer .featureCount()
    if (layercount > 0): #Estas líneas obtienen el número de entidades (features) en la capa cargada y comprueban
        #si hay al menos una entidad presente en la capa.obtienen el número de entidades (features) en la capa cargada
        #y comprueban si hay al menos una entidad presente en la capa.
        options = QgsVectorFileWriter.SaveVectorOptions()
        options.actionOnExistinFile = QgsVectorFileWriter.CreateOrOverwriteLayer #Modo Actualizacion
        options.EditionCapability = QgsVectorFileWriter .CanAddNewLayer
        options.layerName = layer.name()
        _writer = QgsVectorFileWriter.writeAsVectorFormat (layer, GpName, options)
        if _writer[0] == QgsVectorFileWriter.ErrCreateDataSource :
            options.actionOnExistingFile = QgsVectorFileWriter.CreateOrOverwriteFile #Modo de Creacion
            _writer= QgsVectorFileWriter.writeAsVectorFormat (layer, GpName, options)
    print("se genero la capa : "+layer.name())

print ("\nInicia Proceso")
listashapes = ["areas_geoestadisticas_estatales","areas_geoestadisticas_municipales", "servicios_informacion_complementaria_de_tipo_puntual"]

for shape in listashapes:
    generaGpkg(r"D:/Curso_II/areas_geoestadisticas/areas_geoestadisticas.gpkg",shape)

print ("\nTermina Proceso")
