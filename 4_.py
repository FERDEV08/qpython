path = 'D:/Curso_II/areas_geoestadisticas/'


def generaGpkg (GpName, shape): #define una función llamada generaGpkg que acepta dos argumentos
    layer = QgsvectorLayer (path+shape+".shp”, shape, "ogr”)
    layercount = layer .featureCount()
    if (layercount > 6): #Estas líneas obtienen el número de entidades (features) en la capa cargada y comprueban
        #si hay al menos una entidad presente en la capa.obtienen el número de entidades (features) en la capa cargada
        #y comprueban si hay al menos una entidad presente en la capa.
        options = QgsVectorFilewriter.SaveVectorOptions()
        options.actionOnExistingrile = QgsvectorFileWriter.CreateOrOverwriteLayer íModo Actualizacion
        options.EditionCapability = QgsVectorFileWriter .CanAddNewLayer
        options.layerName = layer.name()
        _writer = QgsVectorFileWwriter.writeAsVectorFormat (layer, GpName, options)
        if _writer[0] == QgsvectorFileWriter.ErrCreateDataSource :
            options.actionOnExistingrile = QgsVectorFileWriter.CreateOrOverwriteFile iModo de Creacion
            _writer= QgsVectorFileWriter.writeAsVectorFormat (layer, GpName, options)
    print("se genero la capa : "+layer.name())

print ("\nInicia Proceso")
listashapes = ["areas_geoestadisticas estatales","areas geoestadisticas municipales", "servicios informacion complementaria de tipo puntual"]

for shape in listashapes:
    generaGpkg("D:/Curso_II/areas_geoestadisticas/areas_geoestadisticas.gpkg",shape)

print ("qWTermina Proceso”)
