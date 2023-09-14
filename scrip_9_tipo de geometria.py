#script 9
# consulta la geometría de la capa
capa = QgsVectorLayer("D:/curso_qpy/shp/Shapes/estados.shp","Estados","ogr")
registros = capa.getFeatures()
for r in registros:
    if(r['NOMGEO']=='Colima'):
        geom = r.geometry()
        print("OID: ", r.id())
        print("Nombre del estado: ", r[2])
        print("Informacion de la geometria")
        print("Area: ",geom.area())
        print("Perimetro: ", geom.length())
        geomSingleType = QgsWkbTypes.isSingleType(geom.wkbType())
        
        if geom.type() == QgsWkbTypes.PointGeometry:
            if geomSingleType:
                x = geom.asPoint()
                print("Punto", x)
            else:
                x = geom.asMultiPoint()
                print("Multipunto:", x)
        elif geom.type() == QgsWkbTypes.LineGeometry:
            if geomSingleType:
                x = geom.asPolyline()
                print("Linea", x)
            else:
                x = geom.asMultiPolyline()
                print("Multilinea:", x)
        elif geom.type() == QgsWkbTypes.PolygonGeometry:
            if geomSingleType:
                x = geom.asPolygon()
                print("Poligono", x)
            else:
                x = geom.asMultiPolygon()
                print("Multipoligono:", x)
        else:
            print("Geometría desconocida o invalida")